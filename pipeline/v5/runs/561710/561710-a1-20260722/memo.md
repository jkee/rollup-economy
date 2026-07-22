# 561710 — Exterminating and Pest Control Services

*v5 Stage 1 research memo. Run `561710-a1-20260722`, model `gpt-5.6-terra`, 2026-07-22, attempt 1.*

**Base tier:** CONDITIONAL · A 6.53 · L 2.62 · interval LOW_PRIORITY → PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Recurring route-based service relationships paired with AI-addressable office, dispatch, documentation, and customer-contact work.
**Weakness:** Most industry employment is licensed, physical field treatment work, limiting direct AI substitution and making LMM transfer rates unobserved.

## Business-model lens
- Included: US lower-middle-market operators providing recurring or repeat residential, commercial, termite, rodent, insect, and related structural pest-control services to external customers.
- Excluded: Captive facilities units, shells, non-control financing vehicles, and firms whose business is principally one-time remediation, wildlife removal, product sales, or internal pest-control work.
- Customer and revenue model: External residential and commercial customers, primarily served through scheduled recurring agreements and repeat treatments, with some one-time and ancillary work.
- Deviation from default lens: none

## Executive view
Exterminating and pest-control services is a route-based external service with substantial recurring revenue and visible strategic acquisition activity. Its central tension is that a large share of payroll belongs to technicians performing regulated, physical field work, so AI can improve the operating system around the route more readily than it can replace the route itself (S1, S2, S5).

## How AI changes the work
The largest practical applications are AI-assisted booking, customer messages, recurring scheduling, route sequencing, reporting, payments, and office workflow. The 2023 staffing pattern has 17.22% office and administrative support and 6.37% sales, while pest-control workers are 61.05%; technician documentation and route work add some opportunity, but inspection, treatment, equipment operation, and in-person accountability remain physical (S1, S2, S7).

## Value capture
Recurring agreements support retention of operating improvements, particularly where a provider can use better scheduling and customer communication without changing service quality. That retention is limited by annual renewal pricing, commercial procurement, competition, and the need to preserve technician and customer experience. Rollins describes recurring scheduled prevention and generally initial one-year contracts, while NPMA reports 85.4% recurring residential service revenue in 2025 (S4, S5).

## Firm availability
The trade is fragmented: NPMA reports 16,565 US firms and 81.4% with one or two locations. Transfer evidence is encouraging rather than denominator-complete: Rollins completed 94 acquisitions over three years and the broader BizBuySell market identifies retirement as the top planned-sale motive. Deal probability still depends on route quality, licenses, technician retention, clean records, and owner dependence (S4, S5, S6).

## Demand durability
Demand is supported by physical pest pressure and property, health, and compliance consequences. BLS projects pest-control-worker employment to grow 5% from 2024 to 2034 and notes invasive insects as a driver, while also recognizing some customer self-service. The service requires travel, inspection, treatment selection, and frequently regulated application, leaving an accountable operator necessary for most of the present service basket (S2, S3).

## Risks and uncertainty
The demand estimate is an occupation-growth proxy rather than constant-price service-unit data. Labor productivity gains can decouple employment from service volume. Public recurring-revenue and acquisition evidence comes partly from large operators, while the target is LMM firms. Seasonality, weather, state licensing, pesticide safety, integration quality, technician scarcity, customer churn, and DIY competition can materially change realized economics (S2, S3, S4, S5).

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.475 | — | OBSERVED | — |
| n | — | 70 | — | ESTIMATE | — |
| a | 0.14 | 0.23 | 0.34 | ESTIMATE | S1, S2 |
| rho | 0.4 | 0.6 | 0.75 | ESTIMATE | S3, S7 |
| e | 0.7 | 0.82 | 0.92 | ESTIMATE | S4, S5 |
| s5 | 0.1 | 0.19 | 0.32 | ESTIMATE | S5, S6 |
| q | 0.5 | 0.7 | 0.85 | ESTIMATE | S4, S5 |
| d5 | 0.98 | 1.025 | 1.06 | PROXY | S2 |
| o | 0.84 | 0.93 | 0.98 | ESTIMATE | S2, S3 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 1.06 | 2.62 | 4.84 | ESTIMATE |
| F | 2.86 | 3.98 | 4.94 | ESTIMATE |
| C | 10.00 | 10.00 | 10.00 | ESTIMATE |
| D | 8.23 | 9.53 | 10.00 | ESTIMATE |

