# 811192 — Car Washes

*v5 Stage 1 research memo. Run `811192-a1-20260722`, model `gpt-5.6-terra`, 2026-07-22, attempt 1.*

**Base tier:** LOW_PRIORITY · A 6.40 · L 1.25 · interval STRUCTURAL_OUT → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Recurring membership billing can make centrally managed customer, sales, and administrative workflow improvements economically useful across multiple sites.
**Weakness:** Most of the core service is physical and the sector's mixed formats and local saturation make labor opportunity, demand, and transferability highly site-specific.

## Business-model lens
- Included: US lower-middle-market operators of automatic, tunnel, hand-wash, detailing, mobile, and self-service car-wash sites that sell washing or cleaning services to external vehicle owners and have repeat or membership revenue where applicable.
- Excluded: Captive dealership, fleet, rental-car, or gasoline-station wash units not operated as a separately transferable service business; holding companies; and financing vehicles.
- Customer and revenue model: Consumer and small-fleet vehicle owners buy individual washes, detailing, or self-service time; many automatic and tunnel operators also bill monthly unlimited-wash memberships.
- Deviation from default lens: none

## Executive view
Car washes are a physical local service with repeat consumer demand and a growing membership billing model. The main AI opportunity is in the operational wrapper around the wash rather than the wash itself: member acquisition and retention, customer support, pricing support, scheduling, reporting, and manager workflows. The NAICS code combines automatic, hand, detailing, and self-service activity, so individual-site diligence matters more than a sector average.

## How AI changes the work
O*NET describes vehicle-cleaner work as drying, spraying, scrubbing, inspection, machine monitoring, inventory, and equipment handling. Those tasks explain why a large share of direct service labor is not readily substituted by AI. Automatic and self-service formats already reduce some manual work; AI is more likely to reduce avoidable administrative and sales effort, improve membership recovery, and help managers coordinate sites than to replace physical cleaning or equipment maintenance.

## Value capture
Unlimited memberships create recurring operator-controlled billing. ICA reports strong renewal intent and some willingness to accept price increases when quality is maintained, while Rinsed reported stronger member revenue and weaker retail revenue in its cited period. That supports retaining a portion of workflow gains, but the same ICA evidence warns that saturation and competitive density are rising, which can force savings into service, promotions, or customer pricing.

## Firm availability
The transfer estimate is deliberately uncertain. BizBuySell reports completed sales in a broader automotive-service marketplace and a current industry source documents a 530-location car-wash acquisition. These observations show active transaction channels, not an owner-age-adjusted transfer probability for LMM car washes. Diligence should seek brokered closings, owner succession data, lease assignability, and separation of operating cash flow from real-estate value.

## Demand durability
FHWA expects light-duty VMT to grow slowly over its long-run forecast, providing a modest directional tailwind to the vehicle-use base. Professional washing still competes with home washing, local oversupply, and customer cutbacks, so travel growth is not treated as direct wash-volume growth. The physical service basket remains relevant even when booking, membership, and payment become digital.

## Risks and uncertainty
The code's format mix is the central uncertainty: a hand-detail operation, a self-service asset, and a membership-heavy express tunnel have different labor, customer, and transfer economics. Other risks include local new-site supply, water and equipment reliability, vehicle-damage claims, weather, lease or real-estate dependence, and thin evidence on LMM owner age and qualifying transfers. The compensation-to-receipts input also uses 2024 wages against 2022 receipts and should not be interpreted as a same-vintage site margin.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.4348 | — | OBSERVED | — |
| n | — | 186 | — | ESTIMATE | — |
| a | 0.1 | 0.18 | 0.3 | PROXY | S1, S2 |
| rho | 0.25 | 0.4 | 0.55 | ESTIMATE | S1, S2, S4 |
| e | 0.82 | 0.92 | 0.97 | ESTIMATE | S1 |
| s5 | 0.08 | 0.14 | 0.22 | PROXY | S5, S7 |
| q | 0.4 | 0.55 | 0.68 | ESTIMATE | S3, S4 |
| d5 | 0.95 | 1.02 | 1.07 | PROXY | S6 |
| o | 0.8 | 0.9 | 0.96 | ESTIMATE | S1 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.43 | 1.25 | 2.87 | ESTIMATE |
| F | 4.15 | 5.18 | 5.96 | ESTIMATE |
| C | 8.00 | 10.00 | 10.00 | ESTIMATE |
| D | 7.60 | 9.18 | 10.00 | ESTIMATE |

