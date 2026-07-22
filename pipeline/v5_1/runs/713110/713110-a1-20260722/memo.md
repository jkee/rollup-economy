# 713110 — Amusement and Theme Parks

*v5.1 Stage 1 research memo. Run `713110-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** LOW_PRIORITY · A 5.95 · L 1.25 · interval STRUCTURAL_OUT → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** A mostly irreplaceable physical guest experience preserves operator-required demand while direct consumer pricing allows meaningful retention of successfully implemented savings.
**Weakness:** Most labor is frontline, physical, safety-sensitive, and seasonal, sharply limiting the portion of wages that AI can remove within five years.

## Business-model lens
- Included: US lower-middle-market operators of amusement parks, theme parks, and water parks that earn repeat admissions and in-park revenue from external guests, including season-pass and group customers.
- Excluded: Single-ride concessionaires, arcades, equipment suppliers, event promoters, captive resort attractions, government or nonprofit facilities unavailable for control, shells, and non-control financing vehicles.
- Customer and revenue model: Predominantly direct-to-consumer admissions, season or annual passes, food and beverage, retail, games, parking, and premium add-ons; group sales and sponsorships are secondary.
- Deviation from default lens: none

## Executive view
Amusement and theme parks combine a durable need for accountable physical operators with a relatively narrow AI labor opportunity. The best use cases sit around the park rather than on the ride: ticketing, guest communications, pricing, scheduling, marketing, reporting, finance, and HR. Transferability is plausible, but asset intensity, real-estate structure, seasonality, and constant reinvestment make the operating business more complex than a conventional service company.

## How AI changes the work
AI can draft and personalize marketing, answer routine guest questions, assist contact-center agents, forecast attendance, optimize labor schedules and prices, reconcile transactions, and summarize operating data. The largest occupation, amusement and recreation attendants, also performs physical boarding, inspection, cleaning, ride operation, and safety monitoring, so only part of that wage pool is exposed and implementation requires human escalation and audit trails.

## Value capture
Direct posted-price admissions and in-park purchases create no automatic cost-plus pass-through. Operators can retain gains through margin, selectively lower promotions, or reinvest in attractions and service. Competitive entertainment choices, affordability, pass renewal pricing, and guest expectations will share a meaningful portion of the benefit over five years.

## Firm availability
Most in-band park operators should be coherent, repeat-revenue operating businesses, but some are captive, public, nonprofit, owner-dependent, or entangled with land ownership. Cross-industry succession evidence suggests a mid-teens five-year control-transfer probability after discounting intentions and excluding nonqualifying transfers.

## Demand durability
Physical park visits cannot be replaced wholesale by software, but quantity demand is discretionary and volatile. Recent broader real recreation spending declined after the post-pandemic rebound while industry attendance expectations remained positive, supporting a roughly flat central five-year outlook with a wide range. Maintaining constant quality requires recurring attraction and maintenance capital.

## Risks and uncertainty
The principal risks are safety and liability, weather and seasonality, consumer affordability, labor shortages, local competition, and large maintenance or attraction-capex needs. Evidence on independent parks is sparse: occupation data include arcades, demand data include campgrounds, succession evidence spans all employer businesses, and public-company practices may overstate LMM technology capacity and pricing power.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.3003 | — | OBSERVED | — |
| n | — | 42 | — | ESTIMATE | — |
| a | 0.11 | 0.2 | 0.3 | PROXY | S1, S2, S3, S4 |
| rho | 0.32 | 0.52 | 0.7 | PROXY | S2, S4, S5 |
| e | 0.55 | 0.72 | 0.86 | ESTIMATE | S8 |
| s5 | 0.09 | 0.16 | 0.25 | PROXY | S6, S7 |
| q | 0.48 | 0.69 | 0.86 | PROXY | S5, S6 |
| d5 | 0.84 | 1.01 | 1.18 | PROXY | S9, S10 |
| o | 0.88 | 0.96 | 0.99 | ESTIMATE | S2, S5, S6 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.42 | 1.25 | 2.52 | PROXY |
| F | 1.81 | 2.84 | 3.71 | ESTIMATE |
| C | 9.60 | 10.00 | 10.00 | PROXY |
| D | 7.39 | 9.70 | 10.00 | ESTIMATE |

## Caveats
- a: The closest detailed BLS occupation table is NAICS 713100, which includes arcades as well as amusement and theme parks.
- a: Task exposure is a judgmental mapping, not measured AI displacement, and excludes work already automated.
- a: Seasonal and part-time work makes annual-wage weighting less precise.
- rho: Public-company initiatives may not transfer to capital-constrained independent parks.
- rho: Avoided seasonal hiring may be more achievable than permanent headcount reduction.
- rho: Safety, accessibility, and guest-service failures could halt or reverse implementation.
- e: Census reports establishments, while the frozen dataset input is firms; chains can own multiple parks.
- e: Eligibility cannot be observed from public industry counts.
- e: Real-estate ownership and operating control may be split.
- s5: Gallup is cross-industry and reports intentions, not realized deals.
- s5: Public-company mergers are much larger than the target band.
- s5: Family transfers may not create an actionable third-party control opportunity.
- q: No source isolates customer pass-through of AI-derived savings.
- q: Local competitive intensity and park differentiation vary widely.
- q: A safety or service degradation would force reinvestment and reduce retained benefit.
- d5: The BEA series includes campgrounds and related recreational services.
- d5: Attendance forecasts and consumer spending are sensitive to recession, weather, travel patterns, and major new rides.
- d5: Constant-quality demand is difficult to separate from continual capital additions.
- o: The estimate distinguishes operator-required demand from labor intensity; automation can reduce staffing without eliminating the operator.
- o: A major shift toward virtual entertainment could reduce visits but belongs mainly in d5.
- o: Rules and insurer requirements vary by state and attraction type.

## Sources
- **S1** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 713100 Amusement Parks and Arcades](https://www.bls.gov/oes/2023/May/naics4_713100.htm) (accessed 2026-07-22): Reports 227,040 total industry workers and detailed employment shares and wages, including amusement attendants at 30.66%, cashiers at 6.61%, office and administrative support at 4.50%, management at 3.40%, and customer-service representatives at 1.09%.
- **S2** — [O*NET: Amusement and Recreation Attendants, 39-3091.00](https://www.onetonline.org/link/details/39-3091.00) (accessed 2026-07-22): Lists attendant tasks spanning ticket sales, information, records, scheduling, safety monitoring, boarding assistance, cleaning, inspection, and ride operation; reports 96% constant contact with others and 91% extremely important public contact.
- **S3** — [O*NET: Customer Service Representatives, 43-4051.00](https://www.onetonline.org/link/summary/43-4051.00) (accessed 2026-07-22): Describes routine information, order entry, recordkeeping, complaint resolution, billing, and escalation tasks relevant to park guest service.
- **S4** — [Anthropic Economic Index: New building blocks for understanding AI use](https://www.anthropic.com/research/economic-index-primitives) (accessed 2026-07-22): Reports highly uneven occupational AI use; in November 2025 Claude.ai interactions were 52% augmentation and 45% automation, while computer and mathematical tasks remained disproportionately represented.
- **S5** — [United Parks & Resorts 2024 Form 10-K](https://www.sec.gov/Archives/edgar/data/1564902/000095017025030398/prks-20241231.htm) (accessed 2026-07-22): Describes admissions, passes, in-park revenue, demand-based pricing, hiring challenges, technology cost initiatives, safety and regulatory constraints, principal operating costs, seasonality, and the need for annual attraction investment.
- **S6** — [Six Flags Entertainment Corporation 2024 Form 10-K](https://www.sec.gov/Archives/edgar/data/1999001/000199900125000052/fun-20241231.htm) (accessed 2026-07-22): Defines attendance and revenue from tickets, season passes, memberships, food, beverage, retail, games, parking, online transaction fees, premium products, resorts, and sponsorships; documents the 2024 Cedar Fair/Six Flags combination.
- **S7** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Reports that 52.3% of US employer businesses are owned by people age 55 or older and 22% of employer-business owners planned to sell or transfer ownership within five years.
- **S8** — [Census Bureau Profile: NAICS 713110 Amusement and Theme Parks](https://data.census.gov/profile/713110_-_Amusement_and_theme_parks?codeset=naics~713110) (accessed 2026-07-22): Defines the industry as establishments operating a variety of attractions and reports 742 employer establishments; identifies single-attraction and concession operations as cross-references to other industries.
- **S9** — [Real personal consumption expenditures: Amusement parks, campgrounds, and related recreational services](https://fred.stlouisfed.org/series/DORSRX1A020NBEA) (accessed 2026-07-22): BEA real annual PCE series shows $74.811 billion chained 2017 dollars in 2023, $71.247 billion in 2024, and $69.176 billion in 2025.
- **S10** — [Industry Leaders Report Strong Outlook on Summer Travel Numbers and Industry Trends](https://iaapa.org/about/press-room/attraction-industry-leaders-report-strong-outlook-summer-travel-numbers-and-industry-trends) (accessed 2026-07-22): IAAPA expected a 2% boost in North American theme-park attendance to more than 300 million visits in 2024 and projected consumer spending above $32 billion.
