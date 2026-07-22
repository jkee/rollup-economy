# 441227 — Motorcycle, ATV, and All Other Motor Vehicle Dealers

*v5.1 Stage 1 research memo. Run `441227-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** no base (evidence-first) · A — · L — · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness STRESS_TEST_ONLY · action EVIDENCE_FIRST

**Driver:** Commercially available, powersports-specific AI can absorb repetitive lead response, qualification, follow-up, scheduling, and sales-support work.
**Weakness:** Demand is declining and highly seasonal, while the frozen firm count is missing and the catch-all industry definition prevents a clean eligibility denominator.

## Business-model lens
- Included: US lower-middle-market full-service powersports dealers selling motorcycles, scooters, ATVs, side-by-sides, personal watercraft, snowmobiles, powered golf carts, and closely related vehicles while also supplying repeat repair, maintenance, parts, accessories, warranty, financing, insurance, or trade-in services to external customers.
- Excluded: Pure merchandise retailers without a material repeat service relationship, aircraft-only dealers, utility-trailer-only dealers, online parts-only sellers, manufacturers, private-party sellers, captive internal units, and non-control financing vehicles.
- Customer and revenue model: Primarily consumer vehicle sales with repeat ownership-lifecycle revenue from parts, accessories, service labor, repair, warranty administration, financing and insurance commissions, apparel, and future trade-ins. Unit sales are transactional and seasonal; service and ownership support form the recurring outsourced-service component.
- Deviation from default lens: The NAICS code spans materially different vehicle categories, including motorcycles, ATVs, personal watercraft, utility trailers, aircraft, snowmobiles, and powered golf carts. It is narrowed to full-service powersports-oriented dealers so the operating workflow and repeat customer-service model are coherent.

## Executive view
The coherent opportunity is a full-service powersports dealer, not the entire catch-all NAICS category. AI can automate a meaningful layer of lead handling and sales administration, while physical vehicles, repairs, warranty work, and regulated closing keep the operator central. The industry currently faces material unit-demand and affordability pressure.

## How AI changes the work
Powersports-specific CRM tools already answer and qualify leads, reference live inventory and customer history, manage email and SMS follow-up, summarize conversations, and book appointments. These capabilities target BDC, sales-support, and administrative hours, but not technicians, parts handling, setup, appraisal, delivery, or accountable F&I approval.

## Value capture
Savings should be more retainable in service, parts, and fee workflows than in negotiated vehicle sales. Transparent listings, customer comparison shopping, OEM promotions, inventory carrying costs, and seasonal discounting are strong pass-through channels.

## Firm availability
Fragmentation and rising seller interest support potential control transfers, but the frozen LMM firm count is missing and no source supplies a denominator-based transfer rate. The broad code also makes both eligibility and addressable-firm availability particularly uncertain.

## Demand durability
New motorcycle, scooter, and ATV sales weakened in 2025, following a substantial decline at a major dealer group in 2024. Installed vehicles still require service and parts, and off-highway categories diversify the basket, but five-year demand should be underwritten conservatively.

## Risks and uncertainty
Major risks are prolonged affordability pressure, aging or shrinking rider cohorts, tariffs, OEM distress, franchise-transfer restrictions, seasonal working capital, weather, poor dealer data, and the code's mix of unrelated specialty vehicles. The most important missing evidence is a dealer census by activity and a closed-transfer denominator.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1237 | — | OBSERVED | — |
| n | — | — | — | MISSING | — |
| a | 0.19 | 0.3 | 0.41 | PROXY | S2, S3 |
| rho | 0.34 | 0.54 | 0.71 | ESTIMATE | S2, S3 |
| e | 0.28 | 0.48 | 0.67 | ESTIMATE | S1, S3 |
| s5 | 0.08 | 0.17 | 0.29 | ESTIMATE | S3, S4 |
| q | 0.32 | 0.54 | 0.74 | ESTIMATE | S3 |
| d5 | 0.75 | 0.91 | 1.09 | PROXY | S3, S5 |
| o | 0.8 | 0.91 | 0.98 | ESTIMATE | S2, S3 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.32 | 0.80 | 1.44 | ESTIMATE |
| F | — | — | — | MISSING |
| C | 6.40 | 10.00 | 10.00 | ESTIMATE |
| D | 6.00 | 8.28 | 10.00 | ESTIMATE |

## Caveats
- a: No source directly measures wage-weighted AI exposure for NAICS 441227.
- a: RumbleOn is a large multi-location operator rather than a representative LMM dealership.
- a: The software source is a vendor capability description, not a realized labor study.
- rho: Vendor-reported response and conversion performance is not independently audited in the cited page.
- rho: Implementation may shift staff toward higher-value selling rather than reduce hiring.
- rho: The broad code includes dealer types with different software stacks and seasonal patterns.
- e: The frozen n input is missing and is not replaced or estimated here.
- e: Establishment activity does not map cleanly to firm-level eligibility.
- e: The public dealer-group service mix likely overstates full-service capability among small specialty sellers.
- s5: Seller availability and broker commentary do not measure completed qualifying transfers.
- s5: The source does not quantify owner age, sale failures, or the population at risk.
- s5: Manufacturer consent and franchise rights can limit transferability.
- q: RumbleOn's scale, brand mix, financing, and cost structure differ from independent LMM firms.
- q: Observed category margins are not a direct measure of retention of AI-generated benefits.
- q: Promotional support and inventory aging can quickly override operating-cost savings.
- d5: Nominal revenue does not hold price and quality constant.
- d5: The MIC figures cover motorcycles, scooters, and ATVs but not every vehicle category in NAICS 441227.
- d5: Weather, tariffs, credit availability, interest rates, and OEM inventory cycles create large swings.
- o: Direct OEM sales, mobile mechanics, and online used-vehicle platforms could expand faster than assumed.
- o: Operator need is much lower for marketing and search than for repair, delivery, and regulated transaction steps.
- o: Rules and OEM franchise arrangements vary by state and vehicle category.

## Sources
- **S1** — [2022 NAICS Definition: 441227 Motorcycle, ATV, and All Other Motor Vehicle Dealers](https://www.census.gov/naics/?details=441227&input=441227&year=2022) (accessed 2026-07-22): Defines the industry to include motorcycles, scooters, ATVs, personal watercraft, utility trailers, aircraft, snowmobiles, powered golf carts, and other vehicles, with or without repair and parts activities; supports the heterogeneous lens and eligibility caveat.
- **S2** — [DP360 AI for Specialty Dealerships](https://www.dealershipperformancecrm.com/ai/) (accessed 2026-07-22): Documents powersports-specific automated email and SMS lead response, inventory-aware answers, qualification, follow-up, summaries, appointment handling, and human takeover; also reports vendor performance data across thousands of leads.
- **S3** — [RumbleOn, Inc. 2024 Form 10-K](https://www.sec.gov/Archives/edgar/data/1596961/000159696125000024/rmbl-20241231.htm) (accessed 2026-07-22): Describes a highly fragmented powersports market and dealership life-cycle services; reports 2024 revenue, gross profit, vehicle counts, compensation and other expenses, seasonality, ancillary-service economics, and regulatory constraints.
- **S4** — [Shifting Gears: Planning for Powersports Exit & Succession in Today's Environment, Part 1](https://advisor.morganstanley.com/the-stanek-haack-group/documents/field/s/st/stanek-haack-group/Website_Upload_NPDA_Article_pt_1.pdf) (accessed 2026-07-22): Reports specialist broker observations that more sellers were entering the powersports market, buyers had slowed, and more dealerships were available than during the pandemic, while emphasizing valuation and financing constraints.
- **S5** — [MIC reports 2025 motorcycle, ATV retail sales decline](https://powersportsbusiness.com/top-stories/2026/02/05/mic-reports-2025-motorcycle-atv-retail-sales-decline-as-buyers-shift-to-smaller-models/) (accessed 2026-07-22): Reports Motorcycle Industry Council data showing 2025 US new motorcycle and scooter sales down 7.6% and ATV sales down 3.5%, with motorcycles and scooters representing 73.3% of tracked new-unit sales.