## Caveats
- a: No public source located measures AI-exposed task share or occupation wages specifically for the frozen LMM lens.
- a: The industry contains both labor-intensive detailing and low-attendance self-service formats.
- rho: This is a bounded judgment, not a measured AI adoption rate.
- rho: Existing automatic and self-service formats may already have captured some non-AI labor reduction.
- e: No source gives the eligibility share inside the injected LMM firm count.
- e: A car wash located at a fuel retailer may be classified elsewhere when it is not the establishment's primary activity.
- s5: S5 is not car-wash-specific in its headline transaction sample and its reported typical financials are below the frozen EBITDA band.
- s5: S7 is a large platform transaction, so it is evidence of deal flow rather than a denominator-based small-firm transfer rate.
- q: Member renewal intent is survey evidence, not realized retention or a direct measure of savings capture.
- q: Value capture differs sharply by local density, real-estate constraints, wash quality, and mix of membership versus retail revenue.
- d5: VMT is national and does not capture the local micro-markets where car washes compete.
- d5: The forecast is a travel measure rather than a direct forecast of washes, revenue, or price-adjusted car-wash demand.
- o: No public source measures the share of future car-wash quantity requiring a separately accountable operator.
- o: Operator-required does not mean a staffed attendant must be present for every wash.

## Sources
- **S1** — [Census NAPCS Product List for NAICS 8111](https://www2.census.gov/library/reference/napcs/product-list/web-8111-final-reformatted-edited-us082208.pdf) (accessed 2026-07-22): Defines washing and cleaning as services that may use automatic machines, manual labor, self-service facilities, or a combination; identifies automatic washing, hand washing, self-service washing, and self-service vacuuming as products produced by NAICS 811192.
- **S2** — [O*NET: Cleaners of Vehicles and Equipment](https://www.onetonline.org/link/summary/53-7061.00) (accessed 2026-07-22): Lists vehicle-cleaner tasks including drying, spraying or scrubbing vehicles, inspection, mixing solutions, inventory, monitoring cleaning machines, and activating equipment; also reports physical work activities and work context.
- **S3** — [International Carwash Association CAR WASH Pulse Q1 2026](https://www.carwash.org/car-wash-news/car-wash-pulse-q1-2026-demand-remains-stable-as-price-sensitivity-and-market-saturation-shape-industry-outlook) (accessed 2026-07-22): Reports that nearly eight in ten customers would accept a price increase subject to value and quality, nearly 90 percent of members plan to renew, and saturation and competitive density are leading concerns.
- **S4** — [Rinsed Releases Its Q4 2024 Car Wash Industry Report](https://www.carwash.org/car-wash-news/rinsed-releases-its-q4-2024-car-wash-industry-report) (accessed 2026-07-22): Reports 5.2 percent year-over-year combined same-location member and retail revenue growth, 13.2 percent member-revenue growth, 7.1 percent retail-revenue decline, and average monthly member revenue of 30 dollars.
- **S5** — [BizBuySell Auto Repair and Service Valuation Benchmarks](https://www.bizbuysell.com/learning-center/valuation-benchmarks/auto-repair-and-service/) (accessed 2026-07-22): Reports 1,286 sold listings in a broader auto-service category, 207 median days on market, and completed-sale benchmarks; the page states its transaction data are based on businesses sold and reported to BizBuySell.
- **S6** — [FHWA 2025 Forecasts of Vehicle Miles Traveled](https://www.fhwa.dot.gov/policyinformation/tables/vmt/vmt_forecast_sum.cfm) (accessed 2026-07-22): Projects national light-duty vehicle miles traveled to grow at an average annual rate of 0.5 percent through 2053, with 0.6 percent annual growth from 2023 through 2043.
- **S7** — [Whistle Express agreement to acquire Take 5 Car Wash](https://www.carwash.org/car-wash-news/whistle-express-signs-definitive-agreement-to-acquire-take-5-car-wash) (accessed 2026-07-22): Reports the February 2025 agreement and states that the combined entity would operate 530 locations across 23 states.
