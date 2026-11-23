## DNWE 2.0 — Offline Deterministic Rebuild

## Plan

`Nov 1, 2026 ·`

## Verdict and scope decisions

A fully offline, non-generative DNWE is buildable on your current laptop. Expect a strong rule-and-statistics editor, not a free rewriter: it will cut wordiness, nominalisations, weak passives, repetition and grammar errors, and smooth paragraph flow, while leaving text it cannot safely improve untouched. The rebuild keeps the best ideas from v0.2 (protected-span masking, the semantic gate, per-section policy) and replaces the engine around them. Two decisions shape everything else.

Decision 1 — what "no pretrained neural models" means for parsing. spaCy's en_core_web_sm is a small CNN, so a strict reading of your rule excludes it (spaCy model card). The plan therefore uses non-neural analysers: Stanford's unlexicalised PCFG parser (statistical, Java, outputs Universal Dependencies) for syntax (Stanford Parser). NLTK's averaged-perceptron tagger (a linear model) for fast POS tagging. LemmInflect in dictionary-only mode, because its out-of-vocabulary path uses small neural nets (LemmInflect).

The parser sits behind one interface, so spaCy can be swapped in later if you decide a discriminative analyser (which never generates text) is acceptable. Decision 2 — the quality ceiling. Deterministic systems can only apply transformations someone has specified. Success is measured as lower error and style-issue counts with zero meaning violations, not as "sounds like a different writer".

## Hardware and storage

No GPU is needed at any point; your 16-core, 14 GB machine is well above the recommended tier. Figures for LanguageTool come from its deployment guides; the rest are planning estimates to be confirmed by the benchmark cell. Tier CPU RAM

Minimum 2 cores 4 GB

`Recommended 4–8 8 GB`

`cores`

`Full 8+ 12–16`

`cores GB`

LanguageTool fits one language in about 8–9 GB on disk, with some g credativ).

The Stanford PCFG parser needs lengths (Stanford Parser).

Java 17+ and pandoc are system d the notebook's environment. GPU: optional acceleration has no network.

## Selected tool stack

The biggest upgrade over v0.2 is the hand-written synonym lists with sco

`Job Selected`

Document model pandoc JSON AS

`panflute`

`Disk What it runs`

~3 GB Everything except LanguageTool n-grams; PCFG parsing on one core ~6 GB Parallel PCFG parsing, LanguageTool server, Simple PPDB loaded in memory

~16 Adds LanguageTool's English n-gram data

`GB+ for confusion-word detection`

n about 1 GB of RAM; its optional English n-gram set is guides reporting larger current builds (Railway guide,

roughly 100–500 MB per worker for typical sentence

dependencies; everything else installs with pip into

othing to accelerate, since no component is a neural

lexical resources: PPDB 2.0 and Simple PPDB replace ored, entailment-labelled paraphrases.

`Why it wins Licence`

ST + Reads DOCX, LaTeX, GPL / BSD Markdown into typed

`nodes: Math, Cite, Table`

`and Code are separate`

`from prose, so protection`

`is structural, not regex`

`(panflute)`

`Job Selected`

PDF structure GROBID in CRF-only mode

`Sentence pySBD`

`splitting`

POS tagging NLTK averaged perceptron

`Syntax Stanford PCFG parser`

`Morphology LemmInflect (dictionary`

`mode)`

Paraphrase PPDB 2.0 (S/M sizes)

`lexicon`

`Simplification Simple PPDB`

`lexicon`

`Nominalisations NOMLEX`

`Why it wins Licence`

Default models are linearApachechain CRFs, not deep 2.0 learning; about 0.3 s per PDF on 4 cores (GROBID,

`benchmarks)`

`Rule-based; passes MIT`

`97.92% of the English`

`Golden Rules (paper)`

Linear model, fast, no Apache-

`neural weights 2.0`

`Non-neural constituency GPL`

`+ UD dependency output`

`SPECIALIST-Lexicon- MIT`

`derived lemmas and`

`inflections; needed to re-`

`inflect verbs after`

`nominalisation edits`

Each pair carries an CC-BY

`Equivalence probability`

`and formality score, so`

`only bidirectional-`

`entailment swaps are`

`allowed (PPDB 2.0`

`features)`

4.5 million rules scored CC-BY

`for relative simplicity`

`(paper)`

Maps nouns to their research

`verbs with argument release`

correspondences,

`enabling "conducted an`

analysis of X" → "analysed

`X" (NOMLEX)`

`Job Selected`

Word senses WordNet (via NLTK)

Word frequency wordfreq (frozen data)

Academic AVL (Gardner & Davies) +

`vocabulary AWL (Coxhead)`

`Grammar LanguageTool local server`

`via language_tool_python`

Style rules Vale + proselint and writegood styles

`Abbreviations Schwartz–Hearst`

`( abbreviations package)`

`Metrics textstat, LexicalRichness`

`(MTLD, HD-D), sacrebleu`

`chrF`

Rejected: spaCy, Stanza and UDPipe 2 (neural) layout models); GROBID deep-learning models CRFs); PyMuPDF (AGPL, unnecessary); Concep

