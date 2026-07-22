# 541380 — Testing Laboratories and Services

*v5.1 Stage 1 research memo. Run `541380-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** PRIORITY · A 7.87 · L 5.71 · interval CONDITIONAL → HIGHEST_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** A large repeatable documentation and data layer sits around physical, often accredited testing that customers still need from an accountable operator.
**Weakness:** Instrument integration, validation, and quality-control constraints may keep exposed labor from becoming implemented savings, while procurement can reclaim part of any benefit.

## Business-model lens
- Included: US lower-middle-market laboratories and field-testing firms that repeatedly provide physical, chemical, biological, calibration, electrical, geotechnical, mechanical, nondestructive, thermal, or related analytical testing to external customers.
- Excluded: Medical and veterinary laboratories, captive internal quality-control units, shells, non-control financing vehicles, and firms without a recurring or repeat outsourced-service model.
- Customer and revenue model: External commercial, industrial, and public-sector customers buy tests through per-sample or per-test fees, project scopes, recurring monitoring programs, master service agreements, and related reporting or certification work.
- Deviation from default lens: none

## Executive view
Testing laboratories combine a defensible physical workflow with a sizable digital and administrative layer. The near-term opportunity is to automate intake, data movement, review support, report drafting, scheduling, and quality documentation around the instrument, not to remove the accountable laboratory.

## How AI changes the work
AI can structure requests, register samples, reconcile instrument outputs, flag anomalies, assemble audit trails, draft certificates and reports, answer status inquiries, and assist scientific review. Sample custody, preparation, instrument setup, calibration, fieldwork, physical observation, exception resolution, and accountable signoff remain materially human and equipment dependent.

## Value capture
Per-test, per-sample, and fixed-scope billing should let operators retain much of an internal labor benefit between repricing events. Competitive tenders, sophisticated procurement, contract renewals, customer concentration, and required reinvestment in instruments and compliance will share part of the benefit with customers.

## Firm availability
The code is largely aligned with outsourced repeat services, although captive units, project-only firms, owner-dependent technical practices, customer concentration, and nontransferable quality liabilities reduce eligibility. General succession evidence and sustained sector acquisition activity indicate a meaningful but uncertain five-year flow of control transfers.

## Demand durability
Real demand is likely to grow modestly as regulation, new materials and devices, environmental monitoring, and independent evidence requirements offset productivity and some customer insourcing. Because tests act on physical items and frequently require accredited accountability, software is more likely to change delivery economics than eliminate the service basket.

## Risks and uncertainty
The main uncertainties are the absence of task-time data, lower-middle-market adoption evidence, six-digit real-output data, and a transaction denominator. A poor outcome would combine slow LIMS and instrument integration with aggressive customer repricing, industrial-volume weakness, sensor-driven test elimination, insourcing, or an accreditation or data-integrity failure.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.6827 | — | OBSERVED | — |
| n | — | 187 | — | ESTIMATE | — |
| a | 0.27 | 0.38 | 0.5 | PROXY | S1, S2, S3 |
| rho | 0.38 | 0.55 | 0.72 | PROXY | S3, S4, S11, S12, S13 |
| e | 0.72 | 0.84 | 0.93 | ESTIMATE | S5, S11, S12, S13 |
| s5 | 0.16 | 0.24 | 0.34 | PROXY | S8, S9, S10 |
| q | 0.52 | 0.68 | 0.82 | ESTIMATE | S7, S14 |
| d5 | 0.98 | 1.1 | 1.23 | PROXY | S6, S8 |
| o | 0.82 | 0.9 | 0.96 | PROXY | S11, S12, S13 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 2.80 | 5.71 | 9.83 | PROXY |
| F | 5.01 | 5.88 | 6.59 | ESTIMATE |
| C | 10.00 | 10.00 | 10.00 | ESTIMATE |
| D | 8.04 | 9.90 | 10.00 | PROXY |

## Caveats
- a: BLS occupation shares are May 2023 and do not report task time or current automation within occupations.
- a: The laboratory survey has 110 self-selected respondents, is Europe-skewed, favors larger labs, and is concentrated in food and beverage.
- a: The frozen compensation intensity combines 2024 wage data with 2022 receipts and a harmonized benefits adjustment; that vintage mismatch is separate from this task-exposure estimate.
- rho: Neither survey measures implemented labor substitution at the screened firms.
- rho: Biopharma quality-control laboratories face stricter validation than some NAICS 541380 segments and are often captive rather than outsourced.
- rho: EPA, FDA, and NIST requirements demonstrate constraints in regulated or accredited niches but do not quantify their prevalence across the industry.
- e: No source reports the eligible share of firms in the specified earnings band.
- e: The NAICS code spans laboratory and on-site testing modalities with different repeat-revenue and transferability profiles.
- e: The frozen firm count is an estimate bridged from SUSB size classes using a 15.65% margin assumption, so actual band membership may differ materially.
- s5: Gallup measures plans rather than completed transactions and covers all small employer businesses.
- s5: EY and SGS evidence is global and includes larger testing, inspection, certification, and assurance businesses outside the lens.
- s5: Public deal announcements do not reveal the full denominator or failed transactions.
- q: No source directly measures five-year retained AI benefit for lower-middle-market testing firms.
- q: Oregon State's fee schedule demonstrates billing architecture at a public laboratory, not private-market competitive behavior.
- q: Intertek is a global scaled operator with a broader assurance, testing, inspection, and certification mix.
- d5: BLS does not publish six-digit real output for this industry in the cited table.
- d5: Employment is affected by productivity and therefore is not a direct measure of service quantity.
- d5: The EY forecast is global and spans inspection and certification as well as laboratory testing.
- o: The cited programs are compliance-heavy examples rather than an industry-wide demand census.
- o: Accreditation can be voluntary or customer-required, and not every service in the NAICS code is regulated.
- o: Sensor-based monitoring and customer laboratory investment could reduce outsourced test volume more quickly than assumed.

## Sources
- **S1** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 541380](https://www.bls.gov/oes/2023/may/naics5_541380.htm) (accessed 2026-07-22): Exact industry occupation employment shares and mean wages used to anchor wage-weighted task exposure.
- **S2** — [Inspectors, Testers, Sorters, Samplers, and Weighers](https://www.onetonline.org/link/details/51-9061.00) (accessed 2026-07-22): Task mix spanning physical inspection, sampling, instruments, calibration, data recording, analysis, and reports.
- **S3** — [2026 State of Lab Digitalization](https://www.1lims.com/2026-state-of-lab-digitalization) (accessed 2026-07-22): Laboratory digital-tool adoption, connected-system gaps, LIMS integration, manual processes, priorities, and sample limitations.
- **S4** — [Building the quality control lab of the future](https://www.deloitte.com/us/en/insights/industry/health-care/biopharma-lab-modernization-digital-transformation-qc-lab-future.html) (accessed 2026-07-22): Biopharma quality-control modernization maturity, automation expectations, investment intent, and integration obstacles.
- **S5** — [North American Industry Classification System, United States, 2022](https://www.census.gov/naics/reference_files_tools/2022_NAICS_Manual.pdf) (accessed 2026-07-22): Official scope of NAICS 541380 and included physical, chemical, biological, calibration, electrical, geotechnical, mechanical, nondestructive, and thermal testing.
- **S6** — [Industry employment and output projections](https://www.bls.gov/emp/tables/industry-employment-and-output.htm) (accessed 2026-07-22): 2024-2034 six-digit testing-laboratory employment projection and broader parent-sector real-output projection.
- **S7** — [2025 Year in Review](https://www.intertek.com/investors/2025-year-in-review/) (accessed 2026-07-22): Large-operator evidence that pricing, productivity, mix, leverage, and cost discipline contributed to margin progression.
- **S8** — [Testing, inspection and certification study 2025](https://www.ey.com/en_ch/insights/strategy-transactions/testing-inspection-and-certification-study-2025) (accessed 2026-07-22): Global market-growth expectation, regulatory and digital drivers, and long-run acquisition activity.
- **S9** — [SGS 2025 Full Year Results](https://www.sgs.com/-/media/sgscorp/documents/corporate/reports-and-presentations/2020s/2026/sgs-2025-full-year-results-press-release-en.cdn.en-CL.pdf) (accessed 2026-07-22): Recent bolt-on pace and named US laboratory, testing, calibration, and forensic acquisitions.
- **S10** — [Most U.S. Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): US employer-business owner age and five-year sell-or-transfer intentions.
- **S11** — [Learn About Laboratory Certification for Drinking Water](https://www.epa.gov/dwlabcert/learn-about-laboratory-certification-drinking-water) (accessed 2026-07-22): Approved methods, proficiency testing, certification, audits, and accountable compliance results.
- **S12** — [Testing Laboratories: How to Participate in ASCA](https://www.fda.gov/medical-devices/division-standards-and-conformity-assessment/testing-laboratories-how-participate-asca) (accessed 2026-07-22): ISO/IEC 17025 accreditation, test plans, summary reports, and laboratory integrity requirements in medical-device testing.
- **S13** — [Accreditation](https://www.nist.gov/accreditation) (accessed 2026-07-22): Technical competence, onsite assessment, proficiency testing, personnel, methods, equipment, traceability, sampling, handling, and reporting.
- **S14** — [Cooperative Chemical Analytical Laboratory Fee Schedule](https://ccal.oregonstate.edu/fees) (accessed 2026-07-22): Observable per-analysis, setup, shipping, and sample-pickup fee architecture for laboratory services.
