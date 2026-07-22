# 812910 — Pet Care (except Veterinary) Services

*v5.1 Stage 1 research memo. Run `812910-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** CONDITIONAL · A 6.23 · L 2.16 · interval STRUCTURAL_OUT → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** The need for trusted, accountable physical care of animals in repeat local relationships.
**Weakness:** A heterogeneous industry population and a relatively small administrative task share limit both eligible firm coverage and the scale of incremental automation.

## Business-model lens
- Included: U.S. multi-employee, facility-based pet boarding, daycare, and grooming operators, including businesses combining those services with supervised exercise, feeding, sanitation, monitoring, and non-veterinary ancillary care.
- Excluded: Veterinary services; pet retail and manufacturing; animal shelters; solo or primarily mobile pet sitting, dog walking, and training; captive services; and firms outside the lower-middle-market operating-company population.
- Customer and revenue model: Consumer-paid boarding nights, daycare visits or packages, grooming appointments, memberships, and ancillary services delivered from staffed facilities, with repeat use and local customer relationships but generally limited contractual commitment.
- Deviation from default lens: The official code combines facility-based boarding, daycare, and grooming with solo or mobile sitting, walking, and training. The lens is narrowed to multi-employee facility-based operators solely to obtain a coherent asset, staffing, customer, and transfer model; the excluded activities have materially different economics and operating obligations.

## Executive view
The narrowed segment is a repeat local service built around staffed facilities and the accountable physical care of animals. Its operating obligation is durable, but the amount of work susceptible to incremental AI is modest and concentrated in administration, planning, communication, and observation rather than direct care.

## How AI changes the work
Near-term uses include booking and capacity management, intake and record review, reminders, customer messaging, marketing, staff scheduling, report generation, and triage of camera or sensor alerts. Feeding, cleaning, exercise, animal handling, grooming, behavioral judgment, and emergency response remain human and physical, with safety and liability limiting unattended automation.

## Value capture
Packages, memberships, appointments, and service differentiation can preserve some gains as capacity, convenience, or quality. Local competition and household price sensitivity constrain pricing, while high direct-care labor and staffing expectations mean administrative efficiencies affect only part of the cost base.

## Firm availability
Facility operators can possess transferable staff, systems, customer records, equipment, and premises rights, but the NAICS code also contains many solo and mobile businesses that do not share that model. Even after narrowing, founder or groomer dependence, leases, permitting, reputation, and incomplete records reduce the population of actionable stand-alone companies.

## Demand durability
Pet-care employment and broader personal-service output projections support continued demand, and pet owners need trusted care during travel, work, and routine grooming cycles. Demand remains exposed to household budgets, remote-work patterns, informal substitutes, service frequency, and local capacity additions.

## Risks and uncertainty
The central uncertainty is segmentation: public evidence rarely separates facility boarding, daycare, and grooming from sitting, walking, training, self-employment, or unrelated personal services. Other uncertainties include customer discretionary spending, local regulation and leases, staff availability, animal-safety liability, owner or groomer dependence, and the absence of representative AI realization data.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.4621 | — | OBSERVED | — |
| n | — | 61 | — | ESTIMATE | — |
| a | 0.12 | 0.22 | 0.34 | PROXY | S2, S3 |
| rho | 0.35 | 0.53 | 0.68 | ESTIMATE | S3 |
| e | 0.38 | 0.58 | 0.74 | ESTIMATE | S1, S3 |
| s5 | 0.07 | 0.13 | 0.21 | PROXY | S5 |
| q | 0.4 | 0.56 | 0.71 | ESTIMATE | S3 |
| d5 | 0.98 | 1.1 | 1.22 | PROXY | S3, S4 |
| o | 0.88 | 0.95 | 0.99 | ESTIMATE | S1, S3 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.78 | 2.16 | 4.27 | ESTIMATE |
| F | 1.55 | 2.77 | 3.78 | ESTIMATE |
| C | 8.00 | 10.00 | 10.00 | ESTIMATE |
| D | 8.62 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: The occupational industry table covers broader NAICS 812900 rather than the exact code or narrowed lens.
- a: Task feasibility does not establish adoption, safe unattended use around animals, or realized labor reduction.
- rho: No representative exact-code AI adoption and realization study was located.
- rho: The estimate assumes ordinary business software exists but does not treat basic digitization as incremental AI realization.
- e: Public exact-code data do not cleanly separate the narrowed facility-based segment.
- e: Customer goodwill may attach to individual groomers or founders rather than the business entity.
- s5: The proxy is cross-industry and measures intentions, not completed transactions.
- s5: Small private transactions and transfers are often not publicly reported.
- q: No exact-segment evidence directly measures retention of AI-enabled economics.
- q: Boarding, daycare, and grooming differ in capacity constraints, pricing, and labor intensity.
- d5: Neither BLS series isolates facility-based boarding, daycare, and grooming.
- d5: Employment growth, real output, and unit demand are related but not interchangeable.
- o: The strength of the obligation differs between overnight boarding, routine daycare, and elective grooming.
- o: A high value reflects the persistence of physical care, not nondiscretionary spending or guaranteed customer frequency.

## Sources
- **S1** — [2022 NAICS definition: 812910 Pet Care (except Veterinary) Services](https://www.census.gov/naics/?details=812910&input=812910&year=2022) (accessed 2026-07-22): Defines the exact code as boarding, grooming, sitting, walking, and training services for pets other than veterinary care, establishing its heterogeneous activity mix.
- **S2** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 812900](https://www.bls.gov/oes/2023/may/naics4_812900.htm) (accessed 2026-07-22): Shows animal care and service workers as a large share of employment in the broader other-personal-services industry.
- **S3** — [BLS Occupational Outlook Handbook: Animal Care and Service Workers](https://www.bls.gov/ooh/personal-care-and-service/animal-care-and-service-workers.htm) (accessed 2026-07-22): Details physical care duties, work settings, injury and scheduling conditions, and projected 2024-2034 employment growth for animal care and service workers.
- **S4** — [BLS industry employment and output projections](https://www.bls.gov/emp/tables/industry-employment-and-output.htm) (accessed 2026-07-22): Reports projected 2024-2034 employment and real output for the broader NAICS 812900 industry.
- **S5** — [Gallup: Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Reports national employer-business-owner intentions to sell or transfer within five years and the gap in succession preparation.