`Why it wins Licence`

`Synonym sets and WordNet`

`hypernyms for sense licence`

`checks`

Familiarity scores; data is MIT / CCno longer updated, which BY-SA is fine for a fixed

`resource (report)`

`Separates legitimate research`

`academic terms from lists`

`bloat; the lists cover`

`different ground, so use`

`both (comparison)`

`Rule-based, non-AI, Java LGPL-2.1`

`17+ (wrapper)`

`Markup-aware YAML MIT`

`rules, single Go binary`

`(Vale)`

`Classic deterministic MIT`

`acronym-definition`

`extraction`

`(implementation)`

`Readability, lexical MIT /`

`diversity, surface- Apache`

`preservation scores`

`(LexicalRichness)`

); Docling and Marker for PDFs (neural (neural, and only marginally better than its ptNet (noisy for substitution).

## Pipeline architecture

DNWE 2.0 pipeline · 8 stages, 1 gate The document is protected and analysed once; edits those that pass the gate become records you can acc

## Analysis before any edit

Every document gets a profile first, and every transfo that triggered it. No signal, no edit.

Level Signals measured

Document Section map, term glossary, acronym table, spelling variant (US/UK),

`hedging baseline, citation style`

Paragraph Topic continuity (lexical chains),

`transition-word density, repeated`

`sentence openers, length variance`

are proposed per sentence and only cept or reject.

ormation must cite the profile signal

`Tools`

`pandoc AST, GROBID, Schwartz–`

`Hearst, n-gram counts`

`WordNet chains, opener counts`

`Level Signals measured Tools`

Sentence Length, parse depth, clause count, PCFG parse, NOMLEX, hedge lexicon passive voice with/without agent,

`nominalisation density, hedges and`

`boosters, negation scope`

Word Frequency band, AVL/AWL wordfreq, AVL/AWL, PPDB formality membership, local repetition within a

`window, formality score`

Diagnostics Grammar and spelling matches, LanguageTool, Vale style-rule alerts

The profile also produces targets per register. For example, an academic paragraph flagged for sentence-length monotony triggers a split or merge only if that moves its variance toward the corpus range for academic prose.

## Transformation catalogue

Twelve transformation families operate on parse trees, not strings, which is what separates them from synonym swapping. Each one is a small, testable class with a precondition, an action and a guard.

Family Example Driven by Guard

Nominalisation → "conducted an NOMLEX + Subject and object verb analysis of the data" LemmInflect + parse preserved in the → "analysed the dependency tree

`data"`

Light-verb "make a decision" → Curated list + Tense and agreement collapse "decide" LemmInflect re-inflected

Wordy phrase "due to the fact that" Curated phrase list Exact phrase match reduction → "because" only Redundancy "past history", Curated pleonasm list Never inside quotes removal "completely or terms

`eliminate"`

`Family Example`

Passive → active "The samples were

`analysed by the`

`team" → "The team`

`analysed the`

`samples"`

`Lexical "utilise" → "use"`

`simplification`

`Repetition Third "significant" in`

variation a paragraph → PPDB

`equivalent`

`Sentence split Long coordinated`

`sentence → two`

`sentences`

Sentence merge Two short sentences

`sharing a subject`

`Opener variation Fronted adverbial`

moved in a run of

`identical openers`

`Transition repair Overused`

`"Moreover" replaced`

`or dropped`

Grammar and Agreement, articles,

`spelling typos`

Intensity selects which families run and the targets. Families can be toggled individually.

`Driven by Guard`

Parse with explicit Only when the agent by -agent is present; methods

`sections exempt`

Simple PPDB + PPDB Same POS, same Equivalence ≥ WordNet sense threshold family, not an AVL

`technical term`

Repetition window + Never on glossary

`PPDB terms or statistical`

`words`

Parse: coordinating Each part keeps a conjunction or subject and finite

`semicolon between verb`

`full clauses`

Parse + coreference Merged length under by repeated noun the register's limit Opener counts + Only movable

`parse adverbials`

`Transition-density Logical relation class`

`profile kept (addition stays`

`addition)`

`LanguageTool Only single-`

`matches suggestion fixes, not`

`in protected spans`

minimum confidence; mode selects register

`.`

## Meaning preservation, confidence, reversibility

An edit is applied only if it passes every hard invariant and its confidence clears the intensity threshold; otherwise the original sentence stays. Hard invariants (any failure = reject): 1. Protected nodes byte-identical: pandoc Math, Cite, Code, Table, footnotes, URLs, DOIs, numbers with units.

2. Negation count and scope unchanged after contraction canonicalisation. 3. Hedge and booster inventory unchanged ("may", "suggests", "significantly", "all",

`"only").`

4. Every content-word lemma in the original is still present, or replaced by a PPDB pair with Equivalence above threshold.

## 5. Dependency core preserved: each original subject–verb–object triple maps to one in

the output.

6. Glossary terms and acronyms untouched. Confidence score (0–1) per edit = the rule family's measured precision on a hand-labelled dev set × lexical resource score (PPDB Equivalence, Simple PPDB score) × context penalty (parse ambiguity, sentence length, proximity to a citation). Rule precision is measured, never assumed.

Reversibility. Every edit is stored as a record: span offsets, before, after, rule id, signal that triggered it, confidence, and invariants checked. Rejecting one edit re-renders the document from the original plus the remaining records, so edits never depend on each other silently; overlapping edits are resolved by highest confidence first.

## Document-level consistency

A first pass over the whole document builds a style ledger that every later edit reads and updates, so decisions made in section 2 hold in section 7. Term glossary: noun phrases that recur across sections, capitalised multiword terms, and every Schwartz–Hearst acronym. Glossary terms are never varied; if the author used two spellings of one term, the engine flags it rather than choosing. Acronym discipline: defined once at first use; later full-form repeats are suggestions, never automatic.

Spelling variant: majority US or UK spelling detected and enforced on non-quoted text. Substitution memory: once "utilise" everywhere, and a word chosen as a repetition problem.

Hedging profile per section: results no family may raise or lower it. Number and unit formatting: consist rewritten inside protected spans.

## Format handling

All formats converge on one internal mo runs inside Para and Header nodes are own format.

`Input Route in`

`DOCX pandoc reader`

`LaTeX pandoc reader with`

`+raw_tex`

`Markdown pandoc reader`

`TXT Paragraphs on blank`

`lines, regex protection`

of numbers, citations,

`URLs`

PDF (bornGROBID CRF → TEI digital) XML → sections,

`references, figure and`

`table captions`

→ "use" is applied, the same choice is reused replacement is excluded from becoming the next

and discussion keep the author's hedge density;

stent forms flagged ("10%" vs "10 percent"), not

odel: the pandoc AST, where only Str and Space e editable. Output is written back in the input's

Route out Known limit pandoc DOCX writer Complex Word styling using the original as -- (tracked changes, text reference-doc boxes) may simplify; a

`python-docx run-level`

`patcher is the fallback`

`for exact layout`

pandoc LaTeX writer, or Custom macros pass in-place span patching through as raw TeX and of the .tex source are never edited

pandoc Markdown None significant

`writer`

`Plain text No structural`

`protection, so regex`

`masking applies`

Markdown or DOCX Equations in PDFs (PDF cannot be edited survive only as in place) extracted text; no OCR

`for scans`

For LaTeX papers, in-place patching is the preferred output: each edited sentence is located in the original source by exact string match and replaced there, so your preamble, macros and layout are untouched. Sentences that cannot be matched unambiguously are reported, not edited.

## Notebook structure

One notebook, DNWE_2.ipynb , in 14 sections. Every section ends with an assertion cell, so a broken stage fails loudly instead of passing bad data on. 1. Environment check — Python, Java 17+, pandoc and Vale versions; CPU and RAM report; fails with exact install commands if anything is missing. 2. One-time resource install — pip packages, NLTK data, Stanford parser jar, LanguageTool, GROBID, PPDB S/M, Simple PPDB, NOMLEX, AVL/AWL; SHA-256 checksums recorded in a lockfile. The only cell that touches the network. 3. Offline guard — disables sockets for the rest of the session, so any accidental network call raises an error.

4. Resource loaders — PPDB and Simple PPDB compiled once into SQLite indexes for fast, low-memory lookup.

5. Ingestion — the five format readers from the previous section into the common AST. 6. Protection — structural masking plus regex fallback; round-trip test on every input. 7. Analysis — the profile and style ledger, displayed as tables. 8. Rule families — one class per family, each with inline unit tests drawn from real sentences.

9. Gate and confidence — invariant checks and the scoring model. 10. Orchestrator — runs families in a fixed order per sentence, resolves overlaps, writes edit records.

11. Review view — side-by-side diff with rule, reason and confidence per edit; accept/reject by id.

12. Export — write back to DOCX, LaTeX, Markdown or TXT. 13. Test corpus run — real papers end to end (next section). 14. Benchmark report — quality, preservation, speed and memory tables.

## Evaluation and benchmarks

The pass bar is zero hard-invariant violations across the improvement on the quality metrics. Every number in the notebook from real files; nothing is typed in by hand. Test corpus (real documents, stored locally): 5–10 of your own papers or drafts across DOCX, LaTeX 20–30 open-access papers (arXiv LaTeX sources and four fields.

A dev set of about 300 hand-labelled candidate edits change), used to measure each rule family's precision A held-out test set of the same size checks those thre

Dimension Metric

Integrity Protected-node byte match;

`negation, hedge, number and`

`glossary invariants`

Rule precision Correct edits ÷ applied edits, per family, on the held-out set

Grammar LanguageTool matches per 1,000

`words, before vs after`

Style Vale alerts per 1,000 words

Readability Flesch–Kincaid grade, mean and

`variance of sentence length`

Concision Word count change; nominalisation

`and passive density`

`Lexical diversity MTLD, HD-D`

Surface chrF between input and output

`preservation`

Speed Seconds per 1,000 words, per stage e full corpus, plus measured e report is computed by the

X and PDF.

PMC/PLOS PDFs) across at least

(correct / wrong / meaning n and set confidence thresholds. esholds.

`Pass criterion`

`100%`

≥ 0.95 per family at default

`intensity; families below are`

`disabled`

`Lower after, never higher`

`Lower after`

`Moves toward the register's`

`target range`

`Reduced without integrity loss`

`Not reduced`

Reported, used to detect over-

`editing`

Reported; target under 60 s for a

`10,000-word paper`

`Dimension Metric`

Memory Peak RSS (psutil) and Python

`allocations (tracemalloc), per stage`

Determinism SHA-256 of output across 3 runs

A small blind human check closes the loop: 50 sentence and meaning fidelity on a 1–5 scale, original vs edited in r

## Risks and build order

The main risk is parse errors on long academic sentence any edit whose parse is ambiguous rather than trusting t

Risk Effect

PCFG parse errors on 40+ Wrong split or passive word sentences conversion

`PPDB noise Wrong-sense`

`substitution`

DOCX round-trip loses Altered layout

`formatting`

PDF extraction quality Broken sentences, lost

`equations`

Licence mix (GPL parser, None for personal use CC-BY data)

Rule precision below target Bad edits

Build order — each phase ends with its notebook sectio

## 1. Environment, offline guard, ingestion and protection

sections 1–6).

## 2. Analysis profile and style ledger, checked on the real

`Pass criterion`

Reported; must fit in 8 GB

`Identical`

pairs per run, rated for fluency random order.

es; the plan contains it by refusing the parse.

`Mitigation`

`Structural families skip sentences`

above a length cap or with low parse probability

`Equivalence threshold, POS`

match, WordNet sense check,

`AVL term exclusion`

`Run-level python-docx patcher as`

`fallback`

`Prefer LaTeX/DOCX sources; PDF`

output always marked as derived

Revisit only if you ever distribute

`it`

`Family disabled automatically by`

`the benchmark`

ons passing their assertions: for all five formats (notebook

corpus (section 7).

## 3. Low-risk families first: wordy phrases, redundancy, light verbs, grammar fixes; then

gate and records (sections 8–10). 4. Dev-set labelling and precision measurement; thresholds set from data. 5. Structural families: nominalisation, passive, split/merge, opener and transition repair. 6. Lexical families: Simple PPDB simplification and repetition variation. 7. Export, review view and the full benchmark report (sections 11–14).

## Sources

Stanford Parser · GROBID · GROBID PLOS benchmark PPDB 2.0 feature list · Simple PPDB · NOMLEX pySBD · LemmInflect · Schwartz–Hearst implementation · LexicalRichness language_tool_python · LanguageTool on Railway · credativ LanguageTool guide · Vale panflute and pandoc AST · spaCy en_core_web_sm · AWL vs AVL · wordfreq sunset
