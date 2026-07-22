# 524114 — Direct Health and Medical Insurance Carriers

*v5.1 Stage 1 research memo. Run `524114-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 4.94 · L 0.36 · interval STRUCTURAL_OUT → STRUCTURAL_OUT · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Large, repetitive claims, service, authorization, enrollment, and data workflows create substantial scope for governed AI assistance and avoidable hiring.
**Weakness:** Medical claims consume most premium, margins and renewal pricing are constrained, and only a small uncertain population of independently transferable LMM risk-bearing carriers is available.

## Business-model lens
- Included: Lower-middle-market U.S. direct carriers repeatedly underwriting health and medical insurance risk for external individuals, employers, associations, and government-program members, including risk-bearing group and individual plans, Medicare and Medicaid products, supplemental coverage, dental and vision coverage, and HMOs that provide insurance without directly providing health care.
- Excluded: HMOs that also provide health care, self-insured employer funds, health and welfare funds, reinsurers, brokers and agents without underwriting risk, third-party administrators without direct carrier risk, providers, software vendors, shells, subscale hobby businesses, and non-control financing vehicles.
- Customer and revenue model: Individuals, employers, associations, and government programs pay recurring premiums or capitation for the carrier to assume medical-cost risk, maintain networks and benefits, enroll and serve members, adjudicate claims, manage utilization, meet regulatory obligations, and pay covered providers. Premium and reimbursement rates are renewed or reset periodically, medical claims consume most revenue, and some products operate under federal or state program rules and risk adjustment.
- Deviation from default lens: none

## Executive view
Direct health carriers have unusually large transaction, service, claims, authorization, and data-processing workflows and a high reported rate of AI use or interest. Yet medical costs dominate premiums, margins are thin, rates reset frequently, and the carrier remains accountable for coverage, networks, appeals, and risk, so the opportunity is disciplined operating leverage rather than software replacement of insurance.

## How AI changes the work
AI can classify and extract documents, answer member and provider inquiries, clean provider data, support enrollment, adjudicate routine claims, detect fraud, prioritize reviews, summarize records, assist prior authorization and appeals, model risk adjustment, draft communications, and support pricing and contracting. Human clinical, actuarial, legal, compliance, network, and exception judgment remains central.

## Value capture
Savings can be retained during an existing premium period, especially in administration, but annual renewals, government rate resets, employer procurement, statutory medical-loss ratios and rebates, provider and broker economics, risk adjustment, utilization response, and model and integration costs constrain five-year retention.

## Firm availability
The frozen LMM population is small and uncertain, while attractive carriers offer licenses, covered lives, networks, contracts, data, and claims infrastructure. Transferability is limited by statutory capital, volatile medical trends, nonprofit or sponsor ownership, government contracts, rate and product approvals, network obligations, cybersecurity, and change-of-control review.

## Demand durability
Healthcare need, employer coverage, chronic disease, and Medicare growth support durable plan administration and risk-bearing demand. Enrollment can migrate among commercial carriers, self-funded employers, public programs, and provider-sponsored models, and policy, subsidy, affordability, and Medicaid changes can outweigh underlying medical need.

## Risks and uncertainty
Key risks are medical-cost and utilization spikes, inadequate rates, adverse selection, risk-adjustment error, government reimbursement, MLR rebates, network concentration, provider disputes, appeals and denials, clinical harm, unfair discrimination, privacy and cybersecurity, legacy integration, fraud, regulatory enforcement, and overestimating labor removal from tools that mainly improve service or add review. The general-insurance margin bridge may materially misstate the LMM firm count.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.0432 | — | OBSERVED | — |
| n | — | 41 | — | ESTIMATE | — |
| a | 0.25 | 0.38 | 0.52 | PROXY | S2, S3 |
| rho | 0.34 | 0.55 | 0.72 | PROXY | S3 |
| e | 0.45 | 0.68 | 0.84 | ESTIMATE | S1, S4, S6 |
| s5 | 0.03 | 0.09 | 0.17 | PROXY | S4, S7 |
| q | 0.2 | 0.38 | 0.58 | PROXY | S4, S5, S6 |
| d5 | 0.97 | 1.04 | 1.12 | PROXY | S4, S6 |
| o | 0.86 | 0.94 | 0.985 | PROXY | S1, S3, S6 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.15 | 0.36 | 0.65 | PROXY |
| F | 0.71 | 2.02 | 3.10 | ESTIMATE |
| C | 4.00 | 7.60 | 10.00 | PROXY |
| D | 8.34 | 9.78 | 10.00 | PROXY |

## Caveats
- a: The BLS table covers employers of all sizes and does not separate small risk-bearing carriers from large national plans.
- a: Occupation shares are not task-level AI exposure and include work already performed by rules engines, portals, and electronic claims systems.
- a: Commercial group, individual, Medicare, Medicaid, supplemental, dental, and vision products have different labor and clinical-review intensity.
- rho: The 92% statistic combines current use with plans and exploration and is not an implementation or realized-savings rate.
- rho: NAIC states that AI generally supports rather than fully replaces underwriters, claims professionals, agents, and service representatives.
- rho: Prior authorization and claims models face especially high clinical, fairness, documentation, and appeal constraints.
- e: No source measures default-lens eligibility among the frozen LMM-band firms.
- e: The 41-firm anchor uses a general-insurance margin bridge that may not fit health carriers with high medical-loss ratios, risk adjustment, and government-program revenue.
- e: Legal entities, plans, insurance groups, regional subsidiaries, and provider-sponsored arrangements are not interchangeable transaction units.
- s5: Gallup measures cross-industry intentions rather than completed health-carrier transfers.
- s5: The NAIC filer count includes legal entities and organizational forms outside the LMM control lens.
- s5: No cited source supplies an industry denominator of completed qualifying control deals.
- q: Neither CMS nor NAIC measures five-year retention of implemented AI benefit at LMM carriers.
- q: MLR rules differ by market, and administrative savings do not mechanically create a rebate if the claims-and-quality share remains above the threshold.
- q: Commercial, Medicare, Medicaid, supplemental, dental, and vision products transmit savings through different renewal and rate-setting mechanisms.
- d5: Enrollment across product lines may double-count people and is not constant-quality service volume.
- d5: Premium growth is dominated by medical-cost inflation, benefit, subsidy, and mix changes.
- d5: Policy and reimbursement changes can sharply alter Medicaid, Medicare, and individual-market enrollment within the horizon.
- o: Operator-required plan functions do not guarantee that an independent LMM carrier retains members or contracts.
- o: Self-funded employers may use the same claims and network infrastructure while moving underwriting risk outside the direct-carrier lens.
- o: Medicare, Medicaid, commercial group, individual, supplemental, dental, and vision plans have different substitution paths.

## Sources
- **S1** — [North American Industry Classification System, United States, 2022](https://www.census.gov/naics/reference_files_tools/2022_NAICS_Manual.pdf) (accessed 2026-07-22): Defines 524114 as direct underwriting of health and medical policies, includes risk-only group hospitalization plans and HMOs, and excludes provider HMOs, reinsurance, and captive health and welfare funds.
- **S2** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 524114](https://www.bls.gov/oes/2023/may/naics5_524114.htm) (accessed 2026-07-22): Reports six-digit occupation employment shares and wages, including administrative support, business and financial, IT, customer service, claims adjustment, and claims and policy processing.
- **S3** — [Insurance Topics: Artificial Intelligence](https://content.naic.org/insurance-topics/artificial-intelligence) (accessed 2026-07-22): Reports that 92% of 93 responding health insurers use, plan to use, or plan to explore AI/ML and identifies contracting, authorization, fraud, pricing, data, risk-adjustment, marketing, risk-management, and claims uses plus governance constraints.
- **S4** — [U.S. Health Insurance Industry Analysis Report: 2025 Annual Results](https://content.naic.org/sites/default/files/2025-annual-health-industry-commentary.pdf) (accessed 2026-07-22): Reports 1,156 health-statement filers, 0.4% net margin, 90.3% loss ratio, 10.3% administrative-expense ratio, medical-cost and premium changes, enrollment trends, and product-level economics for 2025.
- **S5** — [Medical Loss Ratio](https://www.cms.gov/marketplace/private-health-insurance/medical-loss-ratio) (accessed 2026-07-22): States that the Affordable Care Act generally requires issuers to spend at least 80% or 85% of premium on medical care and quality improvement and rebate enrollees when the applicable standard is missed.
- **S6** — [Health Insurance](https://content.naic.org/consumer/health-insurance.htm) (accessed 2026-07-22): Describes recurring premiums, insurer payment of covered provider services, individual and employer markets, public programs, renewal, private Medicare plans, networks, self-insured employer alternatives, and regulatory oversight.
- **S7** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Reports that 22% of employer-business owners planned to sell or transfer ownership within five years and documents the intent-based survey population.
