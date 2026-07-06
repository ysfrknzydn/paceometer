# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

A literature-review project for an app called "Paceometer" that the user is building with a professor over the summer. There are two deliverables, not one:

- **`lit_review.md`** — the working bibliography: abstracts, URLs, and access notes for every source, organized by topic cluster. This is a reference document, not prose to be read start-to-finish.
- **`paceometer_review.qmd`** (renders to `paceometer_review.html`) — a polished, professor-facing Quarto report that synthesizes the bibliography into a readable narrative with figures and one interactive tool. This is the actual thing the user presents.

Treat these as separate outputs with separate rules (below), not as drafts of each other.

## Commands

Render the report (from repo root):
```bash
source .venv/bin/activate
quarto render paceometer_review.qmd
```

Preview with live reload (also required to see the interactive OJS tool — see caveat below):
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

**Caveat on viewing the rendered HTML**: opening `paceometer_review.html` directly via `file://` (double-click in Finder) renders everything *except* the live speed-slider tool in the durability-gap section — Chrome/Safari block the ES-module import (`import("https://esm.sh/@observablehq/plot@0.6")`) that OJS cell depends on when loaded from `file://`. Serve it (`quarto preview`, or `python3 -m http.server`) to see that piece working.

## Architecture

- **`pdfs/`** — 55 source PDFs the user has downloaded after reviewing `lit_review.md` entries.
- **`mds/`** — `markitdown`-converted plaintext of every PDF, **renamed to the article's actual title** (not the original download filename — e.g. `1-s2.0-S0001457509002772-main.pdf` became `Intelligent Speed Adaptation - Effects and Acceptance by Young Inexperienced Drivers (Young et al 2010).md`). Read from here, not `pdfs/`, for any full-text research task — it's the cheaper/faster path and titles are already resolved. One file, `1-s2.0-S0747563216304095-main.md`, is a **known mismatched/misfiled source** (converts to an unrelated paper on e-voting) and was deliberately left unrenamed rather than guessed at; flag it again if it resurfaces rather than assuming it's been fixed.
- **`scripts/style.py`** — shared matplotlib rcParams and the brand color constants (mirrors `_brand.yml`'s palette — keep the two in sync if the brand colors change).
- **`scripts/make_figures.py`** — the only source of truth for the report's charts. Every number plotted here was cross-checked against the primary source text in `mds/` (or the original PDF) before being committed to a chart — see the inline comment above the Section 4 fuel-economy figure for a specific example where a published equation, taken at face value, produced physically impossible values (a units-mismatch issue in the source paper, not a transcription error) and was replaced with a clearly-labeled illustrative curve instead. **Do not add a new figure from a number you haven't personally verified against the source text** — a plausible-sounding fork/agent summary is not sufficient grounding for something that will be presented to a professor.
- **`_brand.yml`** — Quarto brand file (colors, fonts), wired in via `format.html.brand: _brand.yml` in the `.qmd`'s YAML.
- **`.venv/`** — Python env with matplotlib/pandas/numpy/jupyter, required both for `make_figures.py` and for Quarto's Python code cells at render time. Activate it before running either `quarto render` or the figure script.

## `lit_review.md` conventions

The user's standing scope instruction: **"ALL I WANT is the abstracts and the URLs."** This file stays a bibliography with organizing context, not analysis — save synthesis/argument-building for the `.qmd` report.

Structure: numbered sections by topic cluster (0 = GW Libraries access notes, 1 = time-saving bias psychology, 2 = crash risk, 3 = fuel consumption, 4 = eco-driving/ISA feedback, 5 = dashboard/gauge UI + prior art, 6 = validated survey instruments, 7 = a completed round of follow-up deep-dives), each entry as Title / Authors / Year / Venue / URL / Abstract. A trailing **"Follow-up searches worth doing next"** list tracks open threads — check it before starting new research to avoid duplicating work, and append new threads rather than losing track of them.

When adding entries: mark uncertain fields explicitly (`unconfirmed, verify at URL`; `Abstract unavailable — see URL`), prefer adding an open-access mirror URL (ResearchGate, PMC, HAL, escholarship.org, rosap.ntl.bts.gov, arXiv) alongside paywalled publisher links, and flag secondary/explainer sources as such so the user knows to chase the primary citation before relying on them academically.

## `paceometer_review.qmd` conventions

This is a synthesis document — unlike `lit_review.md`, prose here is expected to interpret and connect findings, not just list them. Numbers and quotes still need to trace back to a verified source. Genuine open research gaps found in the literature (e.g. the durability of a static pace display's debiasing effect not being tested outside a lab) should be called out prominently — the user has explicitly asked for this kind of gap to be emphasized, not buried in a single sentence, since it's the project's actual research opportunity.

## Operational notes

- Forked subagents' (`Agent` tool, `subagent_type: "fork"`) WebSearch/WebFetch calls were rejected in this environment, likely because there's no live session to approve tool permissions for a background subagent. Forks work fine for **local file reads** (e.g., digesting a batch of `mds/` files in parallel), but do direct web research from the main conversation, not via forks.
- macOS ships bash 3.2 — no associative arrays (`declare -A`) in shell scripts; use plain sequential logic instead.
