# 332710 — Machine Shops

*v5.1 Stage 1 research memo. Run `332710-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** LOW_PRIORITY · A 7.51 · L 1.17 · interval STRUCTURAL_OUT → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Repeat job history plus labor-intensive quoting, programming, scheduling, inspection, and production coordination creates a credible AI-assisted capacity and avoided-hiring opportunity around scarce skilled labor.
**Weakness:** Most labor still supports physical production, implementation is constrained by legacy systems and safety-critical workflows, and competitive rebidding can pass common productivity gains to customers.

## Business-model lens
- Included: U.S. lower-middle-market firms providing recurring or repeat outsourced machining of metal, plastic, and composite parts on a job or order basis, including associated quoting, process planning, CNC programming, setup, inspection, and production coordination.
- Excluded: Captive internal machine departments, shells, non-control financing vehicles, industrial-equipment repair classified outside NAICS 332710, and standardized high-volume turned-product or fastener manufacturing classified outside NAICS 332710.
- Customer and revenue model: Business-to-business job shops principally earn revenue from customer purchase orders or quoted per-job or per-part work; repeat programs can recur, but price, quantity, tolerances, lead time, and quality obligations are commonly reset through new orders or rebids.
- Deviation from default lens: none

## Executive view
Machine shops combine a labor-intensive cost base with repeat outsourced physical work, but AI's most credible near-term role is to compress quoting, scheduling, programming, documentation, inspection analysis, and management effort rather than remove the core machining operation. The opportunity depends on selecting shops with reusable job history, digital machine and quality data, repeat customers, and enough management depth to implement change. It deteriorates quickly in owner-dependent, one-off, customer-concentrated, or poorly digitized shops.

## How AI changes the work
AI can parse drawings and RFQs, retrieve analogous jobs, draft quotes and routers, assist CAM and CNC programming, optimize schedules, flag anomalous inspection results, support predictive maintenance, and automate compliance records. Production remains the dominant occupation group, however, and physical setup, fixturing, tool choice, material movement, machine tending, metrology, root-cause work, and safe intervention constrain substitution. The five-year labor benefit is therefore more likely to appear as avoided indirect hiring, higher spindle utilization, shorter quote response, and operator leverage than as a broadly autonomous factory.

## Value capture
Quoted purchase-order work allows a shop to retain savings until a job is renewed or rebid, and faster delivery or scarce certified capacity can support retention. Over time, transparent digital quoting, customer cost-down expectations, global supplier choice, and competitor adoption should share a substantial portion of common productivity gains with buyers. Durable capture is more plausible when AI raises responsiveness, throughput, yield, and on-time delivery on constrained assets than when it merely lowers an easily benchmarked administrative cost.

## Firm availability
Aging manufacturing ownership creates real succession pressure, and observed manufacturing and machine-shop sales show that control transfers occur. Availability is not the same as retirement incidence: closure is common, and specialized assets, tribal process knowledge, working capital, customer approvals, and owner relationships make many shops difficult to transfer. A buyer should require evidence that customers, certifications, programmers, supervisors, and quality systems survive a change of control.

## Demand durability
Machined parts remain inputs to aerospace, defense, medical, energy, automotive, and industrial supply chains, and reshoring can favor responsive domestic job shops. Exact-industry real output was only modestly above its 2019 level in 2023, while the broader 3327 production index weakened through 2025, so a flat central outlook is more defensible than assuming a manufacturing boom. End-market mix, qualification status, tariffs, offshoring, additive manufacturing, and customer insourcing create a wide range around that center.

## Risks and uncertainty
The largest research gaps are task-level labor exposure, realized small-shop implementation, contract-level savings retention, and denominator-matched control-transfer frequency. Operational risks include quality escapes, unsafe machine intervention, cyber compromise of drawings or connected equipment, poor legacy data, failed ERP or MES integration, scarce programmers and quality staff, customer concentration, capex needs, and loss of owner-held relationships. AI can also intensify price comparison and supplier competition, making an undifferentiated shop a weaker proposition even if its internal costs improve.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.3733 | — | OBSERVED | — |
| n | — | 2876 | — | ESTIMATE | — |
| a | 0.11 | 0.17 | 0.25 | PROXY | S2, S3 |
| rho | 0.28 | 0.46 | 0.66 | PROXY | S3, S4, S5, S6 |
| e | 0.63 | 0.79 | 0.91 | ESTIMATE | S1, S8 |
| s5 | 0.07 | 0.15 | 0.25 | PROXY | S7, S8 |
| q | 0.36 | 0.56 | 0.76 | ESTIMATE | S1, S12 |
| d5 | 0.87 | 1.01 | 1.16 | PROXY | S9, S10, S11 |
| o | 0.86 | 0.94 | 0.98 | ESTIMATE | S1, S6, S11, S12 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.46 | 1.17 | 2.46 | PROXY |
| F | 7.80 | 9.38 | 10.00 | ESTIMATE |
| C | 7.20 | 10.00 | 10.00 | ESTIMATE |
| D | 7.48 | 9.49 | 10.00 | ESTIMATE |

## Caveats
- a: OEWS excludes self-employed owners, so owner-performed quoting, sales, engineering, and administration may be underrepresented.
- a: Occupation-level wage weighting does not observe task shares within occupations or distinguish already-automated work.
- a: The NIST use-case percentages cover U.S. manufacturing generally rather than lower-middle-market machine shops.
- rho: The NIST adoption figures cite manufacturing-wide surveys and include chatbots, which do not establish deep workflow implementation.
- rho: The McKinsey COO survey covers very large global manufacturers and is directionally relevant but structurally unlike LMM job shops.
- rho: Census broadened its AI-use question in November 2025, limiting comparisons with earlier adoption measures.
- rho: OSHA citations demonstrate safety and control constraints, not the causal effect of AI on implementation.
- e: The injected firm count is itself an estimate and may include firms whose margins or receipts were mis-bridged into the EBITDA band.
- e: Establishment-level NAICS classification does not reveal firm-level customer recurrence, owner dependence, or change-of-control restrictions.
- e: BizBuySell is a self-selected marketplace and its sold firms are not a representative eligibility sample.
- s5: McKinsey's figures are modeled and primarily cover firms with fewer than 500 employees, not the EBITDA-defined lens.
- s5: Its sector owner-age statistic combines manufacturing with mining and utilities.
- s5: BizBuySell does not provide the total eligible-firm denominator and skews toward smaller, brokered Main Street deals.
- s5: Family succession may be a true control transfer, but routine internal reorganizations are excluded from this primitive.
- q: No source directly measures how AI-created savings are shared in independent machine-shop contracts.
- q: Xometry is a digital intermediary and may overstate price transparency relative to relationship-based direct accounts.
- q: Retention varies sharply by certification, capacity scarcity, customer concentration, contract length, and whether savings improve throughput rather than reduce quoted cost.
- d5: The exact six-digit real-output series ends in 2023, while the timelier series combines adjacent 3327 industries.
- d5: Historical output is volatile and does not identify demand for only recurring outsourced work.
- d5: Reshoring expectations are directional and sensitive to policy, exchange rates, capacity, skills, and customer qualification timelines.
- d5: The range is a judgmental five-year translation, not a published forecast.
- o: There is no direct measure of operator-required quantity for machine shops.
- o: The estimate may be lower for simple parts that customers can print or machine internally and higher for certified, difficult-tolerance work.
- o: Operator requirement does not imply the current labor model persists; automation can substantially change staffing while leaving accountable ownership intact.

## Sources
- **S1** — [2017 NAICS Definitions: 332710 Machine Shops](https://www.census.gov/naics/2017NAICS/2017_Definition_File.pdf) (accessed 2026-07-22): The fetched Census definition states that machine shops machine metal, plastic, and composite parts on a job or order basis; jobs are generally low volume and use lathes including CNC, boring, grinding, milling, and additive manufacturing. It also distinguishes repair and non-job-order parts manufacturing.
- **S2** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 332710 Machine Shops](https://www.bls.gov/oes/2023/may/naics5_332710.htm) (accessed 2026-07-22): The fetched BLS table reports 265,030 total employees; production occupations at 176,650 or 66.65% with $52,520 annual mean wage; machinists at 64,080 or 24.18%; CNC operators and programmers at 37,240 or 14.05%; inspectors at 9,440 or 3.56%; office support at 9.90%; management at 6.83%; business and financial operations at 3.18%; and architecture and engineering at 2.98%.
- **S3** — [The Rise of Artificial Intelligence (AI) in U.S. Manufacturing](https://www.nist.gov/mep/rise-artificial-intelligence-ai-us-manufacturing-text-only) (accessed 2026-07-22): The fetched NIST page reports 46% of manufacturers using AI tools, more than 80% expecting to increase use in two years, and deployment in manufacturing/production (39%), inventory management (33%), quality (24%), R&D (24%), IT/OT (21%), maintenance/installation (17%), supply chain (11%), and product design (11%). It identifies data quality, cost, skills, cybersecurity, and legacy integration as barriers.
- **S4** — [Large Firms With at Least 20 Employees Biggest AI Users](https://www.census.gov/library/stories/2026/05/ai-use-businesses.html) (accessed 2026-07-22): The fetched Census BTOS article reports overall business AI use at 17-20% from December 2025 to May 2026, expected six-month use at 20-23%, 37% use among firms with at least 250 employees, 32% among firms with 100-249 employees, and less than 20% among firms with four or fewer employees. It notes the November 2025 question broadened to any business function.
- **S5** — [From pilots to performance: How COOs can scale AI in manufacturing](https://www.mckinsey.com/capabilities/operations/our-insights/from-pilots-to-performance-how-coos-can-scale-ai-in-manufacturing) (accessed 2026-07-22): The fetched article reports a 2025 survey of 101 senior operating executives at manufacturers with at least $1 billion revenue: about two-thirds were still at exploration or targeted implementation, only 2% were fully embedded across operations, and 46% cited data or IT/OT limitations. It identifies predictive maintenance, scheduling, process improvement, workforce enablement, and legacy infrastructure as central implementation issues.
- **S6** — [Frequently Cited OSHA Standards Results: NAICS 332710 Machine Shops](https://www.osha.gov/ords/imis/citedstandard.naics?p_esize=&p_naics=332710&p_state=FEFederal) (accessed 2026-07-22): The fetched OSHA table for October 2024 through September 2025 reports 655 citations across 211 inspections and $1,268,548 in current penalties, including 91 citations for general machine requirements and 89 for hazardous-energy control, evidencing physical safety and accountability constraints.
- **S7** — [Navigating the great small business ownership transition](https://www.mckinsey.com.br/our-insights/the-great-ownership-transfer-a-new-era-of-business-stewardship) (accessed 2026-07-22): The fetched article reports more than half of U.S. small-business owners are over 55, one in four is at least 65, six million ownership exits are modeled by 2035, and more than one million are considered viable transfer candidates. It reports 92% of 2022 SMB exits as closures, 5% sales, and 3% transfers; in capital-intensive sectors including manufacturing, more than 60% of owners are over 55 and about 26% are over 65.
- **S8** — [Manufacturing Business Valuation Benchmarks](https://www.bizbuysell.com/learning-center/valuation-benchmarks/manufacturing/) (accessed 2026-07-22): The fetched BizBuySell page analyzes 2,303 sold manufacturing listings, principally small businesses with annual sales below $10 million, and includes metal products and machining. Its 2021-2025 sector table reports machine shops and tool manufacturers at $1,093,406 median revenue, $269,438 median earnings, and $840,000 median sale price, confirming observed but self-selected transfer activity.
- **S9** — [Real Sectoral Output for Manufacturing: Machine Shops (NAICS 332710) in the United States](https://fred.stlouisfed.org/series/IPUEN332710T010000000) (accessed 2026-07-22): The fetched FRED page, sourcing BLS Industry Productivity, reports the exact-industry real sectoral output index at 102.810 in 2019, 92.104 in 2020, 102.580 in 2021, 109.405 in 2022, and 106.272 in 2023.
- **S10** — [Industrial Production: Machine Shops; Turned Product; and Screw, Nut, and Bolt (NAICS 3327)](https://fred.stlouisfed.org/series/IPG3327A) (accessed 2026-07-22): The fetched FRED page, sourcing the Federal Reserve G.17 release, reports the broader NAICS 3327 industrial-production index at 103.5785 in 2023, 98.1082 in 2024, and 94.3232 in 2025.
- **S11** — [What's Coming for U.S. Manufacturing in 2025](https://www.nist.gov/blogs/manufacturing-innovation-blog/whats-coming-us-manufacturing-2025) (accessed 2026-07-22): The fetched NIST MEP outlook expects reshoring to accelerate and create local-supplier opportunities for small manufacturers, while also describing more accessible flexible automation, AI-assisted predictive maintenance and quality control, additive manufacturing for customized and on-demand parts, and the continuing need for workforce training and cybersecurity.
- **S12** — [Xometry 2025 Annual Report and 2026 Proxy Materials](https://investors.xometry.com/node/12451/html) (accessed 2026-07-22): The fetched filing describes custom manufacturing as vast, complex, and fragmented; a platform digitizing pricing, sourcing, and fulfillment; structured data on quoting, pricing, supplier performance, and part quality; and approximately 5,000 active suppliers across 50 countries. It reports 2025 marketplace revenue of $629.6 million, evidence that digital intermediation is material while still relying on physical suppliers.
