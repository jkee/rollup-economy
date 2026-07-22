# 325613 — Surface Active Agent Manufacturing

*v5.1 Stage 1 research memo. Run `325613-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 5.59 · L 0.25 · interval STRUCTURAL_OUT → STRUCTURAL_OUT · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Repeat specification-qualified product demand supports durable operator-required revenue and some savings retention.
**Weakness:** Physical production limits the implementable labor pool, and the estimated LMM universe is small.

## Business-model lens
- Included: Independent lower-middle-market manufacturers of surfactants, finishing agents, and formulated assistants sold repeatedly to external industrial and consumer-product customers.
- Excluded: Captive production, non-operating entities, commodity distribution without manufacturing, and businesses outside the stated EBITDA band.
- Customer and revenue model: Repeat B2B sales of specification-qualified chemical products, often supported by formulation, quality, regulatory, and technical-service work.
- Deviation from default lens: none

## Executive view
The opportunity is a recurring specialty-chemical manufacturing base with meaningful administrative and technical-work augmentation, but only a modest share of total labor is plausibly substitutable because production is physical and regulated.

## How AI changes the work
AI is most relevant to specification and safety-document drafting, formulation and literature search, quality-data review, production and procurement planning, quoting, and technical-sales support. Batch operation, laboratory work, maintenance, material movement, and final accountable release stay human-led.

## Value capture
Qualified products and technical support can make savings sticky, especially in proprietary niches. Commodity competition and procurement-led repricing are the main paths by which customers capture part of the gain.

## Firm availability
The supplied LMM population is small. Many firms should fit the repeat external-sales lens, but owner willingness, environmental liabilities, customer concentration, and strategic ownership can sharply shrink actionable supply.

## Demand durability
Surfactants remain necessary physical ingredients, and safer-chemistry requirements can support reformulation work. Real volumes are more likely stable to modestly growing than displaced by software, though end-market cycles and more concentrated products matter.

## Risks and uncertainty
The largest uncertainties are six-digit occupation mix, actual current automation, transfer incidence, environmental liabilities, and contract-level pass-through. Commodity-heavy targets may have lower retention and weaker differentiation than the central case.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.0484 | — | OBSERVED | — |
| n | — | 16 | — | ESTIMATE | — |
| a | 0.16 | 0.25 | 0.36 | PROXY | S1, S2 |
| rho | 0.35 | 0.52 | 0.68 | ESTIMATE | S3 |
| e | 0.58 | 0.74 | 0.88 | ESTIMATE | S4 |
| s5 | 0.13 | 0.23 | 0.34 | PROXY | S5 |
| q | 0.52 | 0.68 | 0.82 | ESTIMATE | S3 |
| d5 | 0.94 | 1.04 | 1.15 | ESTIMATE | S3, S6 |
| o | 0.9 | 0.96 | 0.99 | ESTIMATE | S3, S6 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.11 | 0.25 | 0.47 | ESTIMATE |
| F | 1.27 | 2.11 | 2.82 | ESTIMATE |
| C | 10.00 | 10.00 | 10.00 | ESTIMATE |
| D | 8.46 | 9.98 | 10.00 | ESTIMATE |

## Caveats
- a: No public six-digit wage-weighted task study was found.
- a: Current automation and plant scale vary materially.
- rho: Bounded judgment rather than an industry adoption measurement.
- rho: EPA ingredient and release requirements illustrate accountability constraints but do not measure AI implementation.
- e: The injected firm count is an estimate based on a margin bridge.
- e: The Census definition confirms activity scope but not independence or transferability.
- s5: Proxy is economy-wide and not industry-specific.
- s5: No denominator-based five-year transfer series was found.
- q: No public contract sample quantifies pass-through.
- q: Retention differs between proprietary formulations and commodity surfactants.
- d5: EPA sources establish use and compliance demand, not market growth.
- d5: End-market and chemistry mix are heterogeneous.
- o: Operator need could shift toward larger suppliers through consolidation.
- o: The estimate concerns quantity requiring a manufacturer, not employment retained.

## Sources
- **S1** — [Chemical Manufacturing: NAICS 325](https://www.bls.gov/iag/tgs/iag325.htm) (accessed 2026-07-22): BLS overview identifies common occupations in chemical manufacturing, including 124,330 chemical equipment operators and tenders in the displayed industry material.
- **S2** — [Chemists and Materials Scientists](https://www.bls.gov/ooh/life-physical-and-social-science/chemists-and-materials-scientists.htm) (accessed 2026-07-22): BLS reports 86,800 chemist jobs in 2024 and 29% in chemical manufacturing, supporting the technical-work proxy.
- **S3** — [Safer Choice Standard and Criteria](https://www.epa.gov/saferchoice/standard) (accessed 2026-07-22): EPA states surfactants reduce surface tension and describes ingredient evaluation and manufacturing-release documentation, supporting product function and compliance-accountability claims.
- **S4** — [ASM Industry Definition for Soap and Cleaning Compound Manufacturing](https://www2.census.gov/econ2007/Reference_materials/htm%20files/32561m.htm) (accessed 2026-07-22): Census lists NAICS 325613 Surface Active Agent Manufacturing within the relevant manufacturing rollup.
- **S5** — [2024 Firms in Focus chartbooks on small business data](https://www.fedsmallbusiness.org/reports/survey/2024/2024-small-business-data-chartbooks) (accessed 2026-07-22): Federal Reserve chartbooks provide owner-demographic evidence, including an age-of-owner chartbook, used only as a broad succession proxy.
- **S6** — [Safer Choice Criteria for Surfactants](https://www.epa.gov/saferchoice/safer-choice-criteria-surfactants) (accessed 2026-07-22): EPA describes surfactants in cleaning products and environmental fate and toxicity criteria, supporting persistent physical function and regulatory constraints.
