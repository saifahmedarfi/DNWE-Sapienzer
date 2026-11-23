#!/usr/bin/env python3
"""DNWE local server: the engine runs on this computer and web/index.html talks to it.

    .venv/bin/python server.py              # then open http://127.0.0.1:8765
    .venv/bin/python server.py --port 9000 --no-browser

The engine is NOT copied here: on start-up the server executes the engine cells of DNWE_2.ipynb
(sections 1-13), so the notebook stays the single source of truth and every change you make there
reaches the web app on the next restart. The notebook's offline and AI-free guards (section 3)
are active inside this process too: it cannot open remote connections or load any neural model.
Standard library only; it listens on 127.0.0.1 and refuses other hosts and origins.
"""
import argparse, base64, difflib, io, json, os, re, signal, sys, tempfile, threading, time, traceback, types, webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

ROOT = Path(__file__).resolve().parent
NOTEBOOK = ROOT / "DNWE_2.ipynb"
PAGE = ROOT / "web" / "index.html"
LAST_ENGINE_CELL = "#@title 13 "            # the orchestrator; everything the engine needs is above it
MAX_BODY = 30 * 2**20                        # base64 of a ~20 MB document
ACCEPTED = (".txt", ".md", ".markdown", ".docx", ".pdf", ".tex")

LOCAL_ORIGIN = re.compile(r"https?://(127\.0\.0\.1|localhost|\[::1\])(:\d{1,5})?")
STATE = {"engine": None, "error": None, "loading_since": time.time(), "ready_at": None}
ENGINE_LOCK = threading.Lock()              # the engine keeps caches and one LanguageTool server


def load_engine():
    """Execute the notebook's engine cells in a module of their own and start LanguageTool."""
    try:
        os.environ.setdefault("DNWE_BASE", str(ROOT))
        os.chdir(ROOT)
        mod = types.ModuleType("dnwe_engine")
        sys.modules["dnwe_engine"] = mod          # dataclasses look their module up here
        nb = json.loads(NOTEBOOK.read_text(encoding="utf-8"))
        for cell in nb["cells"]:
            if cell["cell_type"] != "code":
                continue
            src = "".join(cell["source"])
            title = src.splitlines()[0] if src.strip() else "cell"
            print(f"[engine] {title[:90]}", flush=True)
            exec(compile(src, f"DNWE_2.ipynb · {title[:60]}", "exec"), mod.__dict__)
            if src.startswith(LAST_ENGINE_CELL):
                break
        else:
            raise RuntimeError(f"no cell starting with {LAST_ENGINE_CELL!r} in {NOTEBOOK.name}")
        mod.lt()                                  # start LanguageTool now, not on the first request
        STATE["engine"], STATE["ready_at"] = mod, time.time()
        print(f"[engine] ready in {STATE['ready_at'] - STATE['loading_since']:.0f}s", flush=True)
    except Exception as e:                        # report it in /api/health instead of dying silently
        STATE["error"] = f"{type(e).__name__}: {e}"
        traceback.print_exc()


def word_diff(a, b):
    """[[op, text], ...] with op in eq | del | ins, on word/space/punctuation tokens."""
    split = lambda s: re.findall(r"\s+|\w+|[^\w\s]", s)
    ta, tb = split(a), split(b)
    out = []
    for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(None, ta, tb, autojunk=False).get_opcodes():
        if tag == "equal":
            out.append(["eq", "".join(ta[i1:i2])])
            continue
        if i2 > i1:
            out.append(["del", "".join(ta[i1:i2])])
        if j2 > j1:
            out.append(["ins", "".join(tb[j1:j2])])
    return out


