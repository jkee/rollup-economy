# 331410 — Nonferrous Metal (except Aluminum) Smelting and Refining

*v5.1 Stage 1 research memo. Run `331410-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 5.28 · L 0.28 · interval STRUCTURAL_OUT → STRUCTURAL_OUT · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Trusted assay and recovery relationships for recurring high-value feed streams, enhanced by better yield, traceability, and turnaround.
**Weakness:** A tiny, highly heterogeneous and liability-sensitive acquisition pool makes the service-model incidence difficult to measure and scale.

## Business-model lens
- Included: Independent lower-middle-market refiners and smelters of precious and other nonferrous metals that repeatedly process customer-owned scrap, residues, dore, concentrates, or industrial waste and earn treatment, assay, settlement, or toll-refining fees.
- Excluded: Aluminum smelting; mines without refining; scrap collectors or brokers without metallurgical recovery; captive integrated smelters; large commodity primary smelters outside the LMM band; retail gold buyers without substantive assay and refining; and firms whose economics are primarily speculative metal ownership.
- Customer and revenue model: Customers include jewelers, dental labs, electronics manufacturers, mines, industrial generators, recyclers, and metal dealers. Recurring revenue comes from melt, assay, treatment, and refining fees or retained metal percentages, with settlement based on verified fine-metal content and daily benchmark prices; some firms also purchase lots outright.
- Deviation from default lens: none

## Executive view
The coherent LMM opportunity is not a commodity-scale copper or zinc smelter but a trusted toll refiner handling recurring precious, electronic, dental, mining, or industrial residues. AI can improve process decisions, lot control, assay review, maintenance, settlement, and documentation, while the physical metallurgy and compliance burden remain substantial.

## How AI changes the work
Practical uses include feed classification, recovery-route selection, blend and flux recommendations, process monitoring, anomaly detection, predictive maintenance, laboratory-result review, lot traceability, automated settlement, AML screening, and customer communication. Physical sampling, preparation, melting, chemical processing, assay verification, waste handling, and safety decisions persist.

## Value capture
Benchmark-linked settlement and published fees make simple processing economics transparent. Durable capture comes from recovery yield, turnaround, throughput, assay credibility, difficult-feed expertise, compliance, and fewer disputes. Better recovery may be shared directly with customers, while capacity and reliability gains are more retainable.

## Firm availability
The estimated pool is only 21 LMM firms and spans very different metals and technologies. Family ownership creates some succession potential, but environmental liabilities, permits, security, anti-money-laundering controls, feed provenance, working capital, equipment condition, technical staff, and reputation will sharply reduce the actionable set.

## Demand durability
Electrification and grid investment support copper, while recycling, electronics, jewelry, industrial, and dental streams sustain precious-metal refining. Structural demand does not remove exposure to volatile prices, treatment charges, scrap flows, substitution, global trade, and the possibility that feed is refined by larger or offshore plants.

## Risks and uncertainty
The largest uncertainty is composition of the 21-firm universe: public service evidence is concentrated in precious metals, whereas the NAICS also includes very different base-metal smelters. Environmental remediation, hazardous feeds, assay disputes, theft and fraud, customer concentration, commodity working capital, permitting, and limited AI outcome data are material risks.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.0674 | — | OBSERVED | — |
| n | — | 21 | — | ESTIMATE | — |
| a | 0.17 | 0.27 | 0.39 | PROXY | S1, S2, S3, S4 |
| rho | 0.2 | 0.38 | 0.57 | ESTIMATE | S2, S3, S4, S5 |
| e | 0.18 | 0.34 | 0.52 | PROXY | S5, S6, S7, S8 |
| s5 | 0.09 | 0.16 | 0.24 | PROXY | S5, S9 |
| q | 0.3 | 0.48 | 0.65 | PROXY | S5, S6, S7, S8 |
| d5 | 0.98 | 1.12 | 1.28 | PROXY | S5, S10, S11 |
| o | 0.95 | 0.99 | 1 | ESTIMATE | S1, S2, S5, S10 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.09 | 0.28 | 0.60 | ESTIMATE |
| F | 0.47 | 1.23 | 2.07 | ESTIMATE |
| C | 6.00 | 9.60 | 10.00 | PROXY |
| D | 9.31 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: O*NET spans ferrous and nonferrous furnace work.
- a: The AI source is a vendor description, not a representative outcome study.
- a: Precious-metal refining and large copper, lead, or zinc smelting have very different task mixes.
- rho: No representative adoption data for NAICS 331410 were found.
- rho: Back-office automation is more feasible than autonomous furnace control.
- rho: Assay and settlement outputs require auditability and customer trust.
- e: Website examples are concentrated in precious metals.
- e: Assay settlement can accompany either a service or an outright purchase.
- e: NAICS classification of preprocessors and downstream fabricators may vary.
- s5: Cross-industry intent is not observed transaction probability.
- s5: Stated owner plans may not produce a financeable sale.
- s5: Environmental and compliance liabilities can dominate valuation.
- q: Public retail and small-lot schedules may not resemble industrial contracts.
- q: Metal-price movements can obscure operational value capture.
- q: Customers may demand improved recoveries directly through higher payouts.
- d5: Copper outlook is an imperfect proxy for a multi-metal category.
- d5: Higher metal demand does not automatically raise domestic merchant-refining volume.
- d5: Commodity cycles can overwhelm structural trends within five years.
- o: This factor isolates AI-related obsolescence, not closure from regulation or commodity economics.
- o: A specific legacy facility can become obsolete even when refining remains necessary.
- o: Feed streams can disappear through product substitution or offshoring.

## Sources
- **S1** — [NAICS 331410 - Nonferrous Metal (except Aluminum) Smelting and Refining](https://www.naics.com/naics-code-description/?code=331410&v=2022) (accessed 2026-07-22): Industry boundary for primary nonferrous metals other than aluminum made in smelting and refining mills.
- **S2** — [Metal-Refining Furnace Operators and Tenders](https://www.onetonline.org/link/summary/51-4051.00) (accessed 2026-07-22): Core furnace tasks, controls, sampling, charging, skimming, inspection, maintenance direction, records, physical handling, heat, contaminants, and safety context.
- **S3** — [Smelting Process Intelligence](https://www.bcg.com/x/product-library/smelting-process-intelligence) (accessed 2026-07-22): Commercial availability of AI and machine-learning process optimization for smelters and refiners and decision support for plant output and profitability.
- **S4** — [Only 3.8% of Businesses Use AI to Produce Goods and Services](https://www.census.gov/library/stories/2023/11/businesses-use-ai.html) (accessed 2026-07-22): Broad baseline of low realized AI use, used only to contextualize implementation uncertainty rather than estimate industry adoption.
- **S5** — [David H. Fell & Company Refining Process](https://dhfco.com/refining/) (accessed 2026-07-22): Family-owned refiner example with thousands of repeat customers, lot tracking, process routing, sampling, XRF/ICP/fire assay, and benchmark-linked settlement.
- **S6** — [Mid-States Silver Refining Schedule and Payout Terms](https://www.midstatesrecycling.com/refining_schedule/silver-metallics-98) (accessed 2026-07-22): Transparent treatment charge, minimum fee, payout percentage, assayed fine-metal basis, settlement timing, and contaminant surcharge.
- **S7** — [Argen Refining Conditions](https://argen.com/refining-conditions) (accessed 2026-07-22): Settlement amount defined as precious-metal value less refining and treatment fees and benchmark pricing at settlement.
- **S8** — [Precious Metal Purchase and Toll Refining](https://suranrecycling.com/services/) (accessed 2026-07-22): Two service models, laboratory analysis, benchmark-linked contractual settlement, and customer retention of legal ownership under toll refining.
- **S9** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Cross-industry owner-age and five-year sell, transfer, closure, and succession-intention evidence.
- **S10** — [IEA Copper Outlook](https://www.iea.org/reports/copper-2) (accessed 2026-07-22): Demand, secondary supply and reuse, primary supply requirements, and refining-concentration projections through 2030 and 2040.
- **S11** — [USGS Mineral Commodity Summaries 2026](https://www.usgs.gov/centers/national-minerals-information-center/mineral-commodity-summaries) (accessed 2026-07-22): Authoritative multi-mineral source covering domestic industry structure, government programs, tariffs, and five-year market statistics for more than 90 minerals.
