# 112330 — Turkey Production

*v5.1 Stage 1 research memo. Run `112330-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** no base (evidence-first) · A — · L — · interval STRUCTURAL_OUT → HIGHEST_PRIORITY · readiness STRESS_TEST_ONLY · action EVIDENCE_FIRST

**Driver:** Structured poultry houses and repeated flock cycles create practical monitoring and administrative automation opportunities in a recurring contracted service.
**Weakness:** Integrator control, declining turkey use, disease exposure, and uncertain contract transferability sharply limit grower independence and value retention.

## Business-model lens
- Included: US lower-middle-market independent turkey growers and contract growers that repeatedly raise turkeys for meat or egg production for external integrators, processors, cooperatives, or buyers while retaining accountable responsibility for houses, equipment, labor, utilities, daily husbandry, welfare, biosecurity, environmental compliance, and flock performance.
- Excluded: Shells, captive integrator-owned farms, non-control financing vehicles, passive real-estate or poultry-house lessors, hobby and backyard flocks, poultry hatcheries, slaughter and processing plants without qualifying grow-out operations, other poultry species, farms outside the screened EBITDA band, and operations without transferable customer or production responsibility are excluded.
- Customer and revenue model: Contract growers receive recurring per-flock or performance-linked fees from integrators that commonly own the birds and provide feed, veterinary support, transport, and technical standards, while growers provide houses, equipment, labor, utilities, and husbandry. Independent growers instead own production inputs and sell live birds or eggs under marketing arrangements or spot conditions.
- Deviation from default lens: none

## Executive view
Turkey production is a recurring but tightly coordinated outsourced grow-out service for many farms. The controlled poultry-house environment supports AI-assisted monitoring, forecasting, recordkeeping, and anomaly detection, yet integrators hold substantial control over birds, inputs, protocols, placements, and compensation. The missing firm-count input, declining national use, HPAI risk, and contract assignability are more consequential than the technical feasibility of monitoring tools.

## How AI changes the work
Machine vision, audio, sensors, and mobile robots can reduce routine flock checks, identify abnormal behavior or mortality, monitor litter and distribution, forecast performance, and automate records and alerts. Existing automated feeding, watering, and ventilation are not new opportunity. Humans remain essential for verification, welfare decisions, repairs, cleanout, biosecurity, loading, treatment support, and emergency response.

## Value capture
Contract growers may keep savings under a fixed flock fee or improve performance measures, but integrators can reset fees, standards, placements, required capital, and contract terms. Specialized houses and limited local processor alternatives weaken grower bargaining. Independent producers have more upside but also retain feed, bird, disease, marketing, and price risk.

## Firm availability
The sector contains independent growers, contract growers, and integrator-owned farms; only the first two can satisfy the external-supplier lens, and not all have assignable contracts or qualifying economics. Broader poultry farms are overwhelmingly family-owned but have a younger producer profile than agriculture overall, moderating near-term succession. A facility sale without continued placements is not a transferable operating business.

## Demand durability
Turkey remains an established protein across deli, retail, foodservice, ingredients, and holidays, but national use and per-capita disappearance have trended down. Disease has also reduced supply, creating uncertain recovery potential. Future grower quantity depends heavily on integrator placements, exports, relative protein prices, and HPAI rather than individual farm marketing.

## Risks and uncertainty
The principal risks are HPAI, biosecurity failure, flock depopulation, integrator concentration, nonrenewal, placement cuts, contract nonassignability, required house upgrades, debt, utility and litter costs, animal welfare, environmental permits, heat and ventilation failure, cybersecurity, and missing eligible-firm data. A single disease event or lost integrator relationship can overwhelm labor savings.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | — | — | MISSING | — |
| n | — | — | — | MISSING | — |
| a | 0.2 | 0.34 | 0.49 | PROXY | S5, S6, S8 |
| rho | 0.26 | 0.45 | 0.63 | PROXY | S4, S5, S6, S7, S8 |
| e | 0.45 | 0.62 | 0.78 | ESTIMATE | S1, S2, S4 |
| s5 | 0.12 | 0.22 | 0.34 | PROXY | S2 |
| q | 0.22 | 0.36 | 0.52 | PROXY | S4, S9 |
| d5 | 0.78 | 0.87 | 0.98 | PROXY | S3, S7 |
| o | 0.85 | 0.92 | 0.97 | ESTIMATE | S2, S4, S5, S6, S7 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | — | — | — | MISSING |
| F | — | — | — | MISSING |
| C | 4.40 | 7.20 | 10.00 | PROXY |
| D | 6.63 | 8.00 | 9.51 | ESTIMATE |

## Caveats
- a: No exact turkey-farm occupation or task distribution was found, and the provided labor-share input is missing.
- a: The most specific AI demonstrations concern broilers, which differ from turkeys in size, behavior, stocking, and production cycle.
- a: Many routine environmental and feeding functions are already automated and are excluded from current unautomated exposure.
- rho: Research prototypes are not representative commercial adoption evidence.
- rho: Integrators can enable standardization but can also block tools that do not fit their flock-management and data policies.
- rho: Disease surveillance and indemnity rules increase the cost of relying on imperfect automated judgments.
- e: The provided lower-middle-market firm count is missing and must not be inferred from operation or bird counts.
- e: A contract grower can be economically dependent on one integrator while still legally independent.
- e: Multiple houses, farms, and related real-estate entities may belong to one operating family or contractor.
- s5: The source combines all poultry and egg farms rather than turkey production alone.
- s5: Producer data include up to four people per farm and therefore do not measure farm-level transfer timing.
- s5: A house or land sale can occur without transfer of a viable grower contract or operating company.
- q: Current turkey contracts are private and may differ materially from public broiler evidence.
- q: Lower labor need may not raise compensation if the integrator fixes fees or requires the technology.
- q: Independent and contract-grower commercial retention should not be blended without firm-level contract review.
- d5: Recent production and use reflect HPAI as well as underlying demand, and the two effects cannot be cleanly separated from aggregate data.
- d5: National output does not identify contract-grower versus integrator-owned quantity.
- d5: Breeding and egg production may follow different quantity dynamics from meat grow-out.
- o: The operator can change without changing national turkey quantity, especially when an integrator internalizes or reallocates production.
- o: Automated monitoring can centralize oversight across many houses while local physical accountability remains.
- o: The external-supplier share is not publicly measured at the exact eligible-firm level.

## Sources
- **S1** — [2022 NAICS Definition: 112330 Turkey Production](https://www.census.gov/naics/?details=112&input=112&year=2022) (accessed 2026-07-22): Defines the industry as establishments primarily raising turkeys for meat or egg production and distinguishes poultry hatcheries and other poultry industries.
- **S2** — [2022 Census of Agriculture Highlights: Poultry and Egg Production](https://data.nass.usda.gov/Publications/Highlights/2024/Census22_HL_Poultry.pdf) (accessed 2026-07-22): Reports poultry producer age, family ownership, internet access, farm economics, and that turkey contractees represented 36 percent of farms with turkeys but 75 percent of turkey production in 2022.
- **S3** — [Turkey Sector: Background and Statistics](https://www.ers.usda.gov/newsroom/trending-topics/turkey-sector-background-statistics) (accessed 2026-07-22): Provides recent turkey production value, meat output, domestic disappearance, per-capita disappearance, exports, wholesale prices, and projections, including declines through 2024 and 2025.
- **S4** — [Marketing and Production Contracts Are Widely Used in U.S. Agriculture](https://www.ers.usda.gov/amber-waves/2019/july/marketing-and-production-contracts-are-widely-used-in-u-s-agriculture) (accessed 2026-07-22): Explains that most poultry is produced under contract or on processor-owned farms and defines how production contracts allocate bird ownership, inputs, technical guidance, grower service, and fees.
- **S5** — [Automatic Monitoring of Poultry Behavior for Early Disease Detection](https://www.ars.usda.gov/research/publications/publication/?seqNo115=397940) (accessed 2026-07-22): Reports USDA proof-of-concept that machine vision can automatically monitor broiler behavior and support early detection of sick or diseased birds.
- **S6** — [Poultry Caretaker Robot To Improve Animal Well-Being](https://www.nal.usda.gov/research-tools/food-safety-research-projects/poultry-caretaker-robot-improve-animal-well-being) (accessed 2026-07-22): Describes USDA-supported development of autonomous poultry-house navigation, flock stimulation, litter interaction, mortality identification, obstacle avoidance, and route planning.
- **S7** — [APHIS Updates Policy To Enhance Surveillance of Turkey Flocks](https://www.aphis.usda.gov/news/agency-announcements/aphis-updates-policy-enhance-surveillance-turkey-flocks-highly-pathogenic) (accessed 2026-07-22): Documents enhanced HPAI monitoring, isolation, clinical observation, pre-movement testing, affected commercial turkey premises, and continued biosecurity duties.
- **S8** — [HPAI Poultry Biosecurity Assessments](https://www.aphis.usda.gov/livestock-poultry-disease/avian/avian-influenza/hpai-poultry/biosecurity-assessments) (accessed 2026-07-22): Explains structural and operational biosecurity, mandatory audits before eligible restocking in affected settings, farm practices, wildlife risks, and meat-turkey facility thresholds.
- **S9** — [Fees Paid to Growers for Raising Broiler Chickens Varied Widely in 2020](https://www-tx.ers.usda.gov/data-products/charts-of-note/104642) (accessed 2026-07-22): Provides a broiler proxy for production-contract economics, including integrator and grower responsibilities, performance-linked compensation, and wide grower-fee dispersion.
