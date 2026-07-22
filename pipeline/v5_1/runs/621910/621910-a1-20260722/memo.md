# 621910 — Ambulance Services

*v5.1 Stage 1 research memo. Run `621910-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** LOW_PRIORITY · A 5.58 · L 1.80 · interval STRUCTURAL_OUT → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** AI-assisted dispatch, deployment, documentation, coding, and scheduling can improve scarce-crew productivity across repeat payer and customer relationships.
**Weakness:** Physical transport and emergency clinical responsibility dominate the work, while regulated fee schedules and payer contracts limit retained upside.

## Business-model lens
- Included: US lower-middle-market independent ambulance firms providing recurring or repeat ground or air emergency response, interfacility transport, standby, and medically necessary patient transport with clinical care to external patients, facilities, payers, municipalities, and other customers.
- Excluded: Government-owned or captive ambulance units, nonmedical special-needs transportation, vehicle-only services without medical care, one-off operations without a repeat payer or customer relationship, shells, and non-control financing vehicles.
- Customer and revenue model: Providers respond to emergency calls and scheduled medical transports under recurring payer enrollment, facility, health-system, municipal, managed-care, or event relationships; reimbursement commonly combines a service-level base payment, loaded mileage, geographic adjustments, negotiated rates, and patient cost sharing.
- Deviation from default lens: none

## Executive view
Ambulance services are labor- and asset-intensive, with most value tied to rapid physical response, transport, and accountable clinical care. AI can improve dispatch, deployment, documentation, coding, billing, and decision support, but only a modest share of work is substitutable and nearly all surviving service remains crew-operated.

## How AI changes the work
AI can prioritize and summarize calls, predict demand, stage vehicles, optimize routes and shifts, draft electronic patient-care reports, assist coding, flag protocol exceptions, forecast maintenance, and support clinical decisions. Crews still secure scenes, assess and lift patients, drive, treat, monitor, communicate, and hand off care under time pressure.

## Value capture
Fixed fee schedules can let providers retain cost savings before rate updates, but mandatory assignment, negotiated payer rates, municipal contracts, rebids, denials, bad debt, wage pressure, software cost, and public subsidy structures constrain durable retention.

## Firm availability
Private ambulance firms can offer transferable fleets, teams, payer enrollments, facility relationships, licenses, and dispatch capacity. Eligibility is narrowed by public and captive operations, certificates, municipal dependence, volunteer labor, billing liabilities, owner dependence, and uncertainty in the margin-bridged firm count.

## Demand durability
Emergency events, population aging, and interfacility care support a stable to modestly growing service core. Alternative transport, treat-in-place models, payer medical-necessity controls, public budgets, and workforce shortages limit growth, but they do not remove the physical response requirement for most remaining calls.

## Risks and uncertainty
Key risks are reimbursement adequacy, payer mix, denied claims, self-pay collections, wage inflation, staffing shortages, vehicle and equipment capital, response-time obligations, medical liability, licensure, municipal contracting, cybersecurity, dispatch integration, and unsafe clinical automation. Ground, air, emergency, and scheduled services differ sharply, and the dataset margin bridge may misstate LMM availability.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.5208 | — | OBSERVED | — |
| n | — | 188 | — | ESTIMATE | — |
| a | 0.1 | 0.18 | 0.28 | PROXY | S2, S3, S5 |
| rho | 0.28 | 0.48 | 0.68 | PROXY | S2, S5 |
| e | 0.6 | 0.76 | 0.88 | ESTIMATE | S1, S4, S5 |
| s5 | 0.06 | 0.11 | 0.18 | PROXY | S6 |
| q | 0.16 | 0.3 | 0.45 | ESTIMATE | S4, S5 |
| d5 | 0.98 | 1.04 | 1.11 | PROXY | S3, S5 |
| o | 0.9 | 0.96 | 0.99 | PROXY | S1, S3, S4 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.58 | 1.80 | 3.97 | PROXY |
| F | 3.30 | 4.53 | 5.51 | ESTIMATE |
| C | 3.20 | 6.00 | 9.00 | ESTIMATE |
| D | 8.82 | 9.98 | 10.00 | PROXY |

## Caveats
- a: The occupation table includes ambulance employers of all sizes and ownership types, not only eligible LMM firms.
- a: Employment shares are not wage-weighted task shares and do not measure current automation.
- a: Ground emergency, nonemergency interfacility, specialty transport, and air ambulance workflows differ materially.
- a: The injected compensation ratio combines 2024 wages with 2022 receipts.
- rho: Neither source measures representative AI adoption or realized labor savings.
- rho: CMS ground-ambulance evidence includes government, nonprofit, volunteer, and public-safety organizations unlike the acquisition lens.
- rho: Medical-direction rules, dispatch integration, payer audits, and liability constraints vary by state and service type.
- e: The NAICS definition does not measure recurring relationships, ownership eligibility, transferability, or normalized EBITDA.
- e: CMS data include government, public-safety, nonprofit, volunteer, and institutional organizations outside the lens.
- e: The injected count of 188 uses a broad healthcare-facilities margin bridge that may misclassify thin-margin ambulance firms into or out of the LMM band.
- s5: Gallup is cross-industry and measures intentions rather than completed external control deals.
- s5: No source measures five-year transfer probability for eligible private ambulance firms.
- s5: Licensing, certificates, municipal contracts, payer enrollment, and billing liabilities can block intended sales.
- q: No source directly measures retained AI-derived benefits for lower-middle-market ambulance firms.
- q: Retention differs across Medicare fee schedule, Medicaid, managed care, commercial insurance, facilities, municipalities, and self-pay.
- q: CMS ground-ambulance cost and revenue data combine ownership and operating models and therefore do not establish private-firm profitability.
- d5: BLS forecasts occupations across private ambulance, government, hospital, and other settings rather than purchased 621910 service quantity.
- d5: Employment can diverge from service quantity as deployment and documentation productivity change.
- d5: Local public funding, hospital patterns, population density, disasters, and payer policy create substantial geographic variation.
- o: The sources establish current duties and payment definitions, not a measured year-five operator-required share.
- o: Low-acuity and scheduled transports may face more substitution than emergency advanced-life-support calls.
- o: Air ambulance, specialty care transport, urban ground response, and rural response have different automation constraints.

## Sources
- **S1** — [2022 North American Industry Classification System Manual: 621910](https://www.census.gov/naics/reference_files_tools/2022_NAICS_Manual.pdf) (accessed 2026-07-22): Defines 621910 as ground or air patient transportation with medical care in lifesaving-equipped vehicles operated by trained personnel and distinguishes nonmedical special-needs transportation.
- **S2** — [May 2023 OEWS: Ambulance Services](https://www.bls.gov/oes/2023/may/naics5_621910.htm) (accessed 2026-07-22): Reports the ambulance-services occupation mix, including 70.56% EMTs and paramedics, 4.25% ambulance drivers and attendants, 8.65% office and administrative support, and 3.63% dispatchers.
- **S3** — [EMTs and Paramedics — Occupational Outlook Handbook](https://www.bls.gov/ooh/healthcare/emts-and-paramedics.htm) (accessed 2026-07-22): Describes response, assessment, treatment, transport, monitoring, documentation, supply, and handoff duties; reports substantial ambulance-industry employment and projects 5% occupation growth from 2024 to 2034, citing persistent emergencies and population aging.
- **S4** — [Ambulance Fee Schedule and ZIP Code Files](https://www.cms.gov/medicare/payment/fee-schedules/ambulance) (accessed 2026-07-22): Explains that Medicare Part B uses a national ambulance fee schedule across private, municipal, volunteer, independent, and institutional providers and requires providers and suppliers to accept allowed charges, with patient coinsurance and deductible.
- **S5** — [Medicare Ground Ambulance Data Collection System Report: Year 1 and Year 2 Cohort Analysis](https://www.cms.gov/files/document/medicare-ground-ambulance-data-collection-system-gadcs-report-year-1-and-year-2-cohort-analysis.pdf) (accessed 2026-07-22): Documents ground-ambulance organization, staffing, dispatch, labor, cost, revenue, response, and transport structures; reports 43.1% average labor share of total cost across weighted organizations and large variation by volume, ownership, and geography.
- **S6** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Reports that 22% of US employer-business owners planned to sell or transfer ownership within five years in a fall 2024 survey.
