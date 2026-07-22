# 812199 — Other Personal Care Services

*v5.1 Stage 1 research memo. Run `812199-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** CONDITIONAL · A 6.58 · L 2.94 · interval LOW_PRIORITY → PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** A high share of current-basket quantity still requires local physical delivery, while common administrative workflows offer implementable AI savings.
**Weakness:** The six-digit code is heterogeneous and practitioner-dependent, leaving firm eligibility and qualifying transfer rates weakly evidenced.

## Business-model lens
- Included: US lower-middle-market firms in NAICS 812199 providing repeat external-customer personal-care services, including nonmedical hair-removal, tattoo and piercing, permanent-makeup, tanning, sauna or steam-bath, hair-replacement, and related day-spa services.
- Excluded: Hair, nail, facial, and nonmedical diet or weight-reducing services assigned to other industries; medical or surgical services; self-service-only machines; shells, captive internal units, non-control financing vehicles, and firms outside the approximate $1-10 million normalized EBITDA band.
- Customer and revenue model: Primarily consumer-paid appointments, sessions, packages, memberships, and product add-ons; revenue is local, transaction-heavy, and often driven by repeat visits, referrals, practitioner reputation, and capacity utilization.
- Deviation from default lens: none

## Executive view
Other personal-care services combine a meaningful but bounded back-office AI opportunity with service delivery that remains highly physical and local. The recurring customer relationship is attractive operationally, but heterogeneous service lines, practitioner dependence, and uncertain LMM transfer volume limit confidence.

## How AI changes the work
AI can reduce avoidable labor in lead response, scheduling, reminders, intake drafting, routine customer communications, marketing content, bookkeeping, inventory, and management reporting. It is much less able to substitute for the physical procedure, sanitation, safety judgment, and trust-building work at the point of service.

## Value capture
Direct consumer pricing permits operators to keep some productivity gain rather than contractually passing it through. Local price visibility, promotion intensity, practitioner economics, and low switching costs in some categories will redirect part of the gain to lower prices, marketing, wages, or improved service.

## Firm availability
The code plausibly contains repeat-service external-customer firms in the LMM band, but many establishments are too small, contractor-heavy, or tied to an individual practitioner's reputation. Broad owner-intention data indicate a transfer pool, yet completed industry-specific control-transfer evidence is missing.

## Demand durability
The service basket should remain mostly operator-required because treatment is performed on the customer. Broader category projections indicate modest growth, while tattoo prevalence supports a durable installed customer base; discretionary spending, saturation, home devices, and self-service formats create downside.

## Risks and uncertainty
The principal research risk is aggregation: tattoo, piercing, tanning, hair-removal, sauna, and related services have different labor models, regulation, cyclicality, and self-service threats. Key operating risks include licensing and consent requirements, health and safety incidents, practitioner retention, reputation concentration, local competition, and dependence on discretionary consumer demand.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.4744 | — | OBSERVED | — |
| n | — | 85 | — | ESTIMATE | — |
| a | 0.16 | 0.25 | 0.36 | ESTIMATE | S1, S2 |
| rho | 0.45 | 0.62 | 0.78 | ESTIMATE | S1, S2 |
| e | 0.45 | 0.65 | 0.82 | ESTIMATE | S1, S2 |
| s5 | 0.06 | 0.13 | 0.22 | PROXY | S5 |
| q | 0.38 | 0.56 | 0.72 | ESTIMATE | S1, S2 |
| d5 | 0.94 | 1.07 | 1.2 | PROXY | S3, S4 |
| o | 0.88 | 0.96 | 0.995 | PROXY | S1, S2 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 1.37 | 2.94 | 5.33 | ESTIMATE |
| F | 1.92 | 3.38 | 4.49 | ESTIMATE |
| C | 7.60 | 10.00 | 10.00 | ESTIMATE |
| D | 8.27 | 10.00 | 10.00 | PROXY |

## Caveats
- a: No source measures wage-weighted AI task exposure for this six-digit industry.
- a: The BLS skincare occupation overlaps only part of the heterogeneous NAICS population.
- a: The supplied compensation-to-receipts ratio may blend materially different labor models, including employee, booth, and contractor arrangements.
- rho: Implementation evidence is not reported at six-digit NAICS level.
- rho: Practitioner acceptance and local licensing or consent rules can vary by service and state.
- e: The industry is unusually heterogeneous and no source enumerates the eligible LMM subset.
- e: BLS reports substantial self-employment in the overlapping skincare occupation, but occupation self-employment is not a direct firm-eligibility measure.
- e: The supplied firm count is an estimate derived using a broad-sector margin bridge.
- s5: Gallup covers all US business industries rather than NAICS 812199.
- s5: The survey measures owner intentions, not completed qualifying control transfers.
- s5: Employer and nonemployer findings do not isolate firms in the supplied LMM band.
- q: No source directly measures benefit sharing or five-year retention for this industry.
- q: Pricing power differs sharply by service, local density, practitioner reputation, and membership penetration.
- d5: The BLS forecast is for broader NAICS 812100 and a ten-year employment outcome, not five-year constant-quality demand.
- d5: Pew tattoo prevalence is a 2023 population level rather than an industry growth series.
- d5: The current basket mixes services with different cyclicality, saturation, and technology substitution.
- o: Operator requirement varies substantially across tattoo, piercing, hair-removal, tanning, sauna, and related services.
- o: The BLS task source is an overlapping occupation proxy rather than a complete industry workflow census.

## Sources
- **S1** — [NAICS Sector 81: Other Services (except Public Administration)](https://www.census.gov/naics/resources/archives/sect81.html) (accessed 2026-07-22): Official industry definition and examples for NAICS 812199, used for the lens and the physical-service/operator-required assessment.
- **S2** — [Skincare Specialists - Occupational Outlook Handbook](https://www.bls.gov/ooh/personal-care-and-service/skincare-specialists.htm) (accessed 2026-07-22): Overlapping occupation task mix, work setting, licensing, employment, and self-employment evidence used directionally for AI exposure, implementation, eligibility, and operator requirement.
- **S3** — [Industry Employment and Output Projections](https://www.bls.gov/emp/tables/industry-employment-and-output.htm) (accessed 2026-07-22): Broader NAICS 812100 employment projection from 2024 to 2034 used as a directional demand proxy.
- **S4** — [32% of Americans have a tattoo, including 22% who have more than one](https://www.pewresearch.org/short-reads/2023/08/15/32-of-americans-have-a-tattoo-including-22-who-have-more-than-one/) (accessed 2026-07-22): National 2023 tattoo prevalence and survey methodology, used as a level indicator of one included service line's customer base.
- **S5** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Fall-2024 US business-owner survey reporting five-year sell or transfer intentions for employer and nonemployer owners, used as the control-transfer proxy.
