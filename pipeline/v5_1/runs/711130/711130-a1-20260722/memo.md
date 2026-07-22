# 711130 — Musical Groups and Artists

*v5.1 Stage 1 research memo. Run `711130-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** CONDITIONAL · A 6.59 · L 2.44 · interval STRUCTURAL_OUT → PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Repeat live-performance demand remains operator-required while booking and administrative workflows are increasingly automatable.
**Weakness:** Artist and lineup dependence, plus nonprofit governance, makes much of the apparent firm population non-transferable.

## Business-model lens
- Included: US ensemble operating companies in the roughly $1-10M normalized EBITDA band that repeatedly provide live musical performances to venues, presenters, event clients, ticket buyers, sponsors, and institutions, including transferable bands, orchestras, chamber groups, and multi-ensemble operators.
- Excluded: Independent solo musicians and vocalists, celebrity or bandleader vehicles whose earnings and customer demand are inseparable from one named person, nonprofit or public ensembles without a feasible qualifying control path, music promoters and agents, composition-only businesses, catalog or royalty investment vehicles, shells, and captive internal groups.
- Customer and revenue model: Repeated fixed-fee engagements, guarantees, door or ticket-share arrangements, self-produced ticketed performances, residencies, subscriptions, sponsorships, merchandise, and, for some orchestras, grants and contributions; delivery is project- or season-based rather than continuously contracted.
- Deviation from default lens: NAICS 711130 expressly combines musical groups with independent freelance artists and includes soloists as well as orchestras. The record narrows to ensemble operating companies because personality-dependent solo acts and transferable multi-person service organizations have fundamentally different control-transfer economics; the narrowing is for coherence, not attractiveness.

## Executive view
Ensemble operators have an administratively useful but artistically bounded AI opportunity: booking, marketing, customer response, settlements, scheduling, and sponsorship work can improve, while the live-performance core remains human. The central constraint is not demand but finding firms whose earnings survive a change in the named performers, lineup, or nonprofit governance.

## How AI changes the work
AI can qualify inquiries, draft proposals and contracts for review, maintain CRM records, coordinate calendars, prepare settlement packages, repurpose promotional content, and support finance and sponsor reporting. It can also assist ideation and rehearsal preparation, but replacing the performance itself would change the purchased service and should not be counted as labor substitution.

## Value capture
Per-event guarantees and fixed ticket prices provide some initial insulation from direct pass-through. Renewal bargaining, competitive booking markets, musician compensation, venue shares, and nonprofit reinvestment are likely to distribute a substantial portion of savings over five years.

## Firm availability
The code is unusually heterogeneous: it includes independent soloists, popular artists, bands, and orchestras. A credible control target needs repeat customer relationships and an institutional brand or roster that remains valuable after ownership and personnel changes; many artist entities and charitable orchestras fail one of those tests.

## Demand durability
Recent major-concert results demonstrate strong appetite for live experiences, and BLS expects real output growth in the broader performing-arts sector. Smaller US ensembles face a less uniform picture: classical, jazz, and Latin attendance was weak in pandemic-affected 2022, musician employment growth is limited, and local event demand can be cyclical.

## Risks and uncertainty
Four-digit staffing and output proxies mix music with theater and dance; SUSB-based LMM counts may not fit nonprofit or artist economics; contractors and self-employed performers are incompletely observed; major-tour demand may not transfer to smaller ensembles; copyright, likeness, and union issues can slow AI adoption; and no clean control-transfer series exists. A roll-up could fail if customer demand follows the departing artist rather than the acquired firm.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.5187 | — | OBSERVED | — |
| n | — | 279 | — | ESTIMATE | — |
| a | 0.12 | 0.21 | 0.32 | PROXY | S2, S3, S6 |
| rho | 0.36 | 0.56 | 0.73 | PROXY | S3, S4 |
| e | 0.1 | 0.22 | 0.38 | ESTIMATE | S1, S5, S6 |
| s5 | 0.08 | 0.19 | 0.32 | ESTIMATE | S1, S5 |
| q | 0.4 | 0.6 | 0.78 | ESTIMATE | S5, S9 |
| d5 | 0.92 | 1.07 | 1.2 | PROXY | S6, S7, S8, S9 |
| o | 0.81 | 0.92 | 0.98 | ESTIMATE | S6, S8, S9 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.90 | 2.44 | 4.85 | PROXY |
| F | 1.89 | 4.08 | 5.72 | ESTIMATE |
| C | 8.00 | 10.00 | 10.00 | ESTIMATE |
| D | 7.45 | 9.84 | 10.00 | ESTIMATE |

## Caveats
- a: The only detailed industry occupation table is NAICS 711100, not 711130.
- a: OEWS excludes self-employed workers and may not capture contractors consistently.
- a: Observed generative-AI usage is not equivalent to safe substitution in rights-sensitive creative work.
- rho: Neither implementation source studies musical groups or live-event operations.
- rho: Customer-support productivity may not transfer to relationship-based booking or artistic workflows.
- rho: Rights clearance, performer consent, and brand control may constrain otherwise feasible automation.
- e: Dataset n is margin-bridged using a recreation-industry margin and may misclassify artist and nonprofit economics.
- e: The published NAICS definition establishes heterogeneity but does not quantify the LMM mix.
- e: A transferable brand or repertoire cannot compensate for customer demand tied to an excluded named artist.
- s5: Published music transactions often concern catalogs, royalties, promoters, venues, or agencies rather than NAICS 711130 operating control.
- s5: Personnel succession is not automatically a qualifying control transfer.
- s5: Distress can dissolve a group instead of creating a transferable transaction.
- q: Billing structures and bargaining power vary sharply by genre, venue, and artist recognition.
- q: Live Nation is a global promoter, venue, and ticketing company, not an LMM musical group.
- q: Retained benefit is not equivalent to owner cash flow in a nonprofit ensemble.
- d5: BLS output covers theater and dance as well as music.
- d5: The NEA comparison spans a pandemic disruption and is not a normalized trend.
- d5: Live Nation's results are global, promoter-led, and disproportionately reflect major tours and large venues.
- o: The estimate applies to today's live service basket, not recorded music or composition.
- o: Virtual and synthetic acts may substitute faster for background entertainment and standardized event music than for concerts.
- o: Operator-required demand can persist even when the artist brand is not transferable.

## Sources
- **S1** — [2022 NAICS Definition: 711130 Musical Groups and Artists](https://www.census.gov/naics/?details=711130&input=711130&year=2022) (accessed 2026-07-22): Industry scope and heterogeneity: groups producing live musical entertainment and independent freelance artists, including bands, orchestras, popular artists, musicians, vocalists, and soloists; excludes promoters and independent composers or arrangers.
- **S2** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 711100 Performing Arts Companies](https://www.bls.gov/oes/2023/May/naics4_711100.htm) (accessed 2026-07-22): Nearest industry occupation mix: management 8.62%, arts/design/entertainment/sports/media 41.79%, musicians and singers 15.77%, and office and administrative support 7.48%; the page notes estimates exclude self-employed workers.
- **S3** — [Anthropic Economic Index report: Economic primitives](https://www.anthropic.com/research/anthropic-economic-index-january-2026-report) (accessed 2026-07-22): Observed November 2025 AI-use patterns, including office-administrative tasks at 13% of enterprise API transcripts after a 3 percentage-point rise, automation-oriented email, document, CRM, and scheduling workflows, and arts-related writing and editing use.
- **S4** — [Measuring the Productivity Impact of Generative AI](https://www.nber.org/digest/20236/measuring-productivity-impact-generative-ai) (accessed 2026-07-22): Field evidence from 5,179 customer-support agents that AI assistance raised issues resolved per hour by nearly 14% on average, with larger effects for less-experienced workers.
- **S5** — [Exemption requirements - 501(c)(3) organizations](https://www.irs.gov/charities-non-profits/charitable-organizations/exemption-requirements-501c3-organizations) (accessed 2026-07-22): Tax-exempt organizations must operate for exempt rather than private interests, and no earnings may inure to a private shareholder or individual, constraining conventional owner economics for nonprofit orchestras and ensembles.
- **S6** — [Musicians and Singers: Occupational Outlook Handbook](https://www.bls.gov/ooh/entertainment-and-sports/musicians-and-singers.htm) (accessed 2026-07-22): Musician duties spanning live performance, audition, practice, rehearsal, booking, and promotion; part-time work is common; and employment is projected to rise 1% from 169,800 in 2024 to 171,600 in 2034.
- **S7** — [Employment and output by industry](https://www.bls.gov/emp/tables/industry-employment-and-output.htm) (accessed 2026-07-22): BLS chained-2017-dollar projection for NAICS 711100: output rises from $29.8 billion in 2024 to $36.9 billion in 2034, a 2.1% compound annual rate; employment rises 3.6%.
- **S8** — [Arts Participation Patterns in 2022: Highlights from the Survey of Public Participation in the Arts](https://www.arts.gov/sites/default/files/2022-SPPA-final.pdf) (accessed 2026-07-22): In 2022, 21% of US adults attended an unlisted live music, dance, or theater form; jazz attendance was 6.3%, Latin music 3.9%, and classical music 4.6%, all below 2017; venue and discovery patterns also show bars, outdoor facilities, and social media importance.
- **S9** — [Live Nation Entertainment 2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/1335258/000133525826000009/lyv-20251231.htm) (accessed 2026-07-22): Global live-music demand proxy: 159 million fans attended 55,000 events involving more than 11,000 artists in 2025; fan count rose by 8 million or 5%, and concert revenue rose 10%, with growth concentrated in international markets and stadium content.
