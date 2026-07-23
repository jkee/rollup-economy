# 922110 — Courts

*v5.1 Stage 1 research memo. Run `922110-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** no base (evidence-first) · A — · L — · interval STRUCTURAL_OUT → HIGHEST_PRIORITY · readiness STRESS_TEST_ONLY · action EVIDENCE_FIRST

**Driver:** Large document and administrative workloads create real AI-assisted capacity gains while court demand and accountable judicial authority remain durable.
**Weakness:** NAICS 922110 is public administration with no eligible private-firm population or conventional commercial-retention construct.

## Business-model lens
- Included: Civilian federal, state, and local courts of law and sheriffs' offices conducting court functions, assessed operationally; under the fixed acquisition lens there are no qualifying independent private LMM firms because the industry is public administration.
- Excluded: Military courts, American Indian and Alaska Native tribal courts, private law firms, prosecutors and public defenders, police, corrections, probation and parole, private arbitration, court technology vendors, contractors, shells, captive internal units, non-control financing vehicles, and all entities outside the roughly $1-10M normalized EBITDA band.
- Customer and revenue model: Courts provide constitutionally and statutorily mandated adjudication, case administration, records, hearings, orders, and public access, funded principally through government appropriations and partly through prescribed fees rather than recurring outsourced commercial contracts or market pricing.
- Deviation from default lens: none; applying the fixed default lens produces no qualifying private-firm population because NAICS 922110 is a public-administration activity

## Executive view
Courts have meaningful assistive AI potential in document, research, docket, scheduling, records, and public-service workflows, but risk and governance sharply limit five-year implementation in rights-affecting decisions. Demand is durable and requires an accountable judiciary. The code is structurally outside the acquisition lens: it is public administration, frozen n is missing, the eligible-firm and transfer shares are zero, and commercial retention cannot be defined from appropriations and prescribed fees.

## How AI changes the work
AI can assist intake, completeness checks, docketing, scheduling, transcription, summarization, record search, legal research, draft preparation, guided forms, public information, and anomaly flagging. NCSC reports current court use in document retrieval, chatbots, and guardianship-report screening. Privacy, bias, hallucination, due process, cybersecurity, accessibility, and human-review requirements make ancillary administration more implementable than fact interpretation or final decisions.

## Value capture
There is no conventional commercial value-capture mechanism. Courts are funded through appropriations and prescribed fees, so productivity may appear as shorter queues, avoided hiring, more reviewed cases, service quality, budget reallocation, or lower future appropriations. Without a public-value accounting framework and jurisdiction-specific budget rules, translating those outcomes into retained gross benefit would be artificial.

## Firm availability
The official industry consists of civilian courts of law within Public Administration. It contains no qualifying independent LMM firms under the fixed lens, and frozen n is missing. Judicial appointments, elections, procurements, reorganizations, and outsourcing contracts do not constitute a qualifying control transfer of the court; private technology and support vendors belong to other industries.

## Demand durability
State courts reported 70 million filings in 2024, up 4% from 2023 but still 27% below 2012, while several federal filing categories increased in fiscal 2025. Population and legally enforceable rights sustain demand, although diversion, alternative dispute resolution, policy changes, digital self-service, and case-mix shifts alter workload. BLS expects only modest growth in judges and court-related clerks over the next decade.

## Risks and uncertainty
The decisive risks are structural ineligibility and undefined commercial retention. Operational uncertainties include privacy and sealed records, biased or fabricated output, appeal and due-process risk, procurement delays, legacy systems, cybersecurity, fragmented governance, accessibility, labor rules, public trust, and extreme variation in case complexity. Aggregate filing counts are weak proxies for weighted workload.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | — | — | MISSING | — |
| n | — | — | — | MISSING | — |
| a | 0.3 | 0.45 | 0.6 | PROXY | S2, S3, S4, S5 |
| rho | 0.18 | 0.32 | 0.48 | ESTIMATE | S5 |
| e | 0 | 0 | 0 | OBSERVED | S1 |
| s5 | 0 | 0 | 0 | ESTIMATE | S1, S3 |
| q | — | — | — | MISSING | — |
| d5 | 0.97 | 1.04 | 1.12 | PROXY | S3, S4, S6, S7 |
| o | 0.995 | 0.999 | 1 | ESTIMATE | S1, S3, S5 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | — | — | — | MISSING |
| F | — | — | — | MISSING |
| C | — | — | — | MISSING |
| D | 9.65 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: No source provides a six-digit court-industry wage-weighted task distribution.
- a: Task and staffing mixes vary sharply by jurisdiction, case type, court level, and use of elected clerks or shared administrative offices.
- rho: NCSC documents current experiments and use cases, not realized labor substitution across courts.
- rho: Low-risk ancillary administration can move faster than legal research, fact interpretation, or decisions affecting individual rights.
- e: Frozen n is missing; the zero is an eligibility share based on the industry's public nature, not an estimate of establishment count.
- e: Private court-service and technology contractors may be acquisition candidates in other NAICS codes but are outside this record.
- s5: This is a structural transaction definition, not an assessment of turnover among judges or court administrators.
- s5: Outsourcing a court function to a vendor is a procurement event, not a control transfer of the court.
- q: Prescribed filing fees are not a market price for adjudication and do not create a conventional gross-margin retention mechanism.
- q: Assigning a neutral value would falsely imply commercial evidence.
- d5: The 70 million state-filing figure aggregates unlike case types and reports filings rather than weighted workload.
- d5: Federal caseload is a small, volatile share of total US court activity and was affected by multidistrict litigation and bankruptcy cycles.
- o: The estimate concerns institutional operator necessity, not employee counts or the amount of human work per case.
- o: Online dispute resolution and guided self-service may eliminate parts of the current basket but not the accountable court institution.

## Sources
- **S1** — [2022 North American Industry Classification System Manual: 922110 Courts](https://www.census.gov/naics/reference_files_tools/2022_NAICS_Manual.pdf) (accessed 2026-07-23): Official scope in Sector 92 Public Administration: civilian courts of law and sheriffs' offices conducting court functions, excluding military and tribal courts.
- **S2** — [O*NET Job Duties: Court, Municipal, and License Clerks](https://www.onetonline.org/search/task/choose/43-4031.00) (accessed 2026-07-23): Task proxy covering court-document filing, administrative work, record maintenance, document verification, minutes, and docket or calendar preparation.
- **S3** — [Judges and Hearing Officers](https://www.bls.gov/ooh/legal/judges-and-hearing-officers.htm) (accessed 2026-07-23): Judicial task and operator evidence: judges research and evaluate legal information, conduct hearings, apply law, issue decisions, and work for federal, state, or local government; employment is projected to grow 1% from 2024 to 2034.
- **S4** — [Information Clerks](https://www.bls.gov/ooh/office-and-administrative-support/information-clerks.htm) (accessed 2026-07-23): Court-clerk task and demand proxy: court clerks maintain records, prepare dockets, and receive and send documents; court, municipal, and license clerk employment is projected to rise from 180,400 in 2024 to 185,900 in 2034.
- **S5** — [NCSC Trends in State Courts 2025](https://www.ncsc.org/sites/default/files/media/document/NCSC-Trends-2025.pdf) (accessed 2026-07-23): Current AI evidence: courts use AI for document retrieval, docketing and scheduling, chatbots, summaries, and guardianship-report screening, while privacy and rights-affecting decisions require strong controls and human final decisions.
- **S6** — [National Center for State Courts: Data for Court Professionals](https://www.ncsc.org/resources-courts/data) (accessed 2026-07-23): National state-court demand proxy reporting 70 million filings in 2024, up 4% from 2023 and down 27% from 2012.
- **S7** — [Judicial Business 2025](https://www.uscourts.gov/data-news/reports/statistical-reports/judicial-business-united-states-courts/judicial-business-2025) (accessed 2026-07-23): Federal demand proxy: fiscal 2025 regional appeals rose 5% to 41,824, district filings rose 6% to 382,692, and bankruptcy filings rose 11% to 557,376.
