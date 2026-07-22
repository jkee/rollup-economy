# 621498 — All Other Outpatient Care Centers

*v5.1 Stage 1 research memo. Run `621498-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** CONDITIONAL · A 6.78 · L 2.14 · interval STRUCTURAL_OUT → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Documentation and coordination-heavy recurring outpatient workflows can be automated while growing clinical demand continues to require accountable delivery organizations.
**Weakness:** The residual code combines commercial clinics with safety-net and nonprofit centers, making eligibility, value retention, and transferable control economics unusually uncertain.

## Business-model lens
- Included: Lower-middle-market outpatient centers with medical staff repeatedly delivering general or specialized care to external patients and payors, including multispecialty community clinics, pain therapy centers, sleep disorder centers, and biofeedback centers.
- Excluded: Physician, dentist, or other practitioner offices classified elsewhere; family planning, outpatient mental health or substance use, HMO, dialysis, surgical, emergency, laboratory, imaging, and home-health providers classified elsewhere; captive units, shells, non-control financing vehicles, and nonprofit or public centers without transferable control economics.
- Customer and revenue model: Centers provide recurring visits, diagnostics, treatment, care coordination, and monitoring to patients. Revenue can combine Medicare or Medicaid prospective or fee-schedule payments, commercial insurer contracts, patient cost sharing, grants, and sliding-fee payments; the mix varies sharply between community health centers and commercial specialty clinics.
- Deviation from default lens: none

## Executive view
All other outpatient care centers offer a substantial documentation, billing, intake, referral, messaging, and care-coordination opportunity, but direct clinical work remains human and accountable. Demand is supportive, especially in community and chronic-care settings, yet the code mixes safety-net and commercial specialty models. Public and prospective payment, grant missions, nonprofit ownership, and heterogeneous clinic economics limit both retention and the clean transferable-firm pool.

## How AI changes the work
AI can draft notes, coding suggestions, care plans, chart and referral summaries, portal replies, translations, authorization packages, outreach, scheduling, quality reports, and population-health worklists. It can assist clinical research and diagnosis under review. It is less able to replace examination, testing, therapy, prescribing accountability, multidisciplinary judgment, vulnerable-patient support, or hands-on treatment.

## Value capture
Fixed encounter and contracted rates allow some productivity to remain within an episode, but public payment updates, Medicaid rules, grants, value-based sharing, commercial renewals, sliding fees, and access missions can recapture or redirect it. Commercial specialty clinics may retain more than community health centers, which may use freed capacity to serve additional patients rather than reduce payroll.

## Firm availability
Commercial pain, sleep, biofeedback, and multispecialty clinics can be transferable service firms, and broader healthcare consolidation confirms buyer channels. The code also contains a large safety-net, nonprofit, public, affiliated, and grant-supported presence. Firm counts, sites, awardees, and control targets are therefore not interchangeable, and normalized EBITDA may be especially unreliable across this mix.

## Demand durability
Broad outpatient output and health-center patient use are growing, supported by aging, chronic disease, access gaps, and continued migration to ambulatory care. AI and telehealth can alter the site and labor content of visits, but most diagnosis, treatment, monitoring, and coordinated care still requires a licensed organization. Funding and workforce constraints may limit realized volume despite underlying need.

## Risks and uncertainty
Key uncertainties are the six-digit clinic mix, nonprofit and affiliate share, contracted clinical labor, payer and grant composition, actual transfer history, and realized retained savings. Privacy, bias, unsafe recommendations, documentation errors, denials, cybersecurity, EHR fragmentation, clinician shortages, grant changes, Medicaid policy, and migration to other care settings can offset automation benefits.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.2828 | — | OBSERVED | — |
| n | — | 911 | — | ESTIMATE | — |
| a | 0.23 | 0.35 | 0.48 | PROXY | S2, S3 |
| rho | 0.35 | 0.54 | 0.72 | PROXY | S3 |
| e | 0.34 | 0.54 | 0.72 | ESTIMATE | S1, S7 |
| s5 | 0.09 | 0.18 | 0.29 | PROXY | S4, S5 |
| q | 0.22 | 0.39 | 0.58 | PROXY | S5, S8 |
| d5 | 1.02 | 1.17 | 1.28 | PROXY | S6, S7 |
| o | 0.72 | 0.85 | 0.93 | PROXY | S1, S3, S7 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.91 | 2.14 | 3.91 | PROXY |
| F | 5.41 | 7.23 | 8.45 | ESTIMATE |
| C | 4.40 | 7.80 | 10.00 | PROXY |
| D | 7.34 | 9.95 | 10.00 | PROXY |

## Caveats
- a: No six-digit occupation or payroll-by-function table was located.
- a: The code's clinic types have materially different practitioner, technician, and administrative mixes.
- a: Physician adoption measures use of tools, not wage displacement or avoided hiring.
- rho: AMA does not isolate center type, ownership, size, or NAICS code.
- rho: Reported use includes research and drafting that may save minutes without eliminating positions.
- rho: Underfunded community centers may have high need but limited implementation capacity.
- e: No source measures the share of LMM-band 621498 firms that are transferable commercial operators.
- e: HRSA health centers overlap 621498 imperfectly and their sites are not equivalent to firms.
- e: The supplied firm count is margin-bridged using a hospital and healthcare-facilities margin that may misclassify safety-net and specialty centers.
- s5: Broad owner intentions are not completed healthcare control transfers.
- s5: Physician-practice consolidation is adjacent to, but not the same as, acquisition of a staffed outpatient center.
- s5: Corporate-practice, nonprofit, licensure, grant, and payer rules can prevent or reshape control transactions.
- q: FQHC payment is only one revenue model inside a heterogeneous six-digit code.
- q: No source measures AI-benefit retention, competitive pass-through, or reinvestment for these centers.
- q: Grant restrictions and safety-net missions can turn labor productivity into service expansion rather than owner cash flow.
- d5: BLS combines 621498 with other outpatient center industries that have different growth drivers.
- d5: HRSA centers are not a complete or exact 621498 population and include nonprofit safety-net providers.
- d5: Real-output growth does not directly distinguish visit quantity, case complexity, and quality change.
- o: The operator requirement differs substantially among pain, sleep, biofeedback, community, and multispecialty care.
- o: Telehealth can preserve an accountable operator while reducing the need for a physical center location.
- o: Care may migrate to physician practices, hospitals, retail clinics, or home settings even when total health demand grows.

## Sources
- **S1** — [U.S. Census Bureau: 2022 NAICS Manual, 621498](https://www.census.gov/naics/reference_files_tools/2022_NAICS_Manual.pdf) (accessed 2026-07-22): Defines 621498 as medical-staffed centers providing general or specialized outpatient care and lists community health, pain therapy, sleep disorder, and biofeedback centers while identifying exclusions.
- **S2** — [BLS May 2023 OEWS: Outpatient Care Centers](https://www.bls.gov/oes/2023/may/naics4_621400.htm) (accessed 2026-07-22): Reports the broader outpatient-center occupation mix, including practitioners, nurses, healthcare support, medical assistants, and office, billing, reception, secretarial, and records roles.
- **S3** — [AMA 2026 Physician Survey on Augmented Intelligence](https://www.ama-assn.org/system/files/physician-ai-sentiment-report.pdf/) (accessed 2026-07-22): Reports current physician AI adoption and use cases plus privacy, validation, liability, training, workflow, clinical-accountability, and patient-use constraints.
- **S4** — [Gallup: Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Reports that 22% of U.S. employer-business owners planned to sell or transfer ownership within five years, based on a fall 2024 survey.
- **S5** — [GAO-25-107450: Health Care Consolidation](https://files.gao.gov/reports/GAO-25-107450/index.html) (accessed 2026-07-22): Describes hospital, insurer, corporate, and private-equity acquisition or affiliation channels, MSO roll-ups, specialty variation, and commercial price effects in physician markets.
- **S6** — [BLS Employment and Output by Industry, 2024 to 2034](https://www.bls.gov/emp/tables/industry-employment-and-output.htm) (accessed 2026-07-22): Projects broader NAICS 621400 employment from 1.115 million in 2024 to 1.325 million in 2034 and real output from $217.8 billion to $307.4 billion.
- **S7** — [HRSA Bureau of Primary Health Care: Health Center Program Impact](https://bphc.hrsa.gov/about-health-centers/health-center-program-impact-growth) (accessed 2026-07-22): Reports 32.4 million health-center patients and 139.4 million visits in 2024, the safety-net population served, coordinated services, chronic-disease management, screening, and access role.
- **S8** — [CMS Medicare Learning Network: Federally Qualified Health Center](https://www.cms.gov/files/document/mln006397-federally-qualified-health-center.pdf) (accessed 2026-07-22): Explains encounter-based FQHC payment at the lesser of charges or a geographically adjusted prospective rate and reports the 2026 base rate and annual market-basket update.
