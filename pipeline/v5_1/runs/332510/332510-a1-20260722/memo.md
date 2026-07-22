# 332510 — Hardware Manufacturing

*v5.1 Stage 1 research memo. Run `332510-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** LOW_PRIORITY · A 5.65 · L 1.00 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Recurring customer drawings and qualification create sticky programs with improvable quoting, planning, and quality workflows.
**Weakness:** Most labor is physical and domestic hardware production has shown sustained weakness, limiting both automation scope and demand confidence.

## Business-model lens
- Included: Independent lower-middle-market manufacturers that repeatedly produce customer-designed or private-label hinges, handles, keys, locks, and related metal hardware for external OEM, distributor, or building-products customers.
- Excluded: Manufacturers selling only their own standardized branded hardware, captive plants, pure distributors, shell entities, non-control financing vehicles, and firms outside the normalized EBITDA band.
- Customer and revenue model: Customers buy recurring production runs under drawings, tooling, finish, quality, packaging, and delivery specifications, typically through purchase orders, blanket agreements, or annual supply contracts.
- Deviation from default lens: The code includes both proprietary standardized products and customer-specific contract production. The lens retains recurring outsourced manufacturing so eligibility and value capture describe one coherent model.

## Executive view
The coherent opportunity is the subset of hardware manufacturers producing recurring customer-specific or private-label programs. Labor intensity is meaningful, but most plant labor is physical and recent domestic hardware output has been weak, so the AI case depends on information workflows rather than wholesale factory labor replacement.

## How AI changes the work
AI can accelerate quoting, drawing and specification review, production planning, purchasing, quality-document preparation, inspection analytics, maintenance triage, and customer service. Machining, stamping, finishing, assembly, material handling, and physical inspection execution require equipment and remain less directly exposed.

## Value capture
Savings tied to delivery reliability, scrap reduction, and quality can persist where tooling and qualification create switching cost. OEM and distributor procurement, annual bids, cost models, and metal-index clauses make visible labor savings vulnerable to repricing.

## Firm availability
Founder-owned plants may create succession opportunities, but only a minority are likely to meet the outsourced-service lens. Transferability depends on customer diversification, tooling rights, equipment condition, environmental compliance, workforce depth, and reduced owner dependence.

## Demand durability
Physical hardware remains necessary, but domestic volume is cyclical and exposed to imports, construction weakness, standardization, and inventory corrections. Specialized qualified components should be more durable than commodity catalog items.

## Risks and uncertainty
The case fails if diligence finds a branded product company rather than an outsourced supplier, heavily manual workflows that need capital equipment rather than AI, concentrated bid-driven customers, obsolete machines, or sustained domestic share loss. Product mix and tooling ownership are decisive.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.2484 | — | OBSERVED | — |
| n | — | 156 | — | ESTIMATE | — |
| a | 0.13 | 0.21 | 0.3 | PROXY | S2, S3 |
| rho | 0.32 | 0.48 | 0.65 | ESTIMATE | S2 |
| e | 0.06 | 0.14 | 0.27 | ESTIMATE | S1 |
| s5 | 0.08 | 0.17 | 0.28 | PROXY | S4 |
| q | 0.31 | 0.49 | 0.68 | ESTIMATE | — |
| d5 | 0.79 | 0.96 | 1.11 | PROXY | S5, S6 |
| o | 0.91 | 0.97 | 0.995 | ESTIMATE | S1, S2 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.41 | 1.00 | 1.94 | ESTIMATE |
| F | 0.90 | 2.49 | 4.10 | ESTIMATE |
| C | 6.20 | 9.80 | 10.00 | ESTIMATE |
| D | 7.19 | 9.31 | 10.00 | ESTIMATE |

## Caveats
- a: The occupation data cover NAICS 332 rather than 332510 or the outsourced subset.
- a: ILO exposure is technical potential rather than observed substitution.
- a: Existing CNC, stamping, and conventional automation are excluded from the remaining opportunity.
- rho: No source measures AI implementation in eligible hardware contract manufacturers.
- rho: Small plants with paper travelers and disconnected machines may implement much more slowly.
- e: The provided firm count is margin-bridged and estimated before applying the outsourced-service lens.
- e: Private-label sales do not always constitute customer-controlled outsourced manufacturing.
- s5: Owner-age data are cross-industry, based on 2018, and count responding owners rather than firms.
- s5: Age, intent to sell, and a completed qualifying transfer are different quantities.
- q: No public contract sample establishes pass-through behavior for the eligible population.
- q: Commodity hardware and concentrated customers can make retention materially lower.
- d5: Industrial production includes proprietary and commodity hardware outside the lens.
- d5: Nominal construction spending is not constant-price demand and covers many inputs besides hardware.
- d5: Product mix can diverge materially between residential, commercial, institutional, and OEM hardware.
- o: Operator requirement can persist while work shifts offshore or to a larger supplier.
- o: Demand elimination and import substitution are reflected primarily in d5, not this value.

## Sources
- **S1** — [NAICS Definition: Hardware Manufacturing](https://www.census.gov/naics/?details=33251&input=33251&year=2017) (accessed 2026-07-22): Census defines 332510 as manufacturing metal hardware such as hinges, handles, keys, and locks other than coin-operated and time locks.
- **S2** — [Fabricated Metal Product Manufacturing: NAICS 332](https://www.bls.gov/iag/tgs/iag332.htm) (accessed 2026-07-22): BLS reports 2025 fabricated-metal employment of 56,060 press operators, 67,090 production supervisors, 101,640 machinists, 125,250 team assemblers, and 112,520 welders; it also reports 2024 output fell 4.0%.
- **S3** — [Generative AI and Jobs: Policies to Manage the Transition](https://www.ilo.org/sites/default/files/2024-08/GenAI%20and%20Jobs_Policy%20Brief_ILO.pdf) (accessed 2026-07-22): ILO reports 24% of clerical tasks at high automation exposure and 58% at medium exposure, while other occupational groups have only 1% to 4% highly exposed and no more than 25% medium-exposed tasks.
- **S4** — [Business Owners' Ages](https://www.census.gov/content/dam/Census/library/visualizations/2020/comm/business-owners-ages.pdf) (accessed 2026-07-22): Census reports that 51% of responding owners of employer businesses were age 55 or older, based on the 2019 Annual Business Survey for data year 2018.
- **S5** — [Industrial Production: Hardware Manufacturing](https://fred.stlouisfed.org/data/IPG3325NQ) (accessed 2026-07-22): The Federal Reserve industrial-production series reported a hardware index of 102.3244 in 2019 Q4 and 78.7915 in 2025 Q4, with 2017 equal to 100.
- **S6** — [Monthly Construction Spending, May 2026](https://www.census.gov/construction/c30/current/index.html) (accessed 2026-07-22): Census reports May 2026 construction spending at a $2,210.2 billion annual rate, 1.5% below May 2025, with private residential spending at $930.2 billion and private nonresidential spending at $738.7 billion.
