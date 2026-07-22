# 455110 — Department Stores

*v5.1 Stage 1 research memo. Run `455110-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** no base (evidence-first) · A — · L — · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness STRESS_TEST_ONLY · action EVIDENCE_FIRST

**Driver:** Retention of workflow savings in a posted-price model across service, merchandising, planning, and administrative tasks.
**Weakness:** Structural demand erosion and a poorly observed, likely small pool of independently transferable LMM operators.

## Business-model lens
- Included: US department-store operators in the lower-middle-market EBITDA band that repeatedly retail broad lines of merchandise and associated shopping, fulfillment, return, and customer-support services to external consumers.
- Excluded: Public and very large national chains outside the size band, non-operating real-estate or financing entities, captive internal units, shells, and stores whose economics cannot be transferred apart from a parent chain.
- Customer and revenue model: Predominantly consumer merchandise sales at posted or promoted prices, with repeat but usually non-contractual purchases; ancillary delivery, licensed-department, marketplace, media, and credit-card-related income may supplement merchandise margin.
- Deviation from default lens: none

## Executive view
Department stores offer identifiable AI-enabled labor opportunities in customer service, marketing, merchandising, planning, administration, and supply chain, but much of the workforce performs physical selling and handling. The harder issue is structural: the industry is chain-heavy, independent transferability is uncertain, and real demand has been pressured by online and alternative formats.

## How AI changes the work
AI is already being used by a major operator for shopping assistance, personalization, service, marketing, HR queries, coding, supply chain, and inventory decisions. For LMM operators, the practical five-year opportunity is more likely to come from packaged workflow tools and avoided hiring than from autonomous stores; legacy integration, governance, and thin data constrain implementation.

## Value capture
Posted-price merchandise retail avoids explicit contractual pass-through, so savings can initially accrue to the operator. Over time, frequent promotions, transparent online comparison, overlapping assortments, and service reinvestment share a meaningful portion with customers.

## Firm availability
Transferable targets are likely a minority because many department-store locations belong to large chains and some independents are owner-dependent, distressed, or inseparable from leases and buying relationships. No defensible LMM firm-count input exists, and closed-deal evidence for independent department stores is sparse.

## Demand durability
Nominal department-store sales in 2025 remained well below much of 2021-22, and e-commerce continues to outgrow total retail. Surviving demand still usually needs a merchant accountable for inventory, fulfillment, returns, and consumer obligations, but the quantity routed through traditional department-store operators is likely to contract.

## Risks and uncertainty
The occupation proxy includes supercenters, the principal AI evidence comes from a large chain, sales are nominal, and private-company eligibility and transfer rates are estimated. The thesis weakens materially if local independents lack clean standalone economics, if AI merely shifts labor into oversight, or if continued channel migration overwhelms efficiency gains.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1014 | — | ESTIMATE | — |
| n | — | — | — | MISSING | — |
| a | 0.18 | 0.29 | 0.42 | PROXY | S2, S4 |
| rho | 0.35 | 0.5 | 0.65 | ESTIMATE | S4 |
| e | 0.1 | 0.25 | 0.45 | ESTIMATE | S1 |
| s5 | 0.08 | 0.15 | 0.25 | ESTIMATE | S5 |
| q | 0.55 | 0.7 | 0.82 | ESTIMATE | S4 |
| d5 | 0.72 | 0.83 | 0.96 | PROXY | S5, S6 |
| o | 0.78 | 0.88 | 0.95 | ESTIMATE | S4, S6 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.26 | 0.59 | 1.11 | ESTIMATE |
| F | — | — | — | MISSING |
| C | 10.00 | 10.00 | 10.00 | ESTIMATE |
| D | 5.62 | 7.30 | 9.12 | ESTIMATE |

## Caveats
- a: The available BLS occupation table is NAICS 455000 rather than 455110 and includes warehouse clubs and supercenters.
- a: Macy's is a large-company implementation example and may have capabilities unavailable to LMM operators.
- a: The estimate excludes opportunity already automated and does not treat physical robotics as AI substitution unless it avoids labor within five years.
- rho: Large-chain adoption can overstate LMM implementation capacity.
- rho: The range assumes vendor tools mature and integrate with common POS, ERP, e-commerce, and workforce systems.
- rho: This is implementation of exposed labor opportunity, not technology availability or gross productivity potential.
- e: The injected firm-count input is missing, so this share cannot be reconciled to a defensible eligible-firm count.
- e: NAICS assignment is establishment-based and can obscure multi-format retailers and parent-company ownership.
- e: Eligibility is estimated rather than directly observed.
- s5: Public sales data show sector pressure but do not measure private-company control transfers.
- s5: Distress can produce liquidation or lease termination rather than a transferable operating company.
- s5: No defensible industry-specific denominator or closed-deal series was found.
- q: There are few recurring customer contracts, so renewal repricing is indirect through ongoing price competition.
- q: Margin retention varies sharply by private-label penetration, local differentiation, and product overlap.
- q: The estimate is a discounted five-year share of implemented gross benefit, not gross margin.
- d5: The sales series is nominal and includes large chains, while the primitive is constant-price and specific to the LMM lens.
- d5: Pandemic years distort comparisons and format reclassification may affect the series.
- d5: Merchandise sales are only a proxy for the quantity of the retail service basket.
- o: The boundary between software-enabled retailing and software replacing the retailer is judgmental.
- o: Macy's digital sales share is a large-chain proxy and digital purchases can still require the same accountable operator.
- o: Volume loss is reserved for d5; this primitive only addresses who supplies surviving quantity.

## Sources
- **S1** — [PPI Coverage of the Retail Trade Sector](https://www.bls.gov/ppi/factsheets/ppi-coverage-of-the-retail-trade-sector.htm) (accessed 2026-07-22): Defines NAICS 455110 as department stores with separate departments for broad lines of new merchandise and fixed point-of-sale locations; informs business-model and eligibility analysis.
- **S2** — [May 2023 OEWS Industry-Specific Occupational Employment and Wage Estimates: NAICS 455000 General Merchandise Retailers](https://www.bls.gov/oes/2023/may/naics4_455000.htm) (accessed 2026-07-22): Reports the adjacent-industry occupation mix, including 43.63% sales, 8.41% office support, and 33.00% transportation/material-moving employment; supports the task-exposure proxy.
- **S3** — [Cashiers: Occupational Outlook Handbook](https://www.bls.gov/ooh/sales/cashiers.htm) (accessed 2026-07-22): Projects cashier employment to decline 10% from 2024 to 2034 and attributes the decline partly to self-service checkout and online sales; supports automation and substitution context.
- **S4** — [Macy's, Inc. 2025 Annual Report](https://s202.q4cdn.com/285121676/files/doc_financials/2025/ar/Macy-s-Inc-2025-Annual-Report.pdf) (accessed 2026-07-22): Documents AI use in service, personalization, marketing, HR, coding, supply chain, merchandising and planning; identifies governance and legacy-system risks, price and online competition, and a 35% digital-sales share in 2025.
- **S5** — [Retail Sales: Department Stores, Seasonally Adjusted](https://fred.stlouisfed.org/data/SM4522USS) (accessed 2026-07-22): Census-sourced monthly nominal sales series showing roughly $3.6-$4.0 billion monthly in much of 2021-22 versus roughly $3.2-$3.4 billion in 2025; supports the demand-direction proxy and distress context.
- **S6** — [Quarterly Retail E-Commerce Sales, First Quarter 2026](https://www.census.gov/retail/eCommerce.html) (accessed 2026-07-22): Reports US retail e-commerce sales up 9.8% year over year in first-quarter 2026 versus 3.9% for total retail, with e-commerce at 16.9% of total sales; supports channel-substitution context.
