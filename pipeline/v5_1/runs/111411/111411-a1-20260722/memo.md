# 111411 — Mushroom Production

*v5.1 Stage 1 research memo. Run `111411-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** no base (evidence-first) · A — · L — · interval STRUCTURAL_OUT → HIGHEST_PRIORITY · readiness STRESS_TEST_ONLY · action EVIDENCE_FIRST

**Driver:** Recurring demand for a perishable physical food product, combined with sensor-rich controlled environments where better forecasting and operating decisions can improve yield and reduce loss without inviting direct AI substitution.
**Weakness:** The investment case rests heavily on broad agricultural and task proxies, while much of climate control is already automated and the labor-intensive harvest remains physically difficult to automate; missing compensation and firm-count inputs prevent sizing the economic opportunity.

## Business-model lens
- Included: U.S. lower-middle-market establishments growing edible mushrooms under cover in mines, underground structures, or other controlled environments, including cultivation, climate monitoring, harvesting, grading, packing, food-safety compliance, sales, and distribution coordination.
- Excluded: Hobby and home cultivation, businesses that only manufacture equipment or sell growing kits, restaurants growing solely for their own kitchens, wild mushroom foraging, and mushroom-product processors that do not grow mushrooms.
- Customer and revenue model: Growers earn primarily per-pound crop revenue through recurring wholesale sales of fresh or processed mushrooms to distributors, retailers, foodservice buyers, and processors; specialty growers may add direct restaurant or consumer channels.
- Deviation from default lens: none

## Executive view
Mushroom production is a defensible physical operating business with recurring food demand, but its AI opportunity is evolutionary rather than transformational. The strongest case is a well-run specialty or mixed-variety grower with disciplined food-safety systems, repeat accounts, differentiated quality, and enough data infrastructure to improve yield, energy, scheduling, and administrative throughput. Compensation intensity and the absolute lower-middle-market firm opportunity cannot be assessed because both dataset inputs are missing.

## How AI changes the work
AI can support crop and demand forecasting, environmental anomaly detection, set-point optimization, yield prediction, quality documentation, traceability, labor scheduling, purchasing, route planning, pricing support, and customer service. Climate control is already substantially automatable, while picking, sanitation, packing, maintenance, and biological intervention remain embodied; this caps near-term exposure and shifts value toward decision quality and loss avoidance.

## Value capture
A capable operator should retain part of the gross benefit through higher yield consistency, less spoilage, lower energy or input waste, faster documentation, and leaner planning and customer-service work. Realized capture depends on reliable sensors and records, integration costs, staff adoption, crop variability, and whether savings are measurable enough to avoid being competed away through lower prices.

## Firm availability
Broad U.S. farm demographics point to succession pressure, but mushroom-specific sale probability is not observed. Specialized facilities and know-how can create defensibility yet also narrow the buyer pool; family succession, closure, and asset sales may be more common than clean going-concern transfers. The dataset provides no lower-middle-market firm count, so this packet does not infer an addressable number of targets.

## Demand durability
Recent USDA data indicate a large, stable category with slight volume and value growth, while variety performance diverges. Repeat use in retail and foodservice supports durability, especially where quality and delivery are consistent, but commodity varieties remain exposed to buyer power, imports, input costs, and price competition.

## Risks and uncertainty
Principal uncertainties are the absence of mushroom-specific task shares, AI adoption returns, customer-retention cohorts, owner-transition data, compensation intensity, and eligible firm counts. Operational risks include contamination and recall, crop disease, climate-system failure, energy costs, labor availability, perishability, customer concentration, import competition, and specialized real-estate requirements.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | — | — | MISSING | — |
| n | — | — | — | MISSING | — |
| a | 0.16 | 0.25 | 0.35 | PROXY | S4, S5, S6, S8 |
| rho | 0.38 | 0.56 | 0.72 | ESTIMATE | S5, S6, S8 |
| e | 0.45 | 0.65 | 0.8 | ESTIMATE | S2, S3 |
| s5 | 0.08 | 0.17 | 0.27 | PROXY | S7 |
| q | 0.28 | 0.43 | 0.59 | PROXY | S2, S3, S8 |
| d5 | 0.93 | 1.08 | 1.24 | PROXY | S2, S3 |
| o | 0.93 | 0.98 | 1 | ESTIMATE | S1, S6, S8 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | — | — | — | MISSING |
| F | — | — | — | MISSING |
| C | 5.60 | 8.60 | 10.00 | PROXY |
| D | 8.65 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: No mushroom-specific task-time survey was located.
- a: Vendor descriptions establish technical capability, not adoption or realized labor savings.
- a: Exposure is not equivalent to headcount removal because food-safety checks and physical intervention remain necessary.
- rho: No audited mushroom-farm AI return-on-investment study was located.
- rho: Existing conventional automation reduces the incremental gain attributable specifically to AI.
- rho: Savings may arrive as higher consistency and avoided loss rather than cash payroll reduction.
- e: Industry sales statistics do not identify lower-middle-market establishments.
- e: Grower count was intentionally not researched because firm count is a dataset-injected primitive.
- e: Some operations may be divisions of larger food or agricultural groups rather than independently transferable firms.
- s5: The USDA demographic source covers all U.S. farms, not mushroom growers or lower-middle-market firms.
- s5: Producer age is not a direct measure of sale intent or transaction completion.
- s5: Family succession, closure, or asset liquidation may substitute for a going-concern sale.
- q: USDA reports industry aggregates rather than customer cohorts.
- q: Retention likely differs sharply between commodity Agaricus and differentiated specialty varieties.
- q: Food-safety events or quality lapses can disrupt an otherwise repeat-purchase relationship.
- d5: The cited change is only one marketing year and does not itself establish a five-year trend.
- d5: Nominal sales value can move with price rather than physical demand.
- d5: Aggregate growth conceals declines in white Agaricus and some specialty categories.
- o: This is a structural estimate rather than an observed displacement rate.
- o: Technical feasibility of automated cultivation does not establish economic substitution.
- o: The estimate does not capture competitive margin pressure from better-automated rival growers.

## Sources
- **S1** — [North American Industry Classification System: Sector 11, NAICS 111411 Mushroom Production](https://www.census.gov/naics/resources/archives/sect11.html) (accessed 2026-07-23): Defines the industry as establishments growing mushrooms under cover in mines, underground structures, or other controlled environments.
- **S2** — [USDA NASS Mushrooms Annual Report](https://esmis.nal.usda.gov/publication/mushrooms) (accessed 2026-07-23): Identifies the official annual mushroom measures, including production, sales volume, price per pound, value, variety, utilization, and intentions.
- **S3** — [USDA ERS Vegetables and Pulses Outlook: December 2025](https://ers.usda.gov/sites/default/files/_laserfiche/outlooks/113612/VGS-377.pdf?v=26121) (accessed 2026-07-23): Reports 2024/25 all-mushroom value of about $1.1 billion, sales volume of 669.9 million pounds, and divergent trends across white and brown Agaricus and specialty varieties.
- **S4** — [BLS Occupational Employment and Wage Statistics: Farmworkers and Laborers, Crop, Nursery, and Greenhouse](https://www.bls.gov/oes/2023/may/oes452092.htm) (accessed 2026-07-23): Describes manual crop tasks including planting, cultivating, harvesting, cleaning, grading, sorting, packing, and loading.
- **S5** — [BLS Occupational Employment and Wage Statistics: Support Activities for Agriculture and Forestry](https://www.bls.gov/oes/2023/may/naics3_115000.htm) (accessed 2026-07-23): Provides a broad agricultural labor proxy in which crop, nursery, and greenhouse farmworkers account for a large share of employment.
- **S6** — [Mushroom Climate: Automated Environmental Control](https://mushroom-climate.com/en/automated-environmental-control/) (accessed 2026-07-23): Describes automated climate-control capability across mushroom growing cycles while distinguishing operator and technologist oversight and manual picking.
- **S7** — [USDA NASS 2022 Census of Agriculture Highlights: Farm Producers](https://www.nass.usda.gov/Publications/Highlights/2024/Census22_HL_FarmProducers_FINAL.pdf) (accessed 2026-07-23): Reports that 38% of U.S. farm producers were age 65 or older and average producer age was 58.1 in 2022, supporting a broad succession proxy.
- **S8** — [FDA Webinar on Basic Mushroom Growing, Harvesting, Holding, and Packing Activities Under the Produce Safety Rule](https://www.fda.gov/food/workshops-meetings-webinars-food-and-dietary-supplements/webinar-basic-mushroom-growing-harvesting-holding-and-packing-activities-under-produce-safety-rule) (accessed 2026-07-23): Confirms that mushroom growing, harvesting, packing, and holding are subject to food-safety practices and highlights outbreak risks for specialty mushrooms.
