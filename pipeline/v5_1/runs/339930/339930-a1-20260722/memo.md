# 339930 — Doll, Toy, and Game Manufacturing

*v5.1 Stage 1 research memo. Run `339930-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** CONDITIONAL · A 6.84 · L 3.84 · interval LOW_PRIORITY → PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Digitizable product-development and commercial workflows can be improved while accountable operators remain necessary for physical supply and safety compliance.
**Weakness:** Retailer leverage, hit and license concentration, volatile working capital, and import competition can prevent productivity gains from becoming durable owner cash flow.

## Business-model lens
- Included: US lower-middle-market manufacturers that repeatedly supply dolls, toys, physical games, electronic game devices, parts, accessories, or private-label products to external retailers, distributors, licensors, institutions, and brand owners, including firms that retain accountable product-development, sourcing, compliance, and customer-delivery responsibility while outsourcing some fabrication.
- Excluded: Shells, captive internal units, non-control financing vehicles, pure wholesalers, software publishers, video-game software reproduction, coin-operated amusement-machine manufacturing, sporting-goods manufacturing, and firms whose normalized EBITDA is outside the screened band are excluded. One-off hobby makers and entities that merely license intellectual property without accountable product supply are also excluded.
- Customer and revenue model: Revenue is principally per-unit wholesale or contract-manufacturing sales, often through seasonal line reviews and repeat purchase orders. Economics may also include tooling or development charges, minimum-order commitments, private-label programs, and royalties on licensed characters or brands.
- Deviation from default lens: none

## Executive view
The industry combines a large digital creative and administrative surface with an irreducibly physical, safety-regulated product. The most coherent operating opportunity is in repeat suppliers that own product, customer, vendor, compliance, and inventory workflows; pure licensing shells and one-off creators do not fit. Brand strength and channel position matter at least as much as manufacturing process because retailer leverage and product hits determine whether productivity becomes durable cash flow.

## How AI changes the work
AI can accelerate concept exploration, artwork and packaging drafts, rules and instructions, translation, catalog content, demand sensing, vendor communication, order handling, and customer support. It is less able to replace hands-on prototyping, tooling, assembly, laboratory tests, product inspection, or accountable safety judgments. Real implementation depends on connecting design, licensing, compliance, vendor, retailer, and sales data with reliable human review.

## Value capture
Fixed-price branded products can retain savings until the next product or retailer review, especially where intellectual property, a license, or differentiated distribution limits comparison. Private-label and contract-manufacturing customers can demand lower bids or better service, and royalties, promotions, chargebacks, imports, and imitation can absorb gains. Contract structure and channel concentration therefore require firm-level diligence.

## Firm availability
Census counted 485 US establishments in the industry in 2023, but establishments are not eligible firms and many operators may be too small, outside the EBITDA band, captive, importer-led, or dependent on unstable hits. Broad owner-age evidence suggests succession supply exists, while actual qualifying transfers will be fewer because internal succession, closures, and asset or license sales do not always produce a transferable operating company.

## Demand durability
Household spending evidence supports continued demand for play products but is nominal, broader than the industry, and volatile. Physical play, gifting, education, licensed entertainment, tabletop social activity, and adult collecting are durable use cases. Digital substitution, demographics, consumer cyclicality, short product lives, import competition, and retailer inventory discipline make the path uneven.

## Risks and uncertainty
The largest uncertainties are firm classification, eligible-company count, occupation mix inside this narrow industry, pass-through behavior, succession timing, and constant-price domestic demand. Child-safety certification and testing, intellectual-property provenance, connected-toy privacy and security, recalls, license concentration, retailer concentration, working-capital seasonality, and forecast errors can overwhelm labor savings. Diligence should reject firms whose economics depend on one license, one retailer, or one transient hit without repeatable development and compliance systems.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.6232 | — | OBSERVED | — |
| n | — | 52 | — | ESTIMATE | — |
| a | 0.22 | 0.38 | 0.53 | PROXY | S1, S3, S6 |
| rho | 0.27 | 0.46 | 0.63 | PROXY | S4, S6 |
| e | 0.6 | 0.76 | 0.88 | ESTIMATE | S1, S2 |
| s5 | 0.14 | 0.25 | 0.36 | PROXY | S5 |
| q | 0.33 | 0.51 | 0.69 | ESTIMATE | — |
| d5 | 0.91 | 1.04 | 1.18 | PROXY | S1, S7 |
| o | 0.77 | 0.88 | 0.96 | ESTIMATE | S1, S6 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 1.48 | 4.36 | 8.32 | PROXY |
| F | 2.70 | 3.84 | 4.60 | ESTIMATE |
| C | 6.60 | 10.00 | 10.00 | ESTIMATE |
| D | 7.01 | 9.15 | 10.00 | ESTIMATE |

## Caveats
- a: The BLS occupation table is for NAICS 339, whose product and production mix is much broader than toys and games.
- a: Employment shares are not wage-weighted task shares, and occupation titles do not reveal current automation.
- a: Brand owners that contract out fabrication can be classified differently from otherwise similar operating models.
- rho: Anthropic traffic is vendor-specific and reflects selected users rather than all businesses.
- rho: Toy safety requirements govern final products, not every AI-assisted upstream task.
- rho: Implementation will vary sharply between digital tabletop-game publishers, connected-toy firms, and domestic physical producers.
- e: Census reports establishments rather than firms and does not disclose lower-middle-market eligibility.
- e: Classification can turn on whether a company owns production, contracts it out, imports finished goods, or primarily licenses a brand.
- e: Seasonal or hit-driven product revenue can make normalized EBITDA unstable.
- s5: The Census owner-age distribution is cross-industry, represents responding employer-business owners, and uses 2018 data.
- s5: Owner age is a weak predictor of timing and transfer type without firm-level succession evidence.
- s5: Portfolio sales, license transfers, and corporate carve-outs may not map cleanly to a qualifying operating-company control transfer.
- q: No public source directly measures pass-through of AI-enabled savings in this industry.
- q: Retention differs materially between branded products, licensed properties, private-label supply, and open-book contract manufacturing.
- q: Seasonality and product-mix shifts can obscure productivity-related price effects.
- d5: The expenditure series is nominal, broader than NAICS 339930, household-only, and includes retail margins and imported products.
- d5: Category demand is unusually seasonal and can be concentrated in a small number of hits or licenses.
- d5: Constant-quality adjustment is difficult when electronic features, licensed content, and product mix change.
- o: The Census definition includes physical electronic games but excludes video-game software, making digital substitution a boundary issue.
- o: An accountable brand or importer may remain necessary even when no US manufacturing labor remains.
- o: Connected toys can shift value toward software while retaining physical-product safety obligations.

## Sources
- **S1** — [2022 Economic Census Manufacturing Industry Classification Form: Doll, Toy, and Game Manufacturing](https://bhs.econ.census.gov/ombpdfs2022/export/2022_MC-33993_mu.pdf) (accessed 2026-07-22): Defines the industry's included products and boundaries, including electronic games, and identifies exclusions such as video-game software reproduction, coin-operated amusement machines, sporting goods, wholesalers, and software publishers.
- **S2** — [Toy Makers: 2023 County Business Patterns](https://www2.census.gov/programs-surveys/sis/resources/toy_makers.pdf) (accessed 2026-07-22): Reports 485 US doll, toy, and game manufacturing establishments in 2023 and describes manufacturers as making products and sending them to stores.
- **S3** — [May 2023 OEWS Industry-Specific Occupational Employment and Wage Estimates: NAICS 339 Miscellaneous Manufacturing](https://www.bls.gov/oes/2023/may/naics3_339000.htm) (accessed 2026-07-22): Provides a broader-industry occupation mix: production accounts for 48.81 percent of employment, office and administrative support for 11.06 percent, management for 8.10 percent, and arts, design, entertainment, sports, and media for 2.29 percent.
- **S4** — [Anthropic Economic Index Report: Uneven Geographic and Enterprise AI Adoption](https://www.anthropic.com/research/anthropic-economic-index-september-2025-report) (accessed 2026-07-22): Finds automation patterns in 77 percent of first-party API business uses and identifies context curation, data modernization, and organizational investment as constraints on sophisticated deployment.
- **S5** — [Business Owners' Ages](https://www.census.gov/content/dam/Census/library/visualizations/2020/comm/business-owners-ages.pdf) (accessed 2026-07-22): Reports that 51 percent of responding US employer-business owners were at least age 55, based on the 2019 Annual Business Survey using 2018 data.
- **S6** — [Toy Safety Business Guidance FAQ](https://www.cpsc.gov/FAQ/Toy-Safety) (accessed 2026-07-22): Explains mandatory third-party testing and Children's Product Certificates for toys intended for children, the ASTM F963 toy-safety standard, manufacturer and importer responsibility, and additional lead, phthalate, and tracking-label requirements.
- **S7** — [Estimate of Annual Expenditures for Toys, Hobbies, and Playground Equipment per Consumer Unit](https://fred.stlouisfed.org/series/CXUTOYSLB0101M) (accessed 2026-07-22): BLS Consumer Expenditure data published through FRED show nominal annual spending per consumer unit of 170 dollars in 2020, 199 dollars in 2021, 167 dollars in 2022, 181 dollars in 2023, and 189 dollars in 2024.
