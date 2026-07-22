# 488991 — Packing and Crating

*v5.1 Stage 1 research memo. Run `488991-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 5.82 · L 0.13 · interval STRUCTURAL_OUT → STRUCTURAL_OUT · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** A durable need to physically protect irregular and valuable goods, supplemented by automatable estimating, documentation, planning, and inspection workflows.
**Weakness:** The addressable labor layer is small relative to physical execution, and the injected compensation ratio is both low and potentially distorted by receipts and material pass-through.

## Business-model lens
- Included: US lower-middle-market firms that repeatedly provide outsourced packing, custom or standard crating, protective preparation, marking, weighing, documentation, and related preparation of customer goods for transportation.
- Excluded: Packaging and labeling services classified in 561910, in-house or captive shipper and warehouse packing departments, primary freight carriage or warehousing activities, one-person shells without transferable operations, and non-control financing vehicles.
- Customer and revenue model: Customers include manufacturers, distributors, government agencies, freight forwarders, movers, exporters, art and equipment owners, and other shippers. Revenue is commonly job-, unit-, material-, labor-, or requirements-contract based, including fixed-price work, scheduled repeat services, call-off orders, and customer-specific recurring arrangements.
- Deviation from default lens: none

## Executive view
Packing and crating is a physically executed transportation-support service with a narrow but practical AI layer. The best near-term opportunities are quoting, dimensional capture, crate and material recommendations, scheduling, records, labels, customer communication, and inspection assistance. AI-enabled robotics can address repeated standard handling, but custom, irregular, fragile, and high-value goods preserve manual skill and operator accountability. The unusually low injected compensation ratio should be treated cautiously against the observed labor-intensive occupation mix.

## How AI changes the work
AI can turn photos, dimensions, specifications, destinations, and regulations into draft quotes, bills of material, packing plans, work instructions, labels, and shipment records. Computer vision can assist measurement, condition documentation, and quality checks. Physical robotics is plausible for repetitive picking, packing, and palletizing, while NIST evidence shows perception, grasping, loose packaging, and complex shapes remain difficult; humans continue crate construction, fit-up, padding, securing, and exception handling.

## Value capture
Fixed-price jobs and requirements contracts can preserve productivity gains within a term, especially when fewer estimating hours, lower material waste, and fewer errors are not visible to the buyer. Competitive quotes, reverse auctions, rebids, transparent input costs, and simple customer self-packing return part of the benefit to customers over five years.

## Firm availability
Most active firms in this narrow NAICS should fit the outsourced-service lens and have tangible, transferable operations. Availability is uncertain because the estimated LMM population is small, no direct transfer series exists, and some businesses are bundled with movers, warehouses, forwarders, manufacturers, or packaging suppliers rather than standing alone.

## Demand durability
Growing freight volume supports modest underlying demand, and specialized goods continue to need protection and accountable preparation. Demand is cyclical and mix-sensitive: bulk freight contributes little, while capital equipment, defense, exports, relocations, art, and fragile or regulated goods contribute disproportionately. Insourcing, standardized reusable packaging, and automation can reduce outsourced units.

## Risks and uncertainty
The main risks are injury, damage and claims, customer concentration, lumpy project volume, material inflation, facility and equipment utilization, trade and industrial cycles, and low-price procurement. Evidence is weak at the six-digit level: occupation data combine 488991 with 488999, robotics evidence comes from adjacent applications, and eligibility, transfer frequency, value retention, and operator-required demand are estimates.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.0481 | — | OBSERVED | — |
| n | — | 45 | — | ESTIMATE | — |
| a | 0.07 | 0.14 | 0.24 | PROXY | S2, S3, S4, S5, S6, S7 |
| rho | 0.3 | 0.5 | 0.7 | ESTIMATE | S6, S7, S12 |
| e | 0.65 | 0.82 | 0.94 | ESTIMATE | S1, S9 |
| s5 | 0.1 | 0.18 | 0.3 | ESTIMATE | S11 |
| q | 0.38 | 0.58 | 0.78 | ESTIMATE | S9 |
| d5 | 0.95 | 1.05 | 1.16 | PROXY | S8 |
| o | 0.84 | 0.94 | 0.99 | ESTIMATE | S1, S7, S10 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.04 | 0.13 | 0.32 | ESTIMATE |
| F | 2.20 | 3.27 | 4.21 | ESTIMATE |
| C | 7.60 | 10.00 | 10.00 | ESTIMATE |
| D | 7.98 | 9.87 | 10.00 | ESTIMATE |

## Caveats
- a: The occupation mix covers NAICS 4889 and includes activities outside packing and crating.
- a: O*NET tasks cover packers across all industries and do not provide 488991 task time or payroll weights.
- a: BLS projections largely reflect retail, warehouse, and manufacturing packers, whose automation economics may differ from outsourced custom crating.
- a: The injected compensation ratio is unusually low relative to the physically labor-intensive occupation evidence and may reflect gross receipts, material or pass-through revenue, vintage mismatch, and cross-code harmonization.
- rho: Automation feasibility varies sharply between repeated standard products and one-off irregular or fragile goods.
- rho: NIST robotics evidence covers manufacturing and fulfillment applications rather than 488991 firms.
- rho: Economy-wide AI adoption does not measure successful workflow implementation in packing and crating.
- rho: This primitive excludes demand, pricing, and valuation effects.
- e: No source reports eligibility under the frozen lens.
- e: The injected count of 45 firms is margin-bridged using a broad transportation margin that may not fit material-intensive custom crating.
- e: Establishment classification can be blurred when packing is bundled with moving, freight forwarding, warehousing, or manufactured packaging.
- s5: The SBA retirement evidence is old, economy-wide, and measures expected retirement rather than business transfers.
- s5: Private small-company transactions are underreported.
- s5: Sale of equipment or customer relationships without an operating-company transfer is excluded.
- q: The GAO procurement evidence concerns one Navy competition and is not representative of all commercial accounts.
- q: Material prices and damage claims can obscure retained labor productivity.
- q: The estimate excludes implementation difficulty, demand changes, and valuation effects.
- d5: Aggregate freight tonnage is an indirect driver and includes bulk commodities requiring little or no outsourced packing.
- d5: The BTS forecast is long term and based on an older FAF vintage rather than a five-year 488991 forecast.
- d5: A recession or trade shock at the year-five endpoint could materially reduce specialized crating demand.
- o: Defense household-goods requirements illustrate accountability but not the full industrial and commercial mix.
- o: Robotics progress could accelerate for repeated standard goods while remaining limited for one-off crates.
- o: An automated packing company still counts as an accountable operator under this primitive.

## Sources
- **S1** — [U.S. Census Bureau NAICS Sector 48-49 Definitions](https://www.census.gov/naics/resources/archives/sect48-49.html) (accessed 2026-07-22): NAICS 488991 comprises establishments primarily engaged in packing, crating, and otherwise preparing goods for transportation, while packaging and labeling services are classified in 561910.
- **S2** — [BLS May 2024 OEWS Data Tables for Industry Employment Charts](https://www.bls.gov/oes/2024/may/ind_emp_chart/ind_emp_chart_data.htm) (accessed 2026-07-22): For broader NAICS 4889, the ten largest occupations are 4,540 hand packers, 3,870 material movers, 3,800 heavy truck drivers, 2,510 customer service representatives, 2,010 general and operations managers, 1,340 transportation/material-moving supervisors, 1,320 industrial truck operators, 1,230 shipping/receiving clerks, 1,070 light truck drivers, and 990 office clerks.
- **S3** — [O*NET OnLine: Packers and Packagers, Hand](https://www.onetonline.org/link/details/53-7064.00) (accessed 2026-07-22): Core tasks include inspecting containers and goods, measuring, weighing and counting, recording order information, sealing containers, assembling and padding crates, moving materials, labeling, cleaning, and loading packaging equipment.
- **S4** — [O*NET OnLine: Customer Service Representatives](https://www.onetonline.org/link/summary/43-4051.00) (accessed 2026-07-22): Customer-service tasks include intake and order information, interaction records, notifications, charge calculation, billing, contract forms, complaint resolution, transactional verification, and shipping-method recommendations.
- **S5** — [O*NET OnLine: Office Clerks, General](https://www.onetonline.org/link/summary/43-9061.00) (accessed 2026-07-22): Office-clerk tasks include calls, database and record maintenance, document review, data checking, schedules, correspondence, bills and contracts, forms, basic bookkeeping, and inventory records.
- **S6** — [BLS Occupational Outlook Handbook: Hand Laborers and Material Movers](https://www.bls.gov/ooh/transportation-and-material-moving/hand-laborers-and-material-movers.htm) (accessed 2026-07-22): BLS describes hand packing as labeling, defect inspection, recordkeeping, shipment preparation, and physical work; it projects hand packer employment to decline from 591,800 in 2024 to 559,700 in 2034 and states that evolving warehouse and packaging technology reduces manual tasks.
- **S7** — [NIST: Research Opportunities for Advancing Measurement Science for Manufacturing Robotics](https://nvlpubs.nist.gov/nistpubs/gcr/2024/NIST.GCR.24-054.pdf) (accessed 2026-07-22): NIST reports early growth in AI-enabled picking, sorting, packing, palletizing, and vision systems but explains that random-object picking remains difficult because of perception, planning, control, geometry, material, and grasping challenges; loose or complex packaging remains difficult for advanced systems.
- **S8** — [Bureau of Transportation Statistics: Freight Activity in the U.S. Expected to Grow Fifty Percent by 2050](https://www.bts.gov/newsroom/freight-activity-us-expected-grow-fifty-percent-2050) (accessed 2026-07-22): The BTS/FHWA Freight Analysis Framework projects US freight tonnage to grow 50% from 2020 to 2050 to 28.7 billion tons, with freight value doubling in constant 2017 dollars.
- **S9** — [GAO Bid Protest Decision: Pacific Island Movers](https://www.gao.gov/products/b-287643.2-0) (accessed 2026-07-22): The GAO decision documents a Navy packing-and-crating procurement competed through a reverse auction and revised price proposals, illustrating direct price competition in a customer contract.
- **S10** — [Department of Defense Personal Property Program Tender of Service](https://media.defense.gov/2026/Apr/27/2003920087/-1/-1/0/2025%20DP3%20TENDER%20OF%20SERVICE%20-%2015%20MAY%202025%20%28FINAL%20COPY%29.PDF) (accessed 2026-07-22): The tender makes the service provider liable and responsible for packing, inspection of pre-packed goods, repacking, material and container selection, fragile-item crating, regulatory compliance, accurate inventory, condition documentation, customer review, and backup procedures.
- **S11** — [SBA Office of Advocacy: Retirement, Recessions and Older Small Business Owners](https://advocacy.sba.gov/2012/12/01/retirement-recessions-and-older-small-business-owners/) (accessed 2026-07-22): The study reports that small-business owners in 2010 expected to retire at an average age of 72.6, compared with 68.4 for employees, cautioning against assuming rapid retirement-driven transfers.
- **S12** — [Census Bureau: Large Firms With at Least 20 Employees Biggest AI Users](https://www.census.gov/library/stories/2026/05/ai-use-businesses.html) (accessed 2026-07-22): BTOS data from December 2025 to May 2026 show overall business AI use around 17%-20%, 37% among firms with at least 250 employees, and less than 20% among firms with four or fewer employees, indicating an adoption gap relevant to smaller operators.
