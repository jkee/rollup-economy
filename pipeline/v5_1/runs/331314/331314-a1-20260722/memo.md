# 331314 — Secondary Smelting and Alloying of Aluminum

*v5.1 Stage 1 research memo. Run `331314-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 4.72 · L 0.25 · interval STRUCTURAL_OUT → STRUCTURAL_OUT · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Durable demand for low-energy recycled aluminum combined with measurable yield, uptime, and quality gains in qualified local processing relationships.
**Weakness:** A very small, heterogeneous acquisition pool with heavy physical capital and uncertain toll-processing incidence limits scalable deployment of the thesis.

## Business-model lens
- Included: Independent lower-middle-market operators that repeatedly melt, refine, blend, and alloy customer-owned aluminum scrap, dross, or purchased secondary feedstock into specified billet, ingot, sow, or molten-metal products, including toll processors and regional secondary smelters.
- Excluded: Primary aluminum production; scrap brokers and sorters that do not melt; captive recycling units inside large integrated producers or automotive plants; commodity traders; and businesses whose economics are principally metal-price speculation rather than processing service.
- Customer and revenue model: Customers are automotive, casting, rolling, extrusion, packaging, and other aluminum users. Revenue is earned through per-pound or per-ton toll conversion charges when the customer retains metal ownership, or through the spread between purchased scrap and sold specification alloy in buy/sell operations; energy and metal-price adjustments are often passed through contractually.
- Deviation from default lens: none

## Executive view
This is a small, asset-heavy opportunity set in which the attractive recurring-service model is toll conversion of customer-owned aluminum. AI can improve sorting, recipes, quality, uptime, and administration, but most plant labor and capital remain physical. The investment case depends less on headline automation and more on buying a locally advantaged, permitted plant with stable toll contracts and using digital tools to raise yield and reliability.

## How AI changes the work
The strongest near-term uses are sensor-based scrap classification, blend and chemistry recommendations, furnace-energy optimization, predictive maintenance, visual inspection, production scheduling, document generation, and exception handling. Human operators remain necessary for material handling, furnace operations, maintenance, laboratory verification, and safety-critical decisions.

## Value capture
Toll processors avoid much direct metal-price risk and may pass through energy, but sophisticated customers negotiate transparent conversion fees. Benefits from lower energy use may be shared quickly, while added throughput, reduced alloy loss, fewer rejects, and higher on-time delivery can be retained longer if capacity is constrained or the plant is operationally embedded with customers.

## Firm availability
The modeled LMM universe is only 23 firms, and the subset with meaningful recurring toll revenue is likely smaller. Succession may surface assets, but environmental history, furnace condition, permits, working capital, customer concentration, and metal-price exposure will remove many candidates from a financeable acquisition set.

## Demand durability
Aluminum recycling has strong structural support from its energy advantage, high current recycled contribution, and growing aluminum use in vehicles and packaging. Merchant demand is less certain than metal demand because customers can build captive recycling and new entrants can add capacity; underwriting should emphasize contracted local flows rather than industry tonnage alone.

## Risks and uncertainty
The largest uncertainties are the current share of independent firms operating a genuine toll model, the transferability of large-company contract economics to LMM plants, environmental liabilities, customer concentration, volatile scrap spreads in buy/sell operations, energy and labor availability, and the lack of representative AI deployment data.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.0591 | — | OBSERVED | — |
| n | — | 23 | — | ESTIMATE | — |
| a | 0.16 | 0.26 | 0.37 | PROXY | S1, S2, S3, S4 |
| rho | 0.22 | 0.4 | 0.58 | ESTIMATE | S2, S3, S5 |
| e | 0.12 | 0.28 | 0.48 | PROXY | S5, S6 |
| s5 | 0.08 | 0.14 | 0.22 | PROXY | S7 |
| q | 0.22 | 0.38 | 0.54 | PROXY | S5, S6, S8 |
| d5 | 0.98 | 1.12 | 1.28 | PROXY | S8, S9, S10 |
| o | 0.94 | 0.98 | 1 | ESTIMATE | S1, S2, S6, S8 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.08 | 0.25 | 0.51 | ESTIMATE |
| F | 0.32 | 1.03 | 1.98 | ESTIMATE |
| C | 4.40 | 7.60 | 10.00 | PROXY |
| D | 9.21 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: O*NET is occupational rather than establishment-level evidence.
- a: Vendor evidence demonstrates technical feasibility, not representative adoption or labor savings.
- a: The product mix from toll ingot to molten-metal delivery materially changes task composition.
- rho: No representative adoption study was found for NAICS 331314.
- rho: Implementation feasibility differs sharply between sorting and closed-loop furnace control.
- rho: Safety and metallurgical qualification requirements slow realization.
- e: The principal mix statistic is old and drawn from one large operator.
- e: Revenue mix is not identical to the share of firms meeting the lens.
- e: Some buy/sell contracts have service-like customer relationships despite metal ownership.
- s5: Cross-industry owner intentions are not observed metal-industry transactions.
- s5: A stated succession intention may not result in a marketed or financeable company.
- s5: The small population makes realized availability lumpy.
- q: Customer-retention and contract descriptions come primarily from one operator.
- q: Capture differs between tolling and buy/sell models.
- q: Competitive capacity additions could pass productivity gains to customers faster.
- d5: End-market aluminum growth does not translate one-for-one into merchant secondary-smelting volume.
- d5: New recycling capacity may increase total demand while reducing incumbent utilization.
- d5: Automotive and industrial cycles can overwhelm structural growth over five years.
- o: The range addresses AI-related obsolescence, not ordinary competitive displacement.
- o: Large customers may vertically integrate even if the physical process remains necessary.
- o: Environmental regulation can close assets without making the service technologically obsolete.

## Sources
- **S1** — [NAICS 331314 - Secondary Smelting and Alloying of Aluminum](https://www.naics.com/naics-code-description/?code=331314&v=2022) (accessed 2026-07-22): Industry boundary: recovery of aluminum from scrap or dross and production of alloys, powders, pastes, and flakes from purchased aluminum.
- **S2** — [Metal-Refining Furnace Operators and Tenders](https://www.onetonline.org/link/summary/51-4051.00) (accessed 2026-07-22): Core furnace-operator tasks and work context, including physical operation, impurity removal, frequent decisions, time pressure, and close contact.
- **S3** — [Achieving High-Purity Aluminium Circularity Through Precision AI Sorting](https://www.tomra.com/waste-metal-recycling/media-center/news/2026/achieving-high-purity-aluminium-circularity-through-precision-ai-sorting) (accessed 2026-07-22): Commercial technical evidence for AI-enabled sensor sorting of aluminum alloys and contaminants using XRT, LIBS, and deep-learning visual classification.
- **S4** — [Only 3.8% of Businesses Use AI to Produce Goods and Services](https://www.census.gov/library/stories/2023/11/businesses-use-ai.html) (accessed 2026-07-22): Broad business baseline showing low realized AI use and modest planned near-term adoption, used only as context for implementation uncertainty.
- **S5** — [Real Industry, Inc. 2016 Investor Presentation](https://www.sec.gov/Archives/edgar/data/38984/000156459016028788/rely-ex992_33.htm) (accessed 2026-07-22): Company proxy for approximately 53% tolling and 47% buy/sell mix, toll charges, pass-through costs, and metal-spread economics.
- **S6** — [Real Alloy Business and Tolling Model Description](https://www.sec.gov/Archives/edgar/data/38984/000156459016014765/rely-ex992_6.htm) (accessed 2026-07-22): Customer-owned-metal toll process, energy pass-through, contracted per-pound or per-ton revenue, proximity, just-in-time delivery, and reported customer retention.
- **S7** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Cross-industry evidence on aging U.S. business owners and five-year intentions to sell, transfer, close, or continue operating.
- **S8** — [Constellium 2025 Annual Report](https://www.sec.gov/Archives/edgar/data/1563411/000156341126000147/a2025ars.htm) (accessed 2026-07-22): Downstream aluminum-demand forecasts, margin-over-metal and pass-through contract practices, scrap-spread exposure, and energy-cost importance.
- **S9** — [Recycling](https://www.aluminum.org/Recycling) (accessed 2026-07-22): Industry-association evidence that recycled aluminum uses about 5% of the energy of primary metal, exceeds 80% of U.S. production, and has high industrial recycling rates.
- **S10** — [Automotive Aluminum](https://www.aluminum.org/automotive) (accessed 2026-07-22): Automotive aluminum recycling above 95% and expected North American vehicle content growth to 556 pounds per vehicle by 2030.
