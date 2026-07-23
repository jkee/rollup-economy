# 923140 — Administration of Veterans' Affairs

*v5.1 Stage 1 research memo. Run `923140-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** no base (evidence-first) · A — · L — · interval STRUCTURAL_OUT → HIGHEST_PRIORITY · readiness STRESS_TEST_ONLY · action EVIDENCE_FIRST

**Driver:** Document-heavy benefits administration and routine veteran inquiries create a large, explicitly targeted AI automation opportunity.
**Weakness:** Government-only classification leaves no transferable LMM firm, commercial contract, or owner-retained benefit under the frozen screen.

## Business-model lens
- Included: No qualifying lower-middle-market outsourced-service firms were identified; the correctly classified US population consists of government establishments administering assistance, training, counseling, and related services for veterans and their families or survivors.
- Excluded: Federal, state, and local veterans' affairs agencies and offices, captive government units, hospitals and direct health-care providers, private veterans-service organizations, claims consultants, benefits software vendors, government contractors classified elsewhere, shells, and non-control financing vehicles.
- Customer and revenue model: Veterans' affairs offices administer statutory public programs funded by governmental appropriations rather than recurring fees paid by external commercial customers; veterans and dependents are beneficiaries, not customers under an outsourced-service contract.
- Deviation from default lens: none

## Executive view
Veterans' affairs administration has a large AI-exposed claims, document, eligibility, and inquiry workload, with existing automation and an explicit VA scaling strategy. It remains a government function rather than a transferable outsourced-service firm population, so commercial eligibility, control transfer, and value capture are undefined under the frozen lens.

## How AI changes the work
AI can automate intake, classification, extraction, summarization, routing, preliminary eligibility support, routine inquiries, form completion, correspondence, and information retrieval. Complex adjudication, appeals, counseling, fraud review, rights explanations, privacy, and consequential final decisions require trained and accountable human review.

## Value capture
There is no commercial customer contract or price-renewal mechanism in the classified population. Efficiency may reduce backlog, improve speed, or free appropriated capacity, but those public outcomes cannot be translated into retained operator margin.

## Firm availability
The official population consists of government offices administering veterans' programs. The LMM firm count is missing, agency and leadership changes are not control transfers, and private claims, consulting, software, or service providers are classified elsewhere.

## Demand durability
Disability-claims intake and beneficiary volumes demonstrate substantial current need, with recent claims growth supporting a modest-growth base case. PACT-related surges may normalize, while aging, case complexity, statutory changes, survivors, education, rehabilitation, and counseling can sustain administrative workload.

## Risks and uncertainty
Operational risks include inaccurate or opaque decisions, automation bias, privacy and cybersecurity, fraud, poor legacy integration, weak training and change management, appeals and due-process failures, procurement delays, and the gap between ambitious strategy and production outcomes. The investment lens is empty by definition.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | — | — | MISSING | — |
| n | — | — | — | MISSING | — |
| a | 0.58 | 0.72 | 0.84 | PROXY | S2, S3 |
| rho | 0.42 | 0.6 | 0.75 | PROXY | S3, S4 |
| e | — | — | — | MISSING | — |
| s5 | — | — | — | MISSING | — |
| q | — | — | — | MISSING | — |
| d5 | 0.98 | 1.08 | 1.2 | PROXY | S4, S5 |
| o | 0.82 | 0.9 | 0.97 | ESTIMATE | — |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | — | — | — | MISSING |
| F | — | — | — | MISSING |
| C | — | — | — | MISSING |
| D | 8.04 | 9.72 | 10.00 | ESTIMATE |

## Caveats
- a: O*NET's government-program occupation is broader than veterans' affairs and omits many professional and managerial roles.
- a: VA strategy statements identify possible workflows but do not report wage-weighted exposure or verified avoided hours for this NAICS code.
- a: The frozen labor-share input is missing because government activity has no comparable receipts denominator.
- rho: Strategic plans and pilots are not equivalent to sustained production adoption or avoided hiring.
- rho: GAO identifies planning, training, exam-quality, transparency, and misuse-detection weaknesses.
- rho: Implementation is likely to differ sharply between routine transactions and high-impact adjudication.
- e: The official definition identifies government establishments rather than private firms.
- e: Claims vendors, software providers, and veterans-service organizations belong outside this government NAICS population.
- e: The frozen LMM firm-count input is also missing.
- s5: Leadership turnover and contract recompetes are not control transactions under the screen.
- s5: Government reorganizations do not create transferable equity ownership.
- s5: A probability conditional on an empty eligible population is undefined.
- q: Appropriation changes and budget clawbacks are not customer pricing mechanisms.
- q: No eligible commercial operator was identified.
- q: Public-service benefits cannot be converted into an owner-retained margin without a commercial revenue model.
- d5: Disability claims are only one component of the NAICS service basket.
- d5: A single year's PACT-related growth is not a five-year demand forecast.
- d5: Claims counts, beneficiary counts, and constant-quality administrative workload are different quantities.
- o: The estimate concerns continued operator requirement, not internal labor substitution.
- o: Routine federal benefits transactions are more self-serviceable than complex counseling, appeals, and local liaison work.
- o: Legal authority and human-review requirements may change during the horizon.

## Sources
- **S1** — [NAICS 923140 Administration of Veterans' Affairs](https://www.census.gov/naics/resources/archives/sect92.html) (accessed 2026-07-23): Defines the industry as government establishments administering assistance, training, counseling, and other services for veterans and their dependents, heirs, or survivors; supports the lens.
- **S2** — [43-4061.00 - Eligibility Interviewers, Government Programs](https://www.onetonline.org/link/summary/43-4061.00) (accessed 2026-07-23): Lists government-benefit eligibility, records, reports, data verification, interviews, rights explanations, forms, fraud review, referrals, and payment monitoring tasks; supports the a proxy.
- **S3** — [Building the Future: VA's Strategy for Adopting High-Impact Artificial Intelligence to Improve Services for Veterans](https://department.va.gov/ai/building-the-future-vas-strategy-for-adopting-high-impact-artificial-intelligence-to-improve-services-for-veterans/) (accessed 2026-07-23): Describes current automation, manual workflows, pilots, employee-tool access, claims, customer-support and eligibility use cases, infrastructure, governance, training, and production goals; supports a and rho.
- **S4** — [VA Disability Benefits: Opportunities and Challenges to Modernizing Technology and Adopting AI](https://www.gao.gov/products/gao-26-109137) (accessed 2026-07-23): Documents VA claims-modernization and AI opportunities, oversight and transparency constraints, program scale, and outstanding recommendations; supports rho and d5.
- **S5** — [VA processes one million disability claims faster than ever before](https://news.va.gov/press-room/va-processes-one-million-disability-claims-faster-than-ever-before/) (accessed 2026-07-23): Reports fiscal-2025 claims received and processed, benefit recipients, PACT claims, accuracy, and chatbot availability; supports the d5 proxy and self-service context.