def humanize(req):
    E = STATE["engine"]
    mode, intensity = req.get("mode", E.MODE), req.get("intensity", E.INTENSITY)
    if mode not in E.MODES:
        raise ValueError(f"mode must be one of {', '.join(E.MODES)}")
    if intensity not in E.FAMILIES_BY_INTENSITY:
        raise ValueError(f"intensity must be one of {', '.join(E.FAMILIES_BY_INTENSITY)}")
    text, upload = req.get("text"), req.get("file")
    with tempfile.TemporaryDirectory() as td:
        if upload:
            name = str(upload.get("name", "document"))
            suffix = Path(name).suffix.lower()
            if suffix not in ACCEPTED:
                raise ValueError(f"unsupported file type '{suffix}'; use {', '.join(ACCEPTED)}")
            stem = "web_" + (re.sub(r"[^\w.-]+", "_", Path(name).stem)[:60] or "document")
            path = Path(td) / f"{stem}{suffix}"
            path.write_bytes(base64.b64decode(upload["data"], validate=True))
        elif isinstance(text, str) and text.strip():
            path = Path(td) / "pasted_text.txt"
            path.write_text(text, encoding="utf-8")
        else:
            raise ValueError("paste some text or choose a file")
        freeze = req.get("freeze") or []
        if isinstance(freeze, str):
            freeze = [t for t in re.split(r"[,;\n]+", freeze)]
        freeze = [t.strip() for t in freeze if str(t).strip()][:200]
        t0 = time.perf_counter()
        with ENGINE_LOCK:
            doc, recs, _, rep = E.process(path, mode, intensity, write=False, freeze=freeze)
            rendered, refused = E.render_document(doc, rep["new_masked"])
            original, _ = E.render_document(doc, {})
            exports = E.export_all(doc, rendered)
            before = E.elements_to_text(E.doc_elements(doc, original))
        seconds = time.perf_counter() - t0
        after = exports["txt"].decode("utf-8")
        stem = Path(upload["name"]).stem if upload else "humanized_text"
        order = [k for k in ("pdf", "docx", "tex", "md", "txt") if k in exports]
        if upload and Path(upload["name"]).suffix.lower() in (".md", ".markdown"):
            order = ["md"] + [k for k in order if k != "md"]
        downloads = [{"format": k, "name": f"{stem}.dnwe.{k}", "mime": E.EXPORT_MIME[k],
                      "data": base64.b64encode(exports[k]).decode()} for k in order]
    sc = rep["style_check"]
    return {
        "mode": mode, "intensity": intensity, "format": doc.fmt, "seconds": round(seconds, 2),
        "words": rep["profile"].words, "integrity": rep["integrity"],
        "output_text": after, "diff": word_diff(before, after), "downloads": downloads,
        "freeze": freeze, "input_words": len(before.split()), "output_words": len(after.split()),
        "counts": {s: sum(r.status == s for r in recs) for s in
                   ("applied", "rejected-gate", "below-threshold", "overlap", "advice", "refused-docx")},
        "edits": [{"id": r.rid, "status": r.status, "family": r.family, "rule": r.rule, "section": r.section,
                   "before": r.before, "after": r.after, "sentence_before": r.sentence_before,
                   "sentence_after": r.sentence_after, "reason": r.reason, "gate": r.gate_reasons,
                   "confidence": r.confidence, "confidence_source": r.conf_source} for r in recs],
        "style": {"markers": [{"name": k, "before": v[0], "after": sc["after"].get(k, v)[0], "target": v[1],
                               "ok_before": bool(v[2]), "ok_after": bool(sc["after"].get(k, v)[2])}
                              for k, v in sc["before"].items()],
                  "plan": list(rep["plan"].notes)},
    }


