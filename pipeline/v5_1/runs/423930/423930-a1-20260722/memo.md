# 423930 — Recyclable Material Merchant Wholesalers

*v5.1 Stage 1 research memo. Run `423930-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 6.80 · L 0.30 · interval STRUCTURAL_OUT → STRUCTURAL_OUT · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Physical processing and repeat material flows preserve operator relevance while AI and digitization can reduce commercial, grading, dispatch, and reconciliation work.
**Weakness:** Commodity transparency and operational liabilities can dissipate labor savings and make apparently similar yards differ radically in quality.

## Business-model lens
- Included: Lower-middle-market recyclable-material merchants with repeat industrial, commercial, municipal, or dealer counterparties that source, grade, process, aggregate, broker while taking title to, and sell ferrous metal, nonferrous metal, paper, plastics, electronics, automotive scrap, or other secondary materials.
- Excluded: Municipal collection-only operations, waste haulers and material-recovery facilities classified outside 423930, pure brokers that do not take title, captive industrial scrap units, shells, hazardous-waste specialists, and auto wreckers whose economics are principally retail used-parts sales rather than wholesale scrap flows.
- Customer and revenue model: Repeat purchases of scrap and sales of graded secondary commodities to mills, foundries, processors, exporters, and manufacturers; economics combine commodity spread, processing and upgrading yield, logistics, scale aggregation, and sometimes recurring container, pickup, destruction, or compliance services.
- Deviation from default lens: The highly heterogeneous code is narrowed to repeat-service merchants with recurring generator and consuming-mill relationships and accountable material-handling operations. Pure commodity brokers and used-parts-led dismantlers are excluded because they do not share a coherent recurring outsourced-service model.

## Executive view
Recyclable-material merchants have a durable physical role and a meaningful pool of repetitive commercial and administrative work, but their labor base is less software-exposed than that of office-heavy services. The coherent target is a compliant, repeat-account yard or processor with transferable generator and mill relationships, not a thin broker or opaque owner-operated scrap lot.

## How AI changes the work
AI can assist grading and contamination detection, digitize scale tickets, monitor commodity and freight markets, prepare quotes, optimize dispatch, reconcile settlements, and automate compliance records. Physical handling, machinery, maintenance, safety, and exception-heavy grading remain operator intensive, while robotic sortation requires capital and clean integration.

## Value capture
Transparent commodity prices make savings difficult to retain indefinitely: competition can return them to generators or consuming mills through narrower spreads. Retention improves where the merchant offers scarce processing, high recovery and purity, reliable pickup, compliance, or dense local logistics.

## Firm availability
The supplied count is large, but the verified target pool will shrink after filtering for recurring accounts, clean environmental history, transferable permits and relationships, credible inventory controls, and management depth. Succession and consolidation can create sales, though no public source directly measures qualifying control transfers.

## Demand durability
Scrap remains a necessary manufacturing input with energy and policy advantages, and current ferrous consumption is substantial. Five-year quantity can still swing with steel, construction, auto, packaging, export, and virgin-material cycles, and each material stream has its own economics.

## Risks and uncertainty
Environmental liabilities, theft and title controls, worker safety, commodity volatility, working capital, export exposure, feedstock contamination, and equipment reliability can dominate an otherwise attractive workflow thesis. The largest evidence gaps are target-level task mix, verified AI deployment economics, and control-transfer frequency.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.0683 | — | OBSERVED | — |
| n | — | 1987 | — | ESTIMATE | — |
| a | 0.15 | 0.24 | 0.34 | ESTIMATE | S2, S3, S4 |
| rho | 0.28 | 0.45 | 0.62 | ESTIMATE | S3, S4 |
| e | 0.38 | 0.55 | 0.69 | ESTIMATE | S1 |
| s5 | 0.16 | 0.26 | 0.37 | ESTIMATE | S8, S9 |
| q | 0.22 | 0.39 | 0.56 | ESTIMATE | S5, S6 |
| d5 | 0.88 | 1.09 | 1.3 | ESTIMATE | S5, S6, S7 |
| o | 0.87 | 0.95 | 0.99 | ESTIMATE | S1, S2, S5 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.11 | 0.30 | 0.58 | ESTIMATE |
| F | 7.73 | 9.09 | 10.00 | ESTIMATE |
| C | 4.40 | 7.80 | 10.00 | ESTIMATE |
| D | 7.66 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: BLS recycling occupations cover adjacent material-recovery and waste operations as well as merchant wholesalers.
- a: Capital automation of physical sorting is relevant context but is not counted as AI labor substitution unless it avoids current labor within the five-year implementation path.
- a: The frozen compensation ratio uses 2024 wages over 2022 receipts and is harmonized to an IPS basis.
- rho: DOE projects establish technical activity, not broad commercial adoption in LMM scrap merchants.
- rho: Implementation feasibility differs sharply between high-throughput processors and small mixed-material yards.
- e: The NAICS definition spans automotive, industrial, and other recyclable materials with materially different economics and liabilities.
- e: The frozen n of 1,987 is an ESTIMATE based on size-class receipts and a general distributor margin bridge, not verified LMM EBITDA.
- s5: Shutdowns and establishment exits are not qualifying transfers.
- s5: Environmental liabilities may convert an intended sale into an asset liquidation or prevent a transfer.
- q: Commodity-price and grade-mix movements can overwhelm and obscure retained operating benefit.
- q: Local competition, export access, and material purity produce wide variation in bargaining power.
- d5: Ferrous scrap evidence cannot represent all paper, plastic, e-scrap, automotive, and nonferrous subsegments.
- d5: A policy goal is not a realized forecast, and EPA's national MSW series excludes substantial industrial scrap.
- o: Operator requirement does not guarantee that the operator is an independent LMM merchant; mills, waste companies, and generators may vertically integrate.
- o: Pure matching and brokerage functions are more vulnerable to software than yard-based processing.

## Sources
- **S1** — [NAICS Definition: 423930 Recyclable Material Merchant Wholesalers](https://www.census.gov/naics/?details=423930&input=42393&year=2017) (accessed 2026-07-22): Defines the industry as merchant wholesale distribution of automotive scrap, industrial scrap, and other recyclable materials, including auto wreckers primarily dismantling vehicles to wholesale scrap.
- **S2** — [Careers in Recycling](https://www.bls.gov/green/recycling/) (accessed 2026-07-22): Describes recycling collection, manual and automated sorting, equipment maintenance, facility management, sales, and safety work; notes that automated facilities still use sorters for quality control and equipment protection.
- **S3** — [Development of a Real-Time Conveyor-Mounted Detection, Classification, and Sortation System for Contaminants](https://www.energy.gov/nepa/articles/cx-028325-development-real-time-conveyor-mounted-detection-classification-and) (accessed 2026-07-22): Describes an AMP Robotics, Idaho National Laboratory, and Michigan Tech project using artificial neural networks to identify whole-material and contact contamination in material-recovery streams.
- **S4** — [Funding Selections - REMADE Institute RFP 6](https://www.energy.gov/cmei/ammto/funding-selections-remade-institute-remade-rfp-6) (accessed 2026-07-22): Describes funded AI, computer-vision, robotic-arm, spectroscopy, and machine-learning projects for waste, plastics, textile, and product-core sorting, while characterizing several as lab-to-pilot or demonstration efforts.
- **S5** — [Mineral Commodity Summaries 2025: Iron and Steel Scrap](https://pubs.usgs.gov/periodicals/mcs2025/mcs2025-iron-steel-scrap.pdf) (accessed 2026-07-22): Reports estimated U.S. apparent iron and steel scrap consumption of 63 million tons in 2024 versus 62 million in 2023, $24 billion of domestic purchases in 2024, and describes recycled scrap as vital to steel and cast-iron production.
- **S6** — [Recycling Is the Primary Energy Efficiency Technology for Aluminum and Steel Manufacturing](https://www.eia.gov/todayinenergy/detail.php?id=16211) (accessed 2026-07-22): Reports that secondary steel production uses about 74% less energy than production from iron ore and explains the manufacturing sources and physical flows of new and old metal scrap.
- **S7** — [U.S. National Recycling Goal](https://www.epa.gov/circulareconomy/us-national-recycling-goal) (accessed 2026-07-22): States the federal goal of increasing the U.S. recycling rate to 50% by 2030 and links it to changes in collection, sorting, market development, and investment.
- **S8** — [ABS Characteristics of Business Owners: 2022 Tables](https://www.census.gov/data/tables/2022/econ/abs/2022-abs-characteristics-of-owners.html) (accessed 2026-07-22): Establishes availability of employer-business owner characteristics including owner age, an indirect succession input.
- **S9** — [Business Dynamics Statistics](https://www.census.gov/programs-surveys/bds.html) (accessed 2026-07-22): Explains that BDS measures births, deaths, startups, and shutdowns, clarifying why public business-dynamics measures cannot be treated as qualifying control transfers.