## Caveats
- a: OEWS employment and mean wages are from May 2023, while the frozen compensation input uses 2024 wages.
- a: Occupation categories do not measure task time or AI exposure, and owner labor may be underrepresented.
- rho: The software vendor documents available features rather than independently measured adoption or savings.
- rho: Certification rules apply to restricted-use pesticides and may not cover every treatment, but they illustrate the compliance constraint on field substitution.
- e: NPMA reports residential revenue rather than LMM firm eligibility, and Rollins is a large multi-brand operator rather than the target population.
- e: No published count separates LMM firms by recurring versus principally one-time revenue.
- s5: Rollins acquisitions include businesses of all sizes and may include locations or non-US operations; they are not a denominator-based LMM transfer rate.
- s5: BizBuySell figures are across its tracked US small-business market, not pest control, and planned reasons do not equal completed qualifying transfers.
- q: Public recurring-revenue mix does not measure contractual pass-through or net benefit retention.
- q: The industry has meaningful residential/commercial, seasonal, and one-time revenue variation.
- d5: Occupation projections cover the whole US occupation and are not restricted to LMM operators or the frozen service basket.
- d5: The BLS outlook spans ten years and does not separate quantity from labor productivity.
- o: Licensing and restricted-use pesticide rules vary by state and product; not every service visit entails a restricted-use pesticide.
- o: Termites, wildlife, mosquitoes, rodents, and general recurring prevention may have different operator requirements.

## Sources
- **S1** — [BLS May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 561710](https://www.bls.gov/oes/2023/may/naics5_561710.htm) (accessed 2026-07-22): Industry occupation mix and mean wages: 145,910 total employment; pest-control workers 61.05%; office and administrative support 17.22%; sales 6.37%; management 6.29%.
- **S2** — [BLS Occupational Outlook Handbook: Pest Control Workers](https://www.bls.gov/ooh/Building-and-Grounds-Cleaning/Pest-control-workers.htm) (accessed 2026-07-22): Worker duties, travel, licensing, 90% industry employment, and 5% projected employment growth from 2024 to 2034.
- **S3** — [EPA Federal Certification Standards for Pesticide Applicators](https://www.epa.gov/pesticide-worker-safety/federal-certification-standards-pesticide-applicators) (accessed 2026-07-22): Restricted-use pesticide certification requirement and commercial applicator knowledge requirements for safety, pest management, equipment, and laws.
- **S4** — [NPMA: U.S. Pest Control Industry Sustains Steady Growth with 6% Increase in 2025](https://www.npmapestworld.org/your-business/latest-news/us-pest-control-industry-sustains-steady-growth-with-6-increase-in-2025/) (accessed 2026-07-22): 2025 US structural pest-control service revenue, 16,565 firms, 81.4% with one or two locations, 13.29 million residential customers, and 85.4% recurring residential service revenue.
- **S5** — [Rollins, Inc. 2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/84839/000008483926000008/rol-20251231.htm) (accessed 2026-07-22): Rollins recurring-service model, 75% recurring services, 10% ancillary services, 15% one-time services, initial one-year contracts, and 94 acquisitions over three years including 26 in 2025.
- **S6** — [BizBuySell Insight Report: Q2 2026 Market Trends](https://images.bizbuysell.com/insight-report/) (accessed 2026-07-22): 2,117 US businesses changed hands in Q2 2026; retirement was the leading planned-sale reason at 45%; source is a broader small-business market proxy.
- **S7** — [PestPro CRM Pest Control Business Management Features](https://www.pestprocrm.com/features) (accessed 2026-07-22): Pest-control-specific software offers recurring scheduling, payment links, property records, route planning, automated customer messages, compliance records, and an AI assistant for booking and routing.
