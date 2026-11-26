# DNWE 2.0: results after the evaluation fixes (2026-11-26)

These numbers are measured against the baseline in `DNWE_eval_report.pdf` (engine `d006cf3`). The method was the same: the same 49 inputs, file and paste paths, 4 modes × 3 intensities (1,176 tests), and the same blind judge prompt.

## Before → after

| Measure | Baseline | After fixes |
|---|---|---|
| Judge: accept / minor-fix / reject | 69.2% / 18.3% / 12.4% (725 passages) | **95.8% / 4.0% / 0.1%** (695 passages) |
| Judge: fluency · naturalness · coherence · fidelity · suitability | 4.74 · 4.05 · 4.80 · 4.42 · 3.98 | **4.98 · 4.67 · 4.98 · 4.93 · 4.62** |
| Judge accept rate, conservative / balanced / extensive | 95.2% / 61.9% / 63.4% | **99.3% / 96.2% / 93.6%** |
| Sentences changed, conservative / balanced / extensive | 20.7% / 57.6% / 58.6% | 20.6% / **42.5%** / **49.1%** |
| Words changed, conservative / balanced / extensive | 4.96% / 9.73% / 9.88% | 5.54% / 7.93% / 8.69% |
| HTTP 500 responses (crashes) | 24 | **0** |
| 15,000-word document, end-to-end request | 59–197 s | **≤ 11 s** |
| Integrity failures, citations/URLs/numbers lost | 0 | 0 |
| Notebook tests | 129 | **192** (all pass) |

## What was fixed

1. **Synonym table (§11).**
   - Removed about 40 pairs the judge flagged, for example change→shift, independently→separately, systematically→methodically, suggest↔indicate, version↔variant, result→finding and identify→pinpoint.
   - Added context guards:
     - no swap after a determiner ("the proposed cluster")
     - no swap before a gerund ("difficulty concentrating")
     - "require X to …" is kept
     - past tense vs participle is decided by context, so "are selected" can no longer become "are chose"
2. **Spell-checker (§10).** English spelling "fixes" are skipped in non-English sentences; previously "cantidades" became "candidates".
3. **Restructuring (§11).**
   - No fronting past coordinated actions, so a condition can no longer end up governing every action.
   - "In this paper," and cliché frames are no longer moved to the end.
   - A ", which" split repeats the noun ("This optimizer …") and is refused when "which" is an object.
   - Long or dated location phrases stay where the author put them.
   - "A" is lower-cased when a phrase moves in front of it.
4. **Passive to active (§10).** Relative clauses are never rewritten, so "which can be scraped by P" no longer becomes "P can scrape which".
5. **Intensity (§11, §12).** The open-ended lexical swaps are off; every judged passage that used them was rejected.
   - **Balanced** now rewords about 60% of eligible sentences, so it sits between the other two levels.
   - **Extensive** rewords every sentence it safely can, including methods and results sections, which it treats at balanced strength.
6. **Clichés and register (§11).**
   - "In today's … landscape/world/…," openers are deleted, including after a run-in "Abstract".
   - "unlock the … power of" becomes "benefit from".
   - "plays a crucial role in" becomes the neutral "is central to".
   - Bad contractions ("you've any", "after that's built") are blocked, and a phrase deletion now beats a contraction.
7. **Web server diff (`server.py`).** Lines are aligned first and only changed lines are diffed word by word; this fixed the quadratic slowdown.
8. **Text encoding (§6).** Files are read as UTF-8, then Windows-1252/Latin-1; characters are no longer replaced with "�".
9. **Damaged and empty files.**
   - A damaged PDF or DOCX gets HTTP 400 with a plain message instead of a 500 with a raw exception.
   - Empty, whitespace-only and binary `.txt` uploads are refused, the same way an empty paste is.
   - Error messages name the user's file, not the server's temporary copy.
10. **DOCX downloads (§6).** ZIP entries get a fixed timestamp, so the same input gives the same bytes, as PDF exports already did.

## Caveats

- **Same model family.** The judge is the same model family as the evaluator, and each passage was scored once.
- **Reused verdicts.** In the final round, 576 passages were byte-identical to round-2 passages and kept their round-2 verdicts; only the 119 new passages were judged again.
- **Balanced now changes less.** It rewords 42.5% of sentences instead of 57.6%. Extensive is the "change as much as is safe" level.
- **Remaining issues.**
  - One judged passage was still rejected: a ", which" split repeated the nearest noun, but the clause referred to an earlier phrase.
  - Judges still describe extensive and conversational as mostly word-level; deeper restructuring at extensive is the next improvement.
