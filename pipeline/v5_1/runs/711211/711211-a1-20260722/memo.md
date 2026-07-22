# 711211 — Sports Teams and Clubs

*v5.1 Stage 1 research memo. Run `711211-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** no base (evidence-first) · A — · L — · interval STRUCTURAL_OUT → PRIORITY · readiness STRESS_TEST_ONLY · action EVIDENCE_FIRST

**Driver:** Recurring tickets, sponsorship, and media relationships support durable demand and allow digitally exposed commercial workflows around an operator-required live product.
**Weakness:** The frozen dataset estimates zero target-band firms, leaving eligibility undefined and any firm-transfer opportunity unsupported without direct team-level financial data.

## Business-model lens
- Included: Professional and semiprofessional U.S. sports teams or clubs in the lower-middle-market band that repeatedly provide live and mediated sports entertainment and associated sponsorship inventory to paying fans, sponsors, and media partners.
- Excluded: Major or other teams outside the lower-middle-market EBITDA band, recreational and youth teams, amateur leagues and associations, event promoters that do not participate, racetracks, independent athletes, captive teams, passive minority stakes, and non-control financing vehicles.
- Customer and revenue model: Recurring season and single-game ticket sales, sponsorship and advertising contracts, local or league-distributed media rights, suites and premium seating, concessions, merchandise and licensing, and league distributions; the mix varies materially by sport and league level.
- Deviation from default lens: none

## Executive view
Sports teams combine high recurring fan engagement and commercially valuable media and sponsorship inventory with a service core that software cannot independently provide. AI can improve the commercial and administrative perimeter, but the frozen dataset estimates no firms in the target EBITDA band, so there is no evidenced acquisition population under this screen and the eligible-firm share is undefined.

## How AI changes the work
AI can automate or accelerate fan communications, campaign and sponsorship content, ticket targeting, customer service, bookkeeping, scheduling, scouting summaries, video indexing, and some analytical preparation. The wage-weighted opportunity remains bounded because athlete and coach compensation is large, competitive performance is physical, and medical, roster, coaching, and live-event decisions require accountable humans.

## Value capture
Tickets are demand-priced, and sponsorship and media rights are negotiated or distributed through leagues rather than billed on cost-plus terms, so productivity benefits need not flow directly to customers. League revenue sharing, labor economics, vendor commissions, and reinvestment in roster or fan experience reduce what the operator ultimately retains.

## Firm availability
Recent minor-league baseball sales show that control transfers and multi-team ownership strategies occur, but league approvals and affiliation, venue, and community obligations constrain deals. More fundamentally, the frozen firm estimate is zero; without evidence of a target-band denominator, no eligibility share can be defended and transfer probability is only a counterfactual estimate for a hypothetical eligible club.

## Demand durability
Federal projections imply moderate real output growth for spectator sports, and recent MLB and NHL attendance and media indicators show strong major-league demand. Local and lower-tier clubs face much more volatility from team performance, discretionary spending, media fragmentation, venue quality, and league structure, but continuing sports demand overwhelmingly requires an accountable team operator.

## Risks and uncertainty
The decisive uncertainty is whether any firms actually occupy the target EBITDA band after normalizing player payroll, league distributions, venue arrangements, and related-party costs. Other risks include league approval, affiliation loss, media-rights disruption, collective bargaining, player injury and safety, local public-sector dependence, team-performance volatility, customer concentration, and the mismatch between broad spectator-sports data and sports-team operations.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.742 | — | OBSERVED | — |
| n | — | 0 | — | ESTIMATE | — |
| a | 0.1 | 0.16 | 0.24 | PROXY | S2, S3 |
| rho | 0.38 | 0.55 | 0.72 | ESTIMATE | S3 |
| e | — | — | — | MISSING | — |
| s5 | 0.12 | 0.2 | 0.28 | ESTIMATE | S5, S6 |
| q | 0.62 | 0.72 | 0.82 | ESTIMATE | S7, S8 |
| d5 | 0.96 | 1.11 | 1.25 | PROXY | S4, S9, S10 |
| o | 0.96 | 0.98 | 0.995 | ESTIMATE | S1, S9, S10 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 1.13 | 2.61 | 5.13 | ESTIMATE |
| F | — | — | — | MISSING |
| C | 10.00 | 10.00 | 10.00 | ESTIMATE |
| D | 9.22 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: The occupation data are for NAICS 711200 rather than 711211 and include racetrack and other spectator-sports employment.
- a: OEWS excludes self-employed workers and does not measure tasks already automated.
- a: Observed Claude usage is not equivalent to technical exposure or realized labor substitution.
- a: A small number of highly paid athletes can dominate wage weighting.
- rho: No implementation study specific to lower-middle-market sports teams was found.
- rho: Current adoption may already be high in analytics and ticketing, reducing incremental opportunity.
- rho: League rules, collective bargaining, and sensitive player data constrain autonomous use.
- e: The supplied n is an ESTIMATE derived with a broad Recreation margin and may not reflect player compensation, league distributions, venue economics, or team-specific accounting.
- e: A zero estimated count does not prove that no individual team has LMM normalized EBITDA.
- e: No neutral or zero eligibility share is substituted for the missing denominator.
- s5: The cited transactions demonstrate deal feasibility but do not provide a denominator or observed transfer rate.
- s5: Minor-league baseball may be more actively consolidating than other sports or semiprofessional leagues.
- s5: The primitive is counterfactual in this packet because the frozen LMM firm count is zero.
- q: The public-company evidence comes from major-league teams far above the target band.
- q: Minor-league teams may face more price competition from local entertainment and greater pressure from affiliates or venue partners.
- q: Savings reinvested in the team are not retained gross benefit for this construct.
- d5: BLS output covers all NAICS 711200, not only teams and clubs or the nonexistent frozen LMM subset.
- d5: MLB and NHL evidence reflects major leagues with stronger brands and media economics than most smaller teams.
- d5: Attendance and viewership are quantities related to, but not identical to, constant-quality service demand.
- o: No source directly measures five-year operator displacement for sports teams.
- o: Media consumption can become more software-mediated without eliminating the accountable team operator.
- o: Esports and synthetic sports could become stronger substitutes than current evidence indicates.

## Sources
- **S1** — [NAICS 711211 Sports Teams and Clubs definition](https://www.census.gov/naics/resources/archives/sect71.html) (accessed 2026-07-22): Defines the industry as professional or semiprofessional sports teams or clubs participating in live events before a paying audience and distinguishes recreational teams, leagues, and nonparticipating promoters.
- **S2** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 711200 Spectator Sports](https://www.bls.gov/oes/2023/may/naics4_711200.htm) (accessed 2026-07-22): Reports 150,300 jobs and detailed employment shares and wages, including management, business, computer, athlete, coach, media, sales, office, health, security, food-service, and event-attendant occupations.
- **S3** — [Anthropic Economic Index report: Economic primitives](https://www.anthropic.com/research/anthropic-economic-index-january-2026-report) (accessed 2026-07-22): Documents observed AI use by O*NET and SOC task groups and enterprise automation of office workflows including email, document processing, customer relationship management, and scheduling.
- **S4** — [Employment and output by industry, 2024-2034](https://www.bls.gov/emp/tables/industry-employment-and-output.htm) (accessed 2026-07-22): Projects NAICS 711200 real output from $63.9 billion in 2024 to $78.4 billion in 2034, a 2.1% compound annual increase, and employment from 171,500 to 179,600.
- **S5** — [Reading Fightin Phils Welcome Diamond Baseball Holdings as New Owner](https://www.milb.com/news/reading-fightin-phils-welcome-diamond-baseball-holdings-as-new-owner) (accessed 2026-07-22): Documents the June 2025 sale of the Double-A Reading Fightin Phils to Diamond Baseball Holdings, with the club retaining its affiliation and front-office staff.
- **S6** — [Houston Astros Announce Sale of Three Minor League Affiliates to Diamond Baseball Holdings](https://www.milb.com/news/astros-announce-sale-of-sug-and-two-affiliates-to-dbh) (accessed 2026-07-22): Documents the December 2025 agreed sale of Triple-A, Double-A, and Single-A clubs to a multi-club owner.
- **S7** — [Madison Square Garden Sports Corp. 2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/1636519/000163651925000027/msgs-20250630.htm) (accessed 2026-07-22): Describes membership, group, and dynamically priced single-game tickets; league and local media rights as significant recurring revenue; sponsorship and suite sales; and long-duration media contracts.
- **S8** — [Atlanta Braves Holdings, Inc. 2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/1958140/000110465926020650/batra-20251231x10k.htm) (accessed 2026-07-22): Reports 2025 baseball revenue by event, broadcasting, retail and licensing, and other sources, and describes contractual ticket, sponsorship, and broadcasting rate changes plus MLB revenue-sharing costs.
- **S9** — [MLB attendance reaches 71.4 million; three straight years of growth for first time since 2007](https://www.mlb.com/press-release/press-release-mlb-attendance-reaches-71-4-million-three-straight-years-of-growth-for-first-time-since-2007) (accessed 2026-07-22): Reports 71,409,421 attendance in 2025, a third consecutive year of growth, plus increases across national, local, and streaming viewership.
- **S10** — [NHL sets regular-season attendance record, passes 23 million for first time](https://www.nhl.com/news/nhl-sets-regular-season-attendance-record-in-2024-2025) (accessed 2026-07-22): Reports 23,014,458 attendance and 96.9% capacity in 2024-25, the league's third consecutive regular-season attendance record.
