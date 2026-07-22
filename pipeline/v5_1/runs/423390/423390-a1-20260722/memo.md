# 423390 — Other Construction Material Merchant Wholesalers

*v5.1 Stage 1 research memo. Run `423390-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 6.68 · L 0.49 · interval STRUCTURAL_OUT → STRUCTURAL_OUT · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** AI-addressable quoting and branch administration embedded in recurring, specification-sensitive material fulfillment.
**Weakness:** The NAICS code's product heterogeneity makes eligibility, demand, and retention estimates unusually dependent on an unavailable segment mix.

## Business-model lens
- Included: Independent US lower-middle-market merchant wholesalers repeatedly stocking, quoting, selling, and delivering miscellaneous construction inputs such as flat and plate glass, nonwood fencing and accessories, ceiling and gypsum products, building paper, mastics, culvert pipe, storage bins, and architectural metalwork.
- Excluded: Manufactured-home and prefabricated-building wholesalers whose revenue is predominantly infrequent unit or project sales, manufacturers' captive branches, pure brokers without transferable operations, retailers, and firms outside the EBITDA band.
- Customer and revenue model: Repeat B2B resale to contractors, fabricators, installers, builders, dealers, and facilities customers, with product gross margin paying for local availability, technical selection, quoting, trade credit, and delivery.
- Deviation from default lens: The NAICS definition combines recurring stock-and-flow specialty materials with manufactured homes and prefabricated buildings, whose large-ticket, project-like sales cadence and fulfillment economics would make one screen incoherent. The lens retains repeat construction-input distributors and excludes firms dominated by those unit/project categories.

## Executive view
The retained lens is a collection of repeat specialty-material distributors, not a single uniform product market. Its digital sales and administrative work is meaningfully AI-addressable, while physical inventory, specification accountability, and delivery remain operator-intensive.

## How AI changes the work
AI can accelerate quote and submittal preparation, product matching, order capture, lead selection, credit work, purchasing, and inventory planning. Realization depends on product-master quality and human checks because an incorrect glass, fencing, gypsum, or architectural specification can be costly.

## Value capture
Product-price billing allows initial internal retention of labor savings. Retention varies by segment: technical, fragile, or locally stocked products support service differentiation, while commodity items face stronger bid comparison, online transparency, and supplier-direct pressure.

## Firm availability
Active building-products consolidation indicates buyer demand, but no public cohort measures qualifying 423390 transfers. Eligibility is materially reduced by the decision to exclude manufactured-home and prefab-building specialists and by ordinary concentration and transferability screens.

## Demand durability
The basket participates in repair, remodeling, new construction, and infrastructure, which diversifies but does not eliminate cyclicality. Aging buildings support replacement demand, and most products still need a physical, credit-bearing fulfillment operator even if ordering becomes digital.

## Risks and uncertainty
The six-digit code is unusually heterogeneous, public occupation and deal evidence is broad, and no revenue weights exist for the narrowed product categories. Construction cycles, tariffs, supplier bypass, specifications liability, fragmented data, and platform consolidation could each dominate AI labor savings.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.0871 | — | OBSERVED | — |
| n | — | 508 | — | ESTIMATE | — |
| a | 0.22 | 0.34 | 0.47 | PROXY | S2, S3 |
| rho | 0.25 | 0.41 | 0.6 | ESTIMATE | S3 |
| e | 0.45 | 0.62 | 0.78 | ESTIMATE | S1, S4 |
| s5 | 0.13 | 0.21 | 0.32 | PROXY | S5, S3 |
| q | 0.45 | 0.63 | 0.78 | PROXY | S4, S6 |
| d5 | 0.96 | 1.05 | 1.15 | PROXY | S7, S8 |
| o | 0.8 | 0.9 | 0.97 | ESTIMATE | S3, S6 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.19 | 0.49 | 0.98 | ESTIMATE |
| F | 5.51 | 6.77 | 7.80 | ESTIMATE |
| C | 9.00 | 10.00 | 10.00 | PROXY |
| D | 7.68 | 9.45 | 10.00 | ESTIMATE |

## Caveats
- a: The occupational proxy is broader than 423390 and from May 2022.
- a: The retained product categories themselves have different technical-sales intensity.
- a: The supplied labor ratio mixes 2024 wages with 2022 receipts and is harmonized to the IPS basis.
- rho: Public examples are scaled enterprises, not LMM firms.
- rho: Product-specification errors can create rework or safety liability.
- rho: Implementation difficulty, rather than customer price response, is isolated here.
- e: No public firm-count split isolates the narrowed retained categories from manufactured homes and prefab buildings.
- e: The provided LMM firm count is itself an EBITDA-margin-bridged estimate.
- e: Some custom glass and architectural-metal sellers may still have project-like economics.
- s5: Published deal counts span multiple distribution industries and geographies.
- s5: No 423390 owner-age or succession dataset was found.
- s5: Narrow specialty segments may have very different buyer depth.
- q: Gross margin is not benefit retention.
- q: The 36.2% figure covers excluded manufactured-home and prefab wholesalers as well as retained products.
- q: Direct supplier sales and online marketplaces may accelerate pass-through.
- d5: The demand proxies are much broader than the retained product basket.
- d5: Different 423390 categories can move in opposite directions.
- d5: Tariffs and commodity-price swings complicate conversion from spending to quantity.
- o: Channel displacement may change who operates the service without eliminating the operator role.
- o: Supplier-direct evidence spans distribution categories.
- o: Custom-fabrication interfaces may increase operator need while standardized prefab channels may reduce it.

## Sources
- **S1** — [2022 NAICS Definition: 423390 Other Construction Material Merchant Wholesalers](https://www.census.gov/naics/?chart=2022&details=423390&input=423390) (accessed 2026-07-22): Defines the code and lists its heterogeneous products, including flat glass, fencing, gypsum products, manufactured homes, and nonwood prefabricated buildings.
- **S2** — [May 2022 OEWS: Merchant Wholesalers, Durable Goods](https://www.bls.gov/oes/2022/may/naics3_423000.htm) (accessed 2026-07-22): Reports the broader durable-goods wholesaler occupation mix, including wholesale/manufacturing sales representatives at 16.08% of employment and detailed office occupations.
- **S3** — [Where value is won and lost in distribution](https://www.mckinsey.com/industries/industrials/our-insights/where-value-is-won-and-lost-in-distribution) (accessed 2026-07-22): Describes AI embedded in distributor pricing, procurement, inventory, and customer workflows; construction-material case examples; supplier-direct pressure; and large distribution transactions.
- **S4** — [2022 Economic Census Wholesale Trade Gross Margin Profile](https://data.census.gov/table/ECNGRMARGPROF2022.EC2242GRMARGPROF) (accessed 2026-07-22): Reports 3,760 merchant-wholesaler firms and a 36.2% gross margin for NAICS 423390 in 2022.
- **S5** — [Distribution M&A Activity Rebounds in Q1 as Strategic Buyers Accelerate Dealmaking](https://distributionstrategy.com/2026/05/distribution-ma-activity-rebounds-in-q1-as-strategic-buyers-accelerate-dealmaking/) (accessed 2026-07-22): Reports 87 wholesale-distribution transactions in 2026 Q1 versus 74 in 2025 Q4 and concentration of private-equity-backed activity in industrial and building products.
- **S6** — [The next normal in construction material distribution](https://www.mckinsey.com/capabilities/operations/our-insights/the-next-normal-in-construction-material-distribution) (accessed 2026-07-22): Describes distributors' inventory, logistics, and credit roles and the pressure from online marketplaces, supplier-direct sales, price transparency, and direct-to-site delivery.
- **S7** — [Monthly Construction Spending, May 2026](https://www.census.gov/construction/c30/current/index.html) (accessed 2026-07-22): Reports May 2026 total construction spending 1.5% below May 2025 and first-five-month spending 2.7% below the comparable 2025 period.
- **S8** — [2026 Housing Outlook: Ongoing Challenges, Cautious Optimism and Incremental Gains](https://www.nahb.org/news-and-economics/press-releases/2026/02/2026-housing-outlook-ongoing-challenges-cautious-optimism-and-incremental-gains) (accessed 2026-07-22): Reports home improvement at 45% of residential construction spending in 2025 Q3 and forecasts real remodeling growth of 3% in 2026 and 2% in 2027.
