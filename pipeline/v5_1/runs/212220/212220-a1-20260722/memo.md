# 212220 — Gold Ore and Silver Ore Mining

*v5.1 Stage 1 research memo. Run `212220-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** no base (evidence-first) · A — · L — · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness STRESS_TEST_ONLY · action EVIDENCE_FIRST

**Driver:** Data-rich, high-value operations can create meaningful AI-enabled gains in recovery, uptime, planning, grade control, and safety even when direct labor exposure is modest.
**Weakness:** The LMM firm population is unknown, while commodity pricing and mine-specific geological, environmental, and capital risks dominate transferability and retained value.

## Business-model lens
- Included: Independent U.S. operating companies that develop and run gold or silver mines and associated crushing, grinding, beneficiation, concentration, leaching, recovery, and mine-linked doré production, with recurring sales to external smelters, refiners, traders, or offtake customers.
- Excluded: Exploration-only and pre-production developers, dormant claims, passive royalty or streaming interests, placer artisans without transferable employer operations, captive internal mines, standalone bullion refiners, shells, and non-control financing vehicles.
- Customer and revenue model: Revenue comes from deliveries of doré, concentrate, carbon material, or payable metal under spot-linked, assay-settled, hedged, streaming, royalty-burdened, or offtake arrangements. Economics depend on recoverable ounces, grade, recovery, payability, treatment and refining charges, metal prices, mine life, sustaining capital, and reclamation obligations.
- Deviation from default lens: Gold and silver mining is asset-based commodity production, not an outsourced service, and the code mixes producing mines with development and small placer activity. The lens is narrowed to independent producing employer operations with repeat external metal sales so a transferable operating-company population can be evaluated; the narrowing is for coherence rather than attractiveness.

## Executive view
Gold and silver mining is an asset-heavy commodity business rather than an outsourced service, and the dataset provides no defensible LMM firm count. Producing mines offer data-rich AI opportunities in planning, maintenance, recovery, dispatch, monitoring, and reporting, but physical operations dominate and global metal pricing sharply limits commercial retention.

## How AI changes the work
AI can assist resource modeling, mine planning, grade control, predictive maintenance, dispatch, recovery optimization, safety monitoring, document search, and compliance reporting. Drilling, blasting, underground work, equipment operation, maintenance execution, processing, and accountable safety decisions remain physical and site-specific.

## Value capture
A permitted reserve body and efficient operation can generate large economic gains, yet buyers of doré and concentrate settle against global metal prices, assay, payability, and deductions. Royalties, streams, taxes, and commodity cycles further separate operational productivity from retained pricing.

## Firm availability
The code contains producing mines, development ventures, dormant properties, and small placer activity. Eligibility requires real production, economic reserves, permits, transferable management, manageable reclamation and environmental risk, and an independent employer operation; the missing target count is therefore a fundamental diligence gap.

## Demand durability
Gold and silver retain monetary, investment, jewelry, and growing industrial uses, but U.S. mine output is governed by geology, depletion, reserve replacement, prices, permitting, capital, and project timing. A broad metal-ore growth forecast supports only a wide precious-metal production range.

## Risks and uncertainty
The principal uncertainty is the missing LMM target count. Additional risks include four-digit labor and demand proxies, reserve and grade estimation, recovery, single-mine exposure, commodity prices, royalties and streams, permitting, tailings, environmental and reclamation liabilities, mine safety, capital intensity, and already-deployed automation.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.2248 | — | OBSERVED | — |
| n | — | — | — | MISSING | — |
| a | 0.09 | 0.18 | 0.29 | PROXY | S1, S2, S5 |
| rho | 0.29 | 0.5 | 0.68 | ESTIMATE | S5, S6 |
| e | 0.14 | 0.31 | 0.5 | ESTIMATE | S1, S4, S7 |
| s5 | 0.08 | 0.18 | 0.3 | PROXY | S7, S8 |
| q | 0.03 | 0.12 | 0.28 | ESTIMATE | S3, S7 |
| d5 | 0.76 | 1.08 | 1.42 | PROXY | S3, S4, S7 |
| o | 0.98 | 0.995 | 1 | ESTIMATE | S1, S4, S5, S6, S7 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.23 | 0.81 | 1.77 | ESTIMATE |
| F | — | — | — | MISSING |
| C | 0.60 | 2.40 | 5.60 | ESTIMATE |
| D | 7.45 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: The occupation source covers all metal ore mining.
- a: Already-automated process control and equipment functions are excluded from the residual opportunity.
- rho: NIOSH evidence covers mining generally rather than gold and silver specifically.
- rho: Benefits may increase recovery, reserve conversion, uptime, or safety rather than reduce current labor.
- e: The dataset deliberately provides no defensible LMM firm count.
- e: USGS reports both concentrated large-mine output and numerous smaller placer operations, many of which are not transferable employer firms.
- s5: Gallup covers all U.S. employer businesses rather than mine operators.
- s5: Without n, even a well-estimated probability cannot establish available target count.
- q: Commodity price movements can overwhelm productivity effects.
- q: Streaming and royalty encumbrances vary widely by mine and can materially reduce retained upside.
- d5: The BLS projection covers all metal ore mining and ten years.
- d5: Revenue and reserve values are highly price-sensitive and do not equal constant-quality output quantity.
- o: Some production can shift between independent and captive operators without eliminating physical mine operation.

## Sources
- **S1** — [NAICS Definition: Gold Ore and Silver Ore Mining](https://www.census.gov/naics/resources/archives/sect21.html) (accessed 2026-07-22): Industry boundary covering mine development, mining, beneficiation, and mine-linked bullion or doré production.
- **S2** — [Metal Ore Mining - May 2023 OEWS Industry-Specific Occupational Employment and Wage Estimates](https://www.bls.gov/oes/2023/may/naics4_212200.htm) (accessed 2026-07-22): Four-digit occupation mix and employment shares used to bridge AI task exposure.
- **S3** — [Employment and Output by Industry](https://www.bls.gov/emp/tables/industry-employment-and-output.htm) (accessed 2026-07-22): 2024-2034 real-output projection for NAICS 212200 used as the demand proxy.
- **S4** — [Mineral Commodity Summaries 2026: Gold and Silver](https://pubs.usgs.gov/periodicals/mcs2026/mcs2026.pdf) (accessed 2026-07-22): U.S. precious-metal production, mine concentration, uses, reserves, industry structure, and market trends.
- **S5** — [NIOSH Mining Program Poised to Support Mining of Critical Minerals](https://www.cdc.gov/niosh/bulletin/2025/mining-critical-minerals.html) (accessed 2026-07-22): Mining use of autonomous equipment, real-time monitoring, AI, sensor fusion, and related safety constraints.
- **S6** — [Safety Program for Surface Mobile Equipment Standards for Surface Metal and Nonmetal Mines](https://www.msha.gov/sites/default/files/Regulations/SME-Rule-StandardsforSurfaceMNMMines-Part56.pdf) (accessed 2026-07-22): Mine-operator safety-program and surface mobile-equipment accountability.
- **S7** — [Hecla Mining Company 2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/719413/000119312526055059/hl-20251231.htm) (accessed 2026-07-22): Gold and silver concentrate, carbon, and doré sales; customer channels; operating mines; reserves; production; metal-price exposure; and mine portfolio transactions.
- **S8** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Employer-business owner age and five-year planned sale or transfer used as a qualified succession proxy.
