# 325612 — Polish and Other Sanitation Good Manufacturing

*v5.1 Stage 1 research memo. Run `325612-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** LOW_PRIORITY · A 6.23 · L 1.71 · interval STRUCTURAL_OUT → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Recurring physical replenishment plus document-heavy formulation, quality, scheduling, and compliance workflows creates a credible, implementable AI opportunity.
**Weakness:** The target population and benefit-retention rate are weakly measured, and commoditized private-label programs expose savings to customer repricing and competitive rebids.

## Business-model lens
- Included: US lower-middle-market contract, toll, and private-label manufacturers of sanitation and specialty cleaning goods, including disinfectants, sanitizers, polishes, waxes, and institutional or industrial cleaners, that repeatedly formulate, blend, fill, package, document, or fulfill products for external brands and customers.
- Excluded: Proprietary branded-product manufacturers without meaningful outsourced manufacturing revenue; captive plants; distributors; janitorial or application contractors; soap and detergent manufacturing classified in NAICS 325611; personal-care or cosmetic production outside this code; and firms outside the lower-middle-market control-acquisition band.
- Customer and revenue model: Customers are brands, retailers, distributors, and institutional or industrial product marketers. Revenue recurs through production runs and replenishment orders and is commonly quoted per batch, unit, or packaged program, with formulation, testing, regulatory support, warehousing, and fulfillment bundled or separately charged.
- Deviation from default lens: The code mixes outsourced manufacturing with proprietary branded production, so the lens is narrowed to contract, toll, and private-label operators whose repeat external-customer revenue makes the service construct coherent. The narrowing is based on business-model comparability, not attractiveness.

## Executive view
The coherent opportunity is the outsourced layer of a heterogeneous product-manufacturing code: recurring physical production supported by formulation, quality, regulatory, and fulfillment services. AI can improve a meaningful minority of labor and working-capital workflows, but the physical process and regulated release responsibilities limit automation depth, while procurement pressure limits benefit retention.

## How AI changes the work
Near-term use cases are demand and inventory forecasting, scheduling, quote preparation, formula and specification retrieval, batch-record review, quality anomaly detection, maintenance triage, and customer-service automation. Human accountability remains important for formula changes, claims, sampling, release, safety, and EPA-regulated records.

## Value capture
Value is most defensible when AI lowers scrap and expedites changeovers, improves on-time delivery, or makes small and complex customer programs economical. Savings that look like simple labor or input reductions are more likely to be competed away through rebids, renewal pricing, or explicit pass-through.

## Firm availability
Named contract manufacturers and recent control acquisitions show that eligible assets and buyers exist, but the full code materially overstates the target pool. A proprietary census is needed to separate qualifying outsourced manufacturers from branded, captive, diversified, and adjacent-category operators.

## Demand durability
Sanitation and cleaning products remain physical replenishment goods, and health, institutional hygiene, and industrial-cleaning needs support durable demand. Growth is likely modest rather than exceptional, with downside from commodity weakness, destocking, formulation substitution, concentration, and customer insourcing.

## Risks and uncertainty
The largest uncertainties are the eligible-firm denominator, actual ownership-transfer frequency, contract-level sharing of productivity gains, and plant-specific data readiness. Regulatory claims, hazardous-material handling, product liability, environmental diligence, customer concentration, retailer bargaining power, raw-material volatility, and formula confidentiality can each impair implementation or economics.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.3117 | — | OBSERVED | — |
| n | — | 125 | — | ESTIMATE | — |
| a | 0.17 | 0.28 | 0.4 | PROXY | S1, S2, S3, S4 |
| rho | 0.32 | 0.49 | 0.66 | PROXY | S1, S2, S3, S9, S10 |
| e | 0.22 | 0.39 | 0.57 | ESTIMATE | — |
| s5 | 0.2 | 0.34 | 0.48 | PROXY | S5, S6 |
| q | 0.26 | 0.43 | 0.61 | PROXY | S2, S3, S4, S7 |
| d5 | 0.96 | 1.08 | 1.22 | PROXY | S7, S8 |
| o | 0.91 | 0.97 | 0.99 | ESTIMATE | — |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.68 | 1.71 | 3.29 | PROXY |
| F | 3.01 | 4.61 | 5.73 | ESTIMATE |
| C | 5.20 | 8.60 | 10.00 | PROXY |
| D | 8.74 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: No source reports a wage-weighted AI-exposed task share for this six-digit industry or the narrowed contract-manufacturing lens.
- a: The provided compensation-to-receipts ratio of 0.3117 covers the broader NAICS population and may not match the labor intensity of private-label and toll manufacturers.
- rho: Evidence identifies feasible applications and constraints, not realized adoption rates for the target population.
- rho: Implementation will vary sharply between simple nonregulated polishes and EPA-registered public-health products.
- e: No denominator study measures the contract-manufacturing share of LMM firms in NAICS 325612.
- e: The provided firm count of 125 is estimated from size distributions for the full code; multi-establishment parents and diversified chemical firms can distort the eligible denominator.
- s5: Published transactions are selected examples rather than a measured hazard rate.
- s5: Ultra-Pak also serves personal-care markets and Formula Corp spans categories adjacent to this NAICS code.
- q: No source directly measures five-year retention of AI-enabled gross benefit in the narrowed lens.
- q: Contract structures differ substantially between commodity filling, proprietary formulations, and regulated antimicrobial programs.
- d5: The sources do not isolate outsourced production or hold product quality constant.
- d5: Cleaning-product demand can shift among concentrated, refill, reusable, and conventional formats even when underlying sanitation activity is stable.
- o: This is bounded judgment rather than an observed displacement rate.
- o: The estimate concerns the need for an accountable manufacturing operator, not whether the current supplier or current headcount remains unchanged.

## Sources
- **S1** — [Artificial Intelligence in Manufacturing: Real World Success Stories and Lessons Learned](https://www.nist.gov/blogs/manufacturing-innovation-blog/artificial-intelligence-manufacturing-real-world-success-stories) (accessed 2026-07-22): Small and medium manufacturer AI use cases in predictive maintenance, predictive quality, scrap and yield improvement, forecasting, and process optimization, together with implementation lessons.
- **S2** — [Formula Corp - Private Label & Contract Manufacturing Partner](https://formulacorp.com/) (accessed 2026-07-22): Existence and workflow scope of a US private-label and contract manufacturer offering formulation, scalable production, automated filling and packaging, quality, regulatory, and compliance services.
- **S3** — [Toll Manufacturing of EPA Disinfectants](https://seacole.com/get-epa-disinfectants-quote/) (accessed 2026-07-22): EPA-registered toll and contract manufacturing, quality and compliance, flexible batch sizes, blending, packaging, and physical plant capabilities for disinfectants.
- **S4** — [Contract Manufacturing | B&B Blending](https://www.bbblending.com/contractmanufacturing) (accessed 2026-07-22): Contract chemical tolling for private and government customers, including confidential proprietary blending, packaging, and delivery.
- **S5** — [San Francisco Equity Partners Acquires Formula Corp, a Leading Developer and Manufacturer of Cleaning Products for Consumer and Professional Use](https://markets.financialcontent.com/stocks/article/bizwire-2025-2-20-san-francisco-equity-partners-acquires-formula-corp-a-leading-developer-and-manufacturer-of-cleaning-products-for-consumer-and-professional-use) (accessed 2026-07-22): A 2025 majority acquisition of a custom cleaning-products manufacturer providing turnkey formulation, blending, filling, labeling, packaging, regulatory, and fulfillment services.
- **S6** — [Makai Capital-Backed Paladin Holdings Acquires Ultra-Pak, Inc.](https://www.prnewswire.com/news-releases/makai-capital-backed-paladin-holdings-acquires-ultra-pak-inc-302220107.html) (accessed 2026-07-22): A 2024 lower-middle-market-backed control acquisition of a regional contract manufacturer and packager serving cleaning-product and janitorial-sanitation markets.
- **S7** — [Stepan Company 2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/94049/000119312526074976/scl-20251231.htm) (accessed 2026-07-22): Raw-material cost pass-through through selling prices and mixed recent demand, including lower commodity laundry and cleaning volume partly offset by industrial-cleaning demand.
- **S8** — [ACI Survey: 3/4 Americans Are Changing Their Cleaning Habits to Improve Their Health](https://www.cleaninginstitute.org/newsroom/2025/aci-survey-34-americans-are-changing-their-cleaning-habits-improve-their-health) (accessed 2026-07-22): US survey evidence that cleaning and hygiene remain closely associated with public health and continue to shape reported cleaning behavior.
- **S9** — [Selected EPA-Registered Disinfectants](https://www.epa.gov/pesticide-registration/selected-epa-registered-disinfectants) (accessed 2026-07-22): EPA regulation and registration of disinfectants, approval of label language, and product registration identification, including products sold under multiple company names.
- **S10** — [Pesticide Registration Manual: Chapter 4 - Additional Considerations for Antimicrobial Products](https://www.epa.gov/pesticide-registration/pesticide-registration-manual-chapter-4-additional-considerations) (accessed 2026-07-22): Efficacy-data requirements and regulated public-health antimicrobial claims, including disinfectant, virucide, sanitizer, sterilant, and tuberculocide claims.
