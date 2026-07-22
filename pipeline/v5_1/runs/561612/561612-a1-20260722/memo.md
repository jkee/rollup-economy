# 561612 — Security Guards and Patrol Services

*v5.1 Stage 1 research memo. Run `561612-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** PRIORITY · A 6.43 · L 4.70 · interval LOW_PRIORITY → HIGHEST_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** AI-assisted monitoring, scheduling, dispatch, and reporting can improve coverage per labor hour across a very wage-intensive recurring service.
**Weakness:** Most guard value is embodied physical presence sold by the hour, limiting both substitutable task share and the provider's ability to retain savings.

## Business-model lens
- Included: US lower-middle-market firms providing recurring or repeat outsourced staffed security posts, mobile patrols, access control, visitor screening, parking security, event security, bodyguard, guard-dog, alarm-response, and related on-site protective services to external customers.
- Excluded: Captive in-house guards, public police, installation or remote monitoring of electronic security systems classified in NAICS 56162, armored-car services, investigation services, one-off engagements without a repeat service relationship, shells, and non-control financing vehicles.
- Customer and revenue model: Commercial property owners, residential communities, healthcare and educational institutions, industrial sites, retailers, event operators, government agencies, and other organizations buy guard hours, staffed posts, patrol routes, screening, or protection under recurring contracts, repeat work orders, or scheduled events, commonly priced per labor hour, post, route, or fixed contract period.
- Deviation from default lens: none

## Executive view
Security guarding is exceptionally labor-intensive, but most labor buys physical presence rather than information processing. AI video analytics, alarm triage, workforce scheduling, patrol verification, dispatch, and report automation can reduce selected hours and supervision, while deterrence, access intervention, screening, patrol, first aid, emergency response, and liability preserve a large operator-required core.

## How AI changes the work
AI can identify people, vehicles, objects, and unusual events across camera feeds; prioritize alarms; optimize schedules and patrol routes; verify post attendance; summarize logs; and draft incident reports. Guards still inspect, confront, escort, screen, de-escalate, administer first aid, coordinate responders, and act when systems fail or circumstances are ambiguous.

## Value capture
Fixed-price contracts can retain productivity gains until renewal, but per-hour and cost-plus pricing, wage escalation, frequent competitive bids, customer ownership of security systems, and broadly available technology transmit much of the benefit to customers. Integration, training, privacy, cyber, insurance, and monitoring-center expense also consume savings.

## Firm availability
The code closely matches recurring outsourced security, so most properly classified LMM firms plausibly fit the lens. Transferability depends on licenses, bonding, insurance, supervisors, recruiting and retention, customer consent, labor liabilities, and concentration in a few site contracts; the broad margin bridge may materially misstate the LMM count in this thin-margin industry.

## Demand durability
Crime and vandalism concerns, occupied facilities, access control, and emergency-response needs support a stable service core. BLS expects little employment change and notes that AI-enabled remote monitoring can limit some positions, while a current federal case shows that missing guards can close facilities; end-market demand therefore looks durable but mature and technology-sensitive.

## Risks and uncertainty
The principal risks are hourly billing that passes savings through, customer-controlled technology, low margins, wage inflation, high turnover, overtime, guard shortages, licensing and insurance, labor claims, contract concentration, rebids, false alarms, privacy and cyber failures, and substitution of remote monitoring for low-risk posts. The injected compensation ratio has a wage-receipts vintage mismatch, and the firm count relies on a broad margin assumption.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.9066 | — | OBSERVED | — |
| n | — | 625 | — | ESTIMATE | — |
| a | 0.12 | 0.24 | 0.36 | PROXY | S2, S3 |
| rho | 0.3 | 0.54 | 0.73 | PROXY | S2, S4, S5 |
| e | 0.7 | 0.86 | 0.95 | ESTIMATE | S1 |
| s5 | 0.08 | 0.15 | 0.24 | PROXY | S6 |
| q | 0.15 | 0.31 | 0.49 | ESTIMATE | S2, S4 |
| d5 | 0.9 | 1.02 | 1.14 | PROXY | S2, S5 |
| o | 0.58 | 0.76 | 0.89 | PROXY | S2, S3, S4, S5 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 1.31 | 4.70 | 9.53 | PROXY |
| F | 5.76 | 7.08 | 7.99 | ESTIMATE |
| C | 3.00 | 6.20 | 9.80 | ESTIMATE |
| D | 5.22 | 7.75 | 10.00 | PROXY |

## Caveats
- a: The occupation includes guards employed directly by customers and workers in adjacent investigation and armored-car activities.
- a: No source measures the current automation baseline or wage-weighted task mix of lower-middle-market contract-guard firms.
- a: Exposure varies sharply between static camera-monitoring posts, mobile patrols, armed protection, access control, and event security.
- a: The injected compensation ratio combines 2024 wages and 2022 receipts, creating a stated vintage mismatch outside this primitive.
- rho: BLS provides an occupational outlook, not a measured adoption rate for 561612 firms.
- rho: SIA is a security-technology industry association and describes capabilities and safeguards rather than representative realized savings.
- rho: Customer ownership of cameras, access systems, and networks can slow contractor-led implementation.
- rho: GAO's federal contract-guard findings are a public-sector case and may not generalize to commercial sites.
- e: The Census definition does not measure recurring revenue, contract transferability, or the eligible share of LMM firms.
- e: Special-event and bodyguard work may be repeat business but can be materially less recurring than staffed-site contracts.
- e: The injected count of 625 uses a broad Business and Consumer Services margin bridge that may not reflect thin-margin, wage-intensive guard firms.
- s5: Gallup covers all US employer businesses and measures intentions rather than completed transactions.
- s5: No industry-specific owner-age or completed-control-deal series was found.
- s5: Customer change-of-control rights, licensing, insurance, wage claims, and contract concentration can prevent a planned sale from qualifying.
- q: No source directly measures five-year retention of AI-derived benefits for US lower-middle-market guard contractors.
- q: Retention differs between fixed-price outcomes, per-post contracts, and cost-plus or per-hour staffing.
- q: Customer security budgets may convert labor savings into expanded coverage rather than provider margin.
- d5: BLS forecasts occupation employment across outsourced and captive employers, not purchased 561612 service quantity.
- d5: GAO examines one federal program and does not represent commercial contract demand.
- d5: Guard demand varies with office occupancy, retail conditions, events, crime concerns, public budgets, and customer technology adoption.
- o: Occupational duties do not measure the fraction of contracted service quantity that customers will continue purchasing.
- o: Remote monitoring and automated access control can fully replace some low-risk static posts.
- o: Federal facility evidence may overstate operator requirements relative to commercial sites, while armed and high-risk assignments may require more.

## Sources
- **S1** — [2022 North American Industry Classification System Manual: 561612](https://www.census.gov/naics/reference_files_tools/2022_NAICS_Manual.pdf) (accessed 2026-07-22): Defines 561612 as establishments primarily providing guard and patrol services and gives bodyguard, guard-dog, and parking-security examples.
- **S2** — [Security Guards and Gambling Surveillance Officers — Occupational Outlook Handbook](https://www.bls.gov/ooh/protective-service/security-guards.htm) (accessed 2026-07-22): Describes patrol, access control, alarm and video monitoring, emergency response, deterrence, screening, and reporting; reports that 59% of guards work in investigation, guard, and armored-car services; projects little employment change through 2034; and says AI-enabled remote monitoring may limit employment while protection demand persists.
- **S3** — [O*NET OnLine: Security Guards](https://www.onetonline.org/link/details/33-9032.00) (accessed 2026-07-22): Ranks locking entrances, patrol, medical response, alarm investigation, access authorization, reporting, enforcement, emergency calls, screening-device operation, and equipment inspection among guard tasks.
- **S4** — [SIA Data Privacy Code of Practice for Video Surveillance](https://www.securityindustry.org/report/data-privacy-code-of-practice-video-surveillance/) (accessed 2026-07-22): Explains that AI-powered video systems can recognize people, vehicles, objects, and events, generate alarms, reduce surveillance-fatigue error, and improve response, while requiring privacy and security controls.
- **S5** — [Federal Protective Service: Actions Needed to Address Critical Guard Oversight and Information System Problems](https://www.gao.gov/assets/gao-25-108085.pdf) (accessed 2026-07-22): Reports FPS oversight of about 13,000 contract guards, detection and tracking weaknesses, and facility-service disruption from guard shortages, illustrating both persistent physical screening needs and digitizable oversight.
- **S6** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Reports that 22% of US employer-business owners planned to sell or transfer ownership within five years in a fall 2024 survey.
