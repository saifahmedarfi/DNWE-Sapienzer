# DNWE 2.0
### Deterministic Natural Writing Engine

<p align="center">
  <strong>An offline writing engine. A deterministic humanizer. No AI models.</strong>
</p>

<p align="center">
  <code>OFFLINE</code> &nbsp;·&nbsp;
  <code>DETERMINISTIC</code> &nbsp;·&nbsp;
  <code>MEANING-PRESERVING</code> &nbsp;·&nbsp;
  <code>OPEN SOURCE</code>
</p>

---

## The Engine at a Glance

DNWE studies how a text is written, analyzes its linguistic and stylistic characteristics, and reconstructs its vocabulary, syntax, and discourse into more natural prose.

It uses **no AI models**: no LLMs, no neural networks, and no cloud inference.

The entire implementation lives in one executable Jupyter Notebook: **`DNWE_2.ipynb`**.

## Animated System Workflow

<div align="center">

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 1510" width="100%" role="img" aria-label="DNWE 2.0 animated deterministic writing engine workflow">
<defs>
  <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0%" stop-color="#090D20"/>
    <stop offset="50%" stop-color="#11152D"/>
    <stop offset="100%" stop-color="#071C2B"/>
  </linearGradient>
  <linearGradient id="cyan" x1="0" y1="0" x2="1" y2="0">
    <stop stop-color="#22D3EE"/><stop offset="100%" stop-color="#38BDF8"/>
  </linearGradient>
  <linearGradient id="purple" x1="0" y1="0" x2="1" y2="0">
    <stop stop-color="#A78BFA"/><stop offset="100%" stop-color="#818CF8"/>
  </linearGradient>
  <linearGradient id="pink" x1="0" y1="0" x2="1" y2="0">
    <stop stop-color="#F472B6"/><stop offset="100%" stop-color="#C084FC"/>
  </linearGradient>
  <linearGradient id="green" x1="0" y1="0" x2="1" y2="0">
    <stop stop-color="#34D399"/><stop offset="100%" stop-color="#A3E635"/>
  </linearGradient>
  <linearGradient id="orange" x1="0" y1="0" x2="1" y2="0">
    <stop stop-color="#FBBF24"/><stop offset="100%" stop-color="#FB923C"/>
  </linearGradient>
  <filter id="glow">
    <feGaussianBlur stdDeviation="5" result="blur"/>
    <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
  </filter>
  <filter id="soft">
    <feGaussianBlur stdDeviation="18"/>
  </filter>
  <style>
    text { font-family: Inter, Arial, sans-serif; }
    .title { fill:#F8FAFC; font-size:31px; font-weight:800; letter-spacing:2px; }
    .subtitle { fill:#94A3B8; font-size:14px; letter-spacing:2px; }
    .node-title { fill:#F8FAFC; font-size:19px; font-weight:700; }
    .node-sub { fill:#CBD5E1; font-size:12px; }
    .small { fill:#94A3B8; font-size:11px; }
    .line { fill:none; stroke-width:3; stroke-dasharray:9 12; animation: flow 2.5s linear infinite; }
    .pulse { animation: pulse 3s ease-in-out infinite; transform-box:fill-box; transform-origin:center; }
    .float { animation: float 5s ease-in-out infinite; }
    .glow-cyan { filter:url(#glow); }
    @keyframes flow { to { stroke-dashoffset:-42; } }
    @keyframes pulse { 0%,100% { opacity:.65; } 50% { opacity:1; } }
    @keyframes float { 0%,100% { transform:translateY(0); } 50% { transform:translateY(-5px); } }
  </style>
</defs>

<rect width="1200" height="1510" rx="28" fill="url(#bg)"/>
<circle cx="100" cy="280" r="150" fill="#06B6D4" opacity=".08" filter="url(#soft)"/>
<circle cx="1080" cy="700" r="180" fill="#A855F7" opacity=".08" filter="url(#soft)"/>
<circle cx="600" cy="1250" r="180" fill="#10B981" opacity=".07" filter="url(#soft)"/>

<text x="600" y="65" text-anchor="middle" class="title">DNWE 2.0</text>
<text x="600" y="94" text-anchor="middle" class="subtitle">DETERMINISTIC NATURAL WRITING ENGINE</text>
<text x="600" y="122" text-anchor="middle" fill="#67E8F9" font-size="12" letter-spacing="3">THE OFFLINE LINGUISTIC RECONSTRUCTION PIPELINE</text>

<!-- Input -->
<rect x="360" y="155" width="480" height="80" rx="16" fill="#102A43" stroke="#22D3EE" stroke-width="2"/>
<text x="600" y="187" text-anchor="middle" fill="#67E8F9" font-size="12" font-weight="700" letter-spacing="2">01 · DOCUMENT INPUT</text>
<text x="600" y="211" text-anchor="middle" class="node-title">DOCX · PDF · TXT · Markdown · LaTeX</text>

<path d="M600 235 V270" class="line" stroke="#22D3EE"/>

<!-- Parser -->
<rect x="360" y="270" width="480" height="82" rx="16" fill="#18213D" stroke="#38BDF8" stroke-width="2"/>
<text x="600" y="302" text-anchor="middle" fill="#7DD3FC" font-size="12" font-weight="700" letter-spacing="2">02 · DOCUMENT PROCESSOR</text>
<text x="600" y="327" text-anchor="middle" class="node-title">Structure · Sections · Paragraphs · Metadata</text>
<path d="M600 352 V388" class="line" stroke="#38BDF8"/>

<!-- Profiling -->
<rect x="270" y="388" width="660" height="112" rx="18" fill="#211B43" stroke="#A78BFA" stroke-width="2"/>
<text x="600" y="420" text-anchor="middle" fill="#C4B5FD" font-size="12" font-weight="700" letter-spacing="2">03 · LINGUISTIC &amp; BEHAVIORAL PROFILING</text>
<text x="600" y="449" text-anchor="middle" class="node-title">Sentence Patterns · Vocabulary · Syntax · Discourse</text>
<text x="600" y="475" text-anchor="middle" class="node-sub">Repetition · Connective Density · Readability · Style Markers</text>

<path d="M600 500 V535" class="line" stroke="#A78BFA"/>

<!-- Analysis split -->
<path d="M600 535 H300 V565 M600 535 H900 V565" fill="none" stroke="#C084FC" stroke-width="2" opacity=".8"/>
<rect x="75" y="565" width="450" height="112" rx="16" fill="#241B3A" stroke="#C084FC" stroke-width="2"/>
<text x="300" y="596" text-anchor="middle" fill="#D8B4FE" font-size="12" font-weight="700">04A · LEXICAL ANALYSIS</text>
<text x="300" y="624" text-anchor="middle" class="node-title">Vocabulary &amp; Word Selection</text>
<text x="300" y="649" text-anchor="middle" class="node-sub">Frequency · Context · Word Sense · Terminology</text>

<rect x="675" y="565" width="450" height="112" rx="16" fill="#1C2340" stroke="#818CF8" stroke-width="2"/>
<text x="900" y="596" text-anchor="middle" fill="#A5B4FC" font-size="12" font-weight="700">04B · SYNTACTIC ANALYSIS</text>
<text x="900" y="624" text-anchor="middle" class="node-title">Sentence &amp; Clause Structure</text>
<text x="900" y="649" text-anchor="middle" class="node-sub">Openers · Voice · Length · Complexity · Flow</text>

<path d="M300 677 V710 H600 V735 M900 677 V710 H600" fill="none" stroke="#C084FC" stroke-width="2" stroke-dasharray="6 8"/>

<!-- Planner -->
<rect x="300" y="735" width="600" height="92" rx="18" fill="#302047" stroke="#F472B6" stroke-width="2"/>
<text x="600" y="768" text-anchor="middle" fill="#F9A8D4" font-size="12" font-weight="700" letter-spacing="2">05 · TRANSFORMATION PLANNER</text>
<text x="600" y="797" text-anchor="middle" class="node-title">Mode · Intensity · Rule Selection · Confidence</text>

<path d="M600 827 V865" class="line" stroke="#F472B6"/>

<!-- Transform -->
<rect x="210" y="865" width="780" height="130" rx="18" fill="#29203C" stroke="#FB923C" stroke-width="2"/>
<text x="600" y="897" text-anchor="middle" fill="#FDBA74" font-size="12" font-weight="700" letter-spacing="2">06 · DETERMINISTIC RECONSTRUCTION</text>
<g class="pulse">
<rect x="250" y="920" width="160" height="45" rx="9" fill="#4A2841"/>
<text x="330" y="948" text-anchor="middle" fill="#FBCFE8" font-size="13" font-weight="600">Lexical</text>
<rect x="430" y="920" width="160" height="45" rx="9" fill="#41305C"/>
<text x="510" y="948" text-anchor="middle" fill="#DDD6FE" font-size="13" font-weight="600">Syntactic</text>
<rect x="610" y="920" width="160" height="45" rx="9" fill="#3D315B"/>
<text x="690" y="948" text-anchor="middle" fill="#C7D2FE" font-size="13" font-weight="600">Discourse</text>
<rect x="790" y="920" width="160" height="45" rx="9" fill="#49304A"/>
<text x="870" y="948" text-anchor="middle" fill="#F5D0FE" font-size="13" font-weight="600">Style</text>
</g>

<path d="M600 995 V1030" class="line" stroke="#FB923C"/>

<!-- Gate -->
<rect x="220" y="1030" width="760" height="126" rx="18" fill="#123A37" stroke="#34D399" stroke-width="2"/>
<text x="600" y="1063" text-anchor="middle" fill="#6EE7B7" font-size="12" font-weight="700" letter-spacing="2">07 · MEANING &amp; INTEGRITY GATE</text>
<text x="600" y="1093" text-anchor="middle" class="node-title">Protected Content · Declared Edit Footprint</text>
<text x="600" y="1122" text-anchor="middle" class="node-sub">Validate · Accept · Reject · Preserve Original</text>

<path d="M600 1156 V1190" class="line" stroke="#34D399"/>

<!-- Evaluation -->
<rect x="300" y="1190" width="600" height="90" rx="18" fill="#143A34" stroke="#A3E635" stroke-width="2"/>
<text x="600" y="1223" text-anchor="middle" fill="#BEF264" font-size="12" font-weight="700" letter-spacing="2">08 · QUALITY EVALUATION</text>
<text x="600" y="1253" text-anchor="middle" class="node-title">Integrity · Style · Quality · Determinism</text>

<path d="M600 1280 V1315" class="line" stroke="#A3E635"/>

<!-- Output -->
<rect x="360" y="1315" width="480" height="92" rx="18" fill="#123B42" stroke="#22D3EE" stroke-width="2"/>
<text x="600" y="1348" text-anchor="middle" fill="#67E8F9" font-size="12" font-weight="700" letter-spacing="2">09 · FINAL OUTPUT</text>
<text x="600" y="1378" text-anchor="middle" class="node-title">Edited Document · Review · Edit Log</text>

<text x="600" y="1460" text-anchor="middle" fill="#64748B" font-size="11" letter-spacing="2">NO LLM · NO NEURAL NETWORK · NO CLOUD INFERENCE</text>

<!-- Animated particles -->
<circle r="5" fill="#67E8F9" filter="url(#glow)">
  <animateMotion dur="5s" repeatCount="indefinite" path="M600 235 V500"/>
</circle>
<circle r="5" fill="#F0ABFC" filter="url(#glow)">
  <animateMotion dur="7s" repeatCount="indefinite" path="M600 500 V827"/>
</circle>
<circle r="5" fill="#6EE7B7" filter="url(#glow)">
  <animateMotion dur="6s" repeatCount="indefinite" path="M600 995 V1407"/>
</circle>
</svg>

</div>

---

## 01 — Environment & Execution

The entire system runs through one notebook.

### Requirements

- Java 17+
- Python 3.13
- Project virtual environment
- Dependencies listed in `requirements.txt`

### Setup

```bash
uv venv --seed -p 3.13 .venv
.venv/bin/pip install -r requirements.txt
```

### Document preparation

Place your documents in:

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

Each LaTeX project should be placed in its own folder.

### Execution

1. Open `DNWE_2.ipynb`.
2. Select `MODE` and `INTENSITY` in Section 1.
3. Execute **Run All**.
4. The first run downloads approximately 3 GB of resources in Section 2.
5. Subsequent runs operate offline without network access.

---

## 02 — Configuration

| Setting | Available options |
|---|---|
| `MODE` | `academic` · `technical` · `general` · `conversational` |
| `INTENSITY` | `conservative` · `balanced` · `extensive` |

### Transformation intensity

| Level | Behavior |
|---|---|
| Conservative | Fixes + stock phrasing |
| Balanced | Conservative + discourse/syntax reconstruction |
| Extensive | Balanced + open lexical variation |

The selected intensity controls the scope of transformations, while the selected mode controls the writing context.

---

## 03 — The Meaning Gate

Every transformation must remain within its declared edit footprint.

The meaning gate protects:

- Negations.
- Hedges and uncertainty.
- Numbers and percentages.
- Citations and references.
- Connectives.
- Content words outside the declared edit footprint.

A proposed transformation is rejected if it violates the protected-content rules.

**The objective is not simply to change the text. It is to improve its expression without silently changing what it says.**

---

## 04 — Output Architecture

All generated files are placed in `out/`.

```text
out/
│
├── document.dnwe.*
│
├── document.dnwe.review.html
│
├── document.dnwe.edits.csv
│
├── benchmark.csv
│
├── stage_timings.csv
│
├── determinism.csv
│
├── dev_set.csv
├── test_set.csv
└── labels_archive.csv
```

### Output descriptions

| Output | Purpose |
|---|---|
| `*.dnwe.*` | Edited document in its original format |
| `*.dnwe.review.html` | Before/after style profile and individual edit explanations |
| `*.dnwe.edits.csv` | Editable transformation decisions |
| `benchmark.csv` | Quality and performance evaluation |
| `stage_timings.csv` | Processing time by stage |
| `determinism.csv` | Reproducibility measurements |
| `dev_set.csv` | Development labels |
| `test_set.csv` | Test labels |
| `labels_archive.csv` | Persistent label history |

### Human review loop

```text
GENERATE EDITS
      |
      v
REVIEW HTML / CSV
      |
      v
ACCEPT OR REJECT
      |
      v
UPDATE DECISIONS
      |
      v
apply_decisions()
      |
      v
RENDER FINAL DOCUMENT
```

To reject an individual edit, set its `decision` field to:

```text
reject
```

Then re-render using:

```python
apply_decisions()
```

---

## 05 — Confidence Calibration

Confidence values initially represent **priors**, not proven accuracy.

The calibration process:

1. Section 19 generates `out/dev_set.csv` and `out/test_set.csv`.
2. Human reviewers label each development edit.
3. Accepted labels are recorded as `correct`, `wrong`, or `meaning`.
4. Section 20 calculates measured precision.
5. A transformation family needs at least 15 development labels before measured precision replaces its prior.
6. Families with precision below 0.95 are automatically disabled.
7. Every label is retained in `out/labels_archive.csv`.

Labels follow the edit's content, not its position in the document.

This makes confidence calibration dependent on actual reviewed transformations rather than arbitrary confidence scores.

---

## 06 — Style Markers

DNWE measures:

| Marker | What it examines |
|---|---|
| Sentence-length variation | Differences in sentence length |
| Stock phrasing | Frequency of conventional expressions |
| Connective density | Use of discourse connectives |
| Repeated openers | Recurring sentence beginnings |
| Dash frequency | Use of dashes |

**Important:** These measurements are linguistic and stylistic indicators, not AI-detection or authorship scores.

DNWE does not optimize its transformations for any AI detector.

---

## 07 — Offline Security Architecture

DNWE is designed around local execution.

```text
             LOCAL MACHINE
                  |
          DNWE_2.ipynb
                  |
        ┌─────────┴─────────┐
        |                   |
   LOCAL RESOURCES     LOCAL DOCUMENTS
        |                   |
        └─────────┬─────────┘
                  |
         DETERMINISTIC ENGINE
                  |
           LOCAL OUTPUTS
```

### Enforced restrictions

- No LLM imports.
- No neural-network imports.
- No language-model package imports.
- No cloud inference.
- No remote connections.
- No runtime network dependency.

The notebook enforces these restrictions by blocking prohibited imports and refusing remote connections.

---

## 08 — Single-Paper Processing

For an individual research paper, use **Section 21** of `DNWE_2.ipynb`.

The engine processes the selected document using the configured writing mode and intensity, then produces the edited document and its corresponding review artifacts.

---

## 09 — Project Identity

<div align="center">

### DNWE 2.0

**Understand the writing. Reconstruct the expression. Preserve the meaning.**

<br/>

<code>DETERMINISTIC BY DESIGN</code>

</div>

---

*All processing takes place locally. Initial resource acquisition requires an internet connection; subsequent executions are designed to remain offline.*
