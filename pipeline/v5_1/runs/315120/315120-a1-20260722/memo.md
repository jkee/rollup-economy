# 315120 — Apparel Knitting Mills

*v5.1 Stage 1 research memo. Run `315120-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** no base (evidence-first) · A — · L — · interval STRUCTURAL_OUT → CONDITIONAL · readiness STRESS_TEST_ONLY · action EVIDENCE_FIRST

**Driver:** Integrated digital design and whole-garment production create a credible path to faster, more customized domestic contract manufacturing.
**Weakness:** Long-running domestic output contraction and the missing LMM firm count make demand and acquisition availability unusually uncertain.

## Business-model lens
- Included: US lower-middle-market apparel knitting mills that repeatedly manufacture knit garments or knit fabric-and-garment combinations for external brands, designers, uniform programs, institutions, and private-label customers under contract, replenishment, or recurring production arrangements.
- Excluded: Primarily own-brand apparel companies whose economics depend on retail merchandising and consumer demand rather than outsourced manufacturing, captive mills, shells, non-control financing vehicles, and operations without transferable production and customer systems.
- Customer and revenue model: Repeat B2B contract, private-label, replenishment, small-batch, and on-demand production, generally quoted per unit or production run with customer specifications, samples, purchase orders, quality requirements, and delivery commitments.
- Deviation from default lens: NAICS 315120 includes both own-account branded apparel producers and mills supplying outsourced knitting and garment production. Those models have different commercial retention and demand drivers, so the lens retains recurring contract/private-label manufacturers and excludes primarily own-brand retail economics.

## Executive view
The coherent outsourced-service opportunity is in contract and private-label apparel knitting, not own-brand fashion. Labor intensity is high, but most employment is machine operation, maintenance, and material handling; AI exposure is concentrated in design, sampling, quoting, planning, administration, inspection, and machine support. Domestic demand has contracted sharply, and the missing firm-count input is a fundamental availability limitation.

## How AI changes the work
AI can speed trend and design iteration, virtual sampling, technical-pack interpretation, quoting, production planning, customer communication, visual inspection, maintenance analytics, and exception handling. Computerized whole-garment knitting can integrate design and production, but machines, materials, quality control, sewing exceptions, packing, and maintenance remain physical and often skill constrained.

## Value capture
Contract prices initially let the operator retain savings, yet brand customers rebid programs and compare offshore landed cost. Domestic mills preserve value when they deliver short runs, replenishment, customization, fast turns, better fit, lower inventory risk, or complex knit structures that make switching costly.

## Firm availability
The code does not distinguish contract mills from branded producers, so eligibility is estimated rather than observed. Broad manufacturing ownership suggests succession pressure, but the dataset has no defensible LMM firm count and the shrinking domestic base raises the chance that owner exits become closures or asset sales rather than transferable going concerns.

## Demand durability
US apparel knitting output declined materially through 2025 and remains exposed to imports. Customization, shorter lead times, small orders, replenishment, supply-chain resilience, and automated whole-garment production offer a differentiated domestic niche, but the five-year central case still assumes lower real volume.

## Risks and uncertainty
Primary risks are continuing offshore substitution, volatile trade policy, fashion and inventory cycles, concentrated brand customers, yarn sourcing, legacy machinery, skilled-maintenance scarcity, founder dependence, and technology that raises throughput without producing realizable payroll savings. Absolute firm opportunity is unknowable from the frozen dataset because n is missing.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.4109 | — | OBSERVED | — |
| n | — | — | — | MISSING | — |
| a | 0.12 | 0.2 | 0.31 | PROXY | S1, S2, S3 |
| rho | 0.28 | 0.5 | 0.72 | PROXY | S3, S8 |
| e | 0.25 | 0.45 | 0.65 | ESTIMATE | S3, S7 |
| s5 | 0.11 | 0.24 | 0.4 | PROXY | S6 |
| q | 0.32 | 0.55 | 0.75 | ESTIMATE | S3, S5 |
| d5 | 0.6 | 0.82 | 1.08 | PROXY | S3, S4, S5 |
| o | 0.91 | 0.97 | 1 | ESTIMATE | S3, S7 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.55 | 1.64 | 3.67 | PROXY |
| F | — | — | — | MISSING |
| C | 6.40 | 10.00 | 10.00 | ESTIMATE |
| D | 5.46 | 7.95 | 10.00 | ESTIMATE |

## Caveats
- a: Occupation data are at NAICS 315100 and include operations outside the narrowed contract-manufacturing lens.
- a: Employment shares are not wage shares; management, business, design, and sales work carries above-average wages.
- a: The estimate excludes benefits from robotics that cannot reasonably be attributed to AI-enabled substitution or avoidable hiring.
- rho: USITC technology cases are illustrative innovators, not a representative adoption survey.
- rho: The Auburn survey spans manufacturing sectors and may not reflect very small apparel plants.
- rho: Implementation concerns labor capture only and excludes price, demand, and valuation effects.
- e: No public data separate contract knitting mills from own-brand manufacturers at this code.
- e: The dataset provides no defensible LMM firm count, so this eligibility share cannot be translated into a target count.
- e: Some firms combine contract production and their own labels, requiring revenue-level classification.
- s5: The owner-age source covers women owners across all manufacturing, not all owners in apparel knitting.
- s5: Age 55 or older does not reveal retirement intent or timing.
- s5: The missing dataset firm count prevents a defensible absolute estimate of transferable firms.
- q: No public source measures retention of automation benefits for private US contract apparel knitters.
- q: Yarn, freight, tariff, and mix changes can swamp labor-cost effects in invoice data.
- q: Retention is likely lowest for standardized high-volume programs and highest for fast, customized, or technically difficult orders.
- d5: BLS data are at NAICS 3151 and include business models excluded from the lens.
- d5: Domestic output measures US supply, so import substitution can drive it below underlying US apparel demand.
- d5: Trade policy, sourcing-country shifts, and tariff rules can move five-year demand sharply in either direction.
- o: The estimate is inferred from physical production requirements rather than directly observed.
- o: A highly automated plant still counts as an accountable operator; lower labor intensity is captured in other primitives.
- o: Offshore substitution removes work from US lens firms even though a physical operator remains elsewhere.

## Sources
- **S1** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 315100](https://www.bls.gov/oes/2023/may/naics4_315100.htm) (accessed 2026-07-22): Reports 7,010 jobs and the detailed occupation mix: production 54.31%, maintenance 14.40%, material moving 11.08%, office support 7.80%, business/financial 3.65%, management 3.50%, design/media 1.67%, and sales 1.28%.
- **S2** — [May 2024 OEWS Industry Chart Data](https://www.bls.gov/oes/2024/may/ind_emp_chart/ind_emp_chart_data.htm) (accessed 2026-07-22): Lists the largest apparel-knitting-mill occupations in 2024, led by 1,350 knitting and weaving machine operators, 480 industrial machinery mechanics, 460 hand packers, 450 sewing machine operators, and 390 inspectors/testers.
- **S3** — [Textiles and Apparel: Made in USA... Again?](https://www.usitc.gov/publications/332/working_papers/id_18_55_textiles_and_apparel_made_in_usa._again_.html) (accessed 2026-07-22): Documents apparel automation and barriers, including 3-D whole-garment knitting in 30 minutes or less, virtual sampling, order-to-delivery integration, design/planning connectivity, lagging automation due to fabric handling and import competition, and domestic advantages in customization, smaller orders, and short lead times.
- **S4** — [Labor productivity, unit labor costs, and related data, 2019-2025](https://www.bls.gov/news.release/prin.t03.htm) (accessed 2026-07-22): For NAICS 3151, reports 6,800 jobs in 2025 and annual 2019-2025 changes of 3.9% in labor productivity, -4.1% in real output, and -7.7% in hours worked.
- **S5** — [Adapting Trade Policy for Supply Chain Resilience](https://ustr.gov/sites/default/files/USTR_Adapting%20Trade%20Policy%20for%20Supply%20Chain%20Resilience_0.pdf) (accessed 2026-07-22): USTR states that US apparel manufacturing declined steadily over decades, notes interest in domestic and near-buyer production, and describes textile and apparel as particularly sensitive to import competition.
- **S6** — [The Metamorphosis of Women Business Owners: A Focus on Age](https://www2.census.gov/ces/wp/2024/CES-WP-24-71.pdf) (accessed 2026-07-22): Using 2021 Annual Business Survey data for 2020, reports that 62.4% of women owners of manufacturing employer businesses were age 55 or older, a broad succession proxy.
- **S7** — [2022 NAICS Definition: 315120 Apparel Knitting Mills](https://www.census.gov/naics/?details=31&input=31&year=2022) (accessed 2026-07-22): Defines the industry as establishments primarily engaged in knitting apparel or knitting fabric and then manufacturing apparel; the definition does not distinguish contract production from own-brand manufacturing.
- **S8** — [ICAMS Smart Manufacturing Adoption Study 2024](https://eng.auburn.edu/icams/ISE---ICAMS-SMART-Report_2024_V5.pdf) (accessed 2026-07-22): Among 97 manufacturing respondents, 8% used AI, the implementing share rose 12 percentage points, 58% remained at awareness or research, and lack of business cases and workforce skills were leading barriers.
