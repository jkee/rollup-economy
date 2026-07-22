# 623220 — Residential Mental Health and Substance Abuse Facilities

*v5.1 Stage 1 research memo. Run `623220-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** CONDITIONAL · A 7.42 · L 3.38 · interval LOW_PRIORITY → HIGHEST_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** A large counseling and administrative workforce, persistent treatment need, and active healthcare technology adoption support practical workflow automation.
**Weakness:** Residential treatment is clinically sensitive and payer-managed, so automation must remain supervised while much of the benefit can be repriced or diverted to lower-cost care settings.

## Business-model lens
- Included: United States lower-middle-market operators providing recurring or episode-based residential care and treatment for mental-health and substance-use conditions, including nonhospital rehabilitation facilities, mental-health halfway houses, psychiatric convalescent settings, and residential group homes, with room, board, supervision, counseling, rehabilitation, and support services.
- Excluded: Exclusively outpatient behavioral-health centers, licensed psychiatric hospitals emphasizing medical treatment and monitoring, residential intellectual-disability facilities, temporary shelters, correctional facilities, shell entities, captive units, and non-control financing vehicles.
- Customer and revenue model: Patients are service recipients, while commercial insurers, Medicaid, Medicare and other public programs, and self-pay clients fund care. Revenue is generally episode, day, service, or negotiated-rate based and reduced by payer contractual adjustments, discounts, and collection concessions.
- Deviation from default lens: none

## Executive view
Residential behavioral health combines durable clinical need with a relatively information-intensive workforce, creating meaningful administrative and documentation opportunity. Clinical safety, continuous supervision, heterogeneous payer contracts, nonprofit ownership, and outpatient substitution prevent a simple translation from AI capability to removable labor or retained margin.

## How AI changes the work
Near-term applications include clinical-note drafting, intake summarization, coding and claim checks, utilization-review packets, care-plan assistance, scheduling, compliance retrieval, staff training, and risk triage. Therapy, diagnosis, medication decisions, crisis response, safeguarding, and residential milieu management require accountable professionals.

## Value capture
Fixed day and episode payments can preserve some productivity benefit, particularly between contract renewals. Government rates, commercial utilization management, denials, network competition, self-pay affordability, and the need to reinvest in quality and scarce clinical staff return a substantial share of benefit to payers or patients.

## Firm availability
The industry is fragmented and attracts strategic and sponsor acquisition, including residential assets. The eligible pool is materially narrowed by nonprofit operation, mixed levels of care, licensure and accreditation, state transaction oversight, payer contracts, real-estate arrangements, and liabilities arising from patient incidents or marketing practices.

## Demand durability
Behavioral-health prevalence and undertreatment support demand, and BLS projects continued growth for residential facilities. Residential care remains a small, high-acuity part of the continuum, however, and outpatient treatment, medication, telehealth, payer authorization, and shorter stays can absorb growth or displace days.

## Risks and uncertainty
Central uncertainties are the share of counselor and clinician time that can be removed safely, adoption capacity at small facilities, payer capture of savings, ownership eligibility, and future level-of-care mix. Privacy breaches, biased clinical tools, deficient supervision, adverse patient events, fraud investigations, and abrupt facility closures create unusually serious downside.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.6533 | — | OBSERVED | — |
| n | — | 1019 | — | ESTIMATE | — |
| a | 0.22 | 0.34 | 0.47 | PROXY | S1, S2, S7, S8 |
| rho | 0.22 | 0.38 | 0.55 | PROXY | S7, S8, S9 |
| e | 0.38 | 0.54 | 0.7 | PROXY | S1, S5, S6, S9 |
| s5 | 0.14 | 0.23 | 0.34 | PROXY | S9, S10, S11 |
| q | 0.3 | 0.48 | 0.65 | PROXY | S5, S9 |
| d5 | 0.98 | 1.06 | 1.18 | PROXY | S3, S4, S9 |
| o | 0.72 | 0.84 | 0.94 | ESTIMATE | S1, S4, S8, S9 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 1.26 | 3.38 | 6.76 | PROXY |
| F | 6.45 | 7.80 | 8.84 | ESTIMATE |
| C | 6.00 | 9.60 | 10.00 | PROXY |
| D | 7.06 | 8.90 | 10.00 | ESTIMATE |

## Caveats
- a: Occupation shares measure staffing rather than exposed tasks.
- a: The BLS table covers employers of all sizes and predates the run date.
- rho: Acute-care hospital adoption is not residential behavioral-health adoption.
- rho: Reported tool use does not establish net labor substitution.
- e: SAMHSA's survey includes outpatient and hospital facilities in addition to residential operators.
- e: Facility counts do not map directly to firms or the frozen earnings band.
- s5: Broad behavioral-health deal tracking is not specific to this NAICS code.
- s5: Owner intentions are not completed transactions.
- q: Public operators include hospitals and outpatient programs outside the lens.
- q: Payer and program mix varies sharply among mental-health, substance-use, adolescent, and adult facilities.
- d5: Employment growth is not a direct measure of constant-quality demand.
- d5: SAMHSA prevalence and treatment receipt combine every level of behavioral-health care.
- o: The estimate concerns continued operator requirement, not whether software reduces operator staffing.
- o: Payer level-of-care policies may shift volume outside the lens even when human treatment remains necessary.

## Sources
- **S1** — [NAICS Definition: Residential Mental Health and Substance Abuse Facilities](https://www.census.gov/naics/resources/archives/sect62.html) (accessed 2026-07-22): Industry boundary, included facility types, residential service basket, and separation from outpatient centers and psychiatric hospitals.
- **S2** — [BLS Industry-Specific Occupational Employment and Wage Estimates for 623220](https://www.bls.gov/oes/2023/may/naics5_623220.htm) (accessed 2026-07-22): Detailed employment and wage mix for counselors, social workers, healthcare staff, aides, managers, residential advisors, and office support.
- **S3** — [BLS Industry and Occupational Employment Projections Overview](https://www.bls.gov/opub/mlr/2024/article/industry-and-occupational-employment-projections-overview-and-highlights-2023-33.htm) (accessed 2026-07-22): Projected employment growth for this industry and behavioral-health occupations, plus the role of continued treatment demand.
- **S4** — [SAMHSA National Survey on Drug Use and Health Annual Report](https://www.samhsa.gov/data/sites/default/files/reports/rpt56287/2024-nsduh-annual-national/2024-nsduh-annual-national-html-071425-edited/2024-nsduh-annual-national.htm) (accessed 2026-07-22): Mental-illness and substance-use prevalence, treatment receipt, perceived unmet need, and use of inpatient, outpatient, medication, and telehealth treatment.
- **S5** — [National Substance Use and Mental Health Services Survey Annual Report](https://www.samhsa.gov/data/sites/default/files/reports/rpt56696/2024-nsumhss-annual-report.pdf) (accessed 2026-07-22): Facility operation type and payment acceptance across substance-use and mental-health treatment providers.
- **S6** — [National Substance Use and Mental Health Services Survey Public-Use Data Documentation](https://www.samhsa.gov/data/data-we-collect/n-sumhss-national-substance-use-and-mental-health-services-survey/datafiles/2024) (accessed 2026-07-22): Survey universe, facility-level characteristics, public and private ownership, service provision, utilization, and material survey limitations.
- **S7** — [Hospital Trends in Predictive AI Use, Evaluation, and Governance](https://healthit.gov/data/data-briefs/hospital-trends-use-evaluation-and-governance-predictive-ai-2023-2024/) (accessed 2026-07-22): Adjacent healthcare AI adoption, growth in billing and scheduling applications, governance, monitoring, and the adoption gap for small independent facilities.
- **S8** — [Technology and the Future of Mental Health Treatment](https://www.nimh.nih.gov/health/topics/technology-and-the-future-of-mental-health-treatment) (accessed 2026-07-22): Digital mental-health opportunities, complementary role with professional care, and limitations involving effectiveness, privacy, standards, and crisis support.
- **S9** — [Acadia Healthcare 2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/1520697/000119312526078266/achc-20251231.htm) (accessed 2026-07-22): Residential treatment operations, payer sources, contractual revenue adjustments, disclosed residential acquisition, regulation, and operating demand.
- **S10** — [Private Equity Healthcare Deals Review](https://pestakeholder.org/reports/healthcare-deals-2024-in-review/) (accessed 2026-07-22): Behavioral-health transaction activity, add-on acquisitions, residential-treatment examples, consolidation, closure, and regulatory risks.
- **S11** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Five-year sale and transfer intentions among United States employer-business owners.
