# 624210 — Community Food Services

*v5.1 Stage 1 research memo. Run `624210-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 4.82 · L 0.64 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Persistent food need supports recurring physical service demand that software alone cannot fulfill.
**Weakness:** Much of the category may be nonprofit, donation-funded, and outside a conventional transferable-control investment model.

## Business-model lens
- Included: U.S. operators classified in community food services that repeatedly collect, prepare, distribute, or deliver food to external recipients and that can plausibly support lower-middle-market normalized operating earnings.
- Excluded: Volunteer-only programs, entities without transferable operating control, captive programs, one-off disaster responses, food retail, institutional cafeterias, and social-assistance activities not primarily centered on community food collection, preparation, distribution, or delivery.
- Customer and revenue model: Recipients often pay little or nothing; operating resources commonly come from contributions, donated food, grants, member-network support, public programs, or service contracts. The narrower investable subset may have recurring fixed-fee or reimbursement arrangements with governments, health plans, institutions, or sponsors.
- Deviation from default lens: none

## Executive view
Community food services combine durable social need with a modest administrative automation surface, but the fixed investment lens is a poor fit for much of the category. Many archetypal operators rely on charitable resources and may lack transferable equity or distributable economics, so legal form and revenue model must be established before operational upside matters.

## How AI changes the work
AI can assist intake and eligibility workflows, donor and grant communications, reporting, procurement analysis, volunteer scheduling, inventory exception handling, and route planning. It is unlikely to replace the physical work of food collection, preparation, warehousing, delivery, and recipient-facing service, and sensitive decisions require accountable human review.

## Value capture
Implemented savings can expand mission capacity, improve reserves, or support service quality, but may be shared through grant rules, reimbursement, competitive rebids, and donor expectations. The best retention case is a genuinely transferable operator with multi-year fixed-price contracts; that model should not be assumed for the whole industry.

## Firm availability
The modeled establishment count is especially uncertain as an acquisition pool because an EBITDA placeholder is applied to a sector with donated goods and nonprofit accounting. IRS private-benefit restrictions also make a conventional shareholder control sale inapplicable to section 501(c)(3) operators. Entity-level ownership and financial verification is therefore essential.

## Demand durability
Food insecurity remained widespread in 2024, supporting persistent underlying need, and most current services still require physical operators. Delivered demand can nevertheless diverge from need when appropriations, donations, food supply, benefit policy, or local capacity change.

## Risks and uncertainty
The largest uncertainties are the for-profit and transferable share, the meaning of normalized EBITDA where donated food is material, contract-level benefit retention, and the lack of six-digit task data. Public-benefit expansion, retailer fulfillment, or network consolidation could also displace local operators even if food need remains high.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1488 | — | OBSERVED | — |
| n | — | 229 | — | ESTIMATE | — |
| a | 0.15 | 0.24 | 0.36 | PROXY | S1, S2 |
| rho | 0.25 | 0.45 | 0.65 | ESTIMATE | S2, S5 |
| e | 0.03 | 0.12 | 0.28 | ESTIMATE | S1, S4, S5 |
| s5 | 0.01 | 0.04 | 0.1 | ESTIMATE | S4 |
| q | 0.2 | 0.42 | 0.65 | ESTIMATE | S4, S5 |
| d5 | 0.9 | 1.03 | 1.18 | PROXY | S3 |
| o | 0.72 | 0.88 | 0.97 | PROXY | S1, S5 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.22 | 0.64 | 1.39 | ESTIMATE |
| F | 0.11 | 1.19 | 3.22 | ESTIMATE |
| C | 4.00 | 8.40 | 10.00 | ESTIMATE |
| D | 6.48 | 9.06 | 10.00 | PROXY |

## Caveats
- a: OEWS is for NAICS 624200 and includes housing and emergency-relief establishments outside 624210.
- a: Employment shares are not wage-weighted task shares, and no cited source measures current AI exposure or existing automation.
- rho: No source measures five-year AI implementation in this six-digit industry.
- rho: A national network's technology capacity is unlikely to represent small local operators.
- e: No source measures the share of 624210 establishments meeting the fixed lens.
- e: The frozen firm-count input is margin-bridged from an 8% social-assistance placeholder; donated food and nonprofit accounting can make receipts-to-EBITDA inference materially misleading.
- e: IRS restrictions apply to section 501(c)(3) organizations, not every establishment in the NAICS code.
- s5: There is no observed control-transfer rate for eligible 624210 firms.
- s5: The estimate depends strongly on the unresolved legal-form mix and on whether asset transfers preserve the operating platform.
- q: The Feeding America financial statements describe one large nonprofit network, not the eligible lower-middle-market subset.
- q: Contract economics likely vary sharply between reimbursed programs, fixed grants, and fixed-fee meal delivery.
- d5: Food insecurity prevalence is need, not paid or funded service demand.
- d5: The 2024 measure is one national observation and cannot identify local funding or capacity constraints.
- o: The source establishes current activities, not a five-year substitution rate.
- o: Operator requirement may remain high while the specific local operator type changes through network centralization or retailer partnerships.

## Sources
- **S1** — [2022 NAICS Definition: 624210 Community Food Services](https://www.census.gov/naics/?details=624210&input=62421+&year=2022) (accessed 2026-07-22): Defines the industry as collection, preparation, and delivery of food for people in need, including food banks, meal-delivery programs, and soup kitchens.
- **S2** — [May 2023 OEWS: NAICS 624200 Community Food and Housing, and Emergency and Other Relief Services](https://www.bls.gov/oes/2023/may/naics4_624200.htm) (accessed 2026-07-22): Provides broader-industry employment and wage estimates by occupation, including management, business, office, food-preparation, and transportation roles.
- **S3** — [Household Food Security in the United States in 2024](https://www.ers.usda.gov/publications/113622) (accessed 2026-07-22): Reports that 13.7% of U.S. households were food insecure in 2024 and that prevalence was statistically similar to 2023.
- **S4** — [Inurement/private benefit: Charitable organizations](https://www.irs.gov/charities-non-profits/charitable-organizations/inurement-private-benefit-charitable-organizations) (accessed 2026-07-22): States that a section 501(c)(3) organization cannot operate for private interests and that net earnings cannot inure to a private shareholder or individual.
- **S5** — [Feeding America Financial Statements, June 30, 2025 and 2024](https://www.feedingamerica.org/sites/default/files/2025-11/Feeding%20America_25%20FS_Final.pdf) (accessed 2026-07-22): Documents donated food, contributions receivable, member grants, software assets, donor agreements, and network distribution arrangements at a major community-food nonprofit.
