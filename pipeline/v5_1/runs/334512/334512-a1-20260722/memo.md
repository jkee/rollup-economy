# 334512 — Automatic Environmental Control Manufacturing for Residential, Commercial, and Appliance Use

*v5.1 Stage 1 research memo. Run `334512-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** CONDITIONAL · A 6.54 · L 2.33 · interval LOW_PRIORITY → PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Repeat demand for energy-saving, connected, and replacement controls paired with automatable engineering and indirect workflows.
**Weakness:** Sparse six-digit evidence and uncertainty over how many product manufacturers truly meet the recurring outsourced-service and transferable-firm lens.

## Business-model lens
- Included: US lower-middle-market manufacturers of automatic controls and regulators for heating, air-conditioning, refrigeration, buildings, residences, and appliances that repeatedly supply external customers, including associated engineering, configuration, and support.
- Excluded: Captive internal plants, shells, financing vehicles, firms outside the EBITDA band, pure installers or building-controls software publishers classified elsewhere, and one-off operations without a repeat external-customer model.
- Customer and revenue model: Product and system sales to OEMs, distributors, contractors, building owners, and appliance makers, often supplemented by engineering, software, configuration, replacement, and support revenue; repeat demand comes from production programs, replacement cycles, retrofits, and installed-base support.
- Deviation from default lens: none

## Executive view
Controls manufacturing combines a meaningful but bounded AI opportunity in engineering and indirect work with durable need for physical, validated products. The recurring external-customer lens fits best where OEM programs, replacement parts, software, configuration, or installed-base support create repeat relationships; purely project-based or captive plants are weaker fits.

## How AI changes the work
AI can accelerate requirements parsing, design documentation, embedded-software assistance, quoting, production planning, support triage, supplier analysis, and inspection interpretation. Physical assembly, calibration, environmental testing, field troubleshooting, and accountable design approval remain human- and equipment-intensive.

## Value capture
Differentiated products, qualification histories, proprietary protocols, and switching costs support retention of some productivity benefit. OEM cost-down demands, transparent bills of material, competitive tenders, and eventual repricing share savings with customers.

## Firm availability
The classification contains external product manufacturers, but not every LMM firm supplies a recurring outsourced service or represents a transferable standalone operation. Cross-industry owner aging suggests succession supply, yet industry-specific deal and ownership evidence is absent.

## Demand durability
BLS projects real output growth for the broader instrument category, and DOE identifies large energy-saving potential and meaningful underpenetration of building automation. Controls remain embodied in physical cyber-physical systems, although software platforms and OEM integration can shift value away from standalone manufacturers.

## Risks and uncertainty
The strongest numeric evidence is four-digit rather than six-digit. Product mix spans residential, commercial, refrigeration, and appliances; customer power and differentiation vary widely. Cybersecurity, interoperability, component sourcing, warranty exposure, construction cyclicality, and rapid protocol change can absorb projected AI gains.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.3594 | — | OBSERVED | — |
| n | — | 79 | — | ESTIMATE | — |
| a | 0.18 | 0.28 | 0.4 | PROXY | S2, S3, S4 |
| rho | 0.4 | 0.58 | 0.72 | ESTIMATE | S3, S4, S5 |
| e | 0.38 | 0.56 | 0.72 | ESTIMATE | S1 |
| s5 | 0.12 | 0.22 | 0.34 | PROXY | S6 |
| q | 0.48 | 0.66 | 0.8 | ESTIMATE | S5 |
| d5 | 1.02 | 1.11 | 1.22 | PROXY | S5, S7, S8 |
| o | 0.88 | 0.95 | 0.99 | ESTIMATE | S1, S7 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 1.04 | 2.33 | 4.14 | ESTIMATE |
| F | 2.46 | 3.82 | 4.85 | ESTIMATE |
| C | 9.60 | 10.00 | 10.00 | ESTIMATE |
| D | 8.98 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: The occupational source is NAICS 334500 rather than 334512.
- a: Task exposure is inferred rather than directly measured.
- a: The provided compensation-to-receipts input may blend production labor with software and engineering labor whose automation potential differs sharply.
- rho: NIST evidence describes manufacturing broadly rather than this six-digit industry.
- rho: DOE documents interoperability barriers in building-control deployment, not factory-side AI implementation.
- e: No source measures lens eligibility among firms in the EBITDA band.
- e: The industry definition is establishment-based, whereas eligibility is firm-based.
- e: The supplied LMM firm-count estimate may include units whose economics are consolidated into larger parents.
- s5: The owner-age source is cross-industry, owner-level, and dated 2018.
- s5: Age 55 or older is not itself evidence of intent or ability to sell.
- s5: Strategic subsidiaries may have no individual owner-succession event.
- q: No source directly measures pass-through of AI benefits in this industry.
- q: Capture differs sharply between proprietary installed-base products and commodity OEM components.
- d5: The BLS series is four-digit and spans materially different instrument markets.
- d5: DOE energy-savings potential does not ensure purchase adoption.
- d5: Constant-quality adjustment is approximate for rapidly improving connected-control products.
- o: The boundary between manufacturer, OEM, systems integrator, and software platform may shift.
- o: Open protocols and commodity microprocessors could reduce the operator share faster than assumed.

## Sources
- **S1** — [2022 NAICS definition: Automatic Environmental Control Manufacturing for Residential, Commercial, and Appliance Use](https://www.census.gov/naics/?details=33&input=33&year=2022) (accessed 2026-07-23): Defines 334512 as manufacturing automatic controls and regulators for heating, air-conditioning, refrigeration, and appliances.
- **S2** — [May 2023 OEWS: NAICS 334500 Navigational, Measuring, Electromedical, and Control Instruments Manufacturing](https://www.bls.gov/oes/2023/may/naics4_334500.htm) (accessed 2026-07-23): Provides the broader-industry occupational mix, including 17.58% architecture and engineering, 26.89% production, and 7.77% office and administrative support employment.
- **S3** — [Incorporating AI impacts in BLS employment projections: occupational case studies](https://www.bls.gov/opub/mlr/2025/article/incorporating-ai-impacts-in-bls-employment-projections.htm) (accessed 2026-07-23): States that generative AI can support many architecture and engineering tasks and increase productivity while demand for electrical and electronics engineering remains.
- **S4** — [The Rise of Artificial Intelligence in U.S. Manufacturing](https://www.nist.gov/mep/manufacturing-infographics/rise-artificial-intelligence-us-manufacturing) (accessed 2026-07-23): Describes manufacturing AI applications from predictive maintenance to generative design and notes implementation barriers.
- **S5** — [Artificial Intelligence in Manufacturing: Real World Success Stories and Lessons Learned](https://www.nist.gov/blogs/manufacturing-innovation-blog/artificial-intelligence-manufacturing-real-world-success-stories) (accessed 2026-07-23): Reports manufacturing AI use cases that improved uptime, quality, throughput, and scrap, grounding implementation potential without measuring this industry.
- **S6** — [Business Owners' Ages](https://www.census.gov/content/dam/Census/library/visualizations/2020/comm/business-owners-ages.pdf) (accessed 2026-07-23): Reports that 51% of responding owners of US employer businesses were age 55 or older in 2018, across industries.
- **S7** — [About Building Controls](https://www.energy.gov/cmei/buildings/about-building-controls) (accessed 2026-07-23): Describes controls as cyber-physical building infrastructure, reports roughly 30% HVAC energy-savings potential, and identifies interoperability and workforce barriers.
- **S8** — [Employment and output by industry, 2024–34](https://www.bls.gov/emp/tables/industry-employment-and-output.htm) (accessed 2026-07-23): Projects NAICS 334500 real output from $149.7 billion in 2024 to $184.7 billion in 2034, a 2.1% annual compound rate.
