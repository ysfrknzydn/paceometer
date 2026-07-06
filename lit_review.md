# Paceometer — Literature Review

Compiled abstracts and URLs. Organized by topic cluster. Drop PDFs into this
folder (e.g. `pdfs/`) as you review each entry — filenames matching the
first author + year (e.g. `svenson2008.pdf`) will make them easy to match
back to this list.

---

## 0. Using GW Libraries to get full text (and find more)

I can't log into GW's authenticated systems myself, so I couldn't pull full
text for everything below — several entries are marked "Abstract
unavailable — see URL" because the open web only shows an abstract page
behind a paywall. As a GWU student you likely have full-text access to most
of these already. Two ways in:

- **EZproxy/VPN + direct URL**: log into GW's library system first (or
  connect to the GW VPN), then click the same URLs in this document —
  paywalled publishers (Elsevier/ScienceDirect, SAGE, IEEE Xplore) will
  often recognize your GW session and unlock automatically.
- **Journal Search / Discovery**: paste the article title into GW's main
  library discovery search (library.gwu.edu) or the "Find Journals by
  Journal Title" tool — this resolves via GW's link resolver even when the
  publisher URL itself doesn't recognize you.

### Which GW database to search, by cluster

| Cluster | Best GW database(s) | Why |
|---|---|---|
| 1. Time-saving bias psychology | **PsycINFO**, **PsycARTICLES** | These are the canonical indexes for Svenson/Peer/Eriksson-style cognitive psychology work — likely surfaces additional citing/cited papers this web search missed (e.g. non-English replications, dissertations). |
| 2. Speed vs. crash risk | **TRID**, **Compendex** | TRID is the transportation-research-specific index (has direct records for Nilsson, Elvik, Kloeden); Compendex catches the more engineering-flavored crash-modelling papers. |
| 3. Fuel consumption / drag / fuel economy | **Compendex**, **IEEE All-Society Periodicals Package** | Compendex indexes SAE-style automotive engineering journals directly — likely the fastest way to find the primary (non-secondary-source) papers on speed-vs-fuel-consumption curves that this web search couldn't pin down (see "follow-up searches" at the end of this document). |
| 4. Eco-driving feedback / ISA / HMI | **IEEE ASPP**, **ACM Digital Library**, **TRID** | ISA and driver-feedback studies are frequently published in IEEE Intelligent Transportation Systems venues or ACM AutoUI/CHI proceedings — neither is well covered by general web search. |
| 5. Prior art & dashboard UI | **ACM Digital Library**, **IEEE ASPP** | Gauge/dashboard design and HUD studies are heavily an HCI/AutoUI literature, which lives in ACM/IEEE, not general search engines. |
| 6. Validated UX/acceptance instruments | **PsycTESTS**, **Mental Measurements Yearbook w/ Tests in Print**, **PsycINFO** | **PsycTESTS is the single best resource for this section** — it holds the actual test records (full item wording, scoring instructions, and reported reliability/validity data) for instruments like the SUS, NASA-TLX, and TAM scales, which is more rigorous than the secondary web pages this document currently cites. Search PsycTESTS directly for "Van der Laan acceptance scale," "System Usability Scale," "NASA Task Load Index," and "Technology Acceptance Model" to get the authoritative instrument records. Mental Measurements Yearbook is the equivalent resource if PsycTESTS doesn't have a given instrument. |

### Specific papers in this document worth re-fetching via GW access
These hit a paywall (HTTP 403) or gave only a search-snippet summary during
this research, so the version in this document may be incomplete — get the
full text via GW's ScienceDirect/IEEE access before citing:
- Elvik, "A re-parameterisation of the Power Model..." (2013) — Section 2
- Fuller, "The task-capability interface model of the driving process" — Section 1
- Herberz, Kacperski & Kutzner, "Reducing the time loss bias..." (2019) — Section 1
- "Managing Effectiveness and Acceptability in Intelligent Speed Adaptation Systems" (IEEE) — Section 4
- Cameron & Elvik, "Nilsson's Power Model... urban roads" (2010) — Section 2
- "Updated estimates of the relationship between speed and road safety..." (2019) — Section 2
- Van der Laan, Heino & De Waard (1997), original Power Model paper — Section 6
- "Gauges design for a digital instrument cluster..." (2019) — Section 5 (a free copy may already be at the HAL link listed in that entry — check that first)

---

## 1. Time-Saving Bias & Speed Misperception (core psychology)

This is the academic foundation of the whole app concept: people misjudge
how much time is saved by increasing speed because time = distance/speed is
a hyperbolic (curvilinear) function, not linear. **Note: Peer & Gamliel
(2013), below, already invented and tested a device they literally call the
"Paceometer."** This is the single most important paper for this project —
read it first.

### Pace yourself: Improving time-saving judgments when increasing activity speed
- Authors: Eyal Peer, Eyal Gamliel
- Year: 2013
- Venue/Journal: Judgment and Decision Making, Vol. 8, No. 2, pp. 106–115
- URL: https://www.sas.upenn.edu/~baron/journal/12/121007/jdm121007.html
- Also: https://www.cambridge.org/core/journals/judgment-and-decision-making/article/pace-yourself-improving-timesaving-judgments-when-increasingactivity-speed/73B5AE666D64F1B4DCA7ED4A0A960F81
- Also (with figures of the actual Paceometer device): https://www.researchgate.net/publication/288763459_Pace_yourself_Improving_time-saving_judgments_when_increasing_activity_speed
- Abstract: People systematically misestimate time savings from speed increases — underestimating at low speeds, overestimating at high speeds — because they fail to recognize the curvilinear relationship between speed and time reduction. The authors introduce converting speed measurements to "pace" (minutes per fixed distance) as a debiasing technique. They present a device called the **"Paceometer"** — a modified speedometer that displays the minutes required to complete a fixed distance (10 miles/10 km) at selected speeds, alongside conventional mph/kph. In laboratory and driving-simulator settings, participants given pace data made more accurate estimations of journey duration, time-savings from speed increases, and the speed required to arrive on time, compared to participants given only speed data.

### Reducing the time loss bias: Two ways to improve driving safety and energy efficiency
- Authors: Mario Herberz, Celina Kacperski, Florian Kutzner
- Year: 2019
- Venue/Journal: Accident Analysis & Prevention, Vol. 131, pp. 8–14
- URL: https://www.sciencedirect.com/science/article/abs/pii/S0001457518304809
- DOI: https://doi.org/10.1016/j.aap.2019.06.007
- Abstract: The "time loss bias" is the mirror-image bias — people overestimate the time *lost* when decelerating from high speed. This paper is a direct follow-up test of the Peer & Gamliel Paceometer concept: it tests two interventions in the lab. Providing pace information (min/km) alongside speed had only a **short-term** debiasing effect. Adaptively providing participants with their actual, personalized time losses in real time **eliminated** the bias. Important caveat for this project: the simple static pace display alone may not be enough on its own — durability of the effect may require adaptive/personalized feedback.

### Decisions among time saving options: When intuition is strong and wrong
- Authors: Ola Svenson
- Year: 2008
- Venue/Journal: Acta Psychologica, Vol. 127, Issue 2, pp. 501–509
- URL: https://www.sciencedirect.com/science/article/abs/pii/S000169180700100X
- Also: https://www.researchgate.net/publication/5909620_Decisions_among_time_saving_options_When_intuition_is_strong_and_wrong
- Abstract: The foundational paper on the time-saving bias. When people judge time saved by increasing the speed of an activity, they overestimate time saved at high speeds because they follow a "Proportion heuristic" (judging time saved as proportional to the speed increase from the initial speed) rather than the true reciprocal relationship. A driving-choice study found people incorrectly chose to raise a road's speed from 70→110 km/h over raising a different road's speed from 30→40 km/h, even though the latter saves more time. A second study found the same bias in a healthcare planning context (clinic reorganization), suggesting it's a general cognitive bias, not driving-specific.

