# 321992 — Prefabricated Wood Building Manufacturing

*v5.1 Stage 1 research memo. Run `321992-a1-20260723`, model `claude-sonnet-5`, 2026-07-23, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 5.94 · L 0.54 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Digitizable design-to-production coordination layered onto a durable need for faster, more consistent off-site construction.
**Weakness:** Most value creation still depends on physical plant execution, while only a minority of firms clearly fit the recurring-service lens.

## Business-model lens
- Included: US lower-middle-market makers of prefabricated wood buildings and building components whose builder, dealer, developer, institutional, or commercial customers repeatedly outsource fabrication.
- Excluded: One-off consumer shed or cabin sales, general contractors, on-site installers, captive component plants, retailers, shells, and firms outside the EBITDA band.
- Customer and revenue model: Products are normally priced per building, kit, model, or project; the qualifying subset earns repeat revenue from customers that regularly outsource off-site fabrication.
- Deviation from default lens: Because the code primarily manufactures products, the lens is narrowed to ongoing B2B outsourced-fabrication relationships; transactional one-off sellers are excluded for coherence.

## Executive view
AI can improve the information-rich front and middle of prefabricated wood-building production, but physical factory work limits direct labor substitution. Opportunity under the frozen lens depends on identifying genuine repeat B2B fabricators rather than one-off product sellers.

## How AI changes the work
Useful applications include design-rule assistance, takeoffs, estimating, bills of materials, purchasing, production sequencing, work-instruction generation, quality-document review, and customer support. Cutting, framing, assembly, finishing, and handling still need people and equipment.

## Value capture
Custom engineering, reliable lead times, and program relationships can protect a portion of efficiency gains. Standardized sellers face re-bids and price comparison, while concentrated builders and dealers can force savings through at renewal.

## Firm availability
General succession surveys and manufacturing transaction data imply some control-transfer flow, but industry-specific evidence is absent. Transferability is strongest where repeat customers, trained management, equipment, permits, and real estate are separable from the founder.

## Demand durability
Housing and construction needs support off-site fabrication, and persistent trade shortages can favor factory production. Interest rates, construction cycles, lumber volatility, permitting, and product mix make the five-year quantity outlook unusually wide.

## Risks and uncertainty
Eligibility is the largest measurement risk: repeat sales are not necessarily a recurring outsourced service. Other risks include customer concentration, cyclicality, design liability, working capital, plant utilization, and AI integration errors reaching physical production.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1456 | — | OBSERVED | — |
| n | — | 160 | — | ESTIMATE | — |
| a | 0.09 | 0.17 | 0.28 | PROXY | S1, S2 |
| rho | 0.35 | 0.55 | 0.75 | ESTIMATE | S1 |
| e | 0.08 | 0.2 | 0.38 | ESTIMATE | S3 |
| s5 | 0.11 | 0.2 | 0.32 | PROXY | S4, S5 |
| q | 0.32 | 0.52 | 0.72 | ESTIMATE | S1, S3 |
| d5 | 0.82 | 1.07 | 1.32 | ESTIMATE | S1, S3, S6 |
| o | 0.86 | 0.95 | 0.99 | ESTIMATE | S1, S2 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.18 | 0.54 | 1.22 | ESTIMATE |
| F | 1.41 | 3.22 | 4.86 | ESTIMATE |
| C | 6.40 | 10.00 | 10.00 | ESTIMATE |
| D | 7.05 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: The sources characterize the broader wood-manufacturing and production workforce rather than measuring AI task exposure in this six-digit industry.
- a: The frozen labor ratio combines 2024 wages with 2022 receipts and applies a cross-code harmonization divisor.
- rho: No representative five-year implementation study was found for NAICS 321992.
- rho: Benefits requiring major robotics investment are outside the exposed software-task pool unless AI is the enabling layer.
- e: The 160-firm dataset input is a margin-bridged estimate rather than an observed qualifying-firm census.
- e: Repeat product purchases may still be transactional and therefore ineligible.
- s5: Neither source isolates prefabricated wood buildings or the $1-10M EBITDA band.
- s5: Internal family succession and closures must be separated from qualifying control transfers.
- q: No public pricing-contract sample for qualifying private firms was found.
- q: Retention varies sharply between engineered custom buildings and standardized commodity structures.
- d5: Broad construction and manufactured-housing sources do not isolate prefabricated wood buildings.
- d5: The Census Manufactured Housing Survey explicitly excludes modular homes, so it is useful for boundary definition but not a direct volume series for this code.
- o: Operator persistence is a judgment based on the physical production process, not a directly observed five-year share.
- o: The range does not assume that today's independent supplier ownership structure is permanent.

## Sources
- **S1** — [Wood Product Manufacturing: NAICS 321](https://www.bls.gov/IAG/TGS/iag321.htm) (accessed 2026-07-23): Describes wood-product manufacturing processes including sawing, planing, shaping, laminating, and assembly and provides broad workforce context for the physical-task proxy.
- **S2** — [Production Occupations](https://www.bls.gov/ooh/production/) (accessed 2026-07-23): Describes production workers as operating machinery and equipment to assemble goods, supporting the embodied-work bridge used for AI exposure and operator persistence.
- **S3** — [2022 NAICS Search: 321992 Prefabricated Wood Building Manufacturing](https://www.census.gov/naics/?input=321992&year=2022&details=321992) (accessed 2026-07-23): Defines the industry boundary around establishments primarily manufacturing prefabricated wood buildings and sections and supports the lens distinction between products and outsourced fabrication relationships.
- **S4** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-23): Reports a fall-2024 survey of employer-business owners' plans for selling, transferring, keeping, or closing their firms within five years.
- **S5** — [BizBuySell Insight Report Data Tables](https://www.bizbuysell.com/insight-report-data-tables/) (accessed 2026-07-23): Provides 2025 reported-sale counts and transaction metrics for small manufacturing businesses, a broad realized-transfer proxy.
- **S6** — [Manufactured Housing Survey Frequently Asked Questions](https://www.census.gov/programs-surveys/mhs/about/faq.html) (accessed 2026-07-23): States that the Manufactured Housing Survey does not include modular homes, clarifying that manufactured-home shipment data cannot directly measure this industry's modular-building demand.
