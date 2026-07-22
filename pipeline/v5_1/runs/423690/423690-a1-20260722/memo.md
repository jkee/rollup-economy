# 423690 — Other Electronic Parts and Equipment Merchant Wholesalers

*v5.1 Stage 1 research memo. Run `423690-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 7.12 · L 0.47 · interval STRUCTURAL_OUT → STRUCTURAL_OUT · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Large, recurring product-data, quoting, sourcing, and customer-service workloads are amenable to AI while valuable distribution accountability remains.
**Weakness:** Low labor intensity and powerful suppliers and customers constrain captured savings, while the underlying component market is volatile and concentrated.

## Business-model lens
- Included: Independent US merchant wholesalers repeatedly supplying electronic components, communications and networking equipment, broadcasting equipment, unloaded boards, and related electronic parts to OEMs, contract manufacturers, integrators, resellers, institutions, and other external customers, including product data, sourcing, design-in, availability, logistics, quality, compliance, credit, and lifecycle support.
- Excluded: Manufacturer-owned sales branches, captive procurement units, pure commission brokers, non-operating inventory vehicles, predominantly consumer retail businesses, and firms whose customer, supplier-authorization, compliance, or technical-support relationships would not transfer with control.
- Customer and revenue model: Recurring and repeat B2B component and equipment sales earned primarily through merchandise gross margin, with value also delivered through authorized sourcing, technical selection, design support, product data, forecasting, inventory programs, traceability, credit, logistics, and obsolescence management.
- Deviation from default lens: none

## Executive view
Electronic-parts distribution combines data-intensive selling and sourcing workflows with persistent operator roles in inventory, authorization, traceability, technical support, credit, and exceptions. AI exposure and implementation appear meaningful, while channel concentration, product cycles, supplier power, and a low labor share limit how much gross economic benefit can be captured.

## How AI changes the work
AI can normalize product data, match alternatives, prepare quotes, prioritize accounts, draft customer responses, forecast demand, identify supply risks, retrieve compliance documents, and triage orders and returns. Technical approval, negotiated pricing, quality and counterfeit risk, export controls, supplier and customer relationships, credit, and physical inventory remain accountable human and organizational work.

## Value capture
Faster response, broader sales coverage, improved data quality, fewer errors, and avoided administrative hiring can create value. Some can be retained where technical service, authorization, traceability, availability, and credit matter, but manufacturers, large customers, transparent e-commerce, and technology-enabled competitors should claim a meaningful share.

## Firm availability
The dataset provides an estimated 1,867 band-sized firms, but firm-level eligibility is unknown. Broad succession evidence points to owner turnover and observed wholesale transactions, while supplier consents, working capital, cyclicality, concentration, and key-person technical relationships can reduce transferable supply.

## Demand durability
Semiconductor and electronic-system demand benefits from AI infrastructure, networking, automation, connected products, vehicles, aerospace, and expanding electronic content. Recent revenue growth is unusually price- and memory-driven, and tariffs, export controls, direct channels, inventory corrections, and technology cycles create substantial five-year uncertainty.

## Risks and uncertainty
The core evidence gaps are a six-digit wage-weighted task mix, LMM implementation outcomes, qualifying control-transfer rates, and constant-quality US channel demand. Counterfeits, cyber incidents, export violations, supplier authorization loss, inventory obsolescence, allocation reversals, working-capital shocks, and customer concentration can overwhelm workflow gains.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.0471 | — | OBSERVED | — |
| n | — | 1867 | — | ESTIMATE | — |
| a | 0.28 | 0.43 | 0.57 | PROXY | S2, S3, S4 |
| rho | 0.38 | 0.58 | 0.74 | PROXY | S3, S4 |
| e | 0.52 | 0.72 | 0.84 | ESTIMATE | S1, S3 |
| s5 | 0.08 | 0.16 | 0.26 | PROXY | S5, S6 |
| q | 0.38 | 0.57 | 0.72 | ESTIMATE | S3, S4 |
| d5 | 0.98 | 1.17 | 1.38 | PROXY | S3, S7 |
| o | 0.64 | 0.8 | 0.91 | ESTIMATE | S1, S3, S4 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.20 | 0.47 | 0.79 | PROXY |
| F | 7.02 | 8.65 | 9.67 | ESTIMATE |
| C | 7.60 | 10.00 | 10.00 | ESTIMATE |
| D | 6.27 | 9.36 | 10.00 | ESTIMATE |

## Caveats
- a: The occupation evidence combines six durable-goods wholesale industries and excludes self-employed workers.
- a: ECIA interviews emphasize leading authorized distributors rather than the LMM population.
- a: Existing EDI, e-commerce, ERP, and product-information systems have already automated part of the theoretical task pool.
- rho: The sources establish use cases and executive interest rather than an implemented share of exposed wages.
- rho: Capabilities and vendor products may change faster than the evidence vintage.
- e: NAICS 423690 spans semiconductors, passives, interconnects, communications equipment, phones, broadcasting equipment, and other products with different service intensity.
- e: The industry definition does not reveal independence or transferability.
- s5: The succession survey is cross-industry and reports intentions rather than qualifying completed transfers.
- s5: BizBuySell's reported-sales sample is selective and uses cash flow rather than the frozen EBITDA definition.
- q: No source directly measures discounted five-year retention of implemented AI benefits in this industry.
- q: Value capture differs sharply between scarce or highly engineered parts and readily substitutable catalog items.
- d5: Global semiconductor revenue is not the same quantity as US distributor demand and excludes much communications and broadcasting equipment while including channels outside NAICS 423690.
- d5: ECIA reported a 9.3% Americas authorized-distributor revenue decline in 2024 despite longer-run growth, showing strong cyclicality and category divergence.
- o: The estimate is the share of demand requiring an accountable operator, not the share requiring today's staffing or manual processes.
- o: Operator necessity is higher for regulated, engineered, scarce, and lifecycle-managed parts than for standardized low-value catalog components.

## Sources
- **S1** — [2022 NAICS definition: 423690 Other Electronic Parts and Equipment Merchant Wholesalers](https://www.census.gov/naics/?details=42&input=42&year=2022) (accessed 2026-07-22): Defines merchant wholesaling in the industry and lists covered products including broadcasting and communications equipment, modems and routers, radar equipment, teleconferencing equipment, and unloaded computer boards.
- **S2** — [May 2023 OEWS Industry-Specific Occupational Employment and Wage Estimates: NAICS 4230A1](https://www.bls.gov/oes/2023/may/naics4_4230A1.htm) (accessed 2026-07-22): Provides the occupation and wage mix for the broad durable-goods wholesale group containing NAICS 4236, including sales, management, business, office, technical, repair, and material-moving work.
- **S3** — [ECIA Top 50 Americas Authorized Distributors Report 2025](https://www.ecianow.org/assets/docs/Stats/ESNA%20May25%20Top%2050%20AA%20Report.pdf) (accessed 2026-07-22): Reports a 9.3% 2024 sales decline for the Top 50 Americas authorized distributors, 3.1% five-year distribution revenue CAGR, customer and category mix, concentration, industry risks, and distributor executives' AI, data, customer-service, forecasting, and technical-support applications.
- **S4** — [How generative AI is disrupting distribution](https://www.mckinsey.com/industries/industrials/our-insights/distribution-blog/how-generative-ai-is-disrupting-distribution) (accessed 2026-07-22): Describes generative-AI applications and potential impact across distributor customer operations, marketing and sales, and other information-heavy workflows.
- **S5** — [BizBuySell Insight Report Data Tables](https://www.bizbuysell.com/insight-report-data-tables/) (accessed 2026-07-22): Reports 28 sales of durable-goods wholesalers and distributors during 2025 and transaction benchmarks, confirming observable small-business deal flow in the broad sector.
- **S6** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Reports that 52.3% of US employer businesses are owned by people age 55 or older and that 35% of surveyed owners plan a sale or gift, providing broad succession context.
- **S7** — [Global Annual Semiconductor Sales Increase 25.6% to $791.7 Billion in 2025](https://www.semiconductors.org/global-annual-semiconductor-sales-increase-25-6-to-791-7-billion-in-2025/) (accessed 2026-07-22): Reports 2025 global semiconductor sales, category and regional growth, and an industry projection of roughly $1 trillion in 2026, while identifying AI, IoT, 6G, and autonomous driving as demand drivers.
