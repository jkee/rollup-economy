# 525910 — Open-End Investment Funds

*v5.1 Stage 1 research memo. Run `525910-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** no base (evidence-first) · A — · L — · interval STRUCTURAL_OUT → HIGHEST_PRIORITY · readiness STRESS_TEST_ONLY · action EVIDENCE_FIRST

**Driver:** Official Census and SEC materials consistently separate the investment vehicle from the fee-earning adviser or manager.
**Weakness:** No establishment-level register was available to test for rare correctly classified hybrid operators, so the conclusion relies on official taxonomy and regulatory structure rather than an empirical enumeration.

## Business-model lens
- Included: Potentially included only if an establishment correctly classified in NAICS 525910 supplies recurring outsourced services to unrelated external customers. The official definition instead identifies legal entities and open-end funds that pool securities or other financial instruments and continuously issue and redeem shares.
- Excluded: Open-end mutual funds and money-market mutual funds are excluded because they are investment vehicles, not external-customer service firms. Investment advisers, portfolio managers, administrators, distributors, custodians, and other fee-earning operators are excluded when they are separately classified service establishments.
- Customer and revenue model: Investors purchase and redeem fund shares at net asset value; the fund pools assets and earns investment or property income. The investment adviser is typically a separate entity compensated for managing the portfolio, so adviser fee revenue is not the fund vehicle's external-service revenue.
- Deviation from default lens: none

## Executive view
NAICS 525910 is an investment-vehicle category, not a recurring outsourced-service industry. Census defines it as open-end funds that pool assets and continuously issue and redeem shares, while fund-management employees are classified in NAICS 5239. SEC materials reinforce that the investment adviser is typically a separate entity. Under the frozen lens, eligible establishment share is structurally zero and the remaining operating primitives are undefined.

## How AI changes the work
Portfolio research, compliance, reporting, servicing, and distribution may contain automatable work, but those workflows generally sit with separately organized advisers and service providers. Applying their AI economics to the fund vehicle would cross the official industry boundary.

## Value capture
The fund issues redeemable shares, pools assets, and pays service providers; it is not the fee-earning operator under the lens. Fund returns or expense ratios therefore do not supply a valid retained-benefit measure for a qualifying service firm.

## Firm availability
The supplied LMM firm-count estimate does not establish acquisition-ready service operators. The official classification instead describes legal fund entities, and Census assigns dedicated management establishments to NAICS 5239.

## Demand durability
Demand for pooled, redeemable investment products may persist, but that is product-vehicle demand. It does not establish recurring external-customer service demand within 525910.

## Risks and uncertainty
The main analytical hazard is consolidating the fund, adviser, administrator, distributor, and custodian into one economic unit despite their separate legal and classification roles. Rare vertically integrated or miscoded establishments would require establishment-level verification.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.8483 | — | OBSERVED | — |
| n | — | 46 | — | ESTIMATE | — |
| a | — | — | — | MISSING | — |
| rho | — | — | — | MISSING | — |
| e | 0 | 0 | 0 | OBSERVED | S1, S2 |
| s5 | — | — | — | MISSING | — |
| q | — | — | — | MISSING | — |
| d5 | — | — | — | MISSING | — |
| o | — | — | — | MISSING | — |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | — | — | — | MISSING |
| F | — | — | — | MISSING |
| C | — | — | — | MISSING |
| D | — | — | — | MISSING |

## Caveats
- a: Using the supplied labor ratio would attribute separately classified management labor to the fund vehicle and materially misstate this construct.
- rho: AI adoption by advisers, administrators, transfer agents, or distributors belongs to their operating industries unless an explicit bridge is justified.
- e: This is a taxonomy-based structural zero for the stated lens, not a claim that the investment-fund ecosystem lacks service providers.
- s5: Fund continuation, merger, or liquidation is not equivalent to operating-company survival.
- q: Fund expense ratios and investment returns are not interchangeable with retained gross benefit at a service operator.
- d5: Durable investor use of open-end funds does not establish demand for an in-scope service firm in this code.
- o: Acquiring or governing a regulated fund vehicle is not equivalent to owner-operating an independent LMM service business.

## Sources
- **S1** — [NAICS Sector 52: Finance and Insurance](https://www.census.gov/naics/resources/archives/sect52.html) (accessed 2026-07-22): Official definitions for subsector 525 and industry 525910, including fund-vehicle characteristics, continuous share issuance and redemption, absence of service-sale revenue, and classification of fund-management establishments in NAICS 5239.
- **S2** — [Investment Company Registration and Regulation Package](https://www.sec.gov/about/divisions-offices/division-investment-management/investment-company-registration-regulation-package) (accessed 2026-07-22): Regulatory structure of open-end management companies, redeemable securities, board oversight, and the typically separate investment adviser that manages the portfolio for a fee.
- **S3** — [Investment Companies](https://www.sec.gov/answers/mfinvco.htm) (accessed 2026-07-22): SEC overview of investment companies and open-end mutual funds as collective investment vehicles issuing redeemable shares.
