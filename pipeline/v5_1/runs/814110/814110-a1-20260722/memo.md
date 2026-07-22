# 814110 — Private Households

*v5.1 Stage 1 research memo. Run `814110-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** no base (evidence-first) · A — · L — · interval STRUCTURAL_OUT → HIGHEST_PRIORITY · readiness STRESS_TEST_ONLY · action EVIDENCE_FIRST

**Driver:** The principal driver is persistent household need for trusted, physical care and upkeep, with a small layer of AI-assistable planning and administration.
**Weakness:** The principal weakness is structural: NAICS 814110 contains household employers rather than external-customer operating firms that can be acquired and rolled up.

## Business-model lens
- Included: The official NAICS 814110 population: U.S. private households directly employing workers on or about the premises for household operation, including nannies, babysitters, cooks, maids, housekeepers, butlers, caretakers, drivers, non-medical aides, private nurses, gardeners, and other yard or maintenance workers.
- Excluded: Agencies or independent businesses that control and supply childcare, cleaning, lawn, personal-care, nursing, or other household services to customers; self-employed workers offering services to the public; non-medical personal-care providers and child day-care establishments classified elsewhere; households without employees; and any activity outside the target external-customer LMM firm lens.
- Customer and revenue model: Households are employers and pay employees wages hourly, daily, weekly, or by the job; they may owe payroll taxes and keep employment records. The classified household is not an operating firm selling a recurring outsourced service to external customers, so the screen's customer-revenue and transferable-firm constructs do not apply coherently.
- Deviation from default lens: none; the default lens produces no eligible operating-firm population because NAICS 814110 classifies the household employer itself, while independently controlled agencies and service businesses are classified elsewhere

## Executive view
Private Households is a direct-employment category, not an outsourced-service firm market. AI may assist a limited set of planning, scheduling, record, and communication tasks, while most work remains physical or trust-intensive; the absence of receipts and firm-count anchors correctly exposes the screen mismatch.

## How AI changes the work
AI can help household workers and employers with schedules, shopping and meal plans, translation, instructions, activity ideas, records, and payroll reminders. Cleaning, cooking, childcare, personal attendance, driving, safety monitoring, and grounds work largely require physical presence and human accountability.

## Value capture
A household may reduce paid hours or avoid hiring through better coordination or consumer technology, but that is household expenditure savings. There is no in-code operating firm retaining a gross commercial benefit through customer pricing or contract renewals.

## Firm availability
The classified establishment is the household employer. Agencies and independent service businesses are outside 814110, normalized EBITDA is not meaningful for a household, the frozen firm-count input is missing, and no qualifying control-transfer population exists under the default lens.

## Demand durability
Direct demand for care, cleaning, meals, driving, and property upkeep is durable and BLS projects nearly flat private-household employment. The channel can shift among direct employees, agencies, independent contractors, household self-service, informal work, and consumer technology.

## Risks and uncertainty
The decisive issue is construct fit, compounded by missing receipts and firm-count data, informal employment, privacy and safety, heterogeneous duties, labor supply, worker classification, and substitution into service firms classified elsewhere.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | — | — | MISSING | — |
| n | — | — | — | MISSING | — |
| a | 0.08 | 0.16 | 0.28 | ESTIMATE | S1, S2, S4, S5, S6 |
| rho | 0.2 | 0.38 | 0.58 | ESTIMATE | S1, S2, S4, S5, S6 |
| e | 0 | 0 | 0 | PROXY | S1, S2 |
| s5 | — | — | — | MISSING | — |
| q | — | — | — | MISSING | — |
| d5 | 0.9 | 1 | 1.1 | PROXY | S1, S3 |
| o | — | — | — | MISSING | — |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | — | — | — | MISSING |
| F | — | — | — | MISSING |
| C | — | — | — | MISSING |
| D | — | — | — | MISSING |

## Caveats
- a: No representative occupation mix or wage-weighted task study is available for 814110; BLS OEWS explicitly excludes household workers.
- a: The mix between nannies, cleaners, cooks, aides, drivers, and grounds workers is unknown and materially affects exposure.
- a: Administrative tasks may be performed unpaid by household members rather than included in employee wages.
- rho: No source measures AI implementation in directly employed private-household work.
- rho: Households may use AI for unpaid coordination without reducing paid physical or care hours.
- rho: Safety, trust, and privacy constraints differ sharply across childcare, personal care, cooking, cleaning, driving, and grounds work.
- e: A household may be wealthy and employ several workers, but it is still a consuming household rather than a service firm with normalized EBITDA.
- e: Workers may be recruited through an agency while remaining household employees, but the household still does not sell services externally.
- e: Service agencies and self-employed providers can be investable businesses, but they are classified outside 814110.
- s5: Household wealth transfers and estate events are outside the qualifying-control-transfer construct.
- s5: Sales of domestic staffing or household-service agencies occur in other industry classifications.
- q: A household can retain personal savings from reduced paid hours, but that is consumer expenditure savings rather than operator commercial retention.
- q: Payroll-service or staffing-agency economics belong to firms classified outside 814110.
- d5: BLS employment is a labor-input proxy, not constant-price, constant-quality demand.
- d5: Official payroll data may miss informal household employment and shifts between direct employment, agencies, contractors, and unpaid household work.
- d5: Demand paths differ across childcare, elder support, cleaning, cooking, driving, and grounds work.
- o: Human presence and the roll-up operator construct are different: a nanny or housekeeper may remain necessary without creating an investable firm in this code.
- o: Agency-provided services can require accountable operators, but those agencies are classified outside 814110.

## Sources
- **S1** — [2022 NAICS Definition: 814110 Private Households](https://www.census.gov/naics/?details=814110&input=814110&year=2022) (accessed 2026-07-22): Official household-employer scope, named worker types, exclusions, lens fit, a, rho, e, and d5
- **S2** — [IRS Publication 926 (2026), Household Employer's Tax Guide](https://www.irs.gov/publications/p926) (accessed 2026-07-22): Household employee control test, wage and tax relationship, worker examples, distinction from self-employed and agency-controlled workers, a, rho, and e
- **S3** — [BLS Employment and Output by Industry, 2024-2034](https://www.bls.gov/emp/tables/industry-employment-and-output.htm) (accessed 2026-07-22): Private-household employment of 650,400 in 2024 and 653,000 projected for 2034; d5
- **S4** — [BLS Occupational Outlook Handbook: Childcare Workers](https://www.bls.gov/ooh/personal-care-and-service/childcare-workers.htm) (accessed 2026-07-22): Nanny and childcare duties involving supervision, safety, meals, hygiene, activities, schedules, records, and transport; a and rho
- **S5** — [BLS Occupational Outlook Handbook: Cooks](https://www.bls.gov/ooh/food-preparation-and-serving/cooks.htm) (accessed 2026-07-22): Private-household cook duties involving planning, shopping, preparation, cleaning, and physical food handling; a and rho
- **S6** — [BLS Occupational Outlook Handbook: Grounds Maintenance Workers](https://www.bls.gov/ooh/building-and-grounds-cleaning/grounds-maintenance-workers.htm) (accessed 2026-07-22): Physical groundskeeping duties, tools, safety, and stamina requirements; a and rho
