<!-- ╔══════════════════════════════════════════════════════════════╗
     ║  DNWE 2.0 · README · single-file · animated SVG workflow       ║
     ║  Animations (CSS @keyframes + SMIL) play in any renderer that  ║
     ║  shows raw HTML/SVG: browsers, VS Code preview, Obsidian, etc. ║
     ╚══════════════════════════════════════════════════════════════╝ -->

<div align="center">

<!-- ░░░░░░░░░░░░░░░░░░░  HERO  ░░░░░░░░░░░░░░░░░░░ -->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 240" width="100%" role="img" aria-label="DNWE 2.0 — Deterministic Natural Writing Engine">
<defs>
  <linearGradient id="heroBg" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0%" stop-color="#0A0E24">
      <animate attributeName="stop-color" values="#0A0E24;#0B1830;#160A2E;#0A0E24" dur="12s" repeatCount="indefinite"/>
    </stop>
    <stop offset="100%" stop-color="#071C2B">
      <animate attributeName="stop-color" values="#071C2B;#0A1230;#1A0A2A;#071C2B" dur="12s" repeatCount="indefinite"/>
    </stop>
  </linearGradient>
  <linearGradient id="heroText" x1="0" y1="0" x2="1" y2="0">
    <stop stop-color="#22D3EE"/><stop offset="50%" stop-color="#A78BFA"/><stop offset="100%" stop-color="#F472B6"/>
  </linearGradient>
  <filter id="hGlow"><feGaussianBlur stdDeviation="6" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
  <filter id="hSoft"><feGaussianBlur stdDeviation="22"/></filter>
</defs>
<rect width="1200" height="240" rx="24" fill="url(#heroBg)"/>
<circle cx="160" cy="80" r="120" fill="#06B6D4" opacity=".10" filter="url(#hSoft)"><animate attributeName="opacity" values=".06;.16;.06" dur="7s" repeatCount="indefinite"/></circle>
<circle cx="1040" cy="170" r="140" fill="#A855F7" opacity=".10" filter="url(#hSoft)"><animate attributeName="opacity" values=".16;.06;.16" dur="9s" repeatCount="indefinite"/></circle>
<text x="600" y="110" text-anchor="middle" font-family="Inter,Arial,sans-serif" font-size="62" font-weight="800" letter-spacing="4" fill="url(#heroText)" filter="url(#hGlow)">DNWE&#160;2.0</text>
<text x="600" y="150" text-anchor="middle" font-family="Inter,Arial,sans-serif" font-size="16" letter-spacing="7" fill="#94A3B8">DETERMINISTIC&#160;·&#160;NATURAL&#160;·&#160;WRITING&#160;·&#160;ENGINE</text>
<g font-family="Inter,Arial,sans-serif" font-size="12" font-weight="700" letter-spacing="2">
  <text x="600" y="192" text-anchor="middle" fill="#67E8F9">OFFLINE&#160;&#160;·&#160;&#160;DETERMINISTIC&#160;&#160;·&#160;&#160;MEANING-PRESERVING&#160;&#160;·&#160;&#160;NO&#160;AI&#160;MODELS</text>
</g>
<rect x="2" y="2" width="1196" height="236" rx="24" fill="none" stroke="#22D3EE" stroke-width="1.5" opacity=".35"><animate attributeName="opacity" values=".15;.5;.15" dur="4s" repeatCount="indefinite"/></rect>
</svg>

<br/><br/>

