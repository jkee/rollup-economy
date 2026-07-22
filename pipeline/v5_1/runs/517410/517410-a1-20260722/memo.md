# 517410 — Satellite Telecommunications

*v5.1 Stage 1 research memo. Run `517410-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** LOW_PRIORITY · A 6.22 · L 1.45 · interval STRUCTURAL_OUT → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Recurring mission-critical connectivity can support both automation savings and continued need for an accountable operator.
**Weakness:** The eligible firm universe is small and heterogeneous, while the best public operating evidence comes from scaled companies outside the target size band.

## Business-model lens
- Included: US lower-middle-market firms that provide recurring or repeat satellite signal forwarding, reception, capacity, airtime, or resale services to external telecommunications and broadcasting customers.
- Excluded: Direct-to-home satellite television, media networks, satellite tracking stations classified elsewhere, captive network units, shell spectrum vehicles, equipment-only sellers, and businesses outside the normalized EBITDA band.
- Customer and revenue model: Wholesale and enterprise customers buy recurring access, capacity, airtime, managed connectivity, and usage-based transmission services, sometimes alongside equipment or engineering work.
- Deviation from default lens: none

## Executive view
Satellite telecommunications combines recurring connectivity economics with technically accountable operations. The main opportunity is to automate support, monitoring, commercial, and back-office work without assuming that software replaces the network operator.

## How AI changes the work
AI can classify alarms and tickets, summarize incidents, draft customer communications, reconcile usage and billing, assist sales engineering, and improve forecasting. Radio-frequency design, physical maintenance, safety decisions, licensing, and final incident authority remain human-led.

## Value capture
Monthly access and usage contracts create room to retain operating savings, especially where service reliability and integration matter. Renewal negotiations, concentrated wholesale buyers, competitive capacity, and declining unit prices can transfer a material share to customers.

## Firm availability
The service definition is externally oriented, but only part of the dataset population is likely to be an independent recurring-service business with transferable operations and earnings in scope. Captive units, shells, equipment sellers, and project-heavy engineering firms reduce eligibility.

## Demand durability
Broadband, IoT, mobility, direct-to-device development, resilience, and government missions support demand. Recent global subscriber growth is not a clean forecast for US wholesale providers, and mature capacity plus terrestrial substitution warrants a wide demand range.

## Risks and uncertainty
The largest uncertainties are the exact occupation mix of independent firms, the rate of production AI implementation, private contract repricing, US service-volume growth, and the small number of genuinely transferable firms. Spectrum, licensing, national-security review, launch dependence, and customer concentration add operating and transaction risk.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1811 | — | OBSERVED | — |
| n | — | 55 | — | ESTIMATE | — |
| a | 0.24 | 0.35 | 0.49 | PROXY | S1, S2, S3 |
| rho | 0.39 | 0.57 | 0.73 | PROXY | S3 |
| e | 0.43 | 0.64 | 0.81 | ESTIMATE | S1, S5 |
| s5 | 0.1 | 0.21 | 0.35 | PROXY | S6, S7 |
| q | 0.36 | 0.57 | 0.75 | PROXY | S5 |
| d5 | 0.98 | 1.27 | 1.66 | PROXY | S4, S5 |
| o | 0.87 | 0.95 | 0.99 | ESTIMATE | S1, S8 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.68 | 1.45 | 2.59 | PROXY |
| F | 1.95 | 3.42 | 4.52 | ESTIMATE |
| C | 7.20 | 10.00 | 10.00 | PROXY |
| D | 8.53 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: The occupation source is broader than this six-digit industry and is dominated by large telecommunications carriers.
- a: The estimate excludes tasks already automated, but public sources do not identify their current share in lens firms.
- rho: The survey is global, vendor-sponsored, and not limited to independent satellite telecommunications firms.
- rho: Reported AI projects do not establish the fraction of exposed labor actually implemented.
- e: Public company revenue mixes may not represent privately held firms.
- e: The dataset firm count is an estimate and may include establishments whose legal entity is not independently transferable.
- s5: Owner intentions are not completed transactions and are not satellite-industry-specific.
- s5: Telecom deal counts include large carriers, infrastructure assets, and non-US transactions outside the lens.
- q: Recurring revenue share is not a direct measure of retained automation benefit.
- q: Contract structures differ between fleet operators, capacity resellers, and managed-service providers.
- d5: SIA data are global and cover a broader commercial satellite industry.
- d5: Nominal revenue and subscriber counts do not directly measure constant-price, constant-quality demand for the current basket.
- o: Direct-to-device and vertically integrated constellation providers could disintermediate some resellers.
- o: The estimate does not assume that the same incumbent firm retains the customer, only that a lens-type operator remains required.

## Sources
- **S1** — [2022 NAICS 517410 Satellite Telecommunications definition](https://www.census.gov/naics/?details=517410&input=517410&year=2022) (accessed 2026-07-22): Industry boundary, service activities, and exclusions.
- **S2** — [Telecommunications occupational employment and wage estimates, May 2023](https://www.bls.gov/oes/2023/may/naics3_517000.htm) (accessed 2026-07-22): Broad telecom occupation mix used to map exposed and nonexposed work.
- **S3** — [State of AI in Telecommunications survey findings](https://blogs.nvidia.com/blog/ai-telcos-survey-2025/) (accessed 2026-07-22): Telecom AI deployment, network-operations use, productivity, and cost-impact indicators.
- **S4** — [2026 State of the Satellite Industry Report release](https://sia.org/affordability-productivity-drive-historic-satellite-industry-growth-satellite-industry-association-releases-29th-annual-state-of-the-satellite-industry-report/) (accessed 2026-07-22): Current global satellite subscriber, service-revenue, ground-network, and overall industry growth indicators.
- **S5** — [Iridium Communications 2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/1418819/000141881926000009/irdm-20251231.htm) (accessed 2026-07-22): Satellite service billing model, revenue mix, subscribers, growth, operating requirements, and competitive pricing evidence.
- **S6** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Five-year ownership-transfer intentions among US employer-business owners.
- **S7** — [Consolidated telecommunications](https://www.deloitte.com/us/en/insights/industry/technology/technology-media-and-telecom-predictions/2025/tmt-predictions-consolidated-telecommunications-ramps-up.html) (accessed 2026-07-22): Telecom transaction activity and consolidation direction.
- **S8** — [FCC Space Bureau earth-station licensing procedures](https://docs.fcc.gov/public/attachments/DA-25-875A1.pdf) (accessed 2026-07-22): Continuing licensing and operator responsibilities for satellite earth-station communications.
