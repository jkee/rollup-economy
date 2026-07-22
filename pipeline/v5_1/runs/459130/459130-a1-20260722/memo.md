# 459130 — Sewing, Needlework, and Piece Goods Retailers

*v5.1 Stage 1 research memo. Run `459130-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** no base (evidence-first) · A — · L — · interval STRUCTURAL_OUT → STRUCTURAL_OUT · readiness STRESS_TEST_ONLY · action EVIDENCE_FIRST

**Driver:** Tactile product selection, physical machine and quilting services, and hands-on community education preserve a local operator alongside AI-assisted administration.
**Weakness:** The eligible service-bearing firm share and target-band transfer market are not directly measured, and demand faces digital self-service plus demographic aging.

## Business-model lens
- Included: Lower-middle-market sewing, quilting, yarn, needlework, and piece-goods retailers with repeat external-customer services such as sewing-machine service coordination, repair, long-arm quilting, paid classes, clubs, block-of-the-month programs, subscriptions, or recurring institutional supply and instruction.
- Excluded: Pure fabric, yarn, notion, pattern, and online merchandise sellers; machine-only appliance retailers; reupholstery firms; independent makers selling finished goods; captive operations; shells; non-control financing vehicles; and firms without a recurring or repeat outsourced-service relationship.
- Customer and revenue model: Repeat consumer, guild, school, and institutional relationships combining merchandise margin with repair or service fees, classes, clubs, subscriptions, project programs, machine support, or long-arm services; recurring programs often stimulate repeat materials purchases.
- Deviation from default lens: The code is primarily product retail but contains a distinct service-bearing subset of machine-support, repair, long-arm, instruction, club, subscription, and repeat-program operators. The lens is narrowed to that subset for business-model coherence because ordinary piece-goods sales are transactional.

## Executive view
The relevant opportunity is not ordinary fabric or yarn retail but the subset combining products with machine support, repair, long-arm work, hands-on instruction, clubs, subscriptions, or recurring project programs. AI can reduce information, coordination, marketing, and administration work, while tactile selection, physical service, specialist trust, and live education preserve operator roles.

## How AI changes the work
Near-term uses include pattern and product search, class descriptions and promotion, customer messaging, order entry, inventory suggestions, scheduling, subscription administration, bookkeeping, and first-line troubleshooting. AI-enabled design tools also reduce project setup. Physical repair, material handling, cutting, long-arm quilting, classroom facilitation, and nuanced exception resolution remain human-intensive.

## Value capture
Local differentiation and trusted expertise should preserve more benefit than in commodity retail, particularly for repair, long-arm, and hands-on instruction. Over time, free video education, AI design platforms, online assortments, transparent prices, and manufacturer ecosystems will force sharing through prices, richer service, or convenience.

## Firm availability
Classes, repair, clubs, and project programs make a meaningful minority of shops plausibly eligible, but the share is not directly measured and many services are incidental or free. Broad owner aging supports succession supply, although target-size businesses may be scarce and owner expertise or community goodwill may transfer poorly.

## Demand durability
Quilting participation has remained broadly stable for a decade and highly engaged consumers still prefer local fabric shops, supporting operator demand. Post-pandemic normalization, inflation-driven stash use, an aging participant base, and digital self-service keep the five-year outlook close to flat rather than clearly growing.

## Risks and uncertainty
Evidence is strongest for quilting consumers, not all sewing, yarn, upholstery-material, and needlework retailers. Opt-in survey selection may overstate local loyalty and engagement. Digital instruction and design can erode services, while discretionary spending, inventory breadth, lease costs, owner dependence, and classification leakage constrain transferability.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1014 | — | ESTIMATE | — |
| n | — | — | — | MISSING | — |
| a | 0.15 | 0.23 | 0.33 | PROXY | S1, S2, S3, S5 |
| rho | 0.31 | 0.47 | 0.64 | PROXY | S2, S3, S5 |
| e | 0.07 | 0.14 | 0.24 | PROXY | S1, S4, S6 |
| s5 | 0.09 | 0.16 | 0.25 | PROXY | S4, S7, S8 |
| q | 0.45 | 0.61 | 0.77 | PROXY | S4, S5 |
| d5 | 0.91 | 1 | 1.1 | PROXY | S4, S5 |
| o | 0.58 | 0.74 | 0.88 | PROXY | S2, S4, S5, S6 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.19 | 0.44 | 0.86 | ESTIMATE |
| F | — | — | — | MISSING |
| C | 9.00 | 10.00 | 10.00 | PROXY |
| D | 5.28 | 7.40 | 9.68 | PROXY |

## Caveats
- a: The occupation source covers the broader three-digit NAICS 459000 group and includes unrelated specialty retailers.
- a: Employment shares are not wage-weighted task shares and exclude self-employed owners.
- a: Existing POS, e-commerce, pattern software, and machine automation are not separately measured.
- rho: BLS projections cover all industries and a ten-year horizon, not this industry and five years.
- rho: Cricut is a scaled manufacturer/platform rather than an LMM retailer.
- rho: Self-checkout, e-commerce, and machine automation are not identical to AI implementation.
- e: Customer preference for education does not establish recurring service revenue at the firm level.
- e: Sewing-machine-only retailers and reupholstery services are classified elsewhere, creating boundary leakage.
- e: The frozen n input is missing, so eligible firm count cannot be derived in this packet.
- s5: The quilting survey describes customers, not business owners, and has a long, opt-in questionnaire with likely selection bias.
- s5: The Census age statistic is cross-industry and based on data year 2018 responding owners.
- s5: BizBuySell skews toward transactions below the target LMM EBITDA band.
- q: The consumer survey sample is highly engaged and likely overrepresents local-shop users.
- q: Repair, instruction, long-arm, subscription, and merchandise pricing have different pass-through dynamics.
- q: Cricut's economics reflect a proprietary hardware-software ecosystem unavailable to most retailers.
- d5: Participation and spending intentions are not direct service-quantity measures.
- d5: Survey respondents are self-selected from major quilting brand lists and may overstate engagement.
- d5: Cricut users span paper, vinyl, gifts, and other crafts beyond sewing and needlework.
- o: The quilting survey may overrepresent highly engaged local-shop customers.
- o: Digital substitution varies between fabric selection, yarn, machine repair, long-arm work, patterns, and instruction.
- o: The estimate applies only to the narrowed service-bearing basket, not ordinary merchandise demand.

## Sources
- **S1** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 459000](https://www.bls.gov/oes/2023/may/naics3_459000.htm) (accessed 2026-07-22): Parent-industry occupation shares including sales 56.80%, retail salespersons 37.94%, cashiers 9.17%, office and administrative support 9.99%, self-enrichment teachers 0.62%, and installation, maintenance, and repair 2.76%.
- **S2** — [Occupational Outlook Handbook: Cashiers](https://www.bls.gov/ooh/sales/cashiers.htm) (accessed 2026-07-22): Cashier employment is projected to decline 10% from 2024 to 2034; BLS cites self-service checkout and increasing online sales.
- **S3** — [Occupational Outlook Handbook: Customer Service Representatives](https://www.bls.gov/ooh/office-and-administrative-support/customer-service-representatives.htm) (accessed 2026-07-22): Customer-service-representative employment is projected to decline 5% from 2024 to 2034; duties include complaints, orders, questions, returns, billing, and account updates.
- **S4** — [The Size of the Quilting Market: Quilting Trends Survey Results 2024](https://craftindustryalliance.org/the-size-of-the-quilting-market-quilting-trends-survey-results-2024/) (accessed 2026-07-22): A 37,000-response survey reported 9–11 million active quilters stable over a decade, 30 million active sewists in the U.S. and Canada, 61% local-shop preference, 48% buying fabric most often locally, 31.8% searching and shopping more online, and 80% spending the same or more time and dollars.
- **S5** — [Cricut, Inc. Form 10-K for year ended December 31, 2025](https://www.sec.gov/Archives/edgar/data/1828962/000182896226000010/crct-20251231.htm) (accessed 2026-07-22): Cricut disclosed AI-generated cut-ready images, 5.9 million active users, 3.09 million paid subscribers, repeat material purchases, 23% of users making projects to sell, and revenue declines in 2023–2025 after pandemic-era growth.
- **S6** — [The North American Industry Classification System in the Current Employment Statistics Program](https://www.bls.gov/ces/naics/naics-2022.htm) (accessed 2026-07-22): BLS maps 95.7% of the new 459130 employment definition from legacy sewing, needlework, and piece-goods stores, 4.2% from electronic shopping and mail-order houses, and 0.1% from other direct selling establishments.
- **S7** — [Business Owners' Ages](https://www.census.gov/content/dam/Census/library/visualizations/2020/comm/business-owners-ages.pdf) (accessed 2026-07-22): The 2019 Annual Business Survey, data year 2018, found 51% of responding U.S. employer-business owners were age 55 or older, with explicit representativeness limits.
- **S8** — [Retail Business Valuation Multiples and Financial Benchmarks](https://www.bizbuysell.com/learning-center/valuation-benchmarks/retail-business/) (accessed 2026-07-22): Independent retail transactions reported to BizBuySell had a 2025 median sale price of $273,647; the benchmark reports median revenue of $720,000, median owner earnings of $131,498, and median 165 days on market.
