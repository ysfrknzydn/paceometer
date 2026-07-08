# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

A literature-review project for an app called "Paceometer" that the user is building with a professor over the summer. There are three deliverables, not one:

- **`lit_review.md`** — the working bibliography: abstracts, URLs, and access notes for every source, organized by topic cluster. This is a reference document, not prose to be read start-to-finish.
- **`paceometer_review.qmd`** (renders to `paceometer_review.html`) — a polished, professor-facing Quarto report that synthesizes the bibliography into a readable narrative with figures and one interactive tool. This is the actual thing the user presents.
- **`research_plan.qmd`** (renders to `research_plan.html`) — a forward-looking, prescriptive plan for the remaining summer weeks (an app-build track plus an experiment-design/IRB track), meant to be compared against the user's and professor's existing project roadmap. Not a synthesis of the literature. See "`research_plan.qmd` conventions" below.

Treat these as separate outputs with separate rules (below), not as drafts of each other.

## Commands

Render a report (from repo root; substitute `research_plan.qmd` for the other report):
```bash
source .venv/bin/activate
quarto render paceometer_review.qmd
```

Preview with live reload (also required to see `paceometer_review.qmd`'s interactive OJS tool — see caveat below):
```bash
source .venv/bin/activate
quarto preview paceometer_review.qmd
```

Regenerate the static figures the report embeds:
```bash
source .venv/bin/activate
cd scripts && python make_figures.py
```
This writes `fig01_*.png` … `fig09_*.png` into `figures/`, which the `.qmd`'s Python code cells (`echo: false`, `IPython.display.Image`) load by relative path. Figure numbering is meaningful (matches citation order in the report) — if you add a figure, extend the sequence rather than renumbering existing ones, since captions/alt-text reference specific fig numbers in prose.

**Caveat on viewing the rendered HTML**: opening `paceometer_review.html` directly via `file://` (double-click in Finder) renders everything *except* the live speed-slider tool in the durability-gap section — Chrome/Safari block the ES-module import (`import("https://esm.sh/@observablehq/plot@0.6")`) that OJS cell depends on when loaded from `file://`. Serve it (`quarto preview`, or `python3 -m http.server`) to see that piece working. `research_plan.html` has no OJS cells and opens fine directly from disk.

## Architecture

- **`pdfs/`** — 55 source PDFs the user has downloaded after reviewing `lit_review.md` entries.
- **`mds/`** — `markitdown`-converted plaintext of every PDF, **renamed to the article's actual title** (not the original download filename — e.g. `1-s2.0-S0001457509002772-main.pdf` became `Intelligent Speed Adaptation - Effects and Acceptance by Young Inexperienced Drivers (Young et al 2010).md`). Read from here, not `pdfs/`, for any full-text research task — it's the cheaper/faster path and titles are already resolved. One file, `1-s2.0-S0747563216304095-main.md`, is a **known mismatched/misfiled source** (converts to an unrelated paper on e-voting) and was deliberately left unrenamed rather than guessed at; flag it again if it resurfaces rather than assuming it's been fixed.
- **`scripts/style.py`** — shared matplotlib rcParams and the brand color constants (mirrors `_brand.yml`'s palette — keep the two in sync if the brand colors change).
- **`scripts/make_figures.py`** — the only source of truth for the report's charts. Every number plotted here was cross-checked against the primary source text in `mds/` (or the original PDF) before being committed to a chart — see the inline comment above the Section 4 fuel-economy figure for a specific example where a published equation, taken at face value, produced physically impossible values (a units-mismatch issue in the source paper, not a transcription error) and was replaced with a clearly-labeled illustrative curve instead. **Do not add a new figure from a number you haven't personally verified against the source text** — a plausible-sounding fork/agent summary is not sufficient grounding for something that will be presented to a professor.
- **`_brand.yml`** — Quarto brand file (colors, fonts), wired in via `format.html.brand: _brand.yml` in the `.qmd`'s YAML.
- **`.venv/`** — Python env with matplotlib/pandas/numpy/jupyter, required both for `make_figures.py` and for Quarto's Python code cells at render time. Activate it before running either `quarto render` or the figure script.
- **`research_plan.qmd`** has no Python code cells and doesn't read from `mds/`/`figures/`, but it does have two Mermaid diagrams (a Gantt timeline and a dependency/critical-path flowchart) styled with brand colors — see "Mermaid diagrams in research_plan.qmd" below before editing either. It cross-references `paceometer_review.qmd` by linking directly to anchors in the rendered `paceometer_review.html` (e.g. `[durability-gap section](paceometer_review.html#sec-durability-gap)`), not Quarto's `@sec-` syntax — `@sec-` cross-references only resolve within the same rendered document, not across separately-rendered `.qmd` files.

## `lit_review.md` conventions

The user's standing scope instruction: **"ALL I WANT is the abstracts and the URLs."** This file stays a bibliography with organizing context, not analysis — save synthesis/argument-building for the `.qmd` report.

Structure: numbered sections by topic cluster (0 = GW Libraries access notes, 1 = time-saving bias psychology, 2 = crash risk, 3 = fuel consumption, 4 = eco-driving/ISA feedback, 5 = dashboard/gauge UI + prior art, 6 = validated survey instruments, 7 = a completed round of follow-up deep-dives), each entry as Title / Authors / Year / Venue / URL / Abstract. A trailing **"Follow-up searches worth doing next"** list tracks open threads — check it before starting new research to avoid duplicating work, and append new threads rather than losing track of them.

When adding entries: mark uncertain fields explicitly (`unconfirmed, verify at URL`; `Abstract unavailable — see URL`), prefer adding an open-access mirror URL (ResearchGate, PMC, HAL, escholarship.org, rosap.ntl.bts.gov, arXiv) alongside paywalled publisher links, and flag secondary/explainer sources as such so the user knows to chase the primary citation before relying on them academically.

## `paceometer_review.qmd` conventions

This is a synthesis document — unlike `lit_review.md`, prose here is expected to interpret and connect findings, not just list them. Numbers and quotes still need to trace back to a verified source. Genuine open research gaps found in the literature (e.g. the durability of a static pace display's debiasing effect not being tested outside a lab) should be called out prominently — the user has explicitly asked for this kind of gap to be emphasized, not buried in a single sentence, since it's the project's actual research opportunity.

## Citing sources in `paceometer_review.qmd`

The report's `## References` section lists full citations (authors/year/venue/volume/pages), organized by the report's own section headers, not `lit_review.md`'s section numbers. When adding or correcting a citation there, verify author list, year, and venue directly against that source's own title page/header in `mds/` — don't trust a secondary listing (including `lit_review.md`'s own fields, several of which were originally marked `unconfirmed`) without checking. Where a field genuinely isn't stated or legible in the source itself (a masthead-less preprint, OCR loss on the title page), say so explicitly in the reference entry rather than guessing or dropping the source. Batch this kind of verification across parallel forks when checking many sources at once — it's local-file-only work, well suited to the fork pattern noted below.

## `research_plan.qmd` conventions

Unlike the other two files, this is a forward-looking, prescriptive plan, not a synthesis of the literature: two tracks (app development, experiment design & IRB) running in parallel across a fixed week count, a week-by-week milestones table, proof-of-concept exit criteria, and an "Open Questions for the Professor" section that doubles as a discussion agenda rather than a monologue.

**Voice**: written as if the user is the author, not Claude and not an outside advisor describing the project to "you and your professor." Default register is first-person-plural ("we"/"our") for joint work with the professor; second person ("you") is used only inside "Open Questions for the Professor," which is explicitly addressed to him. Don't reintroduce phrasing that narrates the project from outside (e.g. "the roadmap you and your professor sketched out") anywhere else in the document.

**Budget**: the project currently has zero funding beyond whatever is free for a GW student plus the user's personal Claude subscription. Treat this as a standing constraint on any tool, service, or platform recommendation in this document (it's why Phase 1 recommends a PWA over a native iOS app, and why Phase 2 defaults to a fixed reference speed instead of a metered speed-limit API), not a one-off caveat to check once.

**Realism**: neither the user nor the professor has built an app before, and implementation leans heavily on Claude Code. The week-by-week pacing was deliberately built around that (see the milestones table's own framing paragraph) rather than an experienced-developer's timeline. If you revise the plan, re-check pacing against that constraint instead of assuming it still holds.

## Mermaid diagrams in research_plan.qmd

Two Mermaid diagrams live here (`@fig-track-timeline`, a Gantt chart, and `@fig-critical-path`, a dependency flowchart), both styled to match `_brand.yml`'s palette via a `%%{init: {...}}%%` directive at the top of each code block. Quarto renders Mermaid client-side in the browser (not pre-rendered at `quarto render` time for HTML output), so the only way to verify a change actually worked is to render and then look at a real screenshot — see below. Specific bugs hit while building these, worth knowing before touching either diagram again:

- **Multi-line node labels in flowcharts**: the documented `["text<br/>more text"]` syntax (and the backtick markdown-string variant) renders with the lines overlapping/garbled under Quarto's renderer. The fix is `"flowchart": {"htmlLabels": false}` plus a plain quoted label containing a literal embedded newline (an actual line break inside the quotes, not `<br/>` or `\n`) — this forces Mermaid's older tspan-based text layout, which sizes the node correctly. This did **not** turn out to be a web-font-loading race (a plausible-looking theory that was tested and ruled out — changing `fontFamily` to a system font had zero effect on the bug).
- **Edge label text color** needs `fill`, not `color`, in `themeCSS` (e.g. `.edgeLabel tspan, .edgeLabel text { fill: #0B2545 !important; }`) — SVG text ignores CSS `color`.
- **Gantt milestones** have no dedicated color theme variable; recolor one by repurposing the otherwise-unused `done` class (`doneTaskBkgColor`/`doneTaskBorderColor`) and tagging the milestone task `:milestone, done, ...`.
- **A stray colored line cutting through the whole chart** is the `todayMarker` rendering at the clipped left edge when "today" falls before the chart's start date — add `todayMarker off`.
- **Bar/label width can't be calculated up front**; Mermaid's day-width-to-font-size ratio isn't something to derive from the config docs. The Gantt's task labels were shortened to fit by iterative screenshot testing, not by formula — expect to do the same for any new task label.

To verify any diagram edit, render (`quarto render research_plan.qmd`) then screenshot the real output rather than trusting the source by eye. A small `puppeteer-core` script pointed at the system's already-installed Chrome (`executablePath: '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'`) works without downloading a bundled Chromium; screenshot the specific figure element (e.g. `page.$('#fig-track-timeline')`) after waiting for its `svg` child to appear, then `Read` the resulting PNG. Every bug listed above was only found this way — the mermaid source looks plausible and is wrong in ways only a real render reveals.

## Repository / publishing

This project is a public GitHub repo (`ysfrknzydn/paceometer`), initialized partway through the project's life — check `git status`/`git log` before assuming a clean-slate history. `pdfs/` and `mds/` are gitignored and must stay that way: most of the 54 sources are copyrighted journal articles, and `mds/` is a full-text derivative of the same. `.venv/` and `.claude/` are also gitignored as local-only. Only commit when explicitly asked; when asked, follow the repo's existing commit-message style (see `git log`).

The professor views the rendered reports via `raw.githack.com` links straight to the `.html` files (e.g. `https://raw.githack.com/ysfrknzydn/paceometer/refs/heads/main/lit_review.html`), which serves the actual rendered HTML with the right content-type rather than GitHub's own file viewer. GitHub Pages is deliberately **not** enabled for this repo (confirmed via `gh api repos/ysfrknzydn/paceometer/pages` returning 404) — don't suggest turning it on as a fix for anything; raw.githack already solves the "professor needs to see the styled report, not source" problem for all three `.html` outputs. This matters directly for `lit_review.md`'s `**Jump to a section:**` line near the top: since it's viewed as rendered HTML, its anchors must match **Quarto/Pandoc's** auto-generated heading IDs, not GitHub's markdown-anchor rules — the two differ (Pandoc strips a heading's leading number and keeps periods; GitHub does the reverse), and mixing them up breaks the links silently. Verify the real IDs after any heading-text change with `grep -oE '<section id="[^"]*"' lit_review.html` (post-render), don't hand-compute them.

## Prose style in the `.qmd` reports

Both `paceometer_review.qmd` and `research_plan.qmd`'s prose were deliberately rewritten with the `humanizer` skill to remove AI-sounding patterns. Concretely: no em dashes used as clause separators anywhere in the prose (en dashes for numeric ranges and compound terms like "effectiveness–acceptability paradox" are fine and were kept), no negative-parallelism constructions ("not just X — it's Y") or tailing negations ("no polish yet"), minimal boldface reserved for genuinely load-bearing terms/numbers rather than whole-sentence emphasis. If you edit or add prose in either file, keep it consistent with that pass rather than reintroducing those patterns.

## Operational notes

- Forked subagents' (`Agent` tool, `subagent_type: "fork"`) WebSearch/WebFetch calls were rejected in this environment, likely because there's no live session to approve tool permissions for a background subagent. Forks work fine for **local file reads** (e.g., digesting a batch of `mds/` files in parallel), but do direct web research from the main conversation, not via forks.
- macOS ships bash 3.2 — no associative arrays (`declare -A`) in shell scripts; use plain sequential logic instead.
