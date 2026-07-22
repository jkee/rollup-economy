# 314120 — Curtain and Linen Mills

*v5.1 Stage 1 research memo. Run `314120-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 4.36 · L 0.63 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Recurring specification-heavy private-label production creates repeat digital workflows around a physical product that still needs an accountable operator.
**Weakness:** Eligibility is unobserved and likely limited, while domestic textile-furnishings output has contracted under strong import pressure.

## Business-model lens
- Included: Lower-middle-market U.S. curtain and linen mills providing repeat private-label, contract cut-and-sew, custom institutional, or made-to-specification production to external retailers, hospitality operators, healthcare customers, designers, and distributors.
- Excluded: Stock or owned-brand household textile manufacturing without a recurring outsourced-service relationship; direct-to-consumer retail; wholesalers; window-treatment installation; commercial laundering or linen rental; captive production units; shells; and non-control financing vehicles.
- Customer and revenue model: Customers place recurring purchase orders or production programs for sheets, towels, curtains, draperies, table linens, shower curtains, and related household textiles, priced per unit, lot, style, or contract specification rather than by subscription.
- Deviation from default lens: The code is narrowed to private-label, contract, and made-to-specification production because NAICS 314120 primarily covers goods manufacturing, including stock and custom products for retail sale, while recurring outsourced production has materially different eligibility and commercial-retention economics.

## Executive view
The relevant opportunity is a minority subset of curtain and linen mills that repeatedly manufacture private-label or made-to-spec products for external business customers. These firms have AI-addressable specification, quoting, planning, procurement, and quality workflows, but manual sewing dominates and domestic real output is declining.

## How AI changes the work
AI can structure customer specifications, accelerate quotes and samples, improve material planning and schedules, automate order-status communication, and flag visual defects or documentation exceptions. It does not remove the need for cutting, sewing, handling, maintenance, tactile checks, and final accountability.

## Value capture
Fixed per-unit or per-program pricing can preserve early savings. Retention erodes when concentrated buyers rebid work, require annual cost-downs, compare offshore quotes, or capture transparent clerical savings; value tied to turnaround, compliance, and low defect rates is more durable.

## Firm availability
The frozen dataset estimates 36 firms in the LMM EBITDA band, but the NAICS definition includes stock and custom product manufacturers broadly. Only an unobserved minority is likely to earn enough revenue from repeat outsourced private-label or institutional production to qualify.

## Demand durability
Replacement and institutional consumption keep the physical product basket necessary, while hospitality and healthcare customization can favor responsive suppliers. Still, broader textile-furnishings real output fell each year from 2021 through 2025, and low-cost imported home furnishings set a demanding price benchmark.

## Risks and uncertainty
The central diligence risk is finding that few of the 36 estimated firms actually fit the service lens. Other risks include offshore substitution, retailer concentration, volatile tariffs and input costs, weak domestic volume, legacy systems, limited AI implementation staff, and benefit pass-through at annual sourcing events.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1974 | — | OBSERVED | — |
| n | — | 36 | — | ESTIMATE | — |
| a | 0.09 | 0.16 | 0.27 | PROXY | S2, S3, S7 |
| rho | 0.28 | 0.5 | 0.7 | ESTIMATE | S3, S7 |
| e | 0.07 | 0.18 | 0.35 | ESTIMATE | S1 |
| s5 | 0.08 | 0.17 | 0.27 | PROXY | S4 |
| q | 0.2 | 0.4 | 0.62 | ESTIMATE | S6 |
| d5 | 0.6 | 0.8 | 1 | PROXY | S5, S6 |
| o | 0.88 | 0.95 | 0.99 | ESTIMATE | S1, S6, S7 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.20 | 0.63 | 1.49 | ESTIMATE |
| F | 0.30 | 1.19 | 2.38 | ESTIMATE |
| C | 4.00 | 8.00 | 10.00 | ESTIMATE |
| D | 5.28 | 7.60 | 9.90 | ESTIMATE |

## Caveats
- a: OEWS evidence combines carpet/rug mills with curtain/linen mills at NAICS 3141.
- a: Employment counts are not wage weights and do not measure within-occupation task exposure.
- a: Software-AI exposure omits conventional sewing automation and may omit AI embedded in robotics.
- rho: No 314120-specific survey measures production use of AI rather than generic digitization.
- rho: The estimate assumes usable digital order and specification data.
- rho: Benefits from ordinary sewing machinery are excluded unless AI is essential to the workflow.
- e: The frozen firm count is a margin-bridged estimate rather than an observed list.
- e: Custom products sold to individual retail customers are inside NAICS but generally outside the external-business service lens.
- e: Public information often does not distinguish private-label manufacturing from branded wholesale revenue.
- s5: Gallup covers all employer businesses rather than manufacturing, LMM firms, or this NAICS.
- s5: Stated sale, gift, or public-offering plans are not completed qualifying control transfers.
- s5: A small eligible denominator makes realized five-year rates volatile.
- q: No direct study measures AI-benefit pass-through in U.S. curtain and linen contracts.
- q: The 2021 trade evidence is broad and pandemic-affected, but it establishes strong import benchmarking pressure.
- q: Retention differs materially between retailer private label, custom hospitality work, and small designer programs.
- d5: The output series is NAICS 3141 and includes carpet and rug mills.
- d5: USITC home-furnishing imports cover a broader product basket and 2021 was pandemic-distorted.
- d5: The narrowed contract-service subset may benefit from reshoring or short-lead-time needs even while total domestic output falls.
- o: This estimate conditions on quantity already remaining in d5 and does not count import substitution twice.
- o: Standard products are more vulnerable to direct offshore procurement than short-run customized programs.
- o: No direct survey measures software-only or self-service displacement for contract home-textile production.

## Sources
- **S1** — [2022 Economic Census Form MC-31411: Curtain and Linen Mills](https://bhs.econ.census.gov/ombpdfs2022/export/2022_MC-31411_su.pdf) (accessed 2026-07-22): Identifies 314120 establishments as curtain and linen mills manufacturing household textile products from purchased fabric, on a stock or custom basis, and lists sheets, towels, pillows, shower curtains, and related products.
- **S2** — [BLS OEWS Data Tables for Industry Charts, May 2024](https://www.bls.gov/oes/2024/may/ind_emp_chart/ind_emp_chart_data.htm) (accessed 2026-07-22): Reports the largest occupations in Textile Furnishings Mills, led by 5,870 sewing machine operators, followed by winding, weaving, production supervision, material moving, maintenance, inspection, shipping, and cutting occupations.
- **S3** — [Artificial Intelligence and the Changing Demand for Skills in the Labour Market](https://www.oecd.org/content/dam/oecd/en/publications/reports/2024/04/artificial-intelligence-and-the-changing-demand-for-skills-in-the-labour-market_861a23ea/88684e36-en.pdf) (accessed 2026-07-22): Finds cognitive high-skill occupations more exposed to software AI, non-routine physical occupations less exposed, and textile pressers among the least exposed occupations; also cautions that exposure is not demonstrated adoption.
- **S4** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Gallup's fall-2024 U.S. survey of 1,264 working business owners reports that 22% of employer-business owners planned to sell or transfer ownership within five years and that 52.3% of employer businesses had owners age 55 or older.
- **S5** — [Real Sectoral Output for Textile Furnishings Mills (NAICS 3141)](https://fred.stlouisfed.org/series/IPUEN3141T010000000) (accessed 2026-07-22): BLS real sectoral output index reported 90.993 in 2021, 86.044 in 2022, 81.916 in 2023, 76.026 in 2024, and 72.715 in 2025.
- **S6** — [USITC Trade Shifts 2021: Textiles and Apparel](https://www.usitc.gov/research_and_analysis/tradeshifts/2021/textiles) (accessed 2026-07-22): Reports $15.4 billion of U.S. home-furnishing imports in 2021, up 33.0%, and identifies China and India as major textile and home-furnishing suppliers; supports import competition and demand caveats.
- **S7** — [BLS Occupational Outlook Handbook: Quality Control Inspectors](https://www.bls.gov/ooh/production/quality-control-inspectors.htm) (accessed 2026-07-22): Explains that advanced vision systems and scanners automate some inspection tasks, while random checks, validation, and texture or performance testing continue to require inspectors.
