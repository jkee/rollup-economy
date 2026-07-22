# 531130 — Lessors of Miniwarehouses and Self-Storage Units

*v5.1 Stage 1 research memo. Run `531130-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** CONDITIONAL · A 6.18 · L 2.17 · interval STRUCTURAL_OUT → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Recurring fixed-price rent and standardized digital workflows create a practical route to retain some centralized operating efficiencies.
**Weakness:** The business is already labor-light and digitally self-served, leaving a limited unautomated wage base while local supply can absorb savings through price competition.

## Business-model lens
- Included: US lower-middle-market owner-operators that repeatedly rent secure rooms, compartments, containers, lockers, or outdoor space for customers to store and retrieve their own goods.
- Excluded: Public and contract warehousing, coin- or card-operated lockers, passive shells, captive internal storage, non-control financing vehicles, and firms outside the lower-middle-market band.
- Customer and revenue model: Households and businesses usually pay recurring unit rent, often month to month, with ancillary administrative fees, merchandise, and tenant-protection or insurance revenue.
- Deviation from default lens: none

## Executive view
Self-storage combines recurring property rent with a lean operating model. AI can improve centralized sales, service, collections, marketing, and pricing, but extensive digital self-service and low payroll intensity limit the remaining labor pool.

## How AI changes the work
AI can answer inquiries, recommend unit sizes, draft and route customer communications, predict churn and delinquency, optimize promotions, flag security anomalies, summarize incidents, and coordinate vendors. Physical maintenance, access exceptions, compliance, and lien decisions remain accountable work.

## Value capture
Space is generally rented for a recurring fixed price rather than billed by labor hour, allowing some productivity gains to remain with the operator. Local competition and excess supply can force savings into lower move-in rates, discounts, and higher marketing spend.

## Firm availability
The code aligns closely with the lens and the market remains fragmented, but legal-entity counts can overstate transferable operating firms. Public REIT acquisitions demonstrate an active buyer channel without establishing the independent-firm transfer rate.

## Demand durability
The need for secure flexible space persists, and many tenants stay beyond a year. Demand is locally cyclical, recent public-company evidence shows softness in some markets, and new supply can impair occupancy even when national use remains stable.

## Risks and uncertainty
Key risks are already-automated workflows, weak incremental labor savings, local oversupply, rate transparency, customer-acquisition costs, property tax and insurance inflation, lien-law compliance, cybersecurity, security losses, and a firm count distorted by separate property entities.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1673 | — | OBSERVED | — |
| n | — | 43 | — | ESTIMATE | — |
| a | 0.32 | 0.5 | 0.68 | PROXY | S2, S4 |
| rho | 0.4 | 0.65 | 0.82 | PROXY | S2 |
| e | 0.7 | 0.85 | 0.95 | ESTIMATE | S1, S2 |
| s5 | 0.08 | 0.18 | 0.3 | ESTIMATE | S2 |
| q | 0.45 | 0.65 | 0.8 | ESTIMATE | S2, S3 |
| d5 | 0.9 | 1.03 | 1.18 | PROXY | S2, S3 |
| o | 0.78 | 0.9 | 0.97 | ESTIMATE | S2, S4 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.86 | 2.17 | 3.73 | PROXY |
| F | 1.97 | 3.26 | 4.16 | ESTIMATE |
| C | 9.00 | 10.00 | 10.00 | ESTIMATE |
| D | 7.02 | 9.27 | 10.00 | ESTIMATE |

## Caveats
- a: O*NET covers property managers across residential and commercial assets rather than self-storage employees.
- a: The task sources do not provide self-storage task-time or wage shares.
- a: Public Storage is a technology leader, so its current automation baseline may exceed that of lower-middle-market operators.
- rho: Digital rental completion is not itself AI implementation.
- rho: A large public REIT is not representative of independent lower-middle-market technology budgets.
- rho: Lien, eviction, access, and consumer-protection rules create state-specific exception work.
- e: Facility, establishment, property-owning entity, and operating company counts can differ materially.
- e: The supplied firm count is margin-bridged and may be distorted by real-estate ownership structures.
- e: Public-company square-foot ownership does not measure the share of firms eligible in the supplied band.
- s5: Public Storage's acquisitions are not an industry-wide deal census and skew toward institutionally suitable assets.
- s5: Portfolio transactions can include many facilities but only one control transfer.
- s5: No observed owner-age or succession distribution is available for the target population.
- q: Public REIT pricing systems and brand advantages may overstate independent operators' retention.
- q: Local supply and customer-acquisition spending can dissipate labor savings.
- q: No source directly observes gross-benefit pass-through after automation.
- d5: Revenue and occupancy do not directly measure constant-price, constant-quality service quantity.
- d5: Public portfolios may differ from lower-middle-market facilities by geography, quality, and marketing scale.
- d5: Demand is local and can diverge sharply with migration, housing turnover, and new construction.
- o: Operator requirement varies between simple drive-up sites and climate-controlled multistory facilities.
- o: Remote management may shift work to centralized or outsourced staff rather than eliminate it.
- o: Future access-control and computer-vision systems could reduce the accountable human share further.

## Sources
- **S1** — [2022 NAICS Definition: 531130 Lessors of Miniwarehouses and Self-Storage Units](https://www.census.gov/naics/?details=531130&input=531130&year=2022) (accessed 2026-07-22): Defines the industry as establishments renting secure rooms, compartments, lockers, containers, or outdoor space where clients store and retrieve their goods, and distinguishes public warehousing and coin-operated lockers.
- **S2** — [Public Storage 2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/1393311/000162828026007696/psa-20251231.htm) (accessed 2026-07-22): Reports nearly three quarters of 2025 rentals completed through eRental or Rent by Phone; centralized digital access, payment, pricing, and marketing; fragmented ownership; softer 2025 same-store demand; and 87 facilities acquired in 2025.
- **S3** — [National Storage Affiliates Trust 2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/1031235/000119312526124051/self-20251231.htm) (accessed 2026-07-22): Reports 93.0% average same-store occupancy, 1.4% annual same-store revenue growth, approximately 3.5 years average tenant stay, annual existing-tenant rate management, online competitor-price collection, and continued physical operating expenses.
- **S4** — [O*NET OnLine: Property, Real Estate, and Community Association Managers](https://www.onetonline.org/link/summary/11-9141.00) (accessed 2026-07-22): Lists budgeting, rent collection, records, marketing, tenant communication, complaint resolution, contract coordination, inspections, maintenance, and compliance tasks used to bound the administrative and physical workflow mix.
