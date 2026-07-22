# 332993 — Ammunition (except Small Arms) Manufacturing

*v5.1 Stage 1 research memo. Run `332993-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** LOW_PRIORITY · A 5.87 · L 1.35 · interval STRUCTURAL_OUT → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Funded industrial-base expansion and recurring physical munitions requirements support durable demand and data-rich process-improvement opportunities.
**Weakness:** Only a handful of plausibly transferable LMM operators exist, and acquisition plus AI deployment is constrained by security, safety, qualification, and government-control requirements.

## Business-model lens
- Included: US lower-middle-market privately owned manufacturers and specialist contract producers that repeatedly make medium- or large-caliber ammunition, cartridge cases, grenades, mortar or artillery components, energetics, or load-assemble-pack deliverables for government customers and defense primes.
- Excluded: Small-arms ammunition; guided missiles and space vehicles; firearms; demilitarization-only operations; captive prime-contractor divisions; government-owned plants where the transferable operating business lacks meaningful owned assets or customer diversification; foreign firms; and businesses outside the lower-middle-market control-acquisition band.
- Customer and revenue model: Revenue comes from recurring lots, delivery orders, multiyear procurement, and program subcontracts for specified munitions or components. Pricing is commonly firm-fixed-price for production, with some cost-reimbursement or incentive arrangements for development and specialized work; qualification, security, testing, and traceability are integral to delivery.
- Deviation from default lens: The code combines giant defense primes, government-owned contractor-operated plants, and smaller transferable specialist manufacturers. The lens is narrowed to privately owned LMM manufacturers and specialist contract producers whose repeat external-customer work and operating assets can plausibly transfer as a control acquisition; the narrowing is for business-model coherence, not attractiveness.

## Executive view
Demand evidence is stronger here than in most manufacturing screens: the Army is expanding artillery capacity and multiyear procurement supports the industrial base. The investable LMM population is nevertheless tiny and structurally awkward, while safety, security, qualification, and government-contract constraints limit AI implementation and acquisition flexibility.

## How AI changes the work
AI can improve forecast and materials planning, schedule optimization, machine-health prediction, inspection and radiography triage, quality trend detection, engineering and specification search, bid support, and contract administration. It should remain human-supervised around energetic processing, configuration changes, acceptance, release, safety, and controlled technical data.

## Value capture
Fixed-price production can preserve savings within an award, especially when gains reduce downtime, scrap, or schedule risk. Follow-on competition, cost visibility, audit rights, multiyear purchasing discounts, and prime-customer bargaining should share a meaningful portion over the full horizon.

## Firm availability
Specialist and certified small-business manufacturers exist, but the code also contains giant primes and government-owned facilities. A verified parent-level target census and facility-ownership review is essential; the provided full-code estimate alone is not a dependable acquisition pipeline.

## Demand durability
Current artillery and munitions demand is supported by stockpile replacement, allied supply, readiness, modernization, and funded capacity expansion. The central risk is that conflict-driven orders normalize after substantial new capacity arrives, leaving smaller suppliers exposed to program and customer concentration.

## Risks and uncertainty
Material risks include explosives safety, fatal quality escapes, environmental liabilities, cybersecurity and controlled-data rules, export controls, foreign-ownership review, contract novation, government audits, appropriations, cancellation, sole-source dependence, facility ownership, customer concentration, and scarce skilled labor. The transfer-rate and eligible-denominator estimates are especially weak.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.5163 | — | OBSERVED | — |
| n | — | 11 | — | ESTIMATE | — |
| a | 0.13 | 0.24 | 0.36 | PROXY | S1, S2, S3, S4 |
| rho | 0.27 | 0.43 | 0.59 | PROXY | S1, S2, S3, S4 |
| e | 0.28 | 0.48 | 0.68 | ESTIMATE | — |
| s5 | 0.13 | 0.25 | 0.4 | PROXY | S9 |
| q | 0.35 | 0.54 | 0.7 | PROXY | S8 |
| d5 | 0.88 | 1.16 | 1.5 | PROXY | S5, S6, S7, S8 |
| o | 0.97 | 0.995 | 1 | ESTIMATE | — |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.72 | 2.13 | 4.39 | PROXY |
| F | 0.54 | 1.35 | 2.23 | ESTIMATE |
| C | 7.00 | 10.00 | 10.00 | PROXY |
| D | 8.54 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: No source measures current not-yet-automated AI exposure for NAICS 332993 or the narrowed LMM population.
- a: The provided compensation-to-receipts ratio of 0.5163 combines 2024 wages with 2022 receipts and may be distorted by program timing, government-owned facilities, and the broader code's mix.
- rho: The evidence establishes use cases and operating constraints, not realized five-year AI adoption.
- rho: Government authorization and controlled-data requirements may dominate technical feasibility at some firms.
- e: No complete denominator identifies privately transferable LMM manufacturers inside the code.
- e: The provided firm count of 11 is an estimate from size-class receipts and a margin bridge; defense program timing and government-owned facilities can distort the mapping.
- s5: The cited acquisition is a scale- and geography-mismatched proxy, not an LMM hazard observation.
- s5: Many relevant private transactions may be undisclosed for commercial or security reasons.
- q: The source's contract mix is company-wide and not specific to LMM ammunition contracts.
- q: Retention varies greatly between firm-fixed-price production, cost reimbursement, sole-source awards, and competitive subcontracts.
- d5: Current expansion is heavily influenced by active conflicts and replenishment, which may not persist through year five.
- d5: Government and prime-level demand does not guarantee proportional work for the narrowed LMM supplier population.
- o: This is bounded judgment, not an observed displacement measure.
- o: Operator-required demand can persist even if work moves from an LMM supplier to a prime or government-owned facility.

## Sources
- **S1** — [Artificial Intelligence in Manufacturing: Real World Success Stories and Lessons Learned](https://www.nist.gov/blogs/manufacturing-innovation-blog/artificial-intelligence-manufacturing-real-world-success-stories) (accessed 2026-07-22): Small and medium manufacturer AI applications in predictive maintenance and quality, scrap, throughput, and forecasting, plus data and implementation constraints.
- **S2** — [Ultra Defense Corp](https://www.udcusa.com/) (accessed 2026-07-22): Federally licensed US facilities designing, testing, and manufacturing medium- and large-caliber ammunition for government and commercial customers, including recurring 40mm production.
- **S3** — [American Ordnance LLC - Premier Ammunition Supplier](https://aollc.biz/) (accessed 2026-07-22): Detailed load-assemble-pack, energetics, artillery, mortar, grenade, inspection, engineering, bar-code, automation, and government-customer workflows.
- **S4** — [AMRON | National Defense Corporation](https://www.nationaldefensecorp.com/amron/) (accessed 2026-07-22): A certified small business in NAICS 332993 producing medium-caliber cartridge cases through integrated forming, machining, heat treatment, finishing, and quality-controlled delivery.
- **S5** — [Army seeks to expand and accelerate 155 mm production](https://www.army.mil/article-amp/283210/army_seeks_to_expand_and_accelerate_155_mm_production) (accessed 2026-07-22): Army efforts to expand artillery production, modernize the industrial base, increase load-assemble-pack and component capacity, and create future contracting opportunities.
- **S6** — [Army opens modern projectile loading facility to expand 155 mm artillery production](https://www.army.mil/article-amp/284829/army_opens_modern_projectile_loading_facility_to_expand_155_mm_artillery_production) (accessed 2026-07-22): Opening of new artillery load-assemble-pack capacity as part of a broader production and readiness expansion.
- **S7** — [Ukraine: Status and Challenges of DOD Weapon Replacement Efforts](https://www.gao.gov/products/gao-24-106649) (accessed 2026-07-22): DOD industrial-base investment for ammunition capacity and use of multiyear procurement to provide a stable demand signal and cost savings.
- **S8** — [General Dynamics 2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/40533/000004053326000006/gd-20251231.htm) (accessed 2026-07-22): Defense production contract structures, cost-reimbursement and incentive mechanics, and increased munitions and ordnance awards and backlog.
- **S9** — [Rheinmetall completes acquisition of Spanish defence contractor Expal Systems](https://www.rheinmetall.com/en/media/news-watch/news/2023/8/2023-08-01-rheinmetall-completes-acquisition-of-spanish-defence-contractor-expal-systems) (accessed 2026-07-22): Completed control acquisition of a medium- and large-caliber ammunition producer, demonstrating strategic transferability with substantial scale and geography caveats.
