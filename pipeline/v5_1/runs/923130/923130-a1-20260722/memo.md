# 923130 — Administration of Human Resource Programs (except Education, Public Health, and Veterans' Affairs Programs)

*v5.1 Stage 1 research memo. Run `923130-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** no base (evidence-first) · A — · L — · interval STRUCTURAL_OUT → HIGHEST_PRIORITY · readiness STRESS_TEST_ONLY · action EVIDENCE_FIRST

**Driver:** High-volume applications, redeterminations, records, notices, and cross-dataset checks make the administrative workflow unusually amenable to AI assistance.
**Weakness:** Government ownership eliminates the LMM acquisition, control-transfer, receipts, and commercial-retention constructs, while due process constrains automation.

## Business-model lens
- Included: U.S. federal, state, and local government establishments planning, administering, and coordinating public-assistance, social-work, welfare, Social Security, disability-insurance, Medicare, Medicaid, unemployment-insurance, workers'-compensation, food-assistance, and related human-resource programs.
- Excluded: Education, public-health, and veterans'-affairs program administration; direct operation of social-assistance services; private benefit administrators and software vendors; employment placement offices; schools, hospitals, clinics, charities, insurers, and captive units classified elsewhere; and non-control financing vehicles.
- Customer and revenue model: Government agencies determine eligibility, enroll beneficiaries, calculate and issue or oversee benefits, manage appeals, verify data, prevent improper payments, coordinate programs, and monitor providers or state partners. They are funded through appropriations and taxes rather than recurring commercial fees from external customers.
- Deviation from default lens: The default LMM outsourced-service firm lens is structurally inapplicable because Census defines this code as government establishments, the frozen dataset has no receipts concept, and no defensible firm count exists. The packet preserves the full public-program administration population to assess workflow exposure and durable need, while marking firm-transfer and commercial-retention constructs missing rather than importing private vendors from other NAICS codes.

## Executive view
Human-resource program administration is highly document-, rules-, and data-intensive, creating material AI opportunity in intake, verification, correspondence, case routing, fraud controls, and contact support. Human review, due process, vulnerable populations, legacy systems, and fragmented governance limit implementation, while the government-only classification makes private-firm transfer and commercial retention undefined.

## How AI changes the work
AI can extract evidence, check completeness, match data, summarize contacts, draft notices, answer routine questions, prioritize cases, translate communications, and flag anomalies. Complex eligibility, disability evidence, adverse actions, appeals, investigations, policy, and payment accountability require trained public officials and human review.

## Value capture
Benefits appear as lower backlog, faster decisions, improved access, fewer errors, reduced improper payments, and administrative capacity. They do not flow through market pricing or EBITDA and may be reallocated to service quality or new mandates.

## Firm availability
Census defines government establishments only, and the frozen dataset has neither receipts nor a defensible LMM count. Private technology, eligibility, claims, and contact-center vendors must be screened in their own industry codes.

## Demand durability
Aging raises retirement and Medicare workloads, while disability, unemployment, food-assistance, and welfare caseloads vary with economic conditions and policy. Simplification and self-service may reduce effort per case, but public accountability and large recurring beneficiary populations sustain the service basket.

## Risks and uncertainty
Risks include inaccurate or biased eligibility decisions, weak data, identity errors, privacy, cybersecurity, opaque models, improper denials or payments, appeals, public trust, procurement, legacy systems, fragmented federal-state responsibility, policy changes, and the structural mismatch with a private-company screen.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | — | — | MISSING | — |
| n | — | — | — | MISSING | — |
| a | 0.35 | 0.5 | 0.65 | PROXY | S2, S3, S4, S5 |
| rho | 0.22 | 0.4 | 0.58 | ESTIMATE | S3, S4, S5, S6 |
| e | — | — | — | MISSING | — |
| s5 | — | — | — | MISSING | — |
| q | — | — | — | MISSING | — |
| d5 | 0.99 | 1.07 | 1.18 | PROXY | S1, S7, S8, S9 |
| o | 0.88 | 0.96 | 0.995 | ESTIMATE | S1, S3, S4, S5 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | — | — | — | MISSING |
| F | — | — | — | MISSING |
| C | — | — | — | MISSING |
| D | 8.71 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: Eligibility interviewers are only one occupation and the BLS estimate spans government and private employers rather than NAICS 923130 alone.
- a: The frozen dataset provides no receipts denominator, so exposed work cannot be converted into a conventional private-firm labor-share opportunity.
- rho: Implementation economics differ sharply among federal entitlement systems, state-administered programs, and small local welfare offices.
- rho: Error reduction and backlog clearance are valuable but are not necessarily labor substitution or avoided hiring.
- e: Private eligibility, call-center, systems-integration, and claims-administration contractors belong to other NAICS codes.
- e: Counting agencies or local offices as firms would be a category error rather than a conservative approximation.
- s5: A contract award can transfer service delivery without transferring ownership of the government agency.
- s5: Program administration may move among agencies or government levels while public accountability remains unchanged.
- q: Avoided improper payments accrue to public budgets and program integrity, not operating profit.
- q: Administrative savings may be absorbed by backlogs, new mandates, or benefit-service improvements rather than retained by the agency.
- d5: Older-population growth does not map one-for-one to administrative workload, and SNAP and unemployment caseloads are policy- and cycle-sensitive.
- d5: The code combines programs with opposing demand trends, so one national ratio obscures substantial heterogeneity.
- o: Operational components may migrate to contractors in other industries while accountable administration remains governmental.
- o: Program simplification or automatic enrollment could remove more administrative quantity than current technology deployments suggest.

## Sources
- **S1** — [2022 NAICS Definition: 923130 Administration of Human Resource Programs](https://www.census.gov/naics/?details=923130&input=923130&year=2022) (accessed 2026-07-23): Defines government administration of public assistance, social work, welfare, Social Security, disability insurance, Medicare, unemployment insurance, and workers' compensation, with key exclusions.
- **S2** — [Occupational Employment and Wages: Eligibility Interviewers, Government Programs](https://www.bls.gov/oes/2023/may/oes434061.htm) (accessed 2026-07-23): Defines eligibility work across welfare, unemployment, Social Security, housing, and related programs and reports 150,190 workers nationally in May 2023.
- **S3** — [Federal Low-Income Programs: Use of Data to Verify Eligibility](https://www.gao.gov/products/gao-21-183) (accessed 2026-07-23): Reports agencies using more than 30 electronic data sources across six selected programs and describes integrity and beneficiary-burden benefits and challenges of data verification.
- **S4** — [Fraud and Improper Payments: Data Quality and a Skilled Workforce Are Essential for Realizing AI's Benefits](https://www.gao.gov/products/gao-26-108850) (accessed 2026-07-23): Explains that AI can assist fraud and improper-payment work but requires reliable data, skilled staff, and a human in the loop.
- **S5** — [Combating Fraud: Challenges in Federally Funded, State-Administered Programs](https://files.gao.gov/reports/GAO-26-109093/index.html) (accessed 2026-07-23): Documents state eligibility and payment decisions and constraints from weak controls, limited visibility, data and system problems, and limited program-management capacity.
- **S6** — [Federal Telework: Social Security Administration Needs a Workforce Plan](https://files.gao.gov/reports/GAO-26-107645/index.html) (accessed 2026-07-23): Documents SSA workforce and disability-backlog pressures and reports initial-claim processing time improving from 240 to 209 days during 2025 after prior deterioration.
- **S7** — [Older Adults Outnumber Children in 11 States and Nearly Half of U.S. Counties](https://www.census.gov/newsroom/press-releases/2025/older-adults-outnumber-children.html) (accessed 2026-07-23): Reports the U.S. population age 65 and older grew 3.1% to 61.2 million from 2023 to 2024, increasing aging-related program demand.
- **S8** — [SNAP Data Tables](https://www.fns.usda.gov/pd/supplemental-nutrition-assistance-program-snap) (accessed 2026-07-23): Provides national and state participation, household, benefit, and cost data through fiscal 2025 and monthly data into fiscal 2026, evidencing a continuing administrative workload.
- **S9** — [The Employment Situation — June 2026](https://www.bls.gov/news.release/pdf/empsit.pdf) (accessed 2026-07-23): Reports a 4.2% unemployment rate and 7.1 million unemployed people in June 2026, anchoring current unemployment-insurance workload context.
