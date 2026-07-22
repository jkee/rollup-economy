# 541870 — Advertising Material Distribution Services

*v5 Stage 1 research memo. Run `541870-a1-20260722`, model `gpt-5.6-terra`, 2026-07-22, attempt 1.*

**Base tier:** LOW_PRIORITY · A 5.51 · L 1.16 · interval STRUCTURAL_OUT → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** The service's physical execution requirement preserves an operator role even as AI improves the back office.
**Weakness:** Channel substitution away from printed and in-person promotion can shrink the current service basket before operational improvements compound.

## Business-model lens
- Included: US lower-middle-market firms that repeatedly distribute printed advertising materials or product samples door-to-door or in public locations for external customers, including associated campaign coordination, field staffing, assembly, routing, reporting, and client service.
- Excluded: Mail delivery, wholly electronic distribution, advertising-agency creative and media-buying work, promotional-specialty distributors, captive marketing teams, shells, and non-control financing vehicles.
- Customer and revenue model: Recurring or repeat outsourced campaign execution for advertisers, retailers, agencies, and brand owners; revenue is generally campaign, route, event, staffing, assembly, or distribution fee based rather than software subscription revenue.
- Deviation from default lens: none

## Executive view
Advertising Material Distribution Services is a physical campaign-execution industry: its defined output is the door-to-door or public-place delivery of advertisements and samples. That makes the addressable AI labor opportunity concentrated in the coordination layer rather than the core field service, while demand faces material channel-substitution risk.

## How AI changes the work
AI can make campaign preparation, route and staffing coordination, client reporting, sales support, invoice handling, and exception triage more efficient. The Census product definition covers printed-material and sample distribution in physical locations, so it does not support treating the field-distribution labor itself as readily substituted by AI.

## Value capture
Repeat campaign contracts provide a route to retain savings between renewals, but project and procurement-style pricing gives customers leverage to seek lower fees. Actual value capture depends heavily on whether labor is committed under fixed campaign pricing or repriced after a customer sees the new cost base.

## Firm availability
The eligible universe should exclude owner-dependent, one-off, captive, and highly concentrated operators. National owner evidence indicates material stated transfer intent among employer firms, but it measures plans rather than closed control transactions and should not be treated as industry deal flow.

## Demand durability
Physical sampling and local distribution can still require human, accountable execution when the channel is selected. However, USPS reports a declining marketing-mail volume trend, a close but imperfect warning signal for printed promotion, and advertisers can redirect campaigns to digital channels.

## Risks and uncertainty
The narrow code has sparse public operational data. The best available occupational source is a broader advertising-services sector that is much more white-collar than this industry, so it likely exaggerates AI exposure. Postal volumes are also only a proxy because the NAICS definition includes non-mail street, retail, and door-to-door work.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.4285 | — | OBSERVED | — |
| n | — | 102 | — | ESTIMATE | — |
| a | 0.08 | 0.15 | 0.25 | PROXY | S1, S2 |
| rho | 0.25 | 0.45 | 0.6 | ESTIMATE | S1 |
| e | 0.6 | 0.75 | 0.88 | ESTIMATE | S1, S3 |
| s5 | 0.1 | 0.17 | 0.25 | PROXY | S3 |
| q | 0.35 | 0.5 | 0.65 | ESTIMATE | S1 |
| d5 | 0.75 | 0.85 | 0.95 | PROXY | S1, S4 |
| o | 0.65 | 0.78 | 0.9 | ESTIMATE | S1 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.34 | 1.16 | 2.57 | ESTIMATE |
| F | 3.16 | 4.25 | 5.07 | ESTIMATE |
| C | 7.00 | 10.00 | 10.00 | ESTIMATE |
| D | 4.88 | 6.63 | 8.55 | ESTIMATE |

## Caveats
- a: OEWS excludes self-employed workers and S2 is a four-digit-sector proxy rather than this six-digit industry.
- a: No public 541870 wage-weighted task inventory was located.
- rho: This is a judgment about implementation after task exposure, not a survey measurement.
- rho: It should not be read as a forecast of revenue, customer retention, or pricing.
- e: No public source identifies the lower-middle-market subset or tests transferability for this NAICS code.
- e: S3 covers US business owners generally, not this industry.
- s5: S3 is a national owner survey and reports intended actions, not completed deals.
- s5: The survey includes business sizes outside the lower-middle-market lens and does not isolate advertising-material distributors.
- q: No public contract-price study was located for this narrow NAICS code.
- q: The estimate excludes any demand change and does not assume that field-labor savings are AI-derived.
- d5: USPS marketing mail is not the same as non-mail distribution services.
- d5: The measure is a judgment about constant-price, constant-quality service quantity, not nominal postal revenue.
- o: This is not an observed operator-retention rate.
- o: It assumes the current physical service basket; it does not model new software-native advertising services.

## Sources
- **S1** — [Census Bureau NAPCS Product List for NAICS 54187: Advertising Materials Distribution Services](https://www2.census.gov/library/reference/napcs/product-list/web-54187-final-reformatted-edited-us082208.pdf) (accessed 2026-07-22): Defines 541870 products as distribution of printed advertising materials and product samples door-to-door and in public locations, with possible assembly, reproduction, and creative work; also identifies electronic distribution as a product category.
- **S2** — [BLS May 2023 National Industry-Specific Occupational Employment and Wage Estimates, NAICS 541800](https://www.bls.gov/oes/2023/May/naics4_541800.htm) (accessed 2026-07-22): Reports a 500,130-worker occupation mix for the broader advertising, public relations, and related-services sector, including management, sales, office support, production, and transportation occupational groups; used only as an explicitly adjusted occupation-mix proxy.
- **S3** — [Gallup: Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Reports five-year owner plans, including 22 percent of employer-business owners saying they plan to sell or transfer, and distinguishes employer owners from nonemployers; used as a completion-discounted transfer-intent proxy.
- **S4** — [USPS Postal Facts: A Decade of Facts and Figures](https://facts.usps.com/table-facts/) (accessed 2026-07-22): Reports annual Marketing Mail volume, including 64.1 billion pieces in 2020 and 57.5 billion in 2024, a close physical-advertising-channel proxy for the demand trajectory.
