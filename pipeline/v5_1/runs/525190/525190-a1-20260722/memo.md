# 525190 — Other Insurance Funds

*v5.1 Stage 1 research memo. Run `525190-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** no base (evidence-first) · A — · L — · interval STRUCTURAL_OUT → HIGHEST_PRIORITY · readiness STRESS_TEST_ONLY · action EVIDENCE_FIRST

**Driver:** The official NAICS boundary cleanly separates captive insurance funds from fee-based operating service providers.
**Weakness:** No establishment-level business register was available to test for rare miscoded or hybrid operators, so the conclusion relies on the official industry definition rather than an empirical enumeration.

## Business-model lens
- Included: Potentially included only if an establishment correctly classified in NAICS 525190 supplies recurring outsourced services to unrelated external customers. The official definition identifies no such activity: this industry consists of legal entities organized to provide insurance exclusively for a sponsor, firm, employees, or members.
- Excluded: The defined captive or member-serving insurance-fund vehicles are excluded because they do not sell outsourced services to external customers. Fee- or contract-based insurance carriers, third-party insurance administrators, and portfolio managers are also excluded because Census classifies them in NAICS 5241, 524292, and 523920, respectively.
- Customer and revenue model: The classified entity is a fund or plan serving its sponsor, firm, employees, or members and earns property income rather than revenue from selling services. Any external fee revenue belongs to a differently classified carrier, administrator, or portfolio manager.
- Deviation from default lens: none

## Executive view
NAICS 525190 is a vehicle category, not a recurring outsourced-service industry. Census defines it as insurance funds serving only a sponsor, firm, employees, or members and explicitly routes fee-earning carriers, administrators, and portfolio managers elsewhere. Under the frozen lens, the eligible establishment share is therefore structurally zero and the remaining operating primitives are undefined.

## How AI changes the work
Claims administration, reporting, member communications, and investment operations may contain automatable work, but those activities are generally performed by sponsors or separately classified service providers. Transferring their automation economics into 525190 would conflate a fund with its vendors.

## Value capture
The classified entities earn property income and provide benefits rather than selling services for fees. There is therefore no in-code customer-service revenue base against which to estimate retained AI benefit.

## Firm availability
The supplied LMM firm-count anchor is missing, and the official classification indicates little or no employment in fund vehicles. More importantly, the code definition supplies no qualifying external-service firms; vendors that could be acquisition targets reside in other industries.

## Demand durability
Insurance needs and sponsor obligations may persist, but that durability belongs to the fund or to services purchased from other industries. It does not establish recurring external-customer demand inside 525190.

## Risks and uncertainty
The central risk is classification leakage: commercial administrators, carriers, or asset managers may be casually described as insurance-fund businesses even though Census assigns them elsewhere. Any establishment-level exception would need verification before changing the structural conclusion.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | — | — | MISSING | — |
| n | — | — | — | MISSING | — |
| a | — | — | — | MISSING | — |
| rho | — | — | — | MISSING | — |
| e | 0 | 0 | 0 | OBSERVED | S1 |
| s5 | — | — | — | MISSING | — |
| q | — | — | — | MISSING | — |
| d5 | — | — | — | MISSING | — |
| o | — | — | — | MISSING | — |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | — | — | — | MISSING |
| F | — | — | — | MISSING |
| C | — | — | — | MISSING |
| D | — | — | — | MISSING |

## Caveats
- a: Automation potential at separately classified administrators, carriers, or portfolio managers is not evidence for this industry under the frozen lens.
- rho: Adoption evidence from insurance administrators or portfolio managers would require an explicit cross-industry bridge and would not cure the lens mismatch.
- e: This is a taxonomy-based structural zero for the stated lens, not a claim that insurance-fund ecosystems have no service providers.
- s5: Fund or plan persistence is not equivalent to operating-company survival.
- q: Economics of third-party administrators and carriers belong to other NAICS industries.
- d5: Persistent demand for insurance protection does not establish demand for an in-scope service firm in this code.
- o: Governance of a sponsor-controlled fund is not a proxy for acquiring and operating an independent service business.

## Sources
- **S1** — [NAICS Sector 52: Finance and Insurance](https://www.census.gov/naics/resources/archives/sect52.html) (accessed 2026-07-22): Official definitions for subsector 525 and industry 525190, including the absence of service-sale revenue and cross-references for fee-based carriers, third-party administrators, and portfolio managers.
- **S2** — [Exempt Organization Sample Questions: Voluntary Employee Beneficiary Associations](https://www.irs.gov/charities-non-profits/other-non-profits/exempt-organization-sample-questions-voluntary-employee-beneficiary-associations-veba) (accessed 2026-07-22): Adjacent context on member-benefit entities, including membership, control, fiduciary governance, and benefit restrictions; it is not used to quantify a primitive.
