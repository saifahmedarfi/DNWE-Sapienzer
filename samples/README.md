# samples/

`ai_style_sample.pdf` is **synthetic test input**: a short report written on purpose in the style of
machine-drafted prose (stock phrases, stacked "Moreover/Furthermore" openers, uniform sentence lengths,
dashes, doubled hedges), with headings, a bullet list and a table. Upload it in the web app, or set
`MY_PAPER = BASE / "samples" / "ai_style_sample.pdf"` in section 21, to see every humanizer family act on
a PDF. It is kept out of `corpus/`, which holds the team's real documents.
