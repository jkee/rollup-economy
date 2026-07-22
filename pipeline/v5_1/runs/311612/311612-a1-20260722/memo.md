# 311612 — Meat Processed from Carcasses

*v5.1 Stage 1 research memo. Run `311612-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 6.30 · L 0.39 · interval STRUCTURAL_OUT → STRUCTURAL_OUT · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Durable physical red-meat throughput plus mandatory accountable processing creates a stable base for targeted planning, QA, traceability, and selective automation gains.
**Weakness:** Most labor is manual production and material handling, while the fraction of LMM firms truly operating recurring outsourced programs is unmeasured.

## Business-model lens
- Included: U.S. lower-middle-market establishments that repeatedly process purchased red meat for external customers through private-label, case-ready, co-packing, custom-formulation, cutting, curing, smoking, grinding, cooking, freezing, or related contract programs.
- Excluded: Captive internal plants, manufacturers whose economics primarily depend on their own consumer brands rather than outsourced processing, shells and non-control financing vehicles, slaughter-only establishments, poultry processors, renderers, wholesalers that do not manufacture, and custom-exempt household processing.
- Customer and revenue model: Recurring B2B production programs for retailers, foodservice distributors, institutions, and food brands, typically invoiced per pound, case, SKU, or production run under specifications that incorporate raw-material, packaging, conversion, and logistics economics.
- Deviation from default lens: The code is heterogeneous between branded product manufacturing, merchant-like boxed-meat activity, captive plants, and outsourced private-label or case-ready processing. The lens is narrowed to recurring external-customer processing programs so one commercial-retention and transferability screen remains coherent.

## Executive view
The coherent opportunity is not the full processed-meat code but recurring private-label, case-ready, and contract-processing firms. Physical throughput and regulatory accountability are durable, while AI value is concentrated in planning, quality, traceability, administration, vision inspection, and selective human-in-the-loop automation rather than rapid replacement of most line labor.

## How AI changes the work
Near-term uses include order and production scheduling, yield and demand forecasting, inventory and traceability reconciliation, HACCP-document assistance, QA exception triage, customer service, predictive maintenance, and machine vision. Adaptive robotic cutting is relevant but remains harder because meat varies, plants are wet and hazardous, sanitation is demanding, and existing equipment is often specialized and costly.

## Value capture
Per-pound and per-case program pricing can preserve savings inside a contract period, especially when AI improves yield, reduces overtime, or avoids hiring without changing specifications. Retention erodes at renewal when concentrated customers benchmark conversion costs, rebid private-label work, or negotiate productivity sharing; commodity input pass-through should not be confused with retained AI benefit.

## Firm availability
The private-label and case-ready model is real and transferable transactions occur, but public data do not reveal how many of the 294 frozen-band firms derive enough revenue from recurring outsourced programs. Aging owners and broad food-sector M&A support succession activity, while family transfers, closures, captive ownership, branded economics, and food-safety liabilities reduce the qualifying pool.

## Demand durability
USDA projects combined beef and pork commercial production to rise about 8% from 2026 to 2031. Regardless of software progress, red meat still requires physical processing, cold-chain execution, inspection, hazard controls, records, and responsible establishment sign-off; the main displacement risk is insourcing or consolidation into another plant, not software-only fulfillment.

## Risks and uncertainty
The largest uncertainties are eligibility prevalence, customer concentration, contract repricing, plant-level digital readiness, and the gap between broad manufacturing AI adoption and validated savings in small meat plants. Food-safety failures, recalls, worker injury, commodity volatility, cattle cycles, trade policy, and capex-heavy robotics can overwhelm administrative savings. The compensation-to-receipts input also mixes 2024 wages with 2022 receipts and is IPS-harmonized.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1266 | — | OBSERVED | — |
| n | — | 294 | — | ESTIMATE | — |
| a | 0.1 | 0.17 | 0.27 | PROXY | S2, S3 |
| rho | 0.28 | 0.45 | 0.65 | PROXY | S3, S4, S5, S13 |
| e | 0.18 | 0.32 | 0.48 | ESTIMATE | S1, S6, S7 |
| s5 | 0.12 | 0.2 | 0.3 | PROXY | S7, S8, S9 |
| q | 0.35 | 0.55 | 0.72 | ESTIMATE | S6, S11 |
| d5 | 0.98 | 1.08 | 1.16 | PROXY | S10 |
| o | 0.94 | 0.98 | 0.995 | PROXY | S12, S13 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.14 | 0.39 | 0.89 | PROXY |
| F | 3.21 | 4.80 | 6.06 | ESTIMATE |
| C | 7.00 | 10.00 | 10.00 | ESTIMATE |
| D | 9.21 | 10.00 | 10.00 | PROXY |

## Caveats
- a: OEWS is 2023 and covers NAICS 311600, including slaughter, poultry, and rendering rather than only 311612.
- a: Employment shares are not wage-weighted task shares, and current automation penetration is not reported by occupation.
- a: The frozen compensation ratio l=0.1266 is MED quality, uses 2024 wages over 2022 receipts, and is harmonized to the IPS basis by division by 1.3407.
- rho: Parsec is a vendor-sponsored global manufacturing survey rather than an independent U.S. meat-processor sample.
- rho: The USDA robotics source describes a research project and qualitative industry constraints, not commercial deployment rates.
- rho: Small LMM plants may have weaker data foundations and less capital than surveyed manufacturers.
- e: There is no published census of contract or private-label revenue at NAICS 311612.
- e: Mixed branded and outsourced plants require firm-level revenue classification rather than establishment labels.
- e: The frozen n=294 is an ESTIMATE margin-bridged from SUSB firm-size data using a 15.25% Food Processing EBITDA margin and is not re-estimated here.
- s5: The owner-age evidence is data year 2018, covers all employer businesses, and excludes nonresponding owners.
- s5: Food-and-beverage deal counts include many subsectors, company sizes, asset sales, and transactions outside the narrow lens.
- s5: A single meat-processor acquisition demonstrates feasibility but not frequency.
- q: No public source measures the five-year retained share of AI savings for contract meat processors.
- q: Pricing varies sharply between open-book tolling, formula pricing, fixed-price programs, and processors taking meat-price risk.
- q: Customer concentration and private-label rebids can produce much lower retention than stable differentiated programs.
- d5: USDA forecasts commodity production, not six-digit outsourced-processing demand or a constant-quality service basket.
- d5: The projection includes output handled by slaughter plants, branded manufacturers, and captive facilities outside the lens.
- d5: Health preferences, cattle cycles, trade policy, disease, and substitution toward poultry can move the outcome materially.
- o: Regulation assures an accountable establishment, not that the same outsourced firm remains the supplier.
- o: The estimate does not protect against captive insourcing, consolidation, or customer substitution among physical processors.
- o: Statutory exemptions and state-only regimes exist, though the target lens is commercial recurring B2B production.

## Sources
- **S1** — [North American Industry Classification System: Sector 31-33 definitions](https://www.census.gov/naics/resources/archives/sect31-33.html) (accessed 2026-07-22): Defines 311612 as processing or preserving non-poultry meat and byproducts from purchased meats, including assembly cutting and packing boxed meats, and identifies adjacent exclusions.
- **S2** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 311600](https://www.bls.gov/oes/2023/may/naics4_311600.htm) (accessed 2026-07-22): Reports 542,990 total jobs; production occupations at 59.77%, transportation/material moving at 18.43%, installation/maintenance at 6.47%, office/administrative support at 4.31%, and meat-processing workers at 33.00% of broader-industry employment, with occupation wages.
- **S3** — [Inspection Guidance for Animal Slaughtering and Processing Establishments](https://osha.prod.pace.dol.gov/laws-regs/standardinterpretations/2024-10-15) (accessed 2026-07-22): Includes 311612 in scope; describes dangerous equipment, high mechanization, water and slippery surfaces, sanitation and lockout hazards, and reports a 2022 DART rate of 4.7 per 100 FTE versus 1.7 for private industry.
- **S4** — [Collaborative Cutting: Agile Robot Learners for Multipurpose Meat Industry Automation](https://www.nal.usda.gov/research-tools/food-safety-research-projects/collaborative-cutting-agile-robot-learners-multipurpose-meat-industry-automation) (accessed 2026-07-22): States robotic uptake in American meat and hoofstock facilities remains fairly limited and attributes this to expense, single-purpose designs, high infrastructure requirements, and limited improvement to surrounding work.
- **S5** — [Parsec Survey: 72% of Manufacturers Have Adopted AI, but Only 10% Have Done So at Scale](https://www.parsec-corp.com/news-and-events/parsec-survey-72-of-manufacturers-have-adopted-ai-but-only-10-have-done-so-at-scale) (accessed 2026-07-22): February 2026 global survey of 1,200 manufacturing leaders: 72% reported some AI adoption, 10% scaled deployment, 22% active implementation; leading use cases were quality control, IT operations, and supply chain management, with cost and integration barriers.
- **S6** — [Cargill purchases two meat plants from long-time partner Ahold Delhaize USA](https://www.cargill.com/2024/cargill-purchases-two-meat-plants-from-partner-ahold-delhaize) (accessed 2026-07-22): Documents a long-term retailer partnership producing packaged beef and pork, muscle cuts, and value-added products for grocery-store brands, and the 2024 transfer of two case-ready plants.
- **S7** — [Private equity company acquires meat processor](https://www.foodbusinessnews.net/articles/27197-private-equity-company-acquires-meat-processor) (accessed 2026-07-22): Reports a 2024 middle-market investor acquisition of Branding Iron Holdings, a branded and private-label value-added meat processor with three manufacturing plants.
- **S8** — [Business Owners' Ages](https://www.census.gov/content/dam/Census/library/visualizations/2020/comm/business-owners-ages.pdf) (accessed 2026-07-22): 2019 Annual Business Survey infographic for data year 2018 reports 51% of responding employer-business owners age 55 or older, 43% age 35-54, and 6% age 34 or younger; estimates represent 4.1 million responding owners.
- **S9** — [Food and beverage M&A update: H2 2024](https://www.bakertilly.com/insights/food-and-beverage-ma-update-h2-2024) (accessed 2026-07-22): Capital IQ-based report says 165 U.S. food-and-beverage deals closed in H2 2024, compared with 147 in H1 2024 and 131 in H2 2023; food products were 67% of H2 closings.
- **S10** — [USDA Agricultural Projections to 2035](https://ers.usda.gov/sites/default/files/_laserfiche/outlooks/113817/OCE-2026-1.pdf?v=39134) (accessed 2026-07-22): November 2025 baseline tables project beef commercial production of 25,390 million pounds in 2026 and 27,188 million in 2031, and pork commercial production of 27,475 million pounds in 2026 and 29,917 million in 2031.
- **S11** — [ERS Tracks Meat Prices at the Retail, Wholesale, and Farm Levels](https://www.ers.usda.gov/amber-waves/2015/october/ers-tracks-meat-prices-at-the-retail-wholesale-and-farm-levels) (accessed 2026-07-22): Explains farm, wholesale, and retail meat price spreads as gross-margin indicators and notes that improved meat-processing technology can lower wholesale-to-retail spreads, transferring value to producers and/or consumers.
- **S12** — [9 CFR 302.1: Establishments requiring inspection](https://www.law.cornell.edu/cfr/text/9/302.1) (accessed 2026-07-22): Requires inspection, subject to specified exemptions, at establishments where livestock-derived carcass products are prepared for transport or sale in commerce as human food.
- **S13** — [9 CFR 417.2: Hazard Analysis and HACCP Plan](https://www.law.cornell.edu/cfr/text/9/417.2) (accessed 2026-07-22): Requires official establishments to conduct hazard analysis and, where hazards are reasonably likely, implement written HACCP plans covering listed processing categories, records, controls, and responsible sign-off.