class Handler(BaseHTTPRequestHandler):
    server_version = "DNWE/2.0"
    port = 8765

    def _allowed_hosts(self):
        return {f"127.0.0.1:{self.port}", f"localhost:{self.port}"}

    def _origin_ok(self):
        """Pages from THIS computer may call the API: server.py's own page, the file opened from disk
        (Origin: null) and local dev servers such as VS Code Live Server (http://127.0.0.1:5500).
        Pages from any other site are refused."""
        origin = self.headers.get("Origin")
        return origin is None or origin == "null" or bool(LOCAL_ORIGIN.fullmatch(origin))

    def _send(self, code, body, ctype="application/json; charset=utf-8"):
        data = body if isinstance(body, bytes) else json.dumps(body, ensure_ascii=False).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Cache-Control", "no-store")
        self.send_header("X-Content-Type-Options", "nosniff")
        origin = self.headers.get("Origin")
        if origin and self._origin_ok():          # page opened from disk (file://) sends Origin: null
            self.send_header("Access-Control-Allow-Origin", origin)
            self.send_header("Vary", "Origin")
        self.end_headers()
        self.wfile.write(data)

    def _guard(self):
        if self.headers.get("Host") not in self._allowed_hosts():
            self._send(421, {"error": "this server only answers on 127.0.0.1 / localhost"}); return False
        if not self._origin_ok():
            self._send(403, {"error": "requests from other web pages are refused"}); return False
        return True

    def do_OPTIONS(self):
        if not self._guard():
            return
        self.send_response(204)
        self.send_header("Access-Control-Allow-Origin", self.headers.get("Origin", "null"))
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.send_header("Access-Control-Max-Age", "600")
        self.end_headers()

    def do_GET(self):
        if not self._guard():
            return
        path = self.path.split("?", 1)[0]
        if path in ("/", "/index.html"):
            page = PAGE.read_bytes().replace(b'<html lang="en">', b'<html lang="en" data-served="dnwe">', 1)
            self._send(200, page, "text/html; charset=utf-8")   # marked: the page then calls this same address
        elif path == "/api/health":
            E = STATE["engine"]
            self._send(200, {"ready": E is not None, "error": STATE["error"],
                             "loading_seconds": round(time.time() - STATE["loading_since"]) if E is None else None,
                             "modes": list(E.MODES) if E else [], "intensities": list(E.FAMILIES_BY_INTENSITY) if E else [],
                             "default_mode": E.MODE if E else None, "default_intensity": E.INTENSITY if E else None,
                             "accepted": list(ACCEPTED)})
        elif path == "/favicon.ico":
            self.send_response(204); self.end_headers()
        else:
            self._send(404, {"error": "not found"})

    def do_POST(self):
        if not self._guard():
            return
        if self.path.split("?", 1)[0] != "/api/humanize":
            return self._send(404, {"error": "not found"})
        if STATE["engine"] is None:
            return self._send(503, {"error": STATE["error"] or "the engine is still loading; try again in a few seconds"})
        n = int(self.headers.get("Content-Length") or 0)
        if n <= 0 or n > MAX_BODY:
            return self._send(413, {"error": f"request must be between 1 byte and {MAX_BODY // 2**20} MB"})
        try:
            req = json.loads(self.rfile.read(n))
            self._send(200, humanize(req))
        except (ValueError, KeyError, json.JSONDecodeError) as e:
            self._send(400, {"error": str(e)})
        except Exception as e:
            traceback.print_exc()
            self._send(500, {"error": f"{type(e).__name__}: {e}"})

    def log_message(self, fmt, *args):
        if "/api/health" not in (args[0] if args else ""):
            sys.stderr.write(f"[http] {self.address_string()} {fmt % args}\n")


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--port", type=int, default=int(os.environ.get("DNWE_PORT", 8765)))
    ap.add_argument("--no-browser", action="store_true", help="do not open the page automatically")
    args = ap.parse_args()
    Handler.port = args.port
    httpd = ThreadingHTTPServer(("127.0.0.1", args.port), Handler)
    threading.Thread(target=load_engine, daemon=True).start()
    url = f"http://127.0.0.1:{args.port}/"
    print(f"DNWE server on {url}  (engine loading from {NOTEBOOK.name}; Ctrl+C to stop)", flush=True)
    if not args.no_browser:
        threading.Timer(0.5, lambda: webbrowser.open(url)).start()
    # closing the terminal (SIGHUP) or `kill` (SIGTERM) must stop LanguageTool too, exactly like Ctrl+C;
    # by default those signals end Python at once and leave a ~1 GB Java process running
    def _stop(signum, frame):
        raise KeyboardInterrupt
    for sig in (signal.SIGTERM, getattr(signal, "SIGHUP", None)):
        if sig is not None:
            signal.signal(sig, _stop)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nstopping", flush=True)
    finally:
        httpd.server_close()
        E = STATE["engine"]
        if E is not None and getattr(E, "_LT", None) is not None:
            E._LT.close()


if __name__ == "__main__":
    main()
