# DNWE 2.0 — Deterministic Natural Writing Engine

An offline writing engine and humanizer. It studies how a text is written, then rewrites its
vocabulary, syntax and discourse into more natural prose. A meaning gate rejects any edit that
touches negations, hedges, numbers, citations, connectives or content words outside the edit's
declared footprint.
It uses **no AI models**: no LLMs, no neural networks, no cloud. The notebook enforces this:
neural and language-model packages cannot be imported, and remote connections are refused.

Everything lives in one notebook: [`DNWE_2.ipynb`](DNWE_2.ipynb).

## Run it

1. Java 17+ and the project venv: `uv venv --seed -p 3.13 .venv && .venv/bin/pip install -r requirements.txt`
2. Put documents in `corpus/` (DOCX, Markdown, TXT, PDF directly; each LaTeX project in its own folder).
3. Open `DNWE_2.ipynb`, choose `MODE` and `INTENSITY` in section 1, then **Run All**.
   The first run downloads about 3 GB of resources once (section 2); later runs never touch the network.

| Setting | Options |
|---|---|
| `MODE` | `academic` · `technical` · `general` · `conversational` |
| `INTENSITY` | `conservative` (fixes + stock phrasing) · `balanced` (+ discourse/syntax reconstruction) · `extensive` (+ open lexical variation) |

To edit a single paper, use section 21.

## What you get in `out/`

- `<name>.dnwe.*`: the edited document, in its original format.
- `<name>.dnwe.review.html`: the style profile before → after, plus every edit with its rule, reason and confidence.
- `<name>.dnwe.edits.csv`: set `decision` to `reject` on any row, then re-render with `apply_decisions()`.
- `benchmark.csv`, `stage_timings.csv`, `determinism.csv`: quality, style, speed, memory and reproducibility.

## Make the confidences real: label the dev set

Confidence values are priors until someone labels real edits. Section 19 writes `out/dev_set.csv` and
`out/test_set.csv`. Mark each row **correct**, **wrong** or **meaning**, then run section 20.
A family needs 15 dev labels before its measured precision replaces the prior. Families below
0.95 precision switch off automatically. Labels follow the edit's content, not its position, and
every label is kept in `out/labels_archive.csv`.

## What the style markers are not

They count sentence-length variation, stock phrasing, connective density, repeated openers and
dashes. They are not an AI-detection or authorship score, and the engine does not optimise for
any detector.
