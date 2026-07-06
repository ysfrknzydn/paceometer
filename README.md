# The Paceometer

A literature review supporting a pace-based alternative to the speedometer, built over a summer research project with Dr. John Helveston.

A speedometer tells you how fast you're going. It doesn't tell you what that speed actually buys you. Time to cover a fixed distance is a hyperbola ($t = d/v$), not a straight line, so a fixed speed increase saves a lot of time at low speeds and almost none at high speeds, while crash risk and fuel consumption move in the opposite direction. A **pace** display, minutes required to cover a fixed distance shown alongside (or instead of) mph, makes that arithmetic visible instead of asking drivers to intuit it. This repository reviews the academic literature behind that idea.

## What's here

- **[`paceometer_review.html`](paceometer_review.html)** ([source: `paceometer_review.qmd`](paceometer_review.qmd)) is the main deliverable: a synthesis report covering the time-saving bias, speed vs. crash risk, speed vs. fuel consumption, eco-driving/ISA feedback effectiveness, gauge/dashboard design, and recommended evaluation instruments, with figures generated from primary-source numbers and one interactive tool. It also documents what the review considers the project's central open research question: whether a pace display's debiasing effect survives outside a lab and generalizes to real-world driving, since the one study that has directly tested this found that it does not for a static display, only for a more adaptive one.
- **[`lit_review.md`](lit_review.md)** is the working bibliography behind the report: abstracts, URLs, and access notes for every source, organized by topic cluster, plus a running list of follow-up research threads.
- **`scripts/`** regenerates the report's figures from the underlying data (`make_figures.py`), using shared styling and brand colors (`style.py`).
- **`_brand.yml`** is the Quarto brand file (colors, fonts) used to theme the report.
- **`figures/`** contains the generated chart images the report embeds.

Full text of the source PDFs isn't included in this repository since most are copyrighted journal articles behind institutional paywalls; `lit_review.md` links to each source (including open-access mirrors where available) instead.

## Rendering the report locally

Requires [Quarto](https://quarto.org) and Python.

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install jupyter matplotlib pandas numpy

quarto render paceometer_review.qmd
```

To regenerate the figures from scratch:

```bash
source .venv/bin/activate
cd scripts && python make_figures.py
```

To preview with live reload (needed to see the interactive speed-slider tool, which requires the page to be served over HTTP rather than opened directly from disk):

```bash
source .venv/bin/activate
quarto preview paceometer_review.qmd
```
