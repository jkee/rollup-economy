# 561510 — Travel Agencies

*v5 Stage 1 research memo. Run `561510-a1-20260722`, model `gpt-5.6-terra`, 2026-07-22, attempt 1.*

**Base tier:** LOW_PRIORITY · A 5.54 · L 1.85 · interval STRUCTURAL_OUT → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** A task mix rich in booking, information handling, recordkeeping, and service workflows creates a practical automation surface.
**Weakness:** Direct booking and software substitution threaten both demand durability and the operator's ability to retain productivity gains.

## Business-model lens
- Included: US lower-middle-market travel agencies that act as external agents selling travel, tour, and accommodation services, including repeat leisure and corporate travel planning, booking, ticketing, changes, and account support.
- Excluded: Tour operators, guide services, other reservation-service businesses, captive internal travel departments, shells, and non-control financing vehicles.
- Customer and revenue model: External customers pay directly through planning or service fees and indirectly through supplier commissions; repeat business can arise from corporate accounts, returning leisure clients, groups, and referrals.
- Deviation from default lens: none

## Executive view
Travel agencies combine a meaningful amount of process work with a service layer that remains valuable for complex choices and exceptions. The opportunity depends on preserving differentiated advice while automating preparation, service, and administrative workflows.

## How AI changes the work
Published role data for the broader travel-arrangement group places travel agents, customer-service representatives, reservation agents, and office support at a large share of employment. O*NET lists payment collection, itinerary planning, cost calculation, recordkeeping, reservations, ticketing, and travel information among travel-agent tasks. These are candidates for assisted workflow automation, but client discovery, sales, supplier coordination, and disruption handling require human review.

## Value capture
Agent compensation includes commissions and service fees. That creates room to retain internal productivity gains, especially where specialized advice supports fees, but supplier-set commission policies and transparent online alternatives limit durable capture. Non-commissionable fares have been identified by ASTA as a compensation barrier.

## Firm availability
The frozen firm-count input is not re-estimated. The industry definition fits external agency activity, but qualifying transfers are uncertain because a saleable agency needs transferable customer relationships, clean financials, and less dependence on the owner. A national broker-market source reports retirement as the leading reason owners planning to sell, while also emphasizing buyer selectivity and owner-dependence concerns.

## Demand durability
BLS projects modest occupational growth and expects continued demand for personalized expertise and travel-problem handling. The same source warns that online research and self-booking can limit demand. Durable demand is therefore strongest in complex, exception-prone, and policy-sensitive trips rather than commodity bookings.

## Risks and uncertainty
The core labor proxy uses a broader four-digit industry, not NAICS 561510. There is no direct five-year AI adoption, benefit-retention, transfer-rate, or constant-dollar demand measure for the frozen LMM lens. Travel is cyclical and exposed to macroeconomic, health, geopolitical, and supplier shocks; agency economics can also be reshaped by supplier commission rules and host arrangements.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.2099 | — | OBSERVED | — |
| n | — | 250 | — | ESTIMATE | — |
| a | 0.35 | 0.48 | 0.62 | PROXY | S2, S3, S4 |
| rho | 0.32 | 0.46 | 0.6 | ESTIMATE | S3, S4, S7 |
| e | 0.45 | 0.62 | 0.78 | ESTIMATE | S1 |
| s5 | 0.12 | 0.22 | 0.34 | PROXY | S6 |
| q | 0.25 | 0.4 | 0.55 | ESTIMATE | S4, S5 |
| d5 | 0.95 | 1.01 | 1.07 | PROXY | S4 |
| o | 0.5 | 0.65 | 0.78 | PROXY | S4, S7 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.94 | 1.85 | 3.12 | ESTIMATE |
| F | 4.30 | 5.72 | 6.77 | ESTIMATE |
| C | 5.00 | 8.00 | 10.00 | ESTIMATE |
| D | 4.75 | 6.57 | 8.35 | PROXY |

## Caveats
- a: The published industry occupation mix is at NAICS 561500, not six digits.
- a: Occupation titles do not reveal each firm's automation baseline or share of high-touch specialty itineraries.
- rho: No source measured five-year AI implementation for lower-middle-market travel agencies.
- rho: Implementation may differ sharply between corporate, cruise, luxury, and general leisure agencies.
- e: S1 defines the industry but does not measure customer recurrence, owner dependence, or the frozen EBITDA-band firms.
- e: The supplied firm count is frozen and was not re-estimated here.
- s5: S6 is not an industry-specific census of closed transactions and reports voluntary broker submissions.
- s5: A stated reason for planned sale is not a completed qualifying transfer.
- q: No source measures the five-year retention of AI-derived savings for this lens.
- q: Commission, fee, and supplier-override exposure varies by agency specialty and host arrangement.
- d5: Occupational employment is not industry output and includes agents outside the exact industry.
- d5: Travel demand is exposed to macroeconomic, health, geopolitical, and supplier-disruption shocks.
- o: The evidence is occupational and includes self-employed agents, not only acquired lower-middle-market firms.
- o: Operator need is likely higher in complex corporate, group, and luxury travel than in commodity leisure bookings.

## Sources
- **S1** — [2022 NAICS United States Manual](https://www.census.gov/naics/reference_files_tools/2022_NAICS_Manual.pdf) (accessed 2026-07-22): Defines NAICS 561510 as establishments acting as agents selling travel, tour, and accommodation services to public and commercial clients; separates tour operators, guide services, and other reservation services.
- **S2** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 561500](https://www.bls.gov/oes/2023/may/naics4_561500.htm) (accessed 2026-07-22): Reports broader travel-arrangement-and-reservation-services employment, occupation shares, and mean wages, including travel agents, customer service representatives, reservation agents, and office-support occupations.
- **S3** — [O*NET Job Duties Custom List: Travel Agents](https://www.onetonline.org/search/task/choose/41-3041.00) (accessed 2026-07-22): Lists travel-agent tasks including payment collection, itinerary planning, customer discovery, cost calculation, recordkeeping, reservations, ticketing, and travel information.
- **S4** — [Occupational Outlook Handbook: Travel Agents](https://www.bls.gov/ooh/sales/travel-agents.htm) (accessed 2026-07-22): Describes duties, compensation through commissions and service fees, computer-system training, 2024 employment, 2034 projected employment, continued personalized-advice demand, and online self-booking risk.
- **S5** — [Joint Industry Statement: Commission Transparency and Travel Advisor Compensation](https://asta.org/common/Uploaded%20files/ASTA/IndustryAffairs/JointIndustryStatement.pdf) (accessed 2026-07-22): States that non-commissionable fares have been a barrier to travel-advisor compensation and describes supplier commission policy changes.
- **S6** — [BizBuySell Insight Report: Q2 2026](https://images.bizbuysell.com/insight-report/) (accessed 2026-07-22): Reports nationwide broker-market transactions, buyer selectivity, owner-dependence concerns, and retirement as the leading reason owners planning to sell.
- **S7** — [GSA Travel Agent Services](https://www.gsa.gov/travel/travel-and-lodging-services/travel-category-schedule/travel-agent-services) (accessed 2026-07-22): Lists NAICS 561510 contractor tasks including reserving, booking, ticketing, hotel and car rental services, account reconciliation, meeting planning, and help-desk support.
