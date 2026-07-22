# 314910 — Textile Bag and Canvas Mills

*v5.1 Stage 1 research memo. Run `314910-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** LOW_PRIORITY · A 5.43 · L 1.08 · interval STRUCTURAL_OUT → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Specification-rich repeat fabrication creates AI-addressable commercial and planning work around products that still require a domestic physical operator in many applications.
**Weakness:** Sewing dominates employment, and the share of firms with truly recurring outsourced programs rather than product sales is not observed.

## Business-model lens
- Included: Lower-middle-market U.S. mills providing repeat outsourced design-to-specification and contract fabrication of industrial bags, awnings, sails, tarpaulins, tents, and boat, pool, truck, equipment, or other protective textile covers for external commercial, institutional, government, OEM, fleet, marine, agricultural, and industrial customers.
- Excluded: Commodity or owned-brand product manufacturing sold without a recurring outsourced relationship; one-off consumer craft work; retail installation-only businesses; wholesalers; luggage and handbags classified elsewhere; captive internal plants; shells; and non-control financing vehicles.
- Customer and revenue model: Customers buy repeat production runs or project lots against drawings, dimensions, material, performance, and compliance requirements, with revenue commonly quoted per unit, lot, project, or fixed-price contract.
- Deviation from default lens: The code is narrowed to repeat contract and design-to-specification fabrication because NAICS 314910 combines commodity textile bags with custom awnings, sails, tents, tarpaulins, and covers; these models differ materially in customer relationship, automation workflow, pricing, and retention.

## Executive view
Repeat custom and contract canvas fabrication is a coherent subset of this heterogeneous product code. It has more specification, quoting, scheduling, compliance, and customer-coordination work than commodity sewing alone suggests, but the dominant occupation is still sewing-machine operation and most value creation remains physical.

## How AI changes the work
AI can structure drawings and specifications, retrieve comparable jobs, assist estimates and material takeoffs, improve nesting and schedules, draft proposals and compliance documents, communicate order status, and support camera-based inspection. Cutting, sewing, welding, fitting, assembly, installation, maintenance, and final acceptance remain operator work.

## Value capture
Quoted project and unit prices provide room to retain early savings. Standardized work is exposed to competitive rebids and buyer cost-down demands, while low-volume engineered work can preserve more value through fast turnaround, quality, certification, and domestic-source compliance.

## Firm availability
The frozen dataset estimates 45 LMM-band firms, but only an unobserved subset earns repeat outsourced revenue rather than ordinary goods sales. Custom industrial covers, fleet programs, OEM sewing, institutional tents, and compliant government work are more likely to qualify than commodity bags or consumer one-offs.

## Demand durability
The broader 3149 production index recovered in 2025 after a multi-year decline. Physical wear, weather, replacement, emergency response, fleet and industrial uses support repeat demand, while Berry Amendment rules create a domestic source requirement for covered DoD tents, tarpaulins, covers, and canvas products.

## Risks and uncertainty
The main uncertainty is the eligible-firm denominator. Additional risks are owner-dependent estimating, volatile project backlogs, customer concentration, commodity import competition, case-specific government sourcing rules, legacy drawings, heterogeneous low-volume jobs, and the possibility that physical process constraints leave little realizable labor benefit.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.2592 | — | OBSERVED | — |
| n | — | 45 | — | ESTIMATE | — |
| a | 0.11 | 0.2 | 0.31 | PROXY | S2, S3, S7 |
| rho | 0.3 | 0.52 | 0.72 | ESTIMATE | S7 |
| e | 0.12 | 0.28 | 0.5 | ESTIMATE | S1 |
| s5 | 0.09 | 0.18 | 0.29 | PROXY | S4 |
| q | 0.25 | 0.48 | 0.7 | ESTIMATE | S6 |
| d5 | 0.75 | 0.95 | 1.15 | PROXY | S5, S6 |
| o | 0.9 | 0.96 | 0.99 | ESTIMATE | S1, S6, S7 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.34 | 1.08 | 2.31 | ESTIMATE |
| F | 0.64 | 1.90 | 3.25 | ESTIMATE |
| C | 5.00 | 9.60 | 10.00 | ESTIMATE |
| D | 6.75 | 9.12 | 10.00 | ESTIMATE |

## Caveats
- a: OEWS data cover all Other Textile Product Mills at four digits, not the six-digit target.
- a: Employment counts are not wage weights and omit within-occupation task variation.
- a: Software-AI exposure does not fully capture robotics or automated cutting and sewing.
- rho: No 314910-specific adoption survey distinguishes deployed AI from ordinary CAD, ERP, or cutting automation.
- rho: The estimate assumes drawings and historical quotes can be digitized and governed.
- rho: Customer certification and final acceptance remain human-accountable.
- e: The frozen firm count is margin-bridged from size classes rather than an observed target list.
- e: NAICS product descriptions do not reveal whether sales are repeat outsourced programs or ordinary goods transactions.
- e: Custom residential awning and boat-cover shops may be too project-driven or owner-dependent to qualify.
- s5: Gallup is cross-industry and not specific to manufacturing or the LMM band.
- s5: Plans to sell, gift, or go public are not completed qualifying control transfers.
- s5: A small eligible population means a few deals materially change the realized rate.
- q: No observed study measures AI-benefit pass-through in textile bag and canvas contracts.
- q: Government domestic-sourcing rules protect eligibility but do not eliminate price competition.
- q: Retention differs sharply between commodity bag programs and engineered custom covers or shelters.
- d5: The output series is NAICS 3149 and includes products outside 314910.
- d5: The 2021 level was pandemic-affected and 2025 may reflect inventory or procurement timing.
- d5: Berry Amendment coverage is case-specific and only supports a portion of industry demand.
- o: This estimate conditions on the quantity already surviving in d5 and does not count import displacement twice.
- o: Standard bags are more automatable and directly sourceable than fitted covers, sails, awnings, and shelters.
- o: No direct source measures self-service or software-only displacement in this physical fabrication niche.

## Sources
- **S1** — [2022 Economic Census Form MC-31490: Textile Bag and Canvas Mills](https://bhs.econ.census.gov/ombpdfs2022/export/2022_MC-31490_su.pdf) (accessed 2026-07-22): Defines the 314910 activity as textile bag and canvas products made from purchased materials, including boat, swimming-pool, and truck covers, awnings, sails, tarpaulins, and tents.
- **S2** — [BLS OEWS Data Tables for Industry Charts, May 2024](https://www.bls.gov/oes/2024/may/ind_emp_chart/ind_emp_chart_data.htm) (accessed 2026-07-22): Reports the largest occupations in Other Textile Product Mills: 18,180 sewing-machine operators, 3,650 assemblers/fabricators, 2,700 production supervisors, 2,260 sales representatives, 2,210 general and operations managers, 1,780 office clerks, and 1,590 shipping/inventory clerks.
- **S3** — [Artificial Intelligence and the Changing Demand for Skills in the Labour Market](https://www.oecd.org/content/dam/oecd/en/publications/reports/2024/04/artificial-intelligence-and-the-changing-demand-for-skills-in-the-labour-market_861a23ea/88684e36-en.pdf) (accessed 2026-07-22): Finds high-skill cognitive occupations more exposed to software AI and non-routine physical occupations less exposed, with textile pressers among the least exposed; cautions that exposure measures do not equal observed adoption.
- **S4** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Gallup's fall-2024 U.S. survey of 1,264 working business owners reports that 22% of employer-business owners planned to sell or transfer ownership within five years and that 52.3% of employer businesses had owners age 55 or older.
- **S5** — [Industrial Production: Other Textile Product Mills (NAICS 3149)](https://fred.stlouisfed.org/series/IPG3149A) (accessed 2026-07-22): Federal Reserve real-output index reported 109.6061 in 2021, 94.8138 in 2022, 95.1701 in 2023, 92.8047 in 2024, and 99.6271 in 2025.
- **S6** — [U.S. Department of Commerce: Berry Amendment Covered Items](https://www.trade.gov/berry-covered-items) (accessed 2026-07-22): States that covered DoD procurement generally must be U.S.-produced and expressly includes tents and tent structural components, tarpaulins, covers, synthetic or coated fabric, and canvas products.
- **S7** — [BLS Occupational Outlook Handbook: Quality Control Inspectors](https://www.bls.gov/ooh/production/quality-control-inspectors.htm) (accessed 2026-07-22): Describes specification review, measurement, electronic inspection, reporting, and automated vision systems, while explaining that validation and texture or performance inspections continue to require people.
