# PDF reconstruction and subsequent revision

Source: `prism-uploads/Ummah Connect Integrating Emotion-Aware Moderation in a Mahram-Safe Platform for Muslim Women.pdf`.

The initial conversion reconstructed the source wording and extracted its four screenshots. The current manuscript is a substantive revision following the later revision guide; it is no longer a verbatim transcription of the original paper.

## Assets preserved

The three existing architecture files (`figures/system-architecture.tikz`, `figures/emotion-analysis.tikz`, and `figures/mahram-access.tikz`) remain byte-for-byte unchanged by the revision. All four screenshot files also remain unchanged, and the cooldown asset is currently stored at `mahram-cooldown.png` in the project root. The two distress screenshots are placed side by side without cropping or modifying their pixels.

## Current documents

- `main.tex`: revised seven-section IEEE conference manuscript, six pages.
- `supplementary.tex`: six-page, explicitly unpopulated evaluation-chart and relationship-inventory resource.
- `REVISIONS.md`: detailed change log, all 25 requested visual categories, evidence limits, missing inputs, and reproduction commands.
- `data/README.md`: input schemas for real measurements; no empirical data has been invented.

Original malformed citation text and unresolved markers are corrected or replaced with verified citations. Unsupported numerical claims are explicitly identified as unverified. New recommendation values come only from a labeled synthetic example, not real participants or observed platform outcomes. Original figures and screenshots illustrate the documented prototype, not independently established effectiveness.
## Six-page author/layout update

The title now has three author blocks with the names and email addresses supplied by the authors. The main paper contains only the recommendation-criteria and computed worked-example tables. Seven auxiliary tables, including the former Tables VII and VIII, are preserved in `tables/omitted-main-tables.tex` and printed in the supplement as Tables S3–S9. `tables/supplementary-table-refs.tex` provides self-contained main-paper cross-references.

Retained main-paper prose, all ten figure captions, the bibliography text, and citation order are unchanged. Figures and screenshot assets remain byte-for-byte unchanged; only display sizing and placement are compacted. The title wraps onto two lines, related screenshots are paired, and float spacing is reduced. The six-page layout uses the IEEEtran 9-point option with modest line-spacing compaction; confirm that the target venue permits this font size before submission. No margins are reduced.