# 115116 — Farm Management Services

*v5.1 Stage 1 research memo. Run `115116-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** PRIORITY · A 8.39 · L 4.06 · interval CONDITIONAL → PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** A definitionally recurring contract model combines a large information-processing workload with a durable base of non-operating and aging farmland owners.
**Weakness:** Local relationships, site judgment, and principal dependence can cap implementation and make customer retention fragile through a control transfer.

## Business-model lens
- Included: US lower-middle-market firms providing recurring farm management on a contract or fee basis, including production oversight, tenant and lease management, budgeting and accounting, crop marketing coordination, compliance, reporting, and arrangement of operating services for client farms.
- Excluded: Crop-producing farms and tenant farms, standalone harvesting, labor supply, cultivation, accounting, appraisal, brokerage, or consulting engagements without ongoing farm management, captive internal managers, shells, and non-control financing vehicles.
- Customer and revenue model: Landowners, heirs, trusts, estates, and agricultural investors retain an external manager through renewable management contracts; fees may be fixed, per acre, or linked to rent or adjusted farm income, with ongoing reporting and local oversight.
- Deviation from default lens: none

## Executive view
Farm management services fit the recurring outsourced-service lens unusually well because contract- or fee-based management defines the industry. The work has a sizable digital layer and durable landowner need, but success depends on preserving local expertise, client trust, and accountable field judgment while automating administration and analysis.

## How AI changes the work
AI can materially assist accounting, document intake, budgeting, reporting, lease administration, scheduling, market and yield analysis, compliance drafting, data reconciliation, and routine client updates. Managers still need to inspect farms, select and supervise operators, negotiate, resolve exceptions, and accept responsibility for consequential agronomic and financial decisions.

## Value capture
Per-acre, fixed, rent-linked, and income-linked fees are not simple hourly billing, so internal labor savings can be retained initially. One-year renewals and transparent performance create recurring repricing pressure, while widely available tools can lower client willingness to pay for undifferentiated administrative work.

## Firm availability
Correctly classified LMM firms should mostly be eligible recurring service providers, and the frozen dataset estimates 58 firms in band. General employer-owner evidence suggests meaningful five-year transfer intentions, but completed control deals, owner dependence, and post-sale retention remain unmeasured for this niche.

## Demand durability
USDA reports a large rented-farmland base dominated by non-farming landlords, with an old principal-landlord population. Those conditions support continuing demand for professional oversight, although direct tenant relationships, consolidation, insourcing, and software self-service can constrain quantity growth.

## Risks and uncertainty
Material risks include concentration by client, crop, and geography; annual contract renewal; dependence on individual managers; agronomic and fiduciary errors; weather and commodity stress; fragmented data; cybersecurity; customer self-service; institutional insourcing; and the absence of industry-specific task-time, AI adoption, transaction, churn, and managed-acre data.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.6892 | — | OBSERVED | — |
| n | — | 58 | — | ESTIMATE | — |
| a | 0.52 | 0.65 | 0.78 | PROXY | S2, S3, S4 |
| rho | 0.4 | 0.56 | 0.72 | ESTIMATE | — |
| e | 0.76 | 0.9 | 0.97 | PROXY | S1, S3 |
| s5 | 0.14 | 0.22 | 0.32 | PROXY | S5 |
| q | 0.48 | 0.65 | 0.8 | PROXY | S3, S7 |
| d5 | 0.98 | 1.08 | 1.2 | PROXY | S3, S4, S6 |
| o | 0.78 | 0.88 | 0.95 | ESTIMATE | — |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 5.73 | 10.00 | 10.00 | ESTIMATE |
| F | 3.17 | 4.06 | 4.74 | ESTIMATE |
| C | 9.60 | 10.00 | 10.00 | PROXY |
| D | 7.64 | 9.50 | 10.00 | ESTIMATE |

## Caveats
- a: O*NET covers agricultural managers broadly and is not weighted to this industry's occupation mix.
- a: Provider descriptions establish tasks but not current automation, time shares, or wages.
- a: The frozen labor-share input uses 2024 wages over 2022 receipts and a harmonization factor, so it carries stated vintage and basis uncertainty.
- rho: No farm-management-industry AI adoption or realized labor-savings study was located.
- rho: Implementation should vary by crop, geography, data quality, client sophistication, and existing software stack.
- rho: The estimate excludes pricing, demand, and valuation effects.
- e: The Census definition is a classification rule, not an audit of each firm's revenue quality.
- e: The renewal and tenure evidence comes from one large provider rather than an industry sample.
- e: The frozen count of 58 LMM firms is margin-bridged and quality ESTIMATE.
- s5: Gallup measures stated plans rather than completed control transfers.
- s5: Its sample spans industries and firm sizes rather than LMM farm-management firms.
- s5: Gifts, public offerings, and internal transfers in survey responses may not qualify under the lens.
- q: Published fees come from one regional provider and may not represent national or specialty-crop practices.
- q: One-year contracts increase repricing exposure even when customer relationships persist for decades.
- q: Benefits from improved farm output can flow to clients through fee formulas and are distinct from internal labor savings.
- d5: Rented acres and landlord counts are an addressable-base proxy, not observed management-service demand.
- d5: The industry serves crops and geographies unevenly, while TOTAL covers all US farmland.
- d5: Farmland ownership transfers can create or end management mandates depending on the buyer.
- o: The estimate separates operator requirement from labor substitution inside the operator.
- o: Smaller cash-rent portfolios may be more self-serviceable than complex crop-share or specialty operations.
- o: Remote sensing reduces visit frequency but does not necessarily remove accountability or field verification.

## Sources
- **S1** — [2012 NAICS Definition File: 115116 Farm Management Services](https://www2.census.gov/library/reference/naics/technical-documentation/definition-files/2012_definition_file.pdf) (accessed 2026-07-23): Defines establishments as providing farm management on a contract or fee basis, always including management and potentially arranging partial or complete farm operations; supports the lens and e.
- **S2** — [11-9013.00 - Farmers, Ranchers, and Other Agricultural Managers](https://www.onetonline.org/link/summary/11-9013.00?redir=11-9011.03) (accessed 2026-07-23): Lists management, records, clerical coordination, marketing, analysis, compliance, supervision, inspection, negotiation, planning, scheduling, and relevant software; supports the task-mix proxy for a.
- **S3** — [Farm Management Services for Landowners](https://www.farmersnational.com/farm-and-ranch/services/management) (accessed 2026-07-23): Describes recurring full-service workflows, regular reporting and visits, one-year contracts, and many multi-decade client relationships; supports a, e, q, and d5.
- **S4** — [Professional Farm Management: Preserving Your Legacy, Maximizing Your Land's Potential](https://www.hertz.ag/farm-management) (accessed 2026-07-23): Describes lease and tenant oversight, financial reporting, site visits, landowner segments, precision agriculture, and data-driven decisions; supports a and d5.
- **S5** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-23): Reports US employer-owner age and five-year sell-or-transfer intentions; supports the s5 proxy.
- **S6** — [Most of the U.S. Rented Farmland is Owned by Non-Farmers](https://www.nass.usda.gov/Newsroom/2026/03-12-2026.php) (accessed 2026-07-23): Reports the 2024 TOTAL survey's rented acres, landowner population, non-farming ownership share, rental economics, expected transfers, and landlord ages; supports d5.
- **S7** — [Unique Farm Management Fee System](https://www.stalcupag.com/services/farm-management/unique-farm-management-fee-system/) (accessed 2026-07-23): Discloses per-acre, adjusted-net-income, and 5-to-7-percent cash-rent management fee structures; supports the q proxy.
