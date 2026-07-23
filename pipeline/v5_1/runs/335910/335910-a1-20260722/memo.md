# 335910 — Battery Manufacturing

*v5.1 Stage 1 research memo. Run `335910-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** no base (evidence-first) · A — · L — · interval STRUCTURAL_OUT → CONDITIONAL · readiness STRESS_TEST_ONLY · action EVIDENCE_FIRST

**Driver:** Expanding electrification, storage, data-center, industrial, and specialty applications create durable physical demand and rich process data.
**Weakness:** No defensible LMM firm count exists, and rapidly changing chemistry, capital intensity, and global cost competition can overwhelm AI gains.

## Business-model lens
- Included: US lower-middle-market independent manufacturers supplying specialty, industrial, stationary, motive-power, reserve-power, replacement, and configured battery cells, packs, or systems with repeat external customers and support needs.
- Excluded: Captive vehicle plants, commodity consumer dry-cell megaplants, large integrated gigafactories, shells, non-control financing vehicles, firms outside the EBITDA band, pure distributors, recyclers without qualifying manufacturing, and project developers that do not manufacture batteries.
- Customer and revenue model: Specialized batteries and systems are sold through repeat OEM, distributor, fleet, defense, medical, data-center, telecom, utility, and industrial relationships, with replacement cycles, configuration, chargers, monitoring, spares, and aftermarket support.
- Deviation from default lens: Narrowed because the NAICS code combines global-scale commodity EV and consumer cell plants with LMM specialty, industrial, stationary, and replacement manufacturers whose customers, capital intensity, transferability, and pricing are fundamentally different.

## Executive view
Battery manufacturing has strong demand and useful data-rich AI applications, but the NAICS code is exceptionally heterogeneous and the frozen dataset has no defensible LMM firm count. The coherent specialty and industrial slice remains physical, safety-critical, capital-intensive, and exposed to rapid chemistry and price change.

## How AI changes the work
AI can improve process control, defect detection, formation analysis, yield diagnosis, predictive maintenance, scheduling, supply planning, engineering, and documentation. Material processing, assembly, testing, qualification, traceability, and safety release remain operator-led.

## Value capture
Niche qualifications, proprietary designs, replacement compatibility, and service can retain gains. Fast global learning curves, powerful customers, import competition, chemistry shifts, and expected cost-downs share much of the benefit.

## Firm availability
Specialty and industrial firms may qualify, but captive ventures, gigafactories, commodity plants, and global strategics dominate capacity. With no defensible frozen firm count, availability cannot be translated into a target quantity.

## Demand durability
Storage, UPS, telecom, material handling, defense, aerospace, medical, resilience, and replacement support growth. Global battery demand is expanding rapidly, though most growth lies outside the narrowed LMM slice and is vulnerable to policy, imports, and chemistry shifts.

## Risks and uncertainty
The missing firm denominator is the central availability weakness. Other risks include fire and warranty liability, hazardous materials, permits, export controls, mineral supply, price collapse, obsolescence, customer qualification, capital needs, and global competition.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.2361 | — | OBSERVED | — |
| n | — | — | — | MISSING | — |
| a | 0.16 | 0.27 | 0.39 | PROXY | S1, S2, S3 |
| rho | 0.35 | 0.57 | 0.74 | ESTIMATE | S3, S4 |
| e | 0.28 | 0.46 | 0.65 | ESTIMATE | S1, S5 |
| s5 | 0.1 | 0.18 | 0.28 | PROXY | S6 |
| q | 0.28 | 0.47 | 0.65 | ESTIMATE | S5, S7 |
| d5 | 1.07 | 1.28 | 1.55 | PROXY | S5, S7, S8 |
| o | 0.9 | 0.97 | 0.995 | ESTIMATE | S1, S5 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.53 | 1.45 | 2.73 | ESTIMATE |
| F | — | — | — | MISSING |
| C | 5.60 | 9.40 | 10.00 | ESTIMATE |
| D | 9.63 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: BLS evidence covers all NAICS 335.
- a: The frozen labor ratio is an ancestor-level proxy and may not fit specialty battery operations.
- rho: Manufacturing-wide adoption surveys are not battery-specific.
- rho: Rapid chemistry and equipment changes can make historical training data stale.
- e: The frozen dataset explicitly provides no defensible LMM firm count, so this share cannot be converted into a target count.
- e: NAICS consolidation under 335910 increases business-model heterogeneity.
- s5: Gallup is cross-industry and measures plans rather than completed transfers.
- s5: No defensible dataset firm count exists for this record.
- q: Specialty pricing differs sharply from commodity lithium-ion cells and lead-acid products.
- q: IEA's global cost declines may not map directly to qualified niche batteries.
- d5: Global deployment is dominated by products and manufacturers outside the lens.
- d5: Capacity and energy measures are not constant-quality unit demand and improve with energy density.
- o: Alternative storage technologies can displace batteries in some applications.
- o: A shift to a global supplier can remove an LMM operator without eliminating accountable manufacturing.

## Sources
- **S1** — [2022 NAICS Definition: Battery Manufacturing](https://www.census.gov/naics/?details=33&input=33&year=2022) (accessed 2026-07-22): Defines 335910 broadly across primary and storage batteries, including lead-acid, lithium, rechargeable, and primary cells.
- **S2** — [Electrical Equipment, Appliance, and Component Manufacturing: NAICS 335](https://www.bls.gov/iag/tgs/iag335.htm) (accessed 2026-07-22): Provides broader-sector evidence on assembly, inspection, production, and supervisory occupations.
- **S3** — [2026 Roadmap on Artificial Intelligence and Machine Learning for Smart Manufacturing](https://www.nist.gov/publications/2026-roadmap-artificial-intelligence-and-machine-learning-smart-manufacturing) (accessed 2026-07-22): Documents industrial AI opportunities and data, integration, reliability, explainability, and safety barriers.
- **S4** — [Shaping the AI-Powered Factory of the Future](https://documents.nam.org/tech/Shaping-the-AI-Powered-Factory-of-the-Future-Report.pdf) (accessed 2026-07-22): Reports limited formal operational AI strategy adoption and significant data and legacy-system barriers.
- **S5** — [EnerSys Fiscal 2025 Annual Report](https://www.sec.gov/Archives/edgar/data/1289308/000119312525142739/d934921dars.pdf) (accessed 2026-07-22): Describes industrial, motive, specialty, UPS, telecom, data-center, utility, defense, medical, and aftermarket battery applications and support to over 10,000 customers.
- **S6** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Reports 22% of US employer-business owners planned a sale, transfer, or public offering within five years.
- **S7** — [Global Critical Minerals Outlook 2026: Market Overview](https://www.iea.org/reports/global-critical-minerals-outlook-2026/market-overview) (accessed 2026-07-22): Reports global battery demand grew over 35% in 2025 and surpassed 1.5 TWh.
- **S8** — [Global Energy Review 2026: Battery Storage](https://www.iea.org/reports/global-energy-review-2026/technology-battery-storage) (accessed 2026-07-22): Reports 108 GW of 2025 battery-storage additions, up 40%, and data-center UPS additions rising 30% to 45 GW.
