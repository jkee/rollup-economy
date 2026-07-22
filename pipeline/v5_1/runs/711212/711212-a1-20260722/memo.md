# 711212 — Racetracks

*v5.1 Stage 1 research memo. Run `711212-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 5.32 · L 0.71 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Fixed-price and statutory revenue structures let a capable operator retain part of repeatable administrative and commercial workflow savings without removing the accountable track operation.
**Weakness:** A contracting live-racing calendar combines with an exceptionally thin and unmeasured pool of eligible, transferable independent horse-track operators.

## Business-model lens
- Included: Privately controlled U.S. horse-racetrack operators that repeatedly stage live racing, run the racing office and wagering operation, maintain the racing surface and facility, and serve bettors, spectators, horsemen, sponsors, and event users.
- Excluded: Auto and dog racetracks; owners, trainers, jockeys, and other racing participants classified in 711219; pure casinos, online wagering platforms without track operations, captive internal units, public or nonprofit facilities without transferable control, shells, and non-control financing vehicles.
- Customer and revenue model: Recurring event and wagering revenue from pari-mutuel track commissions, admissions, hospitality, concessions, sponsorship, media or simulcast arrangements, and facility use. Customers include repeat bettors and spectators as well as horsemen, sponsors, and event counterparties; wagering economics are heavily prescribed by state law and horsemen agreements.
- Deviation from default lens: The code mixes horse, auto, and dog racetrack models with materially different regulation, workflows, and revenue mechanisms. The lens is narrowed to horse-racetrack operators for a coherent operating case, without selecting operators for attractiveness.

## Executive view
The coherent opportunity is not the full racetrack code but a small subset of privately controlled horse-track operators. AI can improve administrative, marketing, wagering-support, reporting, and customer-service workflows, yet much of the cost base and service promise remains physical, event-driven, safety-critical, and regulated. The main commercial attraction is that internal savings are not usually subject to cost-plus pass-through; the main constraint is a shrinking live-racing calendar and a very thin, poorly observed pool of transferable firms.

## How AI changes the work
Near-term use cases include customer-response drafting, marketing segmentation and content, sponsor materials, scheduling, invoice and payroll support, wagering exception triage, reconciliation assistance, record extraction, compliance-document preparation, and management reporting. Human review remains central for payouts and disputes, regulatory status enforcement, safety decisions, surface maintenance, veterinary activity, security, and live-event execution. The result is a moderate exposed share with only partial five-year implementation.

## Value capture
Admissions, hospitality, sponsorship, and many venue revenues are fixed-price, which supports retention of internal efficiency gains. Wagering is less flexible: statutory takeout, mandated distributions, purses, horsemen relationships, rebates, and competition for handle constrain how much benefit becomes durable operator economics. Savings may also be reinvested in the fan experience or race product to protect demand.

## Firm availability
Census places horse, auto, and dog track operators together, but the operating cases are not interchangeable. After excluding non-horse tracks, public or nonprofit control, casino-dominant operations, and businesses lacking transferable control, only a minority of the frozen all-code firm population is likely eligible. Specialized licenses, real estate, racing dates, and strategic ownership also make qualifying control transfers infrequent and difficult to separate from asset or regulatory transactions.

## Demand durability
Historical Thoroughbred evidence is weak for growth: reported race count fell from 40,798 in 2019 to 33,410 in 2025, while nominal handle was roughly flat. Digital wagering can preserve betting activity and a track can add hospitality or non-race events, but the current live-racing basket faces closures, substitute gambling, audience aging, and welfare scrutiny. For surviving demand, an accountable physical operator remains highly durable because race staging, accreditation, safety, wagering integrity, and facility maintenance cannot become pure software.

## Risks and uncertainty
The biggest empirical gaps are six-digit occupation weights, current task automation, a complete ownership census, and verified track control-transfer history. The frozen compensation ratio uses 2024 wages over 2022 receipts and the frozen firm count is an estimate for the whole six-digit code; both are imperfect matches to the narrowed horse-track lens. State subsidies and gaming rights can dominate economics, HISA covers Thoroughbred rather than all horse racing, and a facility may cease racing or be redeveloped instead of transferring as a going concern.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.153 | — | OBSERVED | — |
| n | — | 76 | — | ESTIMATE | — |
| a | 0.13 | 0.22 | 0.32 | PROXY | S2, S3, S4, S5 |
| rho | 0.35 | 0.53 | 0.7 | ESTIMATE | S3, S4, S5 |
| e | 0.18 | 0.34 | 0.52 | ESTIMATE | S1 |
| s5 | 0.07 | 0.15 | 0.25 | ESTIMATE | S8 |
| q | 0.43 | 0.61 | 0.76 | PROXY | S7 |
| d5 | 0.72 | 0.86 | 1 | PROXY | S6, S9 |
| o | 0.84 | 0.93 | 0.98 | PROXY | S5, S10 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.28 | 0.71 | 1.37 | ESTIMATE |
| F | 1.08 | 2.55 | 3.84 | ESTIMATE |
| C | 8.60 | 10.00 | 10.00 | PROXY |
| D | 6.05 | 8.00 | 9.80 | PROXY |

## Caveats
- a: The occupational source is NAICS 711200, not 711212, and includes sports teams and clubs whose athlete and media wage mix is unlike a racetrack.
- a: O*NET task lists establish task content but do not measure current automation, time shares, wage weights, or technical substitutability.
- a: The estimate excludes already automated self-service and online wagering from the remaining opportunity, but no track-level baseline was obtainable.
- rho: This is bounded judgment rather than a measured five-year adoption rate.
- rho: Capital constraints at small tracks, legacy totalizator integrations, union arrangements, and state-by-state approvals could slow deployment.
- rho: HISA governs Thoroughbred racing nationally but does not cover every horse-racing breed or every included workflow.
- e: The frozen firm-count input is for all of 711212, while this lens excludes auto and dog tracks, making the population mismatch material.
- e: Establishment classification does not reveal firm-level control, contract structure, nonprofit status, or whether racetrack operations are economically separable from a casino.
- e: The default lens is difficult to apply because many operators sell experiences directly to patrons rather than a conventional outsourced B2B service.
- s5: BizBuySell is a voluntary broad small-business marketplace and does not measure racetrack transactions or a transfer probability.
- s5: No defensible national data on horse-track owner age, succession plans, or qualifying control transfers was found.
- s5: A transfer of real estate, racing dates, or a wagering license may not constitute transfer of an intact operating firm.
- q: California is one large state and not representative of every jurisdiction or breed.
- q: The source describes distribution of wagering revenue, not direct contractual sharing of AI savings.
- q: The value-capture mix differs for admissions, hospitality, sponsorship, media, concessions, and wagering.
- d5: The source covers Thoroughbred racing in the U.S., Canada, and Puerto Rico rather than only U.S. establishments.
- d5: Handle is nominal and is not itself constant-price demand; race count omits quality, attendance, digital engagement, and non-racing venue use.
- d5: Historical contraction does not identify the future effects of state subsidies, new gaming formats, media distribution, or track redevelopment.
- o: HISA applies to Thoroughbred racing and is not a direct quantity forecast.
- o: Some customer-facing wagering and information services can migrate entirely to apps or third-party platforms even while a track operator remains required.
- o: The estimate concerns operator-required service quantity, not preservation of current headcount.

## Sources
- **S1** — [North American Industry Classification System: 711212 Racetracks](https://www.census.gov/naics/resources/archives/sect71.html) (accessed 2026-07-22): Defines 711212 as establishments operating racetracks that may present or promote auto, dog, and horse races, and distinguishes participant owners, trainers, and athletes in 711219.
- **S2** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 711200 Spectator Sports](https://www.bls.gov/oes/2023/may/naics4_711200.htm) (accessed 2026-07-22): Provides the broader-industry occupation mix, including management at 9.60%, sales at 8.13%, office and administrative support at 8.17%, protective service at 3.74%, food service at 4.29%, and building and grounds work at 2.60% of employment.
- **S3** — [O*NET OnLine: Gambling and Sports Book Writers and Runners](https://www.onetonline.org/link/summary/39-3012.00) (accessed 2026-07-22): Describes wagering work that includes receiving, verifying, and recording bets, processing winning tickets, computing results, paying winnings, and answering rules questions.
- **S4** — [O*NET OnLine: Amusement and Recreation Attendants](https://www.onetonline.org/link/summary/39-3091.00) (accessed 2026-07-22): Shows the blend of ticket sales, customer information, attendance and receipt records, safety monitoring, patron direction, cleaning, and equipment inspection in venue-attendant work.
- **S5** — [Horseracing Integrity and Safety Authority: Racetrack Personnel](https://hisaus.org/?occupation=racetrack-personnel) (accessed 2026-07-22): Identifies track management, racing office, maintenance and facilities, and accreditation responsibilities; documents written maintenance procedures, pre-meet and daily surface testing, reporting, onsite inspection, and annual reports.
- **S6** — [The Jockey Club Fact Book: Pari-Mutuel Handle](https://www.jockeyclub.com/factbook/handle.asp?add=&print=Y&section=8) (accessed 2026-07-22): Reports total U.S., Canada, and Puerto Rico handle of $11.722 billion in 2019 and $11.814 billion in 2025, with coverage and rounding notes.
- **S7** — [California Horse Racing Board Annual Report, Fiscal Year 2024-25](https://www.chrb.ca.gov/DocumentRequestor2.aspx?Category=REPORTS&DocumentID=00052729&SubCategory=ANNUAL) (accessed 2026-07-22): States that takeout is set by law; reports conventional Thoroughbred takeout of 15.43%, exotic Thoroughbred takeout of 22.68% or 23.68%, mandated deductions, prescribed division between purses and track commissions, and $87.1 million retained track commissions.
- **S8** — [BizBuySell Insight Report: Small Business Acquisitions Grow 5% in 2024](https://www-tsm2.bizbuysell.com/insight-report/) (accessed 2026-07-22): Reports 9,546 voluntarily reported broad small-business transactions in 2024 and describes marketplace deal conditions; used only as directional transfer-channel evidence, not a racetrack probability.
- **S9** — [The Jockey Club Fact Book: Number of Races by Distance and Surface](https://www.jockeyclub.com/default.asp?area=20&section=FB) (accessed 2026-07-22): Reports 40,798 Thoroughbred races in 2019 and 33,410 in 2025 across the U.S., Canada, and Puerto Rico.
- **S10** — [Horseracing Integrity and Safety Authority: HISA 101](https://hisaus.org/about-us?cat=racetrack-safety-committee) (accessed 2026-07-22): Explains uniform Thoroughbred racetrack rules, accreditation, veterinary oversight, surface maintenance and daily testing, reporting, safety measures, and data obligations.
