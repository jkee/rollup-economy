# 713210 — Casinos (except Casino Hotels)

*v5.1 Stage 1 research memo. Run `713210-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 5.10 · L 0.47 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Administrative, cage, compliance, and surveillance workflows offer bounded AI labor leverage while physical gaming demand remains operator-dependent.
**Weakness:** Nearly all casinos appear to be owner-operated direct-to-consumer venues, leaving very few firms eligible under the outsourced-service lens.

## Business-model lens
- Included: Lower-middle-market operators that repeatedly manage and staff a regulated stand-alone, floating, riverboat, or racetrack casino for an external property, tribal, or governmental license holder.
- Excluded: Owner-operated casinos selling gambling directly to patrons without an external operating customer; casino hotels; passive real-estate or license interests; captive internal operating units; financing vehicles; and firms outside the roughly $1-10M normalized EBITDA band.
- Customer and revenue model: The qualifying customer is an external casino property or license holder paying a recurring management or operating fee; the casino itself earns gross gaming revenue from repeat patron wagering and may also earn food-and-beverage revenue.
- Deviation from default lens: The default eligibility gate is applied strictly: only externally contracted casino management and operating relationships qualify. Direct-to-patron owner-operators are excluded because they do not supply an outsourced service to an external customer. This narrowing is required to keep the screen coherent, not to select for attractiveness.

## Executive view
Stand-alone casinos contain useful AI-assistable workflows in finance, cage operations, surveillance, compliance, marketing, and scheduling, but the ordinary casino is a direct-to-consumer venue rather than an outsourced-service provider. Under the fixed lens, only a rare externally contracted operating company qualifies, and that eligibility problem dominates the opportunity. The surviving eligible firms also face unusually consequential licensing and control-transfer review.

## How AI changes the work
AI is best suited to exception triage, reconciliation support, report drafting, loyalty communications, workforce scheduling, fraud-pattern detection, and prioritizing surveillance footage. It is less able to replace the physical and social core: dealing table games, handling secured cash, responding to patrons, maintaining facilities, providing food service, and exercising accountable compliance judgment. Human review remains important because mistakes can create loss, regulatory exposure, and customer distrust.

## Value capture
Casino patrons do not receive a labor-hours invoice, so savings are not automatically passed through. The manager may still share value through owner contract economics, renewal repricing, incentive formulas, comps, competitive reinvestment, and taxes. Retention depends far more on the unseen management agreement than on the casino's posted game economics.

## Firm availability
Most establishments in the code operate their own patron-facing gambling facility and therefore fail the outsourced-service gate. A small set of contract managers may qualify, but their classification and independence need name-by-name verification. Even when an eligible owner wants to sell, gaming experience requirements, regulator approval, license linkage, and scrutiny of officers and directors narrow the buyer pool.

## Demand durability
Land-based slots and table games remain large and recently grew in nominal dollars, but growth was modest compared with iGaming. Mature-market physical demand is likely roughly flat in real terms over five years, with legalization and new properties supporting some markets while recession, saturation, and online migration pressure others. Physical casino quantity that survives still generally needs an accountable licensed operator.

## Risks and uncertainty
The largest uncertainty is whether any meaningful LMM population actually meets the lens; eligible count could be zero. Additional risks are a broad four-digit occupation proxy, no representative management-contract sample, no denominator-consistent control-transfer history, regulatory variation, already-automated slot operations, online substitution, and using gross gaming revenue as a noisy demand proxy. A direct operator census and contract review could materially change the conclusion.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1596 | — | OBSERVED | — |
| n | — | 120 | — | ESTIMATE | — |
| a | 0.15 | 0.24 | 0.34 | ESTIMATE | S2, S3, S4, S5 |
| rho | 0.3 | 0.5 | 0.7 | ESTIMATE | S4, S5, S8 |
| e | 0 | 0.02 | 0.05 | ESTIMATE | S1, S7 |
| s5 | 0.07 | 0.14 | 0.25 | ESTIMATE | S8 |
| q | 0.45 | 0.68 | 0.85 | ESTIMATE | S6, S7 |
| d5 | 0.88 | 1.02 | 1.15 | PROXY | S6, S9 |
| o | 0.78 | 0.9 | 0.97 | ESTIMATE | S3, S4, S5, S6, S8 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.29 | 0.77 | 1.52 | ESTIMATE |
| F | 0.00 | 0.47 | 1.47 | ESTIMATE |
| C | 9.00 | 10.00 | 10.00 | ESTIMATE |
| D | 6.86 | 9.18 | 10.00 | ESTIMATE |

## Caveats
- a: The BLS occupation mix is NAICS 713200, which also includes other gambling industries, rather than six-digit NAICS 713210 alone.
- a: Employment shares are not wage weights; the estimate qualitatively adjusts for higher-paid administrative and management work.
- a: O*NET task descriptions identify work content but do not measure AI exposure or remaining automation headroom.
- rho: No source measures five-year implementation for contract-managed stand-alone casinos.
- rho: State rules differ, and the Arkansas transfer rule is evidence of regulated control rather than a technology rule.
- rho: Current automation maturity is not measured, so the remaining opportunity may be overstated.
- e: The 120-firm dataset estimate may include entities whose receipts or legal structure do not map cleanly to operating companies.
- e: AGA's 492 commercial-casino count spans facilities and business models and is not a count of eligible firms.
- e: The estimate could be exactly zero if contract managers are classified outside NAICS 713210.
- s5: The Arkansas rule is one jurisdiction and cannot establish a national transfer rate.
- s5: No evidence on owner age, succession readiness, or denominator-consistent eligible-firm deals was found.
- s5: A transfer of a property, license, or passive interest may not be a qualifying transfer of the operating firm.
- q: No representative management-contract dataset was found.
- q: AGA revenue and tax figures cover commercial gaming broadly, not the narrow contract-managed LMM population.
- q: The result is sensitive to whether labor savings accrue to the manager or the property/license owner under the contract.
- d5: Gross gaming revenue is price, mix, hold, and quantity combined; it is not a direct constant-quality quantity measure.
- d5: AGA commercial data do not cover all tribal gaming and include properties outside NAICS 713210.
- d5: Two annual growth observations are a weak basis for a five-year forecast.
- o: The estimate separates operator requirement from headcount; an operator can remain necessary with far fewer employees.
- o: Online substitution is reflected here only when it eliminates physical-facility quantity, while general demand change is assigned to d5.
- o: Regulatory requirements vary materially by state and tribal jurisdiction.

## Sources
- **S1** — [2022 NAICS Definition: 713210 Casinos (except Casino Hotels)](https://www.census.gov/naics/?details=7132&input=7132&year=2022) (accessed 2026-07-22): Defines 713210 as establishments operating gambling facilities with table wagering plus slots or sports betting, often with food and beverage, and includes floating casinos and casinos with racetracks.
- **S2** — [May 2022 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 713200 Gambling Industries](https://www.bls.gov/oes/2022/may/naics4_713200.htm) (accessed 2026-07-22): Reports 201,540 workers and the detailed occupation mix, including 25.78% personal care/service, 17.78% food service, 11.13% protective service, 11.06% office/administrative support, and casino-specific roles.
- **S3** — [O*NET OnLine: Gambling Dealers](https://www.onetonline.org/link/details/39-3011.00) (accessed 2026-07-22): Describes dealer tasks including paying winnings, greeting customers, handling chips and wagers, inspecting equipment, dealing games, applying rules, and answering patron questions.
- **S4** — [O*NET OnLine: Gambling Cage Workers](https://www.onetonline.org/link/summary/43-3041.00) (accessed 2026-07-22): Describes secure patron financial transactions, credit verification, reconciliation, record checking, computer use, and very high accuracy and customer-contact requirements.
- **S5** — [O*NET OnLine: Gambling Surveillance Officers and Gambling Investigators](https://www.onetonline.org/link/details/33-9031.00) (accessed 2026-07-22): Describes regulatory monitoring, video observation and review, suspicious-behavior reporting, surveillance logs, equipment inspection, investigation, and accountable oversight.
- **S6** — [2024 Commercial Gaming Revenue Reaches $71.9B](https://www.americangaming.org/2024-commercial-gaming-revenue-reaches-71-9b-marking-fourth-straight-year-of-record-revenue/) (accessed 2026-07-22): Reports $49.78 billion of 2024 brick-and-mortar slot and table revenue, up 82 basis points; online gaming at 30.0% of commercial gaming revenue; iGaming growth of 28.7%; and $15.66 billion in gaming taxes.
- **S7** — [State of the States 2025](https://www.americangaming.org/resources/state-of-the-states-2025/) (accessed 2026-07-22): Reports 492 U.S. commercial casinos, $49.89 billion in 2024 traditional casino revenue, $15.91 billion of direct gaming taxes, and state-by-state regulatory coverage.
- **S8** — [23 CAR Section 358-217: Transfer of license](https://codeofarrules.arkansas.gov/Rules/Rule?chapterID=238&levelType=section&partID=1258&sectionID=52159&subChapterID=295&subPartID=7965&titleID=23) (accessed 2026-07-22): States that a casino license is effective only for the named entity; transfer requires a buyer with casino gaming experience and Arkansas Racing Commission approval; officer and director changes also require prior approval.
- **S9** — [Commercial Gaming Revenue Hits $78.7 Billion in 2025](https://www.americangaming.org/commercial-gaming-revenue-hits-78-7-billion-in-2025-driving-record-18-1-billion-in-gaming-taxes-nationwide/) (accessed 2026-07-22): Reports $50.94 billion of 2025 traditional gaming revenue, up 2.3%, alongside much faster sports-betting and iGaming growth.
