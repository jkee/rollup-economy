# 325120 — Industrial Gas Manufacturing

*v5.1 Stage 1 research memo. Run `325120-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** LOW_PRIORITY · A 5.96 · L 1.32 · interval STRUCTURAL_OUT → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Recurring consumption, multi-year supply relationships, and regional delivery economics create durable operator-required revenue.
**Weakness:** Manufacturing eligibility within the LMM population is unverified, and much of the contract evidence comes from a global major.

## Business-model lens
- Included: Lower-middle-market manufacturers that repeatedly produce and supply compressed, liquefied, or solid industrial gases to external customers through on-site, merchant/bulk, or packaged-cylinder delivery.
- Excluded: Pure distributors without gas-manufacturing responsibility, captive internal gas plants, integrated units outside the LMM band, equipment-only vendors, shells, and non-control financing vehicles.
- Customer and revenue model: Recurring B2B product and cylinder-use revenue under purchase orders and multi-year supply agreements; larger on-site customers may have minimum purchases and indexed pass-through, while merchant and packaged customers receive repeated deliveries or pickups.
- Deviation from default lens: none

## Executive view
Industrial gas manufacturing closely matches the recurring external-supply lens: customers repeatedly consume physical gases under contracts, and local production/distribution networks matter. AI can improve logistics, cylinder control, planning, and administration, while accountable production and hazardous delivery remain indispensable.

## How AI changes the work
The strongest applications are demand forecasting, route and load optimization, cylinder identification and exception management, dispatch, predictive maintenance, engineering support, safety-document retrieval, quoting, billing, collections, and customer service. Human operators, drivers, technicians, and release authorities remain central to plants, cylinders, field installations, and emergencies.

## Value capture
Multi-year agreements, indexed energy pass-through, installed tanks, cylinder fleets, route density, and supply-critical customer processes support retention. Packaged-gas purchase orders and shorter contracts expose regional firms to renewal pricing and local competitors, so savings are not fully protected.

## Firm availability
Most true LMM manufacturers should be eligible, but some nominal regional gas companies are distributors rather than producers. Tangible assets, routes, contracts, and customers make firms transferable, while permits, cylinder records, safety history, and environmental exposure demand careful diligence.

## Demand durability
Diverse end markets provide resilience, with electronics, healthcare, food, manufacturing, metals, and chemicals requiring recurring gases. Cyclical industrial volume and customer-installed generation are the main quantity risks, not software elimination.

## Risks and uncertainty
Misclassifying distributors as manufacturers is the central eligibility risk. Catastrophic safety events, energy cost, helium availability, cylinder loss, fleet compliance, plant outages, customer concentration, major-company competition, and capital intensity can overwhelm labor savings.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.2098 | — | OBSERVED | — |
| n | — | 24 | — | ESTIMATE | — |
| a | 0.17 | 0.28 | 0.4 | PROXY | S1, S2, S3 |
| rho | 0.38 | 0.56 | 0.72 | ESTIMATE | S2 |
| e | 0.58 | 0.76 | 0.9 | ESTIMATE | S3 |
| s5 | 0.12 | 0.21 | 0.33 | PROXY | S4 |
| q | 0.55 | 0.7 | 0.83 | PROXY | S3 |
| d5 | 0.98 | 1.06 | 1.17 | PROXY | S3, S5 |
| o | 0.93 | 0.98 | 1 | ESTIMATE | S3 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.54 | 1.32 | 2.42 | ESTIMATE |
| F | 1.58 | 2.53 | 3.37 | ESTIMATE |
| C | 10.00 | 10.00 | 10.00 | PROXY |
| D | 9.11 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: No six-digit wage-weighted task inventory was available.
- a: The estimate excludes process and routing automation already in place.
- rho: No representative LMM industrial-gas AI deployment study was found.
- rho: The range excludes autonomous hazardous-material transport and unreviewed plant control.
- e: Eligibility is inferred from the business model rather than observed for the injected firm list.
- e: Some regional firms commonly described as gas companies may only distribute gas produced by a major.
- s5: The survey population is broader and generally smaller than the LMM lens.
- s5: Owner intentions are not observed qualifying control transfers.
- q: Large-company contract terms may not represent regional LMM firms.
- q: The source does not directly measure retained AI benefit.
- d5: Linde is global and much larger than the lens; Americas includes countries beyond the United States.
- d5: Natural-gas consumption is a downstream-activity proxy, not industrial-gas demand.
- o: Operator persistence is inferred from physical delivery and plant obligations rather than directly measured.
- o: On-site generation can displace merchant or packaged suppliers even when aggregate gas use persists.

## Sources
- **S1** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 325000](https://www.bls.gov/oes/2023/may/naics3_325000.htm) (accessed 2026-07-22): Broader chemical-manufacturing occupational mix used to bound wage-weighted task exposure.
- **S2** — [2026 Roadmap on Artificial Intelligence and Machine Learning for Smart Manufacturing](https://www.nist.gov/publications/2026-roadmap-artificial-intelligence-and-machine-learning-smart-manufacturing) (accessed 2026-07-22): Manufacturing AI opportunities and industrial deployment barriers involving data, controls, reliability, explainability, and safety.
- **S3** — [Linde plc 2025 Annual Report](https://assets.linde.com/-/media/global/corporate/corporate/documents/investors/full-year-financial-reports/2025-annual-report-to-shareholders.pdf) (accessed 2026-07-22): Industrial-gas products, delivery modes, contract durations and minimums, price indices, energy pass-through, regional economics, end markets, volume change, and operating accountability.
- **S4** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): U.S. employer-business five-year sale and transfer intentions.
- **S5** — [U.S. industrial natural gas consumption expected to hit records in 2026 and 2027](https://www.eia.gov/todayinenergy/detail.php?id=67686) (accessed 2026-07-22): Near-term U.S. industrial activity and chemical-sector natural-gas demand as a downstream demand proxy.
