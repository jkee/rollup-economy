# 322220 — Paper Bag and Coated and Treated Paper Manufacturing

*v5.1 Stage 1 research memo. Run `322220-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 6.47 · L 0.62 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Repeat, specification- and artwork-heavy bag programs create implementable AI opportunities while policy can shift demand from plastic to paper.
**Weakness:** The broad code mixes incompatible processes, and commodity bidding plus material pass-through limit retained gains in a physical production business.

## Business-model lens
- Included: Independent US manufacturers in the approximately $1-10 million normalized EBITDA band repeatedly supplying paper carryout, merchandise, food, pharmacy, and multiwall industrial bags and sacks to external customers.
- Excluded: Coated or laminated rollstock and packaging paper, surface-coated paperboard, laminated aluminum foil, captive plants, brokers without accountable production, shells, financing vehicles, and firms outside the EBITDA band.
- Customer and revenue model: Recurring business-to-business supply of standard or custom printed bags and sacks under quotes, purchase orders, releases, and supply agreements, with pricing driven by paper, recycled content, coatings or liners, printing, dimensions, run length, compliance, and freight.
- Deviation from default lens: NAICS 322220 combines bag and multiwall-sack converting with coated and laminated packaging paper, surface-coated paperboard, and foil-laminate production. The lens retains paper bags and sacks because they share discrete-product converting, printing, customer, and replenishment workflows; rollstock coating and laminating are excluded because their continuous processes, markets, and economics make a single screen incoherent.

## Executive view
The narrowed paper-bag and sack population has recurring orders, moderate injected labor intensity, and practical AI workflows in quoting, artwork, order handling, scheduling, compliance, and service. Production remains physical, pricing is material-sensitive, and the broad NAICS makes the actual eligible firm pool uncertain.

## How AI changes the work
AI can parse specifications, draft quotes, compare print revisions, enter and validate orders, assist schedules and purchasing, retrieve maintenance knowledge, prepare recycled-content and food-contact records, and triage service. Forming, printing, gluing, sealing, handling, inspection, and repair remain machine- and human-led.

## Value capture
Less scrap, fewer errors, uptime, and service gains can be retained more readily than transparent administrative reductions. Paper escalators, standardized bids, national accounts, and annual negotiations return part of the benefit to customers.

## Firm availability
The frozen estimate of 211 firms spans bag converting and excluded coating, laminating, surface-coated board, and foil businesses. A product-by-parent map is required before relying on it; broad owner aging supports succession pressure but not an observed transfer rate.

## Demand durability
Paper substitution from plastic and recurring retail, food, and industrial uses support modest growth. Reusable bags, source reduction, industrial cycles, and formulation changes offset that tailwind; California's policy shows both the opportunity for recycled paper and the explicit goal of reducing store-provided bags.

## Risks and uncertainty
Major gaps are subgroup weights, six-digit occupations, current automation, margin-band accuracy, customer concentration, paper-price terms, direct shipment history, and policy-driven substitution. PFAS and recycled-content changes can require capital, materials development, qualification, and documentation.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1621 | — | OBSERVED | — |
| n | — | 211 | — | ESTIMATE | — |
| a | 0.1 | 0.17 | 0.26 | PROXY | S1, S2 |
| rho | 0.37 | 0.56 | 0.72 | ESTIMATE | S3, S6 |
| e | 0.3 | 0.5 | 0.68 | ESTIMATE | S2 |
| s5 | 0.14 | 0.24 | 0.36 | PROXY | S5 |
| q | 0.32 | 0.53 | 0.72 | ESTIMATE | S4 |
| d5 | 0.98 | 1.07 | 1.19 | PROXY | S3, S4, S6 |
| o | 0.93 | 0.98 | 1 | ESTIMATE | S2, S4 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.24 | 0.62 | 1.21 | ESTIMATE |
| F | 3.68 | 5.26 | 6.38 | ESTIMATE |
| C | 6.40 | 10.00 | 10.00 | ESTIMATE |
| D | 9.11 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: Occupation data are for NAICS 322, not 322220 or the narrowed lens.
- a: Retail bag and industrial sack plants may have materially different administrative and technical staffing.
- rho: No representative AI deployment evidence for the narrowed population was found.
- rho: Regulatory change can create new documentation work even as AI reduces time per document.
- e: No source reports the firm share of the retained product group.
- e: The injected n=211 is an ESTIMATE using a broad paper-industry margin that may not fit bag converters.
- s5: Owner-age evidence is all-industry and data year 2018.
- s5: The narrowed firms may differ from the overall employer-owner population in age and family ownership.
- q: No representative contract dataset was found.
- q: Retention is likely lower for plain standard sacks and higher for short-run custom printed bags.
- d5: One state's law is not a national demand measure.
- d5: BLS covers all of NAICS 3222, and no direct current shipment forecast for the narrowed basket was found.
- o: Reusable containers can eliminate some single-use bag quantity, captured in d5.
- o: Distributor or e-commerce self-service may replace sales interactions without replacing the converting operator.

## Sources
- **S1** — [Paper Manufacturing: NAICS 322](https://www.bls.gov/iag/tgs/iag322.htm) (accessed 2026-07-22): BLS reports 2025 paper-manufacturing employment of 87,050 paper-goods machine operators, 17,540 production supervisors, 14,210 industrial-truck operators, and 6,640 production managers, supporting a production-heavy labor mix.
- **S2** — [NAICS Code 322220: Paper Bag and Coated and Treated Paper Manufacturing](https://www.census.gov/naics/?details=322220&input=322220&year=2012) (accessed 2026-07-22): Census index entries show the code combines paper and multiwall bags with laminated or coated combinations of paper, plastic and foil and surface-coated paperboard, supporting the coherence narrowing.
- **S3** — [Employment and output by industry, 2024-2034](https://www.bls.gov/emp/tables/industry-employment-and-output.htm) (accessed 2026-07-22): BLS projects converted paper product manufacturing output rising from $99.0 billion in 2024 to $116.9 billion in 2034 in chained 2017 dollars, a 1.7% annual rate, while employment falls 5.4%.
- **S4** — [California SB-1053: Solid waste, recycled paper bags, standards, carryout bag prohibition](https://leginfo.legislature.ca.gov/faces/billNavClient.xhtml?bill_id=202320240SB1053) (accessed 2026-07-22): Chaptered California law makes its revised carryout-bag regime operative January 1, 2026, permits qualifying recycled paper bags, eliminates plastic-film carryout bags, and requires recycled paper bags to contain at least 50% postconsumer material from January 1, 2028.
- **S5** — [Business Owners' Ages](https://www.census.gov/content/dam/Census/library/visualizations/2020/comm/business-owners-ages.pdf) (accessed 2026-07-22): The 2019 Annual Business Survey infographic reports 51% of responding owners of employer businesses were age 55 or older; estimates represent 4.1 million responding owners in data year 2018.
- **S6** — [Authorized Uses of PFAS in Food Contact Applications](https://www.fda.gov/food/process-contaminants-food/authorized-uses-pfas-food-contact-applications) (accessed 2026-07-22): FDA states that in January 2025 it determined 35 food-contact notifications for PFAS grease-proofers applied to paper and paperboard food packaging were no longer effective after abandonment of those uses.
