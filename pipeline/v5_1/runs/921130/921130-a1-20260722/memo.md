# 921130 — Public Finance Activities

*v5.1 Stage 1 research memo. Run `921130-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** no base (evidence-first) · A — · L — · interval STRUCTURAL_OUT → HIGHEST_PRIORITY · readiness STRESS_TEST_ONLY · action EVIDENCE_FIRST

**Driver:** Statutory fiscal responsibilities and growing transaction and debt complexity sustain information-intensive work that AI can assist.
**Weakness:** The classification contains government establishments rather than transferable commercial firms, making firm availability and commercial value capture absent or undefined.

## Business-model lens
- Included: No privately owned firm satisfies the fixed lens. For operational context only, the classified activities are government public-finance functions including tax administration and collection, monetary policy, custody and disbursement of public funds, debt and investment administration, government auditing, and public employee retirement trust administration.
- Excluded: All government departments, agencies, authorities, treasuries, tax offices, central-bank functions, public retirement administrations, and other public establishments are excluded from the transferable-firm population because they are not privately controlled commercial firms; private contractors are classified according to the service they provide rather than as NAICS 921130.
- Customer and revenue model: The classified establishments exercise statutory public authority and are funded through appropriations, taxes, fees, or public funds. They do not earn recurring outsourced-service revenue from external commercial customers, and their budgets, public benefits, and legal mandates are not transferable EBITDA.
- Deviation from default lens: The default lens produces an empty population because Census defines this industry as government establishments. There is no coherent narrowing that converts a public-finance agency into a transferable private firm without leaving NAICS 921130.

## Executive view
Public Finance Activities is a government-only classification and therefore has no transferable private-firm population under the fixed lens. Its work is highly information-intensive and exposed to AI in intake, reconciliation, research, forecasting, taxpayer service, anomaly detection, drafting, and audit support, but implementation is slowed by legacy systems, privacy, due process, model risk, skills, and public accountability. Statutory demand is durable; commercial value capture and control-transfer probability are undefined. The missing compensation-to-receipts and LMM-count inputs are structural consequences of the government setting, not gaps to be filled with private-market proxies.

## How AI changes the work
Public-finance agencies can use AI for document and return processing, account reconciliation, fraud and anomaly detection, forecast support, debt and investment analytics, taxpayer assistance, audit selection, research, and first-draft communications. GAO reports active government use but also incomplete inventories, data-quality and skills gaps, model risk, privacy, bias, cybersecurity, and governance concerns. Human officials remain necessary for legal determinations, enforcement, appeals, monetary and fiscal judgment, and authorization of public funds.

## Value capture
There is no commercial price, renewal, or owner margin to retain. An implemented benefit may reduce backlog, improve collections, expand audit coverage, raise accuracy, shorten response time, or free appropriated resources, but budget rules and political decisions determine where that benefit goes. Those outcomes cannot be translated honestly into the commercial q construct.

## Firm availability
Census explicitly defines the industry as government establishments. Public treasuries, tax authorities, finance departments, central-bank functions, auditors, and retirement administrations cannot undergo a private control acquisition, and private contractors remain classified in their own software, accounting, consulting, collections, or administrative-service codes. The eligible share is structurally zero and the transfer probability is undefined.

## Demand durability
Taxation, fund custody and disbursement, budgeting, debt and investment administration, audit, retirement trusts, and monetary policy are continuing sovereign functions. BLS projects slow real growth in broader government output, and CBO projects large fiscal flows and rising federal debt that sustain administrative complexity. AI can reduce task volume per transaction, but an accountable government operator remains legally required.

## Risks and uncertainty
The decisive issue is lens incompatibility rather than operating attractiveness. Additional uncertainties include the absence of NAICS-specific occupation and workload data, missing receipts-based labor share, wide federal-state-local variation, legislative change, staffing reductions, legacy systems, procurement, cybersecurity, privacy, bias, explainability, appeal rights, records requirements, union constraints, and the risk that nominal fiscal growth is mistaken for service-volume growth.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | — | — | MISSING | — |
| n | — | — | — | MISSING | — |
| a | 0.45 | 0.62 | 0.78 | PROXY | S1, S2, S3, S4 |
| rho | 0.25 | 0.45 | 0.65 | ESTIMATE | S3, S4, S7 |
| e | 0 | 0 | 0 | ESTIMATE | S1 |
| s5 | — | — | — | MISSING | — |
| q | — | — | — | MISSING | — |
| d5 | 0.97 | 1.03 | 1.12 | PROXY | S1, S5, S6 |
| o | 0.96 | 0.99 | 1 | ESTIMATE | S1, S3, S4 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | — | — | — | MISSING |
| F | — | — | — | MISSING |
| C | — | — | — | MISSING |
| D | 9.31 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: No occupation source isolates NAICS 921130, so the broad-government mix is only a proxy.
- a: The assigned labor-share input is missing because government establishments have no comparable receipts denominator.
- a: Exposure describes public-agency work despite the fixed commercial lens having no eligible firms.
- a: Existing rules engines, electronic filing, and analytics must not be counted again as new AI opportunity.
- rho: The estimate applies only to the exposed opportunity in a and not to total agency labor.
- rho: Federal evidence may not transfer to smaller state and local finance offices with different systems and capabilities.
- rho: An active use-case inventory does not establish scaled deployment or realized labor substitution.
- rho: Regulated decisions often require human review even when AI produces an initial recommendation.
- e: The assigned LMM firm-count input is missing, consistent with government and SUSB scope exclusion.
- e: Zero is a structural lens conclusion, not an imputation for missing firm data.
- e: Government contractors may be economically relevant but are outside this NAICS code.
- s5: Public-sector reorganizations are not qualifying control transfers.
- s5: No commercial transaction denominator exists for this lens.
- q: Budgetary capacity and increased tax collection are not equivalent to commercial retained gross benefit.
- q: Appropriation rules may remove, redeploy, or supplement savings in ways the q construct does not represent.
- d5: BLS output aggregates are far broader than public finance and use national production concepts rather than administrative workload.
- d5: CBO projections cover federal finances only and fiscal dollars are not equivalent to constant-quality service quantity.
- d5: Legislation and administrative restructuring can change workload abruptly.
- o: A high operator-required share does not imply current staffing or workflows remain intact.
- o: Private vendors may supply technology and operations while legal accountability remains with government.
- o: This describes public-function durability, not an investable private operator population.

## Sources
- **S1** — [2022 NAICS Definition: 921130 Public Finance Activities](https://www.census.gov/naics/?chart=2022&details=92&input=92) (accessed 2026-07-22): Government-only industry boundary and included public-finance functions: taxation, monetary policy, fund custody and disbursement, debt and investment administration, auditing, and public retirement trust administration.
- **S2** — [May 2023 Occupational Employment and Wage Estimates by Government Ownership](https://www.bls.gov/oes/2023/may/999001.htm) (accessed 2026-07-22): Broad federal, state, and local government occupation and wage mix, including office, business and financial, computer, budget, tax, accounting, audit, and financial-examiner roles; used only as a proxy.
- **S3** — [Artificial Intelligence: IRS Actions Needed to Address Skills Gaps, Information Quality, and Strategic Management](https://www.gao.gov/products/gao-26-107522) (accessed 2026-07-22): IRS AI uses including audit selection and taxpayer questions, its 126 active use cases as of June 2025, and implementation weaknesses involving skills, inventories, information quality, and management.
- **S4** — [Artificial Intelligence: Use and Oversight in Financial Services](https://www.gao.gov/products/gao-25-107197) (accessed 2026-07-22): Federal financial regulators' use and oversight of AI, potential efficiency benefits, and model, bias, data-quality, privacy, and cybersecurity risks; staff generally retain decision authority.
- **S5** — [Industry employment and output projections to 2034](https://www.bls.gov/emp/tables/industry-employment-and-output.htm) (accessed 2026-07-22): Broader real-government output projections: 0.4 percent annual growth for federal government and 0.6 percent for state and local government excluding education and hospitals from 2024 to 2034.
- **S6** — [The Budget and Economic Outlook: 2026 to 2036](https://www.cbo.gov/publication/62105) (accessed 2026-07-22): Projected federal revenues, outlays, deficits, debt, and interest costs, supporting continuing fiscal-administration scale and complexity rather than a direct service-demand measure.
- **S7** — [Administrative Resource Center Monthly Bulletin: August 2025](https://arc.fiscal.treasury.gov/files/bulletin/2025/2025-08.pdf) (accessed 2026-07-22): Treasury shared-services exploration and controlled testing of AI use cases for operational efficiency, indicating implementation activity but not yet measured scaled labor substitution.