### Speeding and the time-saving bias: How drivers' estimations of time saved in higher speed affects their choice of speed
- Authors: Eyal Peer
- Year: 2010
- Venue/Journal: Accident Analysis & Prevention, Vol. 42, Issue 6, pp. 1978–1982
- URL: https://pubmed.ncbi.nlm.nih.gov/20728651/
- Also: https://www.researchgate.net/publication/45799120_Speeding_and_the_time-saving_bias_How_drivers'_estimations_of_time_saved_in_higher_speed_affects_their_choice_of_speed
- Also: https://www.sciencedirect.com/science/article/abs/pii/S0001457510001673
- Abstract: Tests how the time-saving bias translates into actual speed choice. Drivers estimated time savings from acceleration, the speed required for on-time arrival, their personally preferred speed, and predicted other drivers' choices. Drivers who showed a stronger time-saving bias indicated significantly higher required/preferred speeds across all measures and reported exceeding posted speed limits more often — directly linking the cognitive bias to real-world speeding behavior.

### The time-saving bias: Judgements, cognition and perception
- Authors: Gabriella Eriksson, Ola Svenson, Lars Eriksson
- Year: 2013
- Venue/Journal: Judgment and Decision Making, Vol. 8, Issue 4
- URL: https://www.cambridge.org/core/journals/judgment-and-decision-making/article/timesaving-bias-judgements-cognition-and-perception/719FE5568029C6BE7ED418B27E52BF0E
- Abstract: Extends the time-saving bias from hypothetical judgment tasks into an actual driving simulator. Participants drove a set distance at an assigned speed, then had to choose a new speed they believed would save exactly 3 minutes over the same distance. They underestimated time savings when accelerating from low speeds (30 km/h) and overestimated savings from higher speeds (100 km/h) — showing the bias persists even with direct perceptual/experiential feedback from driving itself, not just abstract judgment.

### Driving speed changes and subjective estimates of time savings, accident risks and braking
- Authors: Ola Svenson
- Year: 2009
- Venue/Journal: Applied Cognitive Psychology
- URL: https://onlinelibrary.wiley.com/doi/10.1002/acp.1471
- Abstract: Abstract unavailable via search — see URL. Studies how subjective estimates of time saved, accident risk, and braking distance change together as a function of driving speed changes; relevant if the app later wants to pair the pace display with risk-perception feedback.

