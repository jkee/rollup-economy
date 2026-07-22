# 424910 — Farm Supplies Merchant Wholesalers

*v5.1 Stage 1 research memo. Run `424910-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 6.11 · L 0.26 · interval STRUCTURAL_OUT → STRUCTURAL_OUT · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Essential replenishment demand and repetitive inventory, order and purchasing workflows make targeted automation feasible across a broad operating-firm base.
**Weakness:** Low labor intensity and growing direct-to-farm price transparency limit the size and durability of retained AI-driven economics.

## Business-model lens
- Included: U.S. lower-middle-market merchant wholesalers repeatedly supplying farms, ranches, agricultural retailers, or other wholesalers with animal feed, seed, fertilizer, agricultural chemicals, hay, straw, bulbs, and related consumable farm supplies, together with procurement, inventory, delivery, credit, compliance, and product-support workflows.
- Excluded: Farm machinery and equipment dealers, grain elevators and raw-farm-product assemblers, pet-supply wholesalers, pure commission brokers or electronic marketplaces without merchant-wholesale operations, captive manufacturer branches, shells, and non-control financing vehicles.
- Customer and revenue model: Recurring and seasonal B2B resale of consumable agricultural inputs, usually earning a product spread and sometimes service, delivery, financing, application, or agronomy-related revenue; demand is tied to planted acreage, livestock production, input intensity, weather, and farm economics.
- Deviation from default lens: none

## Executive view
Farm-supply wholesaling has recurring essential demand and practical automation targets in inventory, purchasing, ordering, sales preparation and accounting, but its compensation intensity is low and much work is physical, seasonal or advisory. Stable acreage supports demand, while direct-to-farm commerce, price transparency and consolidation constrain operator durability and captured savings.

## How AI changes the work
AI and workflow software can improve replenishment, demand planning, quotations, customer support, purchase orders, pick-pack control, invoicing and product-record compliance. Bulk handling, delivery, hazardous-product custody, field exceptions and accountable agronomic judgment remain labor- and operator-intensive.

## Value capture
Savings can initially stay inside a product spread, but farmers compare inputs aggressively and increasingly see online price benchmarks. Commodity product comparability, manufacturer programs and seasonal bidding should pass a meaningful share of benefit to customers or suppliers over five years.

## Firm availability
Most true merchant wholesalers serve external customers repeatedly, although the code includes cooperative, manufacturer-affiliated, importer, mixed-channel and thin-market models. A completed CHS cooperative acquisition demonstrates control transfer, but governance, local relationships and strategic buyer structure complicate availability.

## Demand durability
Seed, feed, fertilizer and crop protection remain necessary inputs, and USDA projects only modest erosion in major-crop acreage. The local independent channel is less durable than end demand because manufacturers, cooperatives and online platforms can consolidate or bypass local distribution.

## Risks and uncertainty
The occupational proxy is broad, product categories have sharply different margins and service needs, and no representative AI adoption, transfer-rate or benefit-retention study was found. Weather, planted mix, livestock cycles, farm solvency, regulation, precision application, working capital and direct-channel adoption can materially alter results.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.0513 | — | OBSERVED | — |
| n | — | 1223 | — | ESTIMATE | — |
| a | 0.12 | 0.24 | 0.37 | PROXY | S2, S3 |
| rho | 0.32 | 0.52 | 0.68 | ESTIMATE | S3 |
| e | 0.58 | 0.75 | 0.88 | ESTIMATE | S1 |
| s5 | 0.09 | 0.18 | 0.29 | ESTIMATE | S4 |
| q | 0.22 | 0.42 | 0.62 | ESTIMATE | S6 |
| d5 | 0.86 | 0.97 | 1.07 | PROXY | S5 |
| o | 0.62 | 0.78 | 0.9 | PROXY | S6, S7 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.08 | 0.26 | 0.52 | ESTIMATE |
| F | 6.71 | 8.22 | 9.24 | ESTIMATE |
| C | 4.40 | 8.40 | 10.00 | ESTIMATE |
| D | 5.33 | 7.57 | 9.63 | PROXY |

## Caveats
- a: The BLS occupation population is broader than farm supplies.
- a: The software page demonstrates automation scope and customer anecdotes, not representative causal labor savings.
- a: Exposure is lower for bulk handling, driving, application support and trusted agronomic advice.
- rho: No representative farm-supply-wholesaler implementation-rate study was found.
- rho: Small rural firms may adopt more slowly than software reference customers.
- rho: Regulated product decisions require human review even when records and recommendations are automated.
- e: The Census instrument lists operation types but does not report their shares within the six-digit industry.
- e: Cooperatives can provide highly transferable operations yet require a different governance path from ordinary company acquisitions.
- e: The frozen LMM count is a margin-bridged estimate.
- s5: A single disclosed cooperative acquisition confirms feasibility but not a population transfer rate.
- s5: Public deal evidence overrepresents larger cooperative and strategic transactions.
- s5: Some cooperative combinations may have governance characteristics unlike a conventional control acquisition.
- q: FBN demonstrates price transparency and online comparison but does not measure pass-through from AI savings.
- q: Retention differs greatly between commodity fertilizer or feed and differentiated seed, chemicals or technical service.
- q: Volatile product costs can obscure operating-efficiency retention in accounting data.
- d5: Planted acreage is not an input-volume forecast and excludes livestock, horticulture and smaller crops.
- d5: Nominal production expenses are not used as a direct constant-price quantity measure.
- d5: Weather and commodity-price cycles can produce large annual departures from the baseline.
- o: Restricted-use pesticide requirements do not apply to feed, seed, fertilizer and all chemicals.
- o: A national marketplace remains an operator and logistics provider even when it eliminates a local intermediary.
- o: The relevant loss is quantity no longer requiring an operator of the lens's kind, not labor automation within a surviving operator.

## Sources
- **S1** — [2022 Economic Census Wholesale Trade Survey: NAICS 424910](https://bhs.econ.census.gov/ombpdfs2022/export/2022_WH-42491_su.pdf) (accessed 2026-07-22): The Census instrument identifies farm supplies sold to farmers or resellers, including feed, seeds, fertilizers and agricultural chemicals, and distinguishes merchant wholesalers from manufacturer branches, agents, brokers and electronic markets, supporting lens boundaries and eligibility caveats.
- **S2** — [Merchant Wholesalers, Nondurable Goods: NAICS 424](https://www.bls.gov/iag/tgs/iag424.htm) (accessed 2026-07-22): BLS reports common broad-wholesaler occupations including sales representatives, heavy truck drivers, freight movers and shipping and traffic clerks, anchoring the occupation-mix proxy for AI exposure.
- **S3** — [Inventory app for farm machinery and supply distributors](https://www.handifox.com/farm-machinery-and-supply) (accessed 2026-07-22): The fetched page documents farm-supply inventory tracking, barcode scanning, automated reorder triggers and purchase orders, order processing, pick-pack, mobile workflows and accounting integration; a customer quote reports order-processing and sales-integration time improving by 2x.
- **S4** — [CHS acquires West Central Ag Services to expand reach](https://www.chsinc.com/news-and-stories/2025/01/02/chs-and-west-central-sale-closes) (accessed 2026-07-22): CHS states that it closed the acquisition of West Central Ag Services on January 2, 2025, kept locations operational, continued grain and agronomy services, and offered employment to all employees, supporting control-transfer feasibility.
- **S5** — [USDA Agricultural Projections to 2035](https://ers.usda.gov/sites/default/files/_laserfiche/outlooks/113817/OCE-2026-1.pdf?v=39134) (accessed 2026-07-22): USDA projects eight-major-crop planted acreage at 247.6 million acres in 2026/27, below 246 million from 2028 through 2035 and 241.6 million in 2035; it also projects total farm production expenses rising from $465.9 billion in 2026 to $500.7 billion in 2031.
- **S6** — [How do I get started shopping for inputs on FBN Direct?](https://www.fbn.com/en-ca/community/faq/how-do-i-get-started-shopping-for-inputs-on-fbn-direct) (accessed 2026-07-22): FBN describes online shopping for chemicals, seeds, animal health and feed with direct-to-farm delivery, product comparisons, invoice-based price transparency and online purchasing, supporting channel-bypass and pricing-pressure evidence.
- **S7** — [Inspections under the Federal Insecticide, Fungicide and Rodenticide Act](https://www.epa.gov/compliance/inspections-under-federal-insecticide-fungicide-and-rodenticide-act) (accessed 2026-07-22): EPA states that pesticide marketplace inspections cover correct channel distribution, storage and disposal, and that restricted-use pesticide dealer inspections enforce sales and distribution records and sales only to appropriately certified parties, supporting accountable-operator requirements for part of the basket.