![offline](https://img.shields.io/badge/runs-100%25%20offline-0ea5e9?style=for-the-badge&logo=ghostery&logoColor=white)
![deterministic](https://img.shields.io/badge/output-deterministic-a78bfa?style=for-the-badge)
![meaning](https://img.shields.io/badge/meaning-preserved-34d399?style=for-the-badge)
![no-ai](https://img.shields.io/badge/no%20LLM-no%20neural%20net-f472b6?style=for-the-badge)
![python](https://img.shields.io/badge/python-3.13-3776ab?style=for-the-badge&logo=python&logoColor=white)
![java](https://img.shields.io/badge/java-17+-f89820?style=for-the-badge&logo=openjdk&logoColor=white)

</div>

---

## ✦ The Engine at a Glance

**DNWE** studies *how* a text is written — its linguistic and stylistic fingerprint — and reconstructs its **vocabulary, syntax, and discourse** into more natural prose.

It uses **no AI models**: no LLMs, no neural networks, no cloud inference. The entire implementation lives in one executable notebook — **`DNWE_2.ipynb`**.

> [!NOTE]
> **Understand the writing · reconstruct the expression · preserve the meaning.**

---

## ⚡ Animated System Workflow

<div align="center">

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 1560" width="100%" role="img" aria-label="DNWE 2.0 animated deterministic writing engine workflow">
<defs>
  <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0%" stop-color="#090D20"><animate attributeName="stop-color" values="#090D20;#0B1330;#140A2A;#090D20" dur="14s" repeatCount="indefinite"/></stop>
    <stop offset="50%" stop-color="#11152D"/>
    <stop offset="100%" stop-color="#071C2B"><animate attributeName="stop-color" values="#071C2B;#0A1030;#1A0A2A;#071C2B" dur="14s" repeatCount="indefinite"/></stop>
  </linearGradient>
  <linearGradient id="cyan" x1="0" y1="0" x2="1" y2="0"><stop stop-color="#22D3EE"/><stop offset="100%" stop-color="#38BDF8"/></linearGradient>
  <linearGradient id="purple" x1="0" y1="0" x2="1" y2="0"><stop stop-color="#A78BFA"/><stop offset="100%" stop-color="#818CF8"/></linearGradient>
  <linearGradient id="pink" x1="0" y1="0" x2="1" y2="0"><stop stop-color="#F472B6"/><stop offset="100%" stop-color="#C084FC"/></linearGradient>
  <linearGradient id="green" x1="0" y1="0" x2="1" y2="0"><stop stop-color="#34D399"/><stop offset="100%" stop-color="#A3E635"/></linearGradient>
  <linearGradient id="orange" x1="0" y1="0" x2="1" y2="0"><stop stop-color="#FBBF24"/><stop offset="100%" stop-color="#FB923C"/></linearGradient>
  <filter id="glow"><feGaussianBlur stdDeviation="5" result="blur"/><feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
  <filter id="soft"><feGaussianBlur stdDeviation="18"/></filter>
  <style>
    text { font-family: Inter, Arial, sans-serif; }
    .title { fill:#F8FAFC; font-size:31px; font-weight:800; letter-spacing:2px; }
    .subtitle { fill:#94A3B8; font-size:14px; letter-spacing:2px; }
    .node-title { fill:#F8FAFC; font-size:19px; font-weight:700; }
    .node-sub { fill:#CBD5E1; font-size:12px; }
    .line { fill:none; stroke-width:3; stroke-dasharray:9 12; animation: flow 2.2s linear infinite; }
    .pulse { animation: pulse 3s ease-in-out infinite; transform-box:fill-box; transform-origin:center; }
    .brd { animation: brd 3.4s ease-in-out infinite; }
    @keyframes flow { to { stroke-dashoffset:-42; } }
    @keyframes pulse { 0%,100% { opacity:.6; } 50% { opacity:1; } }
    @keyframes brd { 0%,100% { stroke-opacity:.45; } 50% { stroke-opacity:1; } }
  </style>
</defs>

<rect width="1200" height="1560" rx="28" fill="url(#bg)"/>
<circle cx="100" cy="300" r="150" fill="#06B6D4" opacity=".08" filter="url(#soft)"><animate attributeName="opacity" values=".04;.12;.04" dur="8s" repeatCount="indefinite"/></circle>
<circle cx="1080" cy="760" r="180" fill="#A855F7" opacity=".08" filter="url(#soft)"><animate attributeName="opacity" values=".12;.04;.12" dur="10s" repeatCount="indefinite"/></circle>
<circle cx="600" cy="1300" r="180" fill="#10B981" opacity=".07" filter="url(#soft)"><animate attributeName="opacity" values=".04;.11;.04" dur="9s" repeatCount="indefinite"/></circle>

<text x="600" y="66" text-anchor="middle" class="title" filter="url(#glow)">PIPELINE</text>
<text x="600" y="95" text-anchor="middle" class="subtitle">OFFLINE&#160;LINGUISTIC&#160;RECONSTRUCTION</text>

<!-- 01 Input -->
<rect x="360" y="135" width="480" height="80" rx="16" fill="#102A43" stroke="#22D3EE" stroke-width="2" class="brd"/>
<text x="600" y="167" text-anchor="middle" fill="#67E8F9" font-size="12" font-weight="700" letter-spacing="2">01 · DOCUMENT INPUT</text>
<text x="600" y="191" text-anchor="middle" class="node-title">DOCX · PDF · TXT · Markdown · LaTeX</text>
<path d="M600 215 V252" class="line" stroke="#22D3EE"/>

<!-- 02 Processor -->
<rect x="360" y="252" width="480" height="82" rx="16" fill="#18213D" stroke="#38BDF8" stroke-width="2" class="brd"/>
<text x="600" y="284" text-anchor="middle" fill="#7DD3FC" font-size="12" font-weight="700" letter-spacing="2">02 · DOCUMENT PROCESSOR</text>
<text x="600" y="309" text-anchor="middle" class="node-title">Structure · Sections · Paragraphs · Metadata</text>
<path d="M600 334 V371" class="line" stroke="#38BDF8"/>

<!-- 03 Profiling -->
<rect x="270" y="371" width="660" height="112" rx="18" fill="#211B43" stroke="#A78BFA" stroke-width="2" class="brd"/>
<text x="600" y="403" text-anchor="middle" fill="#C4B5FD" font-size="12" font-weight="700" letter-spacing="2">03 · LINGUISTIC &amp; BEHAVIORAL PROFILING</text>
<text x="600" y="432" text-anchor="middle" class="node-title">Sentence Patterns · Vocabulary · Syntax · Discourse</text>
<text x="600" y="458" text-anchor="middle" class="node-sub">Repetition · Connective Density · Readability · Style Markers</text>
<path d="M600 483 V518" class="line" stroke="#A78BFA"/>

<!-- 04 split -->
<path d="M600 518 H300 V548 M600 518 H900 V548" fill="none" stroke="#C084FC" stroke-width="2" opacity=".8"/>
<rect x="75" y="548" width="450" height="112" rx="16" fill="#241B3A" stroke="#C084FC" stroke-width="2" class="brd"/>
<text x="300" y="579" text-anchor="middle" fill="#D8B4FE" font-size="12" font-weight="700">04A · LEXICAL ANALYSIS</text>
<text x="300" y="607" text-anchor="middle" class="node-title">Vocabulary &amp; Word Selection</text>
<text x="300" y="632" text-anchor="middle" class="node-sub">Frequency · Context · Word Sense · Terminology</text>
<rect x="675" y="548" width="450" height="112" rx="16" fill="#1C2340" stroke="#818CF8" stroke-width="2" class="brd"/>
<text x="900" y="579" text-anchor="middle" fill="#A5B4FC" font-size="12" font-weight="700">04B · SYNTACTIC ANALYSIS</text>
<text x="900" y="607" text-anchor="middle" class="node-title">Sentence &amp; Clause Structure</text>
<text x="900" y="632" text-anchor="middle" class="node-sub">Openers · Voice · Length · Complexity · Flow</text>
<path d="M300 660 V693 H600 V718 M900 660 V693 H600" fill="none" stroke="#C084FC" stroke-width="2" stroke-dasharray="6 8" class="line"/>

<!-- 05 Planner -->
<rect x="300" y="718" width="600" height="92" rx="18" fill="#302047" stroke="#F472B6" stroke-width="2" class="brd"/>
<text x="600" y="751" text-anchor="middle" fill="#F9A8D4" font-size="12" font-weight="700" letter-spacing="2">05 · TRANSFORMATION PLANNER</text>
<text x="600" y="780" text-anchor="middle" class="node-title">Mode · Intensity · Rule Selection · Confidence</text>
<path d="M600 810 V848" class="line" stroke="#F472B6"/>

<!-- 06 Transform -->
<rect x="210" y="848" width="780" height="130" rx="18" fill="#29203C" stroke="#FB923C" stroke-width="2" class="brd"/>
<text x="600" y="880" text-anchor="middle" fill="#FDBA74" font-size="12" font-weight="700" letter-spacing="2">06 · DETERMINISTIC RECONSTRUCTION</text>
<g class="pulse">
<rect x="250" y="903" width="160" height="45" rx="9" fill="#4A2841"/><text x="330" y="931" text-anchor="middle" fill="#FBCFE8" font-size="13" font-weight="600">Lexical</text>
<rect x="430" y="903" width="160" height="45" rx="9" fill="#41305C"/><text x="510" y="931" text-anchor="middle" fill="#DDD6FE" font-size="13" font-weight="600">Syntactic</text>
<rect x="610" y="903" width="160" height="45" rx="9" fill="#3D315B"/><text x="690" y="931" text-anchor="middle" fill="#C7D2FE" font-size="13" font-weight="600">Discourse</text>
<rect x="790" y="903" width="160" height="45" rx="9" fill="#49304A"/><text x="870" y="931" text-anchor="middle" fill="#F5D0FE" font-size="13" font-weight="600">Style</text>
</g>
<path d="M600 978 V1013" class="line" stroke="#FB923C"/>

<!-- 07 Gate -->
<rect x="220" y="1013" width="760" height="126" rx="18" fill="#123A37" stroke="#34D399" stroke-width="2" class="brd"/>
<text x="600" y="1046" text-anchor="middle" fill="#6EE7B7" font-size="12" font-weight="700" letter-spacing="2">07 · MEANING &amp; INTEGRITY GATE</text>
<text x="600" y="1076" text-anchor="middle" class="node-title">Protected Content · Declared Edit Footprint</text>
<text x="600" y="1105" text-anchor="middle" class="node-sub">Validate · Accept · Reject · Preserve Original</text>
<path d="M600 1139 V1173" class="line" stroke="#34D399"/>

<!-- 08 Eval -->
<rect x="300" y="1173" width="600" height="90" rx="18" fill="#143A34" stroke="#A3E635" stroke-width="2" class="brd"/>
<text x="600" y="1206" text-anchor="middle" fill="#BEF264" font-size="12" font-weight="700" letter-spacing="2">08 · QUALITY EVALUATION</text>
<text x="600" y="1236" text-anchor="middle" class="node-title">Integrity · Style · Quality · Determinism</text>
<path d="M600 1263 V1298" class="line" stroke="#A3E635"/>

<!-- 09 Output -->
<rect x="360" y="1298" width="480" height="92" rx="18" fill="#123B42" stroke="#22D3EE" stroke-width="2" class="brd"/>
<text x="600" y="1331" text-anchor="middle" fill="#67E8F9" font-size="12" font-weight="700" letter-spacing="2">09 · FINAL OUTPUT</text>
<text x="600" y="1361" text-anchor="middle" class="node-title">Edited Document · Review · Edit Log</text>

<text x="600" y="1448" text-anchor="middle" fill="#64748B" font-size="11" letter-spacing="2">NO LLM · NO NEURAL NETWORK · NO CLOUD INFERENCE</text>

<!-- particles -->
<circle r="5" fill="#67E8F9" filter="url(#glow)"><animateMotion dur="5s" repeatCount="indefinite" path="M600 215 V518"/></circle>
<circle r="5" fill="#F0ABFC" filter="url(#glow)"><animateMotion dur="7s" repeatCount="indefinite" path="M600 518 V810"/></circle>
<circle r="4" fill="#FDBA74" filter="url(#glow)"><animateMotion dur="4.5s" repeatCount="indefinite" path="M600 848 V1013"/></circle>
<circle r="5" fill="#6EE7B7" filter="url(#glow)"><animateMotion dur="6s" repeatCount="indefinite" path="M600 1013 V1390"/></circle>
</svg>

</div>

---

## 🛠️ 01 — Environment & Execution

The entire system runs through one notebook.

<table>
<tr><td>

**Requirements**
- Java **17+**
- Python **3.13**
- Project virtual environment
- Dependencies in `requirements.txt`

</td><td>

**Setup**
```bash
uv venv --seed -p 3.13 .venv
.venv/bin/pip install -r requirements.txt
```

</td></tr>
</table>

### 📁 Document preparation

```text
corpus/
├── research_paper.pdf
├── technical_document.docx
├── notes.md
├── document.txt
└── latex_project/
    ├── main.tex
    ├── references.bib
    └── sections/
```

> Each LaTeX project lives in its own folder.

### ▶️ Execution

```text
┌─ 1 ─ Open DNWE_2.ipynb
├─ 2 ─ Select MODE and INTENSITY in Section 1
├─ 3 ─ Run All
├─ 4 ─ First run downloads ≈ 3 GB of resources (Section 2)
└─ 5 ─ Every run after that is fully offline
```

---

## 🎛️ 02 — Configuration

| Setting | Available options |
|---|---|
| `MODE` | `academic` · `technical` · `general` · `conversational` |
| `INTENSITY` | `conservative` · `balanced` · `extensive` |

### Transformation intensity

| Level | Behavior |
|:--|:--|
| 🟢 **Conservative** | Fixes + stock phrasing |
| 🔵 **Balanced** | Conservative + discourse / syntax reconstruction |
| 🟣 **Extensive** | Balanced + open lexical variation |

*Intensity controls the **scope** of transformations; mode controls the **writing context**.*

---

## 🔐 03 — The Meaning Gate

Every transformation must stay within its **declared edit footprint**.

<div align="center">

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 210" width="100%" role="img" aria-label="Meaning gate protected content">
<defs>
  <filter id="g2"><feGaussianBlur stdDeviation="3" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
  <style>.chip{animation:cp 3s ease-in-out infinite;transform-box:fill-box;transform-origin:center}@keyframes cp{0%,100%{opacity:.75}50%{opacity:1}}</style>
</defs>
<rect width="1100" height="210" rx="20" fill="#0C1A18"/>
<rect x="2" y="2" width="1096" height="206" rx="20" fill="none" stroke="#34D399" stroke-width="1.5" opacity=".4"/>
<text x="550" y="44" text-anchor="middle" font-family="Inter,Arial" font-size="15" font-weight="700" letter-spacing="2" fill="#6EE7B7" filter="url(#g2)">🔒 PROTECTED CONTENT</text>
<g font-family="Inter,Arial" font-size="13" font-weight="600" fill="#D1FAE5">
<g class="chip"><rect x="60"  y="78" width="190" height="44" rx="12" fill="#12332E" stroke="#34D399"/><text x="155" y="105" text-anchor="middle">Negations</text></g>
<g class="chip"><rect x="270" y="78" width="250" height="44" rx="12" fill="#12332E" stroke="#34D399"/><text x="395" y="105" text-anchor="middle">Hedges &amp; uncertainty</text></g>
<g class="chip"><rect x="540" y="78" width="250" height="44" rx="12" fill="#12332E" stroke="#34D399"/><text x="665" y="105" text-anchor="middle">Numbers &amp; percentages</text></g>
<g class="chip"><rect x="810" y="78" width="230" height="44" rx="12" fill="#12332E" stroke="#34D399"/><text x="925" y="105" text-anchor="middle">Citations</text></g>
<g class="chip"><rect x="270" y="134" width="190" height="44" rx="12" fill="#12332E" stroke="#34D399"/><text x="365" y="161" text-anchor="middle">Connectives</text></g>
<g class="chip"><rect x="480" y="134" width="350" height="44" rx="12" fill="#12332E" stroke="#34D399"/><text x="655" y="161" text-anchor="middle">Content words outside the footprint</text></g>
</g>
</svg>

</div>

A proposed transformation is **rejected** if it violates the protected-content rules.

> [!IMPORTANT]
> **The objective is not simply to change the text. It is to improve its expression without silently changing what it says.**

---

## 📦 04 — Output Architecture

All generated files land in `out/`.

```text
out/
├── document.dnwe.*            → edited document, original format
├── document.dnwe.review.html  → before/after profile + per-edit explanations
├── document.dnwe.edits.csv    → editable transformation decisions
├── benchmark.csv              → quality & performance evaluation
├── stage_timings.csv          → processing time by stage
├── determinism.csv            → reproducibility measurements
├── dev_set.csv                → development labels
├── test_set.csv               → test labels
└── labels_archive.csv         → persistent label history
```

### 🔁 Human review loop

<div align="center">

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1160 150" width="100%" role="img" aria-label="Human review loop">
<defs>
  <linearGradient id="loop" x1="0" y1="0" x2="1" y2="0"><stop stop-color="#22D3EE"/><stop offset="50%" stop-color="#A78BFA"/><stop offset="100%" stop-color="#34D399"/></linearGradient>
  <marker id="arw" markerWidth="10" markerHeight="10" refX="7" refY="3" orient="auto"><path d="M0 0 L7 3 L0 6 Z" fill="#A78BFA"/></marker>
  <filter id="g3"><feGaussianBlur stdDeviation="2.5" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
  <style>.seg{stroke-dasharray:7 9;animation:fl 1.6s linear infinite}@keyframes fl{to{stroke-dashoffset:-32}}</style>
</defs>
<rect width="1160" height="150" rx="18" fill="#0B1020"/>
<g font-family="Inter,Arial" font-size="12.5" font-weight="700" fill="#E2E8F0">
<rect x="24"  y="52" width="168" height="46" rx="12" fill="#14233f" stroke="#22D3EE"/><text x="108" y="80" text-anchor="middle" fill="#67E8F9">GENERATE EDITS</text>
<rect x="246" y="52" width="196" height="46" rx="12" fill="#1b1f3c" stroke="#818CF8"/><text x="344" y="80" text-anchor="middle" fill="#A5B4FC">REVIEW HTML / CSV</text>
<rect x="496" y="52" width="196" height="46" rx="12" fill="#241b3a" stroke="#C084FC"/><text x="594" y="80" text-anchor="middle" fill="#D8B4FE">ACCEPT / REJECT</text>
<rect x="746" y="52" width="176" height="46" rx="12" fill="#2a1d3f" stroke="#F472B6"/><text x="834" y="80" text-anchor="middle" fill="#F9A8D4">apply_decisions()</text>
<rect x="976" y="52" width="160" height="46" rx="12" fill="#12332e" stroke="#34D399"/><text x="1056" y="80" text-anchor="middle" fill="#6EE7B7">RENDER DOC</text>
</g>
<g stroke="url(#loop)" stroke-width="3" fill="none" marker-end="url(#arw)">
<path class="seg" d="M192 75 H244"/><path class="seg" d="M442 75 H494"/><path class="seg" d="M692 75 H744"/><path class="seg" d="M922 75 H974"/>
</g>
<path class="seg" d="M1056 102 V124 H108 V102" stroke="#475569" stroke-width="2" fill="none" marker-end="url(#arw)"/>
<text x="582" y="140" text-anchor="middle" font-family="Inter,Arial" font-size="10.5" letter-spacing="2" fill="#64748B">set decision → reject, then re-render</text>
</svg>

</div>

To reject an individual edit, set its `decision` field to `reject`, then re-render with `apply_decisions()`.

---

## 🎯 05 — Confidence Calibration

Confidence values start as **priors**, not proven accuracy.

```text
① Section 19 → out/dev_set.csv + out/test_set.csv
② Reviewers label each development edit
③ Labels recorded as: correct · wrong · meaning
④ Section 20 → measured precision
⑤ ≥ 15 dev labels before measured precision replaces a family's prior
⑥ Families below 0.95 precision → auto-disabled
⑦ Every label kept in out/labels_archive.csv
```

> Labels follow the **edit's content**, not its position in the document — so calibration rests on actually-reviewed transformations, not arbitrary scores.

---

## 📐 06 — Style Markers

| Marker | What it examines |
|:--|:--|
| 📏 Sentence-length variation | Differences in sentence length |
| 🧱 Stock phrasing | Frequency of conventional expressions |
| 🔗 Connective density | Use of discourse connectives |
| 🔁 Repeated openers | Recurring sentence beginnings |
| ➖ Dash frequency | Use of dashes |

> [!WARNING]
> These are **linguistic & stylistic indicators**, *not* AI-detection or authorship scores. **DNWE does not optimize its transformations for any AI detector.**

---

## 🛡️ 07 — Offline Security Architecture

<div align="center">

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 420" width="80%" role="img" aria-label="Offline security architecture">
<defs>
  <linearGradient id="core" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#22D3EE"/><stop offset="100%" stop-color="#34D399"/></linearGradient>
  <filter id="g4"><feGaussianBlur stdDeviation="4" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
  <style>.ln{stroke-dasharray:8 10;animation:f4 1.8s linear infinite}@keyframes f4{to{stroke-dashoffset:-36}}.ring{animation:rp 4s ease-in-out infinite;transform-box:fill-box;transform-origin:center}@keyframes rp{0%,100%{opacity:.3}50%{opacity:.8}}</style>
</defs>
<rect width="1000" height="420" rx="22" fill="#07131A"/>
<circle cx="500" cy="210" r="150" fill="none" stroke="#22D3EE" stroke-width="1" class="ring"/>
<circle cx="500" cy="210" r="110" fill="none" stroke="#34D399" stroke-width="1" class="ring"/>
<text x="500" y="40" text-anchor="middle" font-family="Inter,Arial" font-size="13" font-weight="700" letter-spacing="3" fill="#64748B">LOCAL MACHINE — NO NETWORK EGRESS</text>
<g font-family="Inter,Arial" font-weight="700">
<rect x="390" y="78" width="220" height="56" rx="14" fill="#102A2E" stroke="url(#core)" stroke-width="2"/><text x="500" y="112" text-anchor="middle" font-size="15" fill="#67E8F9">DNWE_2.ipynb</text>
<rect x="110" y="250" width="250" height="56" rx="14" fill="#141d33" stroke="#818CF8" stroke-width="2"/><text x="235" y="284" text-anchor="middle" font-size="14" fill="#A5B4FC">LOCAL RESOURCES</text>
<rect x="640" y="250" width="250" height="56" rx="14" fill="#141d33" stroke="#818CF8" stroke-width="2"/><text x="765" y="284" text-anchor="middle" font-size="14" fill="#A5B4FC">LOCAL DOCUMENTS</text>
<rect x="360" y="180" width="280" height="60" rx="14" fill="#102A2E" stroke="#34D399" stroke-width="2"/><text x="500" y="216" text-anchor="middle" font-size="15" fill="#6EE7B7" filter="url(#g4)">DETERMINISTIC ENGINE</text>
<rect x="385" y="330" width="230" height="56" rx="14" fill="#123B42" stroke="#22D3EE" stroke-width="2"/><text x="500" y="364" text-anchor="middle" font-size="14" fill="#67E8F9">LOCAL OUTPUTS</text>
</g>
<g stroke="#34D399" stroke-width="2.5" fill="none">
<path class="ln" d="M500 134 V178"/>
<path class="ln" d="M235 250 V210 H360"/>
<path class="ln" d="M765 250 V210 H640"/>
<path class="ln" d="M500 240 V328"/>
</g>
</svg>

</div>

**Enforced restrictions:** `no LLM imports` · `no neural-network imports` · `no language-model packages` · `no cloud inference` · `no remote connections` · `no runtime network dependency`.

The notebook enforces these by **blocking prohibited imports** and **refusing remote connections**.

---

## 📄 08 — Single-Paper Processing

For an individual research paper, use **Section 21** of `DNWE_2.ipynb`. The engine processes the selected document under the configured mode and intensity, then emits the edited document and its review artifacts.

---

<div align="center">

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 170" width="100%" role="img" aria-label="DNWE 2.0 identity">
<defs>
  <linearGradient id="ftxt" x1="0" y1="0" x2="1" y2="0"><stop stop-color="#22D3EE"/><stop offset="50%" stop-color="#A78BFA"/><stop offset="100%" stop-color="#F472B6"/></linearGradient>
  <filter id="fg"><feGaussianBlur stdDeviation="5" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
</defs>
<rect width="1200" height="170" rx="22" fill="#0A0E24"/>
<rect x="2" y="2" width="1196" height="166" rx="22" fill="none" stroke="#A78BFA" stroke-width="1.5" opacity=".35"><animate attributeName="opacity" values=".15;.5;.15" dur="4s" repeatCount="indefinite"/></rect>
<text x="600" y="72" text-anchor="middle" font-family="Inter,Arial" font-size="40" font-weight="800" letter-spacing="3" fill="url(#ftxt)" filter="url(#fg)">DNWE 2.0</text>
<text x="600" y="108" text-anchor="middle" font-family="Inter,Arial" font-size="15" letter-spacing="1" fill="#CBD5E1">Understand the writing · Reconstruct the expression · Preserve the meaning</text>
<text x="600" y="140" text-anchor="middle" font-family="Inter,Arial" font-size="12" font-weight="700" letter-spacing="4" fill="#64748B">DETERMINISTIC BY DESIGN</text>
</svg>

<br/>

*All processing takes place locally. Initial resource acquisition needs an internet connection; every execution after that is designed to remain offline.*

</div>