### Exploring the time-saving bias: How drivers misestimate time saved when increasing speed
- Authors: Eyal Peer (with additional analysis building on Svenson's paradigm)
- Year: 2011
- Venue/Journal: Judgment and Decision Making
- URL: https://www.cambridge.org/core/journals/judgment-and-decision-making/article/exploring-the-timesaving-bias-how-drivers-misestimate-time-saved-when-increasing-speed/04BFC4A7CEF6B6B9C413B86FEF33E536
- Also: https://www.researchgate.net/publication/49596600_Exploring_the_time-saving_bias_How_drivers_misestimate_time_saved_when_increasing_speed
- Abstract: Abstract unavailable via search — see URL. Further empirical exploration of the conditions under which the time-saving bias occurs and its magnitude across different speed ranges.

### When two motivations race: The effects of time-saving bias and sensation-seeking on driving speed choices
- Authors: (Peer et al. — exact author order unconfirmed, verify at URL)
- Year: unconfirmed, verify at URL
- Venue/Journal: unconfirmed, verify at URL
- URL: https://www.researchgate.net/publication/231611173_When_two_motivations_race_The_effects_of_time-saving_bias_and_sensation-seeking_on_driving_speed_choices
- Abstract: Abstract unavailable via search — see URL. Investigates how the time-saving bias interacts with sensation-seeking personality traits in determining driving speed choice — potentially relevant for user-segmentation if the app targets a psychographic subgroup.

### The task-capability interface model of the driving process
- Authors: Ray Fuller
- Year: 2000 / later refined 2005, 2008
- Venue/Journal: Transportation Research Part F
- URL: https://www.sciencedirect.com/science/article/abs/pii/S0761898000900062
- Also (diagram): https://www.researchgate.net/publication/251012088_The_task-capability_interface_model_of_the_driving_process
- Abstract: Not the time-saving bias literature directly, but the standard theoretical model of how drivers regulate speed: driving difficulty arises from the interaction between task demand (strongly driven by speed) and driver capability. Drivers homeostatically adjust speed to keep perceived task difficulty within a tolerable range — raising speed when a road feels "too easy." Useful framing for why a pace display might change behavior: it changes the perceived "reward" side of the demand/capability/reward equation, not just difficulty.

### Deep dive: Is the "durability gap" real? (Does a static pace display keep working over time?)

**Short answer: yes, this is a real and still-open gap, not a one-off finding.**
It's directly documented in the primary literature, and it matches a much
broader, independently-replicated pattern in the general cognitive-debiasing
literature. Read the entries below together with Peer & Gamliel (2013) and
Herberz, Kacperski & Kutzner (2019) above.

### Reducing the time loss bias: Two ways to improve driving safety and energy efficiency (expanded notes)
See full citation above under Section 1. Additional detail from this deep
dive: the study used a video-based, controlled-access-highway driving
scenario and directly pitted the static **Paceometer** (pace info added to
the speedometer) against a newly designed **"Pop-up assistant"** that
adaptively tells the driver, in the moment, how much time a given
deceleration will actually cost. A mixed-design ANOVA found both tools
improved time-loss estimation, but the Pop-up assistant was superior and
produced **temporal spillover effects** — the correction generalized beyond
the exact scenario it was trained on, which the static pace display did not
achieve as strongly. The authors explicitly note that whether a Paceometer
would keep correcting drivers' intuitions under **daily, real-world driving**
is an open question for future research — as of this search, no published
study has closed that gap. That's the crux of your app's core research
contribution opportunity: nobody has tested this in the field yet.

### Retention and Transfer of Cognitive Bias Mitigation Interventions: A Systematic Literature Study
- Authors: J.E. (Hans) Korteling, Jasmin Y.J. Gerritsma, Alexander Toet
- Year: 2021
- Venue/Journal: Frontiers in Psychology
- URL: https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2021.629354/full
- Also: https://pmc.ncbi.nlm.nih.gov/articles/PMC8397507/
- Abstract: Systematic review of cognitive bias mitigation research; of 52 candidate studies, only **12 adequately measured retention (≥14 days) or transfer to new contexts**. Where durability was found, effects persisted up to 12 weeks — but almost exclusively in interventions that were **repeated** (multiple play sessions beat single sessions) and **active/experiential** (games consistently outperformed passive video/information interventions). The review's overall conclusion is blunt: there is currently **insufficient evidence that bias-mitigation interventions substantially improve real-world decisions**, and genuine behavioral transfer to real life remains "barely known." This is the general-literature backdrop that makes the Herberz et al. (2019) finding about the static Paceometer unsurprising — a single passive display is exactly the profile of intervention this review finds weakest, and durability data for the Paceometer specifically simply doesn't exist yet.

### Debiasing Decisions: Improved Decision Making With a Single Training Intervention
- Authors: Carey K. Morewedge, Haewon Yoon, Irene Scopelliti, Carl W. Symborski, James H. Korris, Karim S. Kassam
- Year: 2015
- Venue/Journal: Policy Insights from the Behavioral and Brain Sciences, Vol. 2, Issue 1, pp. 129–140
- URL: https://journals.sagepub.com/doi/abs/10.1177/2372732215600886
- Also: https://www.researchgate.net/publication/281206303_Debiasing_Decisions_Improved_Decision_Making_With_a_Single_Training_Intervention
- Abstract: Important counter-example/nuance to the durability problem. Two longitudinal experiments found that a **single training session** — either an instructional video or, more effectively, playing a computer game — produced medium-to-large debiasing effects for other well-known biases (bias blind spot, confirmation bias, fundamental attribution error) that **persisted for months**, not just minutes. The key design variable isn't repetition per se — it's whether the intervention is **active/experiential** (a game) rather than **passive** (just being shown information, which is what a static gauge does). This reframes the design implication for your app: the fix for durability may not strictly require "adaptive, personalized" feedback — it may more fundamentally require making the pace information something the user actively engages with, not just glances at.

### Professionally biased: Misestimations of driving speed, journey time and time-savings among taxi and car drivers
- Authors: Eyal Peer, Lidor Solomon
- Year: 2012
- Venue/Journal: Judgment and Decision Making, Vol. 7, Issue 2, pp. 165–172
- URL: https://www.cambridge.org/core/journals/judgment-and-decision-making/article/professionally-biased-misestimations-of-driving-speed-journey-time-and-timesavings-among-taxi-and-car-drivers/D6445A0CB792546294E3EE1F688F5AA1
- Abstract: Tests whether years of real-world professional driving experience (taxi drivers) reduces the time-saving bias compared to ordinary drivers. Both groups substantially overestimated average speed (roughly 2x actual) and overestimated time savings from accelerating. Taxi drivers' errors were somewhat smaller than car drivers' but **remained substantial despite constant real-world exposure to the true speed-time relationship**. Relevant because it rules out "drivers will just learn this from experience over time" as a null hypothesis — mere repeated exposure to real driving outcomes, without an explicit corrective display, does not durably fix the bias, which strengthens (rather than weakens) the case that some form of ongoing in-app feedback is needed.

### Modeling and debiasing resource saving judgments
- Authors: Ola Svenson, Nichel Gonzalez, Gabriella Eriksson
- Year: 2014
- Venue/Journal: Judgment and Decision Making, Vol. 9, Issue 5
- URL: https://www.cambridge.org/core/journals/judgment-and-decision-making/article/modeling-and-debiasing-resource-saving-judgments/02704D142B168920E2BF7A9FA40AFA20
- Abstract: Three studies testing simple debiasing strategies for the time/resource-saving bias. Asking participants to explicitly calculate savings from a reference alternative produced only **modest** improvement; having participants judge a sequence of successive speed increases on the same task reduced the bias more, but did **not eliminate it**. Reinforces that simple, one-off corrective techniques (including, by extension, a static pace display) have only partial power on their own.

### The time-savings and the time-loss bias in traffic (2025 replication)
- Authors: Marinković, T.; Stančić, S.; Dimitrijević, S.
- Year: 2025
- Venue/Journal: СИНЕЗА (Sineza), Vol. 6, No. 2, pp. 17–30
- URL: https://sineza.ff.unibl.org/sineza/article/view/128
- DOI: 10.63356/sin.2025.013
- Abstract: A recent, more tightly controlled replication (larger sample) of both the time-saving bias (TSB) and time-loss bias (TLB) in Bosnia and Herzegovina, following up on earlier local research that had found people overestimate time saved when accelerating from both low *and* high initial speeds (a partial deviation from the classic Svenson pattern). Useful as evidence the bias — and the open question of how to durably correct it — is still an active, unresolved research area as of 2025, not something already fully solved elsewhere in the literature.

### Time-saving bias — background/overview
- Source: Wikipedia
- URL: https://en.wikipedia.org/wiki/Time-saving_bias
- Note: Not a primary source — useful as a fast overview and reference-chasing index into the Svenson/Peer literature above.

---

## 2. Speed vs. Crash Risk & Severity

Quantifies "risk increases much faster than time-saving reward" as speed
rises — the mirror curve to the time-saving hyperbola.

### Traffic Safety Dimensions and the Power Model to Describe the Effect of Speed on Safety
- Authors: Göran Nilsson
- Year: 2004
- Venue/Journal: Doctoral thesis / Bulletin 221, Lund Institute of Technology, Lund University
- URL: https://trid.trb.org/View/749149
- Also: https://portal.research.lu.se/en/publications/traffic-safety-dimensions-and-the-power-model-to-describe-the-eff/
- Abstract: The definitive statement of the "Power Model," originally derived by Nilsson (1981) from Swedish rural speed-limit changes (1967–1972). Fatal crashes scale with roughly the **4th power** of the change in mean speed; serious-injury crashes with the **3rd power**; all-injury crashes with the **2nd power**. Widely used by OECD countries to estimate the safety effect of speed limit/enforcement changes.

### The mathematical relation between collision risk and speed — a summary (Power Model primer)
- Authors/Organization: European Transport Safety Council (ETSC)
- Year: unconfirmed, verify at URL (PDF)
- Venue/Source: ETSC report
- URL: https://etsc.eu/wp-content/uploads/The-mathematical-relation-between-collision-risk-and-speed.pdf
- Abstract: A plain-language technical summary of the Nilsson Power Model and its exponents, aimed at policy/practitioner audiences. Good starting point before reading Nilsson's full thesis. (PDF text extraction failed via fetch tool — open directly.)

### Nilsson's Power Model connecting speed and road trauma: Applicability by road type and alternative models for urban roads
- Authors: Cameron, M.; Elvik, R.
- Year: 2010
- Venue/Journal: Accident Analysis & Prevention
- URL: https://www.sciencedirect.com/science/article/abs/pii/S000145751000148X
- Also: https://pubmed.ncbi.nlm.nih.gov/20728642/
- Abstract: Tests whether the Power Model (derived from rural/highway data) also applies to urban arterial roads. Finds it holds well for rural highways/freeways but **not directly applicable to urban arterial roads**, where the relationship between speed change and crashes is weaker/different — proposes alternative models for urban contexts.

### A re-parameterisation of the Power Model of the relationship between the speed of traffic and the number of accidents and accident victims
- Authors: Rune Elvik
- Year: 2013
- Venue/Journal: Accident Analysis & Prevention
- URL: https://www.sciencedirect.com/science/article/abs/pii/S0001457512002667
- Abstract: Abstract unavailable via search — see URL. Elvik re-derives the Power Model's exponents with an updated, larger dataset, proposing separate parameter sets for urban/residential roads vs. rural roads/freeways, and finds the speed-safety relationship has weakened somewhat in more recent data compared to Nilsson's original estimates.

### Speed and Road Safety: Synthesis of Evidence from Evaluation Studies
- Authors: Rune Elvik
- Year: 2005
- Venue/Journal: Transportation Research Record (Transportation Research Board), No. 1908, pp. 59–69
- URL: https://journals.sagepub.com/doi/10.1177/0361198105190800108
- Also: https://trid.trb.org/view/762266
- Abstract: Meta-analysis synthesizing 98 studies (460 estimates) of the relationship between speed changes and changes in accidents/casualties. Broadly supports the Power Model; concludes the speed–safety relationship is causal, not merely statistical/correlational. Also finds an exponential function fits injury-accident data particularly well as an alternative functional form.

### Updated estimates of the relationship between speed and road safety at the aggregate and individual levels
- Authors: Elvik, Rune (verify full author list at URL)
- Year: 2019
- Venue/Journal: Accident Analysis & Prevention
- URL: https://www.sciencedirect.com/science/article/abs/pii/S000145751830839X
- Also: https://www.researchgate.net/publication/330800621_Updated_estimates_of_the_relationship_between_speed_and_road_safety_at_the_aggregate_and_individual_levels
- Abstract: Abstract unavailable via search — see URL. Most recent (as of search) update to Power Model parameter estimates, distinguishing aggregate (population/road-level) vs. individual (driver-level) speed-risk relationships — relevant if the app wants to communicate "your" personal risk vs. general road statistics.

### Travelling Speed and the Risk of Crash Involvement: Volume 1: Findings
- Authors: Kloeden, C.N.; McLean, A.J.; Moore, V.M.; Ponte, G.
- Year: 1997
- Venue/Source: Australian Office of Road Safety / NHMRC Road Accident Research Unit, University of Adelaide
- URL: https://trid.trb.org/View/499447
- Also (related follow-up rural study): https://www.researchgate.net/publication/237250995_Travelling_Speed_and_the_Risk_of_Crash_Involvement_on_Rural_Roads
- Abstract: Landmark Adelaide case-control study: 151 crash-involved vehicles vs. 604 matched controls, using reconstructed free travel speeds. Found the risk of a casualty crash **doubles with each 5 km/h increase** above a 60 km/h zone speed; on rural roads, risk was more than double at +10 km/h above average traffic speed and nearly sixfold at higher speeds. One of the most-cited empirical sources for the "risk rises much faster than speed" claim.

### Re-visiting crash–speed relationships: A new perspective in crash modelling
- Authors: unconfirmed, verify at URL
- Year: unconfirmed, verify at URL
- Venue/Journal: Accident Analysis & Prevention
- URL: https://www.sciencedirect.com/science/article/pii/S000145751530083X
- Abstract: Abstract unavailable via search — see URL. Proposes an alternative modelling framework for the crash-speed relationship; useful as a critical/updated counterpoint to the classic Power Model.

### Exploration of Vehicle Impact Speed – Injury Severity Relationships for Application in Safer Road Design
- Authors: unconfirmed, verify at URL
- Year: 2016
- Venue/Journal: Transportation Research Procedia (ScienceDirect, open access)
- URL: https://www.sciencedirect.com/science/article/pii/S2352146516304021
- Abstract: Abstract unavailable via search — see URL. Open-access paper (full text likely free) on how injury severity in a crash scales with impact speed — the kinetic-energy side of "why higher speed disproportionately increases the cost of a crash."

---

## 3. Speed vs. Fuel Consumption & Fuel Economy Databases

### Speed vs. Fuel Consumption (concepts to read further into primary sources)
- Source: Multiple secondary/explainer sources found; no single peer-reviewed paper stood out as canonical in initial search — recommend a follow-up targeted search of SAE International and Transportation Research Part D for the primary studies once you're ready to dig deeper here.
- Key facts surfaced (verify against a primary source before citing academically):
  - Aerodynamic drag scales with the **square of speed** (drag force ∝ v²), and the power needed to overcome it scales with the **cube of speed** (power ∝ v³) — meaning fuel needed to overcome drag rises much faster than speed itself at highway speeds.
  - At highway speeds, aerodynamic drag can account for up to ~50–60% of total resistive load on a vehicle.
  - Rule-of-thumb figure cited by secondary sources: driving 100 km/h instead of 110 km/h can save roughly 10% on fuel.
- Overview URL: https://en.wikipedia.org/wiki/Energy-efficient_driving
- Secondary explainer URLs (not peer-reviewed, use with caution, good for citation-chasing):
  - https://www.shriramgi.com/article/how-car-aerodynamics-affects-speed-safety-and-fuel-efficiency
  - https://autoexpert.com.au/owning-a-car/2010/9/17/the-effect-of-travelling-speed-aerodynamic-drag-on-fuel-cons.html
  - https://us.haynes.com/blogs/tips-tutorials/aerodynamics-and-how-they-affect-fuel-economy

### Aerodynamic Drag Analysis of a Passenger Car for Increasing Fuel Economy
- Authors: unconfirmed, verify at URL
- Year: 2025
- Venue/Journal: SciEn Conference Series: Engineering
- URL: https://scienpg.com/scs/index.php/engineering/article/view/scse.2025.3.132
- Abstract: Abstract unavailable via search — see URL. A CFD/engineering study on how drag reduction improves fuel economy; useful for the technical justification of the drag-speed-fuel relationship.

### Multi-Objective Aerodynamic Optimization of Ride Height and Rake Angle in a Sedan Car Using CFD and Machine Learning
- Authors: unconfirmed, verify at URL (arXiv preprint)
- Year: 2025
- Venue/Journal: arXiv preprint
- URL: https://arxiv.org/pdf/2509.02917
- Abstract: Abstract unavailable via search — see URL. More of an automotive-engineering CFD paper than a driver-behavior one; tangential but potentially useful if the app ever models per-vehicle aerodynamic profiles rather than just EPA combined-mpg figures.

## Fuel Economy Databases, APIs & Cost Calculators

### FuelEconomy.gov Web Services (Official EPA/DOE Fuel Economy API)
- Organization: U.S. Department of Energy / U.S. EPA
- Year: ongoing/current
- Venue/Source: fueleconomy.gov
- URL: https://www.fueleconomy.gov/feg/ws/
- Bulk data download: https://www.fueleconomy.gov/feg/download.shtml
- Description: Official U.S. government RESTful API providing city/highway/combined MPG, emissions ratings, vehicle classification, and drivetrain data by year/make/model/trim, for model years 1984–present (~40,000 vehicle records). Data available as JSON or XML; no authentication/API key required. Also includes a `/ws/rest/fuelprices` endpoint returning current fuel prices used by the site, and bulk CSV/XML downloads for offline use. **This directly answers your question — yes, a free, no-auth, public make/model/year fuel-economy database exists and is exactly what you'd need to calculate per-vehicle fuel savings.**

### Third-party wrappers around the FuelEconomy.gov API (useful references, not primary sources)
- `fueleconomy` (Ruby/JSON API wrapper): https://github.com/ryankirkman/fueleconomy
- `mpg` (R package for FuelEconomy.gov data): https://github.com/rOpenGov/mpg — docs: https://ropengov.github.io/mpg/
- `fuel-economy` (JS/JSON wrapper): https://github.com/twindual/fuel-economy
- `vin-fuel-economy` (VIN → EPA fuel economy matching): https://github.com/jeremysabath/vin-fuel-economy
- FuelEconomy.gov API guide (blog walkthrough): https://mpgcalculators.com/blog/fueleconomy-gov-api-web-services/
- Note: the `vin-fuel-economy` repo is particularly relevant — it suggests a path from "scan/enter VIN" → EPA MPG record, which could simplify onboarding (user wouldn't have to manually pick make/model/trim/year).

### AAA "Your Driving Costs" (annual report series)
- Organization: AAA (American Automobile Association)
- Year: annual, e.g. 2022–2025 editions found
- Venue/Source: AAA Newsroom
- URL (2025 edition): https://newsroom.aaa.com/wp-content/uploads/2025/09/AAA-Brochure-Your-Driving-Cost-9.2025.pdf
- URL (overview page): https://www.aaa.com/autorepair/articles/your-driving-costs
- Description: Annual report on total per-mile driving costs, broken out by vehicle category (small sedan, medium sedan, SUV, pickup, hybrid, EV) and by cost component (fuel, maintenance, depreciation, insurance, etc.). Reports cost per mile in cents — e.g. 2025 edition: small sedan fuel cost ≈9.9¢/mile, hybrid ≈8.55¢/mile, EV ≈5.07¢/mile. Directly useful as a validated methodology/benchmark for a "cost per mile" feature, and as a sanity-check dataset for whatever calculation the app does internally from local gas prices + EPA mpg.

---

## 4. Eco-Driving Feedback, Intelligent Speed Adaptation & In-Vehicle HMI Effectiveness

Answers: does showing a driver this kind of feedback actually change behavior?

### Average impact and important features of onboard eco-driving feedback: A meta-analysis
- Authors: unconfirmed, verify at URL
- Year: 2020
- Venue/Journal: Transportation Research Part F: Traffic Psychology and Behaviour
- URL: https://www.sciencedirect.com/science/article/abs/pii/S1369847819300737
- Also (open access preprint/report versions): https://ncst.ucdavis.edu/project/meta-analysis-eco-driving-feedback-research and https://escholarship.org/uc/item/99m5j3q7 and https://rosap.ntl.bts.gov/view/dot/37090
- Abstract: Meta-analysis of 17 studies / 23 effect sizes on in-vehicle eco-driving feedback. Overall effect: **~6.6% improvement in fuel economy**. Feedback showing both instantaneous *and* accumulated performance produced larger effects; multimodal feedback outperformed visual-only; gamification helped. Important caveat: benefits **deteriorate over time** (novelty effect) — combining feedback with education/rewards is recommended for durable impact. Directly relevant: this is the closest existing analogue to "will a pace display actually change driving behavior long-term," and suggests the answer is "yes, modestly, but expect fade without reinforcement design."

### Effective and Acceptable Eco-Driving Guidance for Human-Driving Vehicles: A Review
- Authors: Ran Tu, Junshi Xu, Tiezhu Li, Haibo Chen
- Year: 2022
- Venue/Journal: International Journal of Environmental Research and Public Health (MDPI) / also PMC
- URL: https://www.mdpi.com/1660-4601/19/12/7310
- Also: https://pmc.ncbi.nlm.nih.gov/articles/PMC9223297/
- Also (arXiv preprint): https://arxiv.org/abs/2203.15787
- Abstract: Reviews static vs. dynamic eco-driving guidance systems. Content of suggestions, display method, and driver demographics all affect outcomes. Drivers generally already have basic eco-driving knowledge — the harder problem is motivating long-term acceptance/practice, which is under-researched. Notably: **visualized in-vehicle assistance is reported to be the most distracting** guidance modality — a direct design caution for a pace gauge sharing dashboard real estate with other information.

### Intelligent Speed Adaptation: A Review
- Authors: Kristie Young, Michael A. Regan
- Year: unconfirmed (Australian, early-to-mid 2000s), verify at URL
- Venue/Source: Monash University Accident Research Centre / Australian ISA literature review
- URL: https://homes.plan.aau.dk/agerholm/ISA%20litteratur/Intelligent%20Speed%20Adaptation.%20A%20review.%20Australien.pdf
- Abstract: PDF text extraction failed — open directly. Comprehensive literature review of Intelligent Speed Adaptation (ISA) systems (in-vehicle systems that warn or intervene when a driver exceeds the speed limit), covering system types, driver acceptance, and effectiveness evidence from international trials.

### Active Intelligent Speed Assistance (ISA): A Comprehensive Review of International Field Evidence, Technology Readiness, and Policy Implications for the United States
- Authors: Elena Orlova
- Year: unconfirmed, verify at URL (SSRN working paper)
- Venue/Source: SSRN
- URL: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6106528
- Abstract: Abstract unavailable via search — see URL. Recent (SSRN-hosted) review of real-world ISA field trial data. Reported findings from search snippets: active ISA reduced severe-speeding drive time by ~50% (25 mph roads) to ~77% (50 mph roads); effect held even for habitual speeders. Also documents the **"effectiveness-acceptability paradox"**: the more effective an ISA system is at curbing speed, the less acceptable drivers find it — mandatory/enforcing systems work best but face adoption resistance, while voluntary/advisory systems (closer to what a Paceometer app would be) are better accepted but less effective. This is a central design tension for your app to reckon with explicitly.

### Managing Effectiveness and Acceptability in Intelligent Speed Adaptation Systems
- Authors: unconfirmed, verify at URL
- Year: unconfirmed, verify at URL
- Venue/Source: IEEE Conference Publication (IEEE Xplore)
- URL: https://ieeexplore.ieee.org/document/1706761/
- Abstract: Abstract unavailable via search (paywalled) — see URL. Directly addresses the effectiveness/acceptability trade-off named above.

### Intelligent Speed Adaptation (ISA) — EU policy overview
- Organization: European Commission, Mobility & Transport / Road Safety
- Year: current/ongoing page
- URL: https://road-safety.transport.ec.europa.eu/eu-road-safety-policy/priorities/safe-road-use/safe-speed/archive/speeding/new-technologies-new-opportunities/intelligent-speed-adaptation-isa_en
- Description: EU policy summary page on ISA, relevant background since the EU mandated ISA (warning-only "advisory" form) in all new vehicle types from July 2022 — useful regulatory/market context if the app's positioning needs to differentiate from mandated OEM ISA systems.

---

## 5. Existing Paceometer Prior Art & Dashboard/HUD UI Design

### Part A — Prior Art

**Key finding: the "Paceometer" already exists as an academic research prototype**, not a commercial or patented automotive product. See Peer & Gamliel (2013) in Section 1 above — they built and tested a dashboard-style device explicitly named "Paceometer" showing minutes-per-fixed-distance alongside speed, evaluated in lab and driving-simulator settings for its effect on time-saving judgment accuracy (not yet, as far as this search found, evaluated for long-term real-world speeding reduction or shipped as a consumer product/app). This appears to be your closest and most important piece of prior art — both a validation that the concept works cognitively, and a gap (no real-world deployed product) that your app could fill.

No automotive patents or commercial products describing an inverse-speed/pace-based automotive dashboard display turned up in patent search. Patents found were unrelated conventional speedometer/odometer patents (e.g. US4031510A, US5475724, US9493106) — listed below for completeness/reference, but they are **not** paceometer prior art:
- https://patents.google.com/patent/US4031510A/en — speed detection system, standard speedometer tech
- https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/5475724 — speedometer/odometer apparatus
- https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/9493106 — image-displaying speedometer

Note: "pace" displays are extremely common in running/cycling contexts (Garmin, Strava, etc. — min/mile or min/km displays), but these are a different, well-established, non-automotive product category and not directly relevant prior art for a vehicle dashboard, beyond validating that people intuitively understand pace units in a non-driving context.

**Recommendation:** before going further, it's worth a dedicated Google Patents / USPTO full-text search for phrases like "reciprocal speed display," "time per distance vehicle display," and "inverse speedometer" — the searches so far were not exhaustive of patent databases specifically.

### Part B — Dashboard, HUD & Gauge UI Design Research

### The effects of dashboard design form on driving information reading performance under different time pressures
- Authors: Yunxing Liu, Zhangfan Shen
- Year: 2025
- Venue/Journal: Frontiers in Psychology
- URL: https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2025.1635951/full
- Also: https://pmc.ncbi.nlm.nih.gov/articles/PMC12612637/
- Abstract: Tests how graphical form (semicircular/circular/horizontal/vertical bar), scale precision, and indicator type affect dashboard reading speed/accuracy under time pressure (2000ms/4000ms limits), across 288 trials with 30 participants. **Semicircular and horizontal bar gauges with progress-bar indicators and low scale precision produced the fastest, most accurate readings** under both time pressures — directly actionable for how to actually draw a pace gauge, especially given pace's non-linear (hyperbolic) native scale.

### Gauges design for a digital instrument cluster: Efficiency, visual capture, and satisfaction assessment for truck driving
- Authors: unconfirmed, verify at URL
- Year: 2019
- Venue/Journal: Applied Ergonomics
- URL: https://www.sciencedirect.com/science/article/abs/pii/S0169814119300216
- Also: https://hal.science/hal-03186314v1
- Abstract: 18 truck drivers evaluated 8 gauge designs (varying shape/orientation/indicator type) across quantitative, qualitative, and check-reading tasks. Horizontal gauges with pointer indicators were objectively most efficient (up to 280ms faster eyes-on-gauge time), while drivers subjectively preferred circular/horizontal designs. Reinforces the same design conclusion as the Frontiers 2025 paper above from an independent driving-specific study.

### Dashboard Layout Effects on Drivers' Searching Performance and Heart Rate: Experimental Investigation and Prediction
- Authors: unconfirmed, verify at URL
- Year: 2022
- Venue/Journal: Frontiers in Public Health
- URL: https://www.frontiersin.org/journals/public-health/articles/10.3389/fpubh.2022.813859/full
- Abstract: Abstract unavailable via search — see URL. Studies how overall dashboard *layout* (not just individual gauge shape) affects driver visual search performance and physiological stress (heart rate) — relevant once you're deciding where on the dashboard/HUD to place a pace readout relative to speed.

### NHTSA Visual-Manual/Glance Duration Guidelines (regulatory context for any new gauge)
- Organization: NHTSA (National Highway Traffic Safety Administration) / Alliance of Automobile Manufacturers
- Year: guideline in ongoing effect
- Description: NHTSA driver-distraction guidelines cap acceptable individual glances at in-vehicle displays at **2 seconds**, used as the standard benchmark for evaluating whether a new gauge/display is safe to glance at while driving. Any pace-display design should be validated against this threshold.
- Reference context (HUD-specific complication): a comparative HUD vs. head-down-display study found HUDs performed *worse* on the standard NHTSA eye-glance test yet produced *better* driving performance — suggesting the standard glance-duration test may not fully capture safety for HUD-style displays: https://dl.acm.org/doi/abs/10.1145/3003715.3005419

### Evaluating Automotive Augmented Reality Head-up Display Effects on Driver Performance and Distraction
- Authors: unconfirmed, verify at URL
- Year: unconfirmed, verify at URL
- Venue/Source: NSF PAGES (conference paper record)
- URL: https://par.nsf.gov/biblio/10184842-evaluating-automotive-augmented-reality-head-up-display-effects-driver-performance-distraction
- Related full text: https://par.nsf.gov/servlets/purl/10283675
- Abstract: Abstract unavailable via search — see URL. Relevant if the app is ever built as an AR-HUD overlay rather than a phone-mount or built-in dashboard display.

---

## 6. Validated Survey Instruments for App/UX Evaluation

For when you're ready to evaluate the app itself. Two are especially worth
leading with: **Van der Laan** because it was built and repeatedly validated
specifically for in-vehicle/transport-telematics systems (i.e., exactly this
product category, not a generic app), and **SUS** because it's the fastest,
most standardized general usability benchmark if you want a comparable
"usability score." UEQ/AttrakDiff add the hedonic/experiential dimension
(does it feel good to use, not just is it usable) which matters for a
persuasive/behavior-change app. NASA-TLX matters specifically because this
is a driving-context display — you need to show the gauge doesn't add
dangerous cognitive/visual workload.

### A simple procedure for the assessment of acceptance of advanced transport telematics
- Authors: Van der Laan, J.D.; Heino, A.; De Waard, D.
- Year: 1997
- Venue/Journal: Transportation Research Part C: Emerging Technologies, Vol. 5, Issue 1, pp. 1–10
- URL: https://www.sciencedirect.com/science/article/abs/pii/S0968090X96000253
- Instrument PDF (ready to administer): https://site.unibo.it/hfrs/en/questionnaire-and-scales-2/acceptance-scale/van-der-laan-acceptance-scale-english.pdf/@@download/file/Van%20der%20Laan%20Acceptance%20Scale%20(English).pdf
- Also: https://research.rug.nl/en/publications/a-simple-procedure-for-the-assessment-of-acceptance-of-advanced-t/
- Also: https://www.hfes-europe.org/accept/accept.htm
- Abstract: **The standard validated instrument for measuring driver acceptance of new in-vehicle/transport-telematics systems** — this is the same category of device as a Paceometer, and it's the instrument used throughout the ISA acceptance literature referenced in Section 4. Nine 5-point rating items loading onto two scales: **usefulness** and **satisfaction**. Validated across six independent studies/environments; shown sensitive to opinion differences both between specific system features and between driver groups. Given how short it is (9 items) and how directly it matches your domain, this is the strongest first candidate for evaluating the Paceometer app.

### Method-oriented systematic review on the simple scale for acceptance measurement in advanced transport telematics
- Authors: Jan C. Zoellick, Adelheid Kuhlmey, Liane Schenk, Stefan Blüher
- Year: 2021
- Venue/Journal: PLoS ONE
- URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC7993792/
- Also: https://pubmed.ncbi.nlm.nih.gov/33764981/
- Abstract: Systematic review of 128 studies (6,058 participants) that used the Van der Laan scale, mostly on mobility/driving-simulator systems in Europe. Found the scale reliable where reliability was reported (median Cronbach's α > .83) but flagged that most published applications report incompletely, and that the proposed two-factor (usefulness/satisfaction) structure only replicated in 2 of 10 factor analyses that tested it. **Practical implication: use the scale, but also run and report your own reliability/factor checks rather than assuming the published structure holds for your app.**

### System Usability Scale (SUS)
- Authors: John Brooke
- Year: 1996 (original); validation studies since, e.g. Bangor, Kortum & Miller 2008; Lewis 2018
- Venue/Journal: Originally an industry technical report (Digital Equipment Corp.); validation literature in journals like International Journal of Human-Computer Interaction
- URL (instrument + background): https://www.asarif.com/notes/scales/System_Usability_Scale.pdf
- Also (validation study): https://www.researchgate.net/publication/273297038_Validation_of_the_System_Usability_Scale_SUS
- Also (overview): https://www.sciencedirect.com/topics/computer-science/system-usability-scale
- Abstract: The most widely used general-purpose usability instrument. 10 items, alternating positive/negative statements, 5-point Likert scale, yields a single 0–100 comparability score. Technology-independent (works for apps, hardware, websites). Validated as reliable even with small samples (n≈5 for early formative testing). Useful as a fast, broadly benchmarked "how usable is this app" score to report alongside the more domain-specific Van der Laan scale.

### User Experience Questionnaire (UEQ)
- Authors: Bettina Laugwitz, Theo Held, Martin Schrepp
- Year: 2008 (original); UEQ-S short form Schrepp et al. 2017; UEQ+ modular extension since
- Venue/Journal: Originally presented at USAB 2008 (Springer); ongoing validation via ueq-online.org
- URL: https://www.ueq-online.org/
- Handbook (full instrument + scoring): https://www.ueq-online.org/Material/Handbook.pdf
- Abstract: 26-item instrument measuring 6 factors: attractiveness, perspicuity (clarity), efficiency, dependability, stimulation, and novelty — split into pragmatic (goal-directed: perspicuity/efficiency/dependability) and hedonic (stimulation/novelty) quality. Validated across 11 usability tests (144 participants) plus a large online survey (722 participants) with good construct validity. The 8-item UEQ-S short form is available if a 26-item survey is too long for your study design. Useful if you want to capture "is the Paceometer engaging/interesting to use," not just "is it usable" (SUS) or "is it useful for driving" (Van der Laan).

### AttrakDiff
- Authors: Marc Hassenzahl and colleagues
- Year: original framework ~2003, instrument refined through the 2000s
- Venue/Source: attrakdiff.de (instrument host); underlying theory published across several Hassenzahl papers/book chapters
- URL: https://www.attrakdiff.de/sience-en.html
- Abstract: Semantic-differential scale (opposite-adjective pairs, 7-point) measuring **pragmatic quality (PQ)**, two facets of **hedonic quality** — identity (HQ-I, self-expression) and stimulation (HQ-S, novelty/challenge) — and overall **attractiveness (ATT)**. Full version has 28 item-pairs; a 10-item short form exists for higher response rates. Validated across multiple studies showing pragmatic and hedonic quality are perceived as distinct, independent dimensions that combine to predict attractiveness. Alternative/complement to UEQ for the hedonic side of evaluation.

### Mobile App Rating Scale (MARS) / User version (uMARS)
- Authors: Stoyanov, S.R. et al. (original MARS, 2015); uMARS end-user version by Stoyanov et al. following
- Year: 2015 (MARS); uMARS shortly after
- Venue/Journal: JMIR mHealth and uHealth
- URL (uMARS): https://mhealth.jmir.org/2016/2/e72/
- Also (validation, PLOS ONE): https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0241480
- Abstract: Built for rating mobile health apps but structurally generic enough to be relevant to any behavior-change mobile app. 29 items across three sections: objective quality (19 items: engagement, functionality, aesthetics, information quality — 4 subscales), subjective quality (4 items), and perceived impact (6 items, e.g. likelihood to actually change the target behavior). The original MARS assumes expert/trained raters; **uMARS is the simplified end-user self-report version** — likely the more appropriate variant if you want actual app users (not you/the professor) rating it. Validated in many languages (German, Japanese, Korean, French, Arabic, Traditional Chinese, etc.), suggesting broad cross-context reliability. Worth considering specifically because it has a "perceived impact" subscale, which maps directly onto your research question of whether the app changes speeding behavior, not just whether it's pleasant to use.

### Technology Acceptance Model (TAM) scales
- Authors: Fred D. Davis
- Year: 1989
- Venue/Journal: MIS Quarterly
- URL: https://www.sciencedirect.com/topics/social-sciences/technology-acceptance-model
- Abstract: Two six-item scales measuring **perceived usefulness** (reliability .98) and **perceived ease of use** (reliability .94), theorized as the two primary determinants of whether users adopt a technology (grounded in the Theory of Reasoned Action). Extremely widely used/replicated across technology domains generally (not automotive-specific like Van der Laan). Could serve as a generic cross-check alongside Van der Laan, since TAM's two factors map closely onto Van der Laan's usefulness/satisfaction split but with a much larger cross-domain replication base outside of transport telematics.

### NASA Task Load Index (NASA-TLX)
- Authors: Sandra Hart, Lowell Staveland (NASA Ames Research Center)
- Year: 1988 (original); widely revalidated since, including for driving contexts
- Venue/Journal: originally Human Mental Workload (Elsevier book chapter); driving-specific validations in journals like Transportation Research Part F
- URL (software/background): https://www.researchgate.net/publication/23964010_NASA_TLX_Software_for_assessing_subjective_mental_workload
- Also (driving-specific one-item adaptation): https://www.sciencedirect.com/science/article/abs/pii/S1369847822000365
- Abstract: Subjective multidimensional workload rating across 6 subscales (mental demand, physical demand, temporal demand, performance, effort, frustration), combined into a weighted overall workload score. Extensively used to validate that new in-vehicle displays/HMIs don't dangerously increase driver workload — this is the standard instrument to pair with any driving-simulator or on-road test of the Paceometer gauge, to demonstrate it doesn't add unsafe cognitive/visual load relative to a standard speedometer. A validated one-item shorthand version specifically for driver-vehicle interaction studies also exists (see second URL) if a full 6-subscale NASA-TLX is too burdensome for your study design.

### Driving simulator HMI evaluation methodology (general reference)
- Source: overview/survey of methods, not a single citable instrument
- URL: https://link.springer.com/article/10.1007/s12239-013-0108-x
- Also: https://ietresearch.onlinelibrary.wiley.com/doi/10.1049/itr2.12362
- Description: General references on how driving-simulator studies combine objective measures (eye-tracking/glance duration, vehicle telemetry) with the subjective questionnaires above (acceptance, usability, trust, workload) to evaluate in-vehicle displays — useful methodological template for designing your own eventual Paceometer evaluation study, whether in a simulator or on-road.

---

## 7. Follow-Up Deep Dive (the five threads from the earlier "worth doing next" list)

### 7a. Primary (non-secondary-source) fuel-consumption-vs-speed studies

General web search kept surfacing explainer articles rather than the underlying
papers; searching SAE International and Transportation Research Part D
directly by title turned up the actual primary sources below.

#### Estimated speed/fuel consumption relationships for a large sample of cars
- Authors: David L. Greene
- Year: 1981
- Venue/Journal: Energy, Vol. 6, Issue 5, pp. 441–446
- URL: https://www.sciencedirect.com/science/article/abs/pii/0360544281900062
- Abstract: Abstract unavailable via search (paywalled) — see URL. One of the earliest large-sample empirical studies of the speed/fuel-consumption curve, using data on 350 model-year 1965–77 automobiles collected by *Consumer Reports*. A foundational citation for anyone building a speed-vs-fuel curve, predating the modern VSP-based modelling approach.

#### Multivariate Analysis of Traffic Factors Related to Fuel Consumption in Urban Driving
- Authors: Leonard Evans, Robert Herman, Team Lam
- Year: 1976
- Venue/Journal: Transportation Science, Vol. 10, No. 2, pp. 205–215
- URL: unconfirmed, search "Evans Herman Lam 1976 Multivariate Analysis of Traffic Factors Related to Fuel Consumption in Urban Driving Transportation Science" via GW library discovery (likely INFORMS/JSTOR)
- Abstract: Abstract unavailable via search — see URL. Classic early multivariate treatment of how urban driving factors (including speed/stops) relate to fuel consumption; frequently cited alongside Greene (1981) as foundational.

#### Passenger Car Fuel Economy – Trends and Influencing Factors
- Authors: Thomas C. Austin, Karl H. Hellman (U.S. EPA)
- Year: 1973
- Venue/Journal: SAE Technical Paper 730790
- URL: https://saemobilus.sae.org/papers/passenger-car-fuel-economy-trends-influencing-factors-730790
- Abstract: Analyzes fuel economy patterns and contributing variables using nearly 4,000 tests of passenger cars ranging from 1957 production models to 1975 prototypes, with fuel consumption computed via carbon-balance methodology from 1972 Federal Test Procedure emissions data. Regression analysis quantifies factors affecting fuel economy, including the effect of emissions-control regulation. One of the earliest large-scale SAE treatments of the topic — useful as a historical baseline citation.

#### Modelling of the fuel consumption for passenger cars regarding driving characteristics
- Authors: H. Wang, L. Fu, Y. Zhou, H. Li
- Year: 2008
- Venue/Journal: Transportation Research Part D: Transport and Environment, Vol. 13, pp. 479–482
- URL: https://www.sciencedirect.com/science/article/abs/pii/S1361920908001041
- Also: https://www.researchgate.net/publication/248318886_Modelling_of_the_fuel_consumption_for_passenger_cars_regarding_driving_characteristics
- Abstract: Using a portable emissions measurement system on ten passenger cars, finds fuel consumption per unit distance is **optimal at 50–70 km/h**, and increases significantly with acceleration. Develops a Vehicle-Specific-Power (VSP) based model to calculate fuel consumption, validated against measured data. Directly useful for a "sweet spot" framing in the app (there's an efficiency-optimal speed band, not just "slower is always better").

#### Fast computing and approximate fuel consumption modeling for Internal Combustion Engine passenger cars
- Authors: Olivier Orfila, Camila Freitas Salgueiredo, Guillaume Saint Pierre, H. Sun, Y. Li, Dominique Gruyer, Sebastien Glaser
- Year: 2017
- Venue/Journal: Transportation Research Part D: Transport and Environment, Vol. 50, pp. 14–25
- URL: https://www.sciencedirect.com/science/article/abs/pii/S1361920916304278
- Also (open access): https://eprints.qut.edu.au/120348/
- Abstract: Introduces SEFUM (Semi-Empirical Fuel Use Modeling), a fuel-consumption model calibrated with only a few manufacturer-supplied parameters, benchmarked against three literature models on a 600 km experimental dataset (21 drivers, normal vs. eco-driving conditions, 15 km test trip). Evaluated on instantaneous RMSE, cumulative error, and computation time. Relevant if the app ever wants to estimate fuel consumption from a physics-based model rather than only looking up EPA/WLTP combined-mpg figures.

#### Experimental testing and simulations of speed variations impact on fuel consumption of conventional gasoline passenger cars
- Authors: unconfirmed, verify at URL
- Year: 2017
- Venue/Journal: Transportation Research Part D: Transport and Environment
- URL: https://www.sciencedirect.com/science/article/abs/pii/S1361920916307386
- Abstract: Tests whether cycling speed within a band (50–70 km/h and 90–110 km/h) rather than holding constant speed can reduce fuel consumption, via both track tests (professional driver) and backward quasi-static powertrain simulation. Finds a measurable fuel-consumption reduction is achievable with speed variation, with no vehicle modification needed. Tangential to the core pace-display concept but relevant if the app ever explores "optimal speed variation" coaching, not just "slow down" coaching.

*(SAE International full-text search was done via SAE Mobilus web search, not the GW-authenticated version — GW's Compendex/SAE access, per Section 0, may surface additional primary papers, particularly newer ones behind the SAE Mobilus paywall.)*

### 7b. Google Patents full-text search: "reciprocal speed display," "time-per-distance vehicle gauge," "inverse speedometer"

Ran targeted phrase searches (not just general web search) for these three
phrasings. **Result: no patent describing a literal pace/inverse-speed
(minutes-per-fixed-distance) automotive display was found** — this
reinforces, rather than overturns, the Section 5 Part A conclusion that the
Paceometer exists only as an academic research prototype (Peer & Gamliel
2013), not a patented product.

One partial analog turned up and is worth recording:

#### Instrument Panel Display (US4308527)
- Inventors: Michel L. Moreau, Michel Harmand
- Assignee: Automobiles Peugeot S.A. / Automobiles Citroën S.A.
- Year: filed 1979, granted 1981
- URL: https://patents.google.com/patent/US4308527
- Description: Describes a dashboard with multiple horizontally-spaced speed-indicating scales stacked vertically, where **scale width is explicitly inversely proportional to its vertical position** — lower speeds get wider, lower-positioned scales; higher speeds get narrower, higher-positioned scales, with color-coded (green→red) electroluminescent segments highlighting the current range. Note: this is an inverse relationship between *display geometry and speed*, not between *displayed value and speed* — it does not show pace/time-per-distance. Not Paceometer prior art, but the closest "inverse-scaled" automotive gauge patent found, and possibly useful precedent for how patent offices have handled nonlinear-scale speed displays.

Other patents checked and ruled out as irrelevant (standard speedometers, distance-detection/parking-assist systems, generic reconfigurable digital gauges): US1209359A, US1408598A, US1782914, US1080308A, US2887084A, US1274816A, WO2006112811A1, US4449114, US20130174773A1, US5920256A, US7106213B2, US20080174417A1, US4630043A, US5469184A, US10086702, D1051160, D1054429, WO2009151253A2, DE19959597C1.

**Remaining gap:** this was still a web-search-driven patent check, not an exhaustive USPTO/Google Patents classification-code search (e.g. by CPC class for vehicle instrument displays). A dedicated Google Patents Advanced Search session (not just natural-language query) is still worth doing if patent landscape clearance becomes important later (e.g. before filing anything).

### 7c. Real-world/on-road field test or smartphone app test of the Paceometer concept

**Result: still no field or app-deployment study found — this remains an open gap**, but one additional simulator study surfaced that's worth adding to Section 1, since it independently replicates the core pace/inverted-speed debiasing mechanism:

#### Estimated time of arrival and debiasing the time saving bias
- Authors: Gabriella Eriksson, Christopher J.D. Patten, Ola Svenson, Lars Eriksson
- Year: 2015
- Venue/Journal: Ergonomics, Vol. 58, Issue 12, pp. 1939–1946
- URL: https://www.tandfonline.com/doi/full/10.1080/00140139.2015.1051592
- Also: https://pubmed.ncbi.nlm.nih.gov/26230872/
- Also: https://www.researchgate.net/publication/280581188_Estimated_time_of_arrival_and_debiasing_the_time_saving_bias
- Abstract: Two studies. Study 1 (questionnaire) tests whether providing estimated-time-of-arrival information affects time-saving judgments. Study 2 (active driving-simulator task) has participants drive a fixed distance at a given speed, then choose a new speed intended to save exactly 3 minutes over the same distance — a control group used a standard speedometer and over/undershot the 3-minute target in the classic time-saving-bias pattern (undershooting when accelerating from low speed, overshooting from high speed); a second group used **an alternative meter displaying the inverted speed (pace)** and came significantly closer to the true target. Confirms, independently of Peer & Gamliel and Herberz et al., that an inverted-speed/pace meter debiases judgment — but again only in a driving-simulator setting, not real-world driving.

Searched specifically for: Peer & Gamliel field-study follow-ups, "paceometer" + "app," "paceometer" + "field study"/"on-road," and citation-chasing forward from the 2013/2019 papers. Nothing indicates the Paceometer concept — or any of its close variants (Herberz et al.'s Pop-up assistant, this inverted-speed meter) — has been tested outside a lab or driving simulator, or built as a shipping smartphone app. **This is still the single clearest open research-contribution opportunity for your project**: a real-world or app-based field test of pace-display debiasing would be, as far as this search can tell, the first of its kind.

### 7d. EU/UK vehicle CO2 and fuel-consumption open datasets (non-US markets)

#### EU: Monitoring of CO2 emissions from passenger cars (Regulation (EU) 2019/631)
- Organization: European Environment Agency (EEA)
- Year: ongoing/annual, current regulation since 2019
- URL (interactive tool): https://co2cars.apps.eea.europa.eu/
- URL (dataset page): https://www.eea.europa.eu/en/datahub/datahubitem-view/fa8b1229-3db6-495d-b18e-9c9b3267c02b
- Description: Per-vehicle registration-level dataset covering every new car registered in the EU27 (plus Iceland from 2018, Norway from 2019) — manufacturer, type-approval number, type/variant/version, make/commercial name, CO2 emissions (both NEDC and WLTP protocols), vehicle mass, wheelbase, track width, engine capacity/power, fuel type/mode, eco-innovations, and electricity consumption for EVs/PHEVs. Data downloadable as CSV/TXT/SQL; also exposed via a "Discodata" SQL-Server REST endpoint for programmatic queries. This is the closest EU equivalent to fueleconomy.gov, though it's registration/compliance data (per-vehicle-sold records) rather than a clean make/model/trim lookup table, so more transformation would be needed to build an app-facing "pick your car" API than FuelEconomy.gov requires.
- Also (general EU open-data catalog entry): https://data.europa.eu/euodp/en/data/dataset?tags=cars

#### UK: Car Fuel Data, CO2 and Vehicle Tax Tools
- Organization: Vehicle Certification Agency (VCA), an executive agency of the UK Department for Transport
- Year: ongoing, covers new cars + used cars registered on/after 1 March 2001
- URL: https://www.vehicle-certification-agency.gov.uk/fuel-consumption-co2/new-car-fuel-consumption/
- Tool URL: https://carfueldata.vehicle-certification-agency.gov.uk/
- Also: https://www.gov.uk/co2-and-vehicle-tax-tools
- Description: UK government database of fuel consumption, CO2 emissions, exhaust pollutant levels, noise levels, and vehicle tax band for nearly all new (and post-2001 used) cars sold in the UK, manufacturer-reported and government-checked. Content is downloadable in bulk for offline analysis. No confirmed public API (unlike FuelEconomy.gov or the EEA's Discodata endpoint) — bulk CSV download appears to be the only programmatic access path currently; worth double-checking data.gov.uk directly in case an API has since been added, as the metadata record found during this search was ambiguous on that point.

### 7e. Acceptance/usability scale combined with a measured speed-reduction (behavior-change) outcome

**Result: yes, precedent exists** — at least two published studies pair a validated acceptance/usability framework with an objectively measured driving-behavior outcome, which is the combination your eventual app evaluation will likely need.

#### Evaluation of the Driving Performance and User Acceptance of a Predictive Eco-Driving Assistance System for Electric Vehicles
- Authors: Sai Krishna Chada, Daniel Görges, Achim Ebert, Roman Teutsch, Shreevatsa Puttige Subramanya
- Year: 2023
- Venue/Journal: Transportation Research Part C: Emerging Technologies (also arXiv preprint)
- URL: https://www.sciencedirect.com/science/article/abs/pii/S0968090X23001821
- Also (open access preprint): https://arxiv.org/abs/2208.11429
- Abstract: Introduces pEDAS, a predictive eco-driving assistance system for battery-electric vehicles using model-predictive control and dynamic programming to suggest energy-optimal speeds. Tested with 41 driving-simulator participants. **Objective outcomes**: mean energy savings up to ~10%, reduced speed-limit violations, fewer unnecessary stops. **Subjective outcomes**: user acceptance measured via the Technology Acceptance Model (TAM) and Theory of Planned Behavior (TPB), analyzed with structural equation modeling; perceived usefulness and perceived behavioral control were the significant predictors of intention to use the system. This is a direct methodological template for your project — objective speed/energy metrics collected in parallel with a validated acceptance instrument, analyzed for how they relate to each other, in the same eco-driving/ISA-adjacent product category as a Paceometer app.

#### Intelligent speed adaptation — Effects and acceptance by young inexperienced drivers
- Authors: unconfirmed full author list, verify at URL
- Year: 2010
- Venue/Journal: Accident Analysis & Prevention
- URL: https://www.sciencedirect.com/science/article/abs/pii/S0001457509002772
- Also: https://www.academia.edu/37505097/Intelligent_speed_adaptation_Effects_and_acceptance_by_young_inexperienced_drivers
- Abstract: Compares an "informative" ISA system against an "actively supporting" ISA system in a driving simulator, across inexperienced and experienced drivers. **Objective outcome**: the informative system reduced speeding behavior by over 8% relative to control, particularly at the top end of the speed distribution; the actively-supporting system did not reliably reduce speed and, for inexperienced drivers, may have modestly increased it. **Subjective outcome**: acceptance ratings (Van der Laan-style) differed by driver experience — young/inexperienced drivers rated both systems as less acceptable than experienced drivers did, despite similar or better objective effectiveness for the informative system. No evidence of increased subjective workload or negative behavioral adaptation. Useful precedent specifically for the finding that **effectiveness and acceptance can diverge by user subgroup (experience level)** — a design consideration for how you segment/test the Paceometer app's target users.

---

## Follow-up searches worth doing next (not yet completed)
- Re-run the Section 7a fuel-consumption-vs-speed search inside SAE Mobilus and Compendex via GW's authenticated access (Section 0) — this search only used SAE Mobilus's public web search, which likely misses newer paywalled papers.
- Get the exact URL/DOI for Evans, Herman & Lam (1976), "Multivariate Analysis of Traffic Factors Related to Fuel Consumption in Urban Driving," Transportation Science 10(2) — not resolved to a direct link in this round.
- A genuine classification-code (CPC/USPC) search on Google Patents Advanced Search or USPTO full-text search, rather than natural-language queries, to more exhaustively clear/confirm automotive prior art for a pace/inverse-speed display.
- Confirm whether the UK VCA's Car Fuel Data tool has gained a public API since this search (only a bulk-download path was confirmed); check data.gov.uk directly.
- Now that Eriksson, Patten, Svenson & Eriksson (2015) is confirmed as a third independent replication of the inverted-speed/pace debiasing effect (alongside Peer & Gamliel 2013 and Herberz et al. 2019), citation-chase forward from all three to see if anyone has since attempted a field or app study — worth periodically re-checking as this is a fast-moving-enough niche that a 2025/2026 paper could close the gap.
