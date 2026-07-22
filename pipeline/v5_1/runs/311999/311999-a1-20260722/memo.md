# 311999 — All Other Miscellaneous Food Manufacturing

*v5.1 Stage 1 research memo. Run `311999-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 5.21 · L 0.81 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Physical, repeat outsourced production remains necessary while document-heavy planning, traceability, service, quality, and maintenance workflows offer targeted AI leverage.
**Weakness:** The eligible population is a minority hidden inside a heterogeneous NAICS code, and powerful customers can reclaim efficiency gains through repricing or rebids.

## Business-model lens
- Included: Independent US contract and private-label manufacturers in NAICS 311999 that repeatedly formulate, blend, process, package, or label miscellaneous shelf-stable food for external brand, retail, foodservice, or ingredient customers, within the lower-middle-market EBITDA band.
- Excluded: Own-brand manufacturers without a recurring outsourced-production relationship, captive plants, pure distributors and brokers, farms, software vendors, non-control financing vehicles, and food activities classified outside NAICS 311999.
- Customer and revenue model: B2B production programs and repeat purchase orders for food made to customer specifications; revenue is generally per unit or batch, with pricing that may embed conversion fees, ingredient and packaging costs, or negotiated cost pass-throughs.
- Deviation from default lens: Narrowed to contract and private-label manufacturers because NAICS 311999 combines own-account branded product makers with firms performing recurring outsourced production; only the latter form a coherent population under the fixed service lens.

## Executive view
The coherent opportunity is not the full miscellaneous-food category but independent contract and private-label plants that repeatedly execute customer production programs. Their physical, regulated production remains operator-required, while planning, documentation, customer service, quality review, forecasting, and maintenance contain implementable AI-assisted labor opportunity. The main economic uncertainty is how much of any gain survives procurement-led repricing.

## How AI changes the work
AI is most applicable around the line rather than as a replacement for the line: production scheduling, demand and material forecasting, specification and traceability records, customer communications, invoice and order handling, machine-vision triage, predictive maintenance, and investigation support. Physical blending, packaging, sanitation, allergen control, changeovers, maintenance execution, and release accountability limit the exposed share and require human validation.

## Value capture
A buyer can initially retain savings through avoided hiring, reduced administrative effort, lower scrap, and better uptime. Capture is weaker where customers receive open-book costing, cost-plus conversion pricing, frequent bids, or explicit productivity sharing. Retail and branded customers have procurement leverage, and competitive capacity can turn internal efficiency into lower renewal pricing.

## Firm availability
Only an estimated minority of firms in this residual NAICS category principally serve external customers through recurring contract or private-label programs. No reliable industry denominator exists for qualifying control transfers; a firm-by-firm roster and transaction match are essential. Customer concentration, food-safety history, equipment condition, certifications, and formulation ownership can sharply reduce transferability.

## Demand durability
Broad real food spending is resilient and physical food cannot be delivered by software alone. Outsourcing should persist where brands and retailers lack specialized lines, certifications, or economical scale. However, individual programs can be short, rebid, reformulated, shifted to another plant, or insourced, so durable category demand does not guarantee durable revenue for one operator.

## Risks and uncertainty
The largest evidence gaps are the eligible-firm share, qualifying transfer rate, customer contract economics, and actual task-level labor mix in small plants. Regulatory traceability increases both workflow opportunity and compliance burden. Commodity volatility, recalls, allergens, customer concentration, retailer bargaining power, legacy systems, low-quality plant data, and capex needs can overwhelm modest labor savings.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1839 | — | OBSERVED | — |
| n | — | 120 | — | ESTIMATE | — |
| a | 0.12 | 0.22 | 0.32 | PROXY | S2, S4 |
| rho | 0.3 | 0.5 | 0.7 | PROXY | S3, S4, S5 |
| e | 0.18 | 0.3 | 0.45 | ESTIMATE | S1, S7 |
| s5 | 0.12 | 0.18 | 0.28 | ESTIMATE | — |
| q | 0.18 | 0.35 | 0.55 | ESTIMATE | S7, S8 |
| d5 | 0.94 | 1.02 | 1.1 | PROXY | S6, S7 |
| o | 0.9 | 0.96 | 0.99 | ESTIMATE | S5, S7 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.26 | 0.81 | 1.65 | PROXY |
| F | 2.06 | 3.24 | 4.47 | ESTIMATE |
| C | 3.60 | 7.00 | 10.00 | ESTIMATE |
| D | 8.46 | 9.79 | 10.00 | ESTIMATE |

## Caveats
- a: The occupation table is for four-digit NAICS 311900 and includes branded and larger manufacturers outside the lens.
- a: Occupation shares are employment-weighted rather than wage-weighted; the range is a judgmental task decomposition.
- a: Exposure is not equivalent to full-job elimination and excludes already-automated work.
- rho: Current AI-use surveys are cross-sector or all-manufacturing and define use more broadly than realized labor substitution.
- rho: The NIST adoption figure relies on cited external survey work and includes chatbots, not only factory-floor implementation.
- rho: FDA traceability requirements apply only to covered foods and can create compliance work as well as automation opportunity.
- e: No source measures the contract/private-label share of LMM firms in NAICS 311999.
- e: Public-company channel evidence may not represent private LMM firms.
- e: Eligibility may change materially with the threshold used for recurring outsourced revenue.
- s5: This is a bounded hazard estimate, not an observed industry transfer rate.
- s5: Small private transactions are underreported and NAICS coding in deal databases is noisy.
- s5: Regulatory problems, customer concentration, or deferred capex can make an apparent firm non-transferable.
- q: Pricing terms vary by customer, ingredient volatility, formulation ownership, and capacity scarcity.
- q: The cited public-company disclosures are examples, not a measured distribution for NAICS 311999 LMM contracts.
- q: The estimate excludes demand volume loss and implementation failure, which belong in other primitives.
- d5: The USDA series covers all food at home and away from home, far broader than miscellaneous contract manufacturing.
- d5: Constant-dollar expenditure is an imperfect proxy for constant-quality physical quantity.
- d5: The public-company contract channel is adjacent and one-year growth is volatile.
- o: This is an operator-necessity judgment, not a measured substitution rate.
- o: The FDA traceability rule covers specified foods, not every 311999 product.
- o: Alternative physical manufacturers count as operator-required supply even if the incumbent loses the customer.

## Sources
- **S1** — [2022 NAICS Definition: 311999 All Other Miscellaneous Food Manufacturing](https://www.census.gov/naics/?details=311999&input=311999&year=2022) (accessed 2026-07-22): Official scope and illustrative products for the heterogeneous residual food-manufacturing category.
- **S2** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 311900](https://www.bls.gov/oes/2023/may/naics4_311900.htm) (accessed 2026-07-22): Broader other-food-manufacturing occupation mix, including 259,650 total jobs, 43.62% production, 7.15% office/administrative, 6.04% installation/maintenance, 5.69% management, 3.64% business/financial, and 2.64% sales.
- **S3** — [Large Firms With at Least 20 Employees Biggest AI Users](https://www.census.gov/library/stories/2026/05/ai-use-businesses.html) (accessed 2026-07-22): BTOS evidence that overall business AI use was 17%-20% from December 2025 to May 2026, expected six-month use was 20%-23%, and adoption rose with firm size.
- **S4** — [The Rise of Artificial Intelligence in U.S. Manufacturing: Text Only](https://www.nist.gov/mep/rise-artificial-intelligence-ai-us-manufacturing-text-only) (accessed 2026-07-22): Manufacturing AI applications in quality control, predictive maintenance, demand forecasting, resource management, and scheduling; reported adoption and barriers including data, cost, skills, cybersecurity, and legacy-system integration.
- **S5** — [FSMA Final Rule on Requirements for Additional Traceability Records for Certain Foods](https://www.fda.gov/food/food-safety-modernization-act-fsma/fsma-final-rule-requirements-additional-traceability-records-certain-foods) (accessed 2026-07-22): Covered manufacturers must maintain key data for critical tracking events, maintain a traceability plan, and provide relevant records or an electronic sortable spreadsheet to FDA within 24 hours; enforcement is deferred until July 20, 2028.
- **S6** — [Total U.S. food spending reached $2.51 trillion in 2025](https://www.ers.usda.gov/data-products/charts-of-note/114212) (accessed 2026-07-22): USDA constant-dollar food expenditure evidence: total spending rose from $2.49 trillion in 2024 to $2.51 trillion in 2025, with long-run growth in both food at home and away from home.
- **S7** — [John B. Sanfilippo & Son, Inc. 2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/880117/000095017025110463/jbss-20250626.htm) (accessed 2026-07-22): Adjacent public-company evidence that contract-manufacturing net sales rose 8.4% and volume 23.3% in fiscal 2025, while commodity costs and competitive pricing pressure affected margins.
- **S8** — [Manufacturing and Supply Agreement filed with the SEC](https://www.sec.gov/Archives/edgar/data/55067/000119312523249062/d517693dex102.htm) (accessed 2026-07-22): Example of outsourced-food manufacturing economics with a manufacturing fee tied to total product costs, quarterly cost review, reimbursement mechanics, and limits on annual conversion and overhead cost increases.
