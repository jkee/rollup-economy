# 813212 — Voluntary Health Organizations

*v5.1 Stage 1 research memo. Run `813212-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** LOW_PRIORITY · A 5.54 · L 1.22 · interval STRUCTURAL_OUT → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Fundraising, communications, reporting, research support, and administration create a broad AI-assistable workflow base.
**Weakness:** Charitable governance and the lack of equity ownership make eligible firms and qualifying control transfers unusually scarce.

## Business-model lens
- Included: United States lower-middle-market voluntary health organizations that repeatedly raise and administer external funding for disease-related research, prevention, health education, patient support, navigation, or related charitable health programs.
- Excluded: Shells, captive internal programs, organizations outside voluntary health, pure financing vehicles without transferable operations, inactive charities, and organizations whose programs, donor relationships, governance, or key-person identity cannot continue through a change of control.
- Customer and revenue model: Revenue commonly comes from recurring individual gifts, foundation and corporate grants, sponsorships, events, bequests, and government or institutional awards. Donors and grantors fund services delivered to patients, researchers, caregivers, or the public, so the economic customer and beneficiary are often different parties.
- Deviation from default lens: none

## Executive view
Voluntary health organizations contain substantial fundraising, communications, reporting, research, and administrative work that AI can assist, but the screened population only partly fits a conventional outsourced-service model and offers very few qualifying control transfers.

## How AI changes the work
The clearest uses are prospect research, donor segmentation, appeal and grant drafting, constituent-service support, literature synthesis, document extraction, campaign analysis, program reporting, and knowledge retrieval. Patient interaction, scientific review, sensitive communications, partnership management, and governance remain human-accountable.

## Value capture
Fixed awards and unrestricted donations can convert efficiency into added mission capacity or resilience. Restricted funds, donor scrutiny, competitive fundraising, software and assurance costs, and expectations for more program output limit the share retained by the operator.

## Firm availability
Some scaled organizations have durable brands, donor files, staff, systems, programs, and institutional relationships. Eligibility and transferability are reduced by charitable-asset restrictions, affiliate control, board governance, key-person identity, donor concentration, and the absence of conventional equity ownership.

## Demand durability
Health research, education, prevention, and patient support remain socially necessary, and recent real giving to health has grown. Funding is volatile, however, and some information, navigation, and fundraising activity can be absorbed by health systems or digital platforms.

## Risks and uncertainty
Key risks are poor fit to an outsourced-customer lens, nonprofit scale-band measurement, rare control combinations, privacy and health misinformation, donor and grant concentration, restricted funds, federal funding shifts, affiliate rights, cyber risk, and loss of trust from low-quality automation.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1275 | — | OBSERVED | — |
| n | — | 566 | — | ESTIMATE | — |
| a | 0.33 | 0.49 | 0.64 | PROXY | S2, S3 |
| rho | 0.3 | 0.49 | 0.67 | PROXY | S4 |
| e | 0.12 | 0.28 | 0.46 | ESTIMATE | S1, S7 |
| s5 | 0.004 | 0.015 | 0.04 | PROXY | S6, S7 |
| q | 0.42 | 0.62 | 0.78 | ESTIMATE | S4, S5, S7 |
| d5 | 0.9 | 1.07 | 1.24 | PROXY | S5 |
| o | 0.7 | 0.84 | 0.93 | ESTIMATE | S3, S4, S7 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.50 | 1.22 | 2.19 | PROXY |
| F | 0.39 | 1.96 | 3.92 | ESTIMATE |
| C | 8.40 | 10.00 | 10.00 | ESTIMATE |
| D | 6.30 | 8.99 | 10.00 | ESTIMATE |

## Caveats
- a: No six-digit wage-weighted task study was found.
- a: The four-digit occupation mix combines voluntary health organizations with other grantmaking and giving services.
- a: AI assistance in communication and analysis is not equivalent to substituting relationship, health, scientific, or governance work.
- rho: The survey is not specific to voluntary health organizations or the LMM band.
- rho: Reported AI use does not measure the fraction of exposed labor actually substituted.
- rho: Health-related privacy, trust, and accuracy requirements may make implementation slower than in general fundraising work.
- e: No direct audit of the frozen margin-bridged LMM population was found.
- e: The dataset's commercial-services EBITDA margin is an awkward bridge for nonprofit operating economics and may misclassify the relevant scale band.
- e: Donors and beneficiaries are often different parties, so recurring charitable activity does not always satisfy an outsourced-customer relationship.
- e: Affiliation, restricted assets, governance rights, and key-person dependence are not visible in the industry definition.
- s5: The merger evidence is old, cross-sector, and limited to four states.
- s5: The cited rate excludes some asset and contract transfers and does not isolate durable control changes.
- s5: Nonprofit combinations do not create a conventional seller liquidity event, and charitable assets remain dedicated to exempt purposes.
- q: No direct evidence measures post-AI benefit retention in voluntary health organizations.
- q: Retained benefit is mission capacity or financial resilience, not distributable profit.
- q: Restricted funding and donor expectations vary widely across research, education, advocacy, and patient-service programs.
- d5: Giving by recipient category is broader than NAICS 813212 and is not a constant-quality service-volume index.
- d5: Two favorable annual observations do not establish a five-year trend.
- d5: Large gifts and financial-market conditions can move funding without a matching change in service demand.
- o: No direct substitution study isolates NAICS 813212.
- o: The operator-required share varies between research funding, public education, advocacy, and direct patient support.
- o: Some basic information and donor-service activity may migrate to health systems, platforms, or self-service tools.

## Sources
- **S1** — [2022 NAICS Definition: 813212 Voluntary Health Organizations](https://www.census.gov/naics/?details=813&input=813&year=2022) (accessed 2026-07-22): Official definition covering fundraising for health-related research, disease prevention, health education, and patient services.
- **S2** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 813200 Grantmaking and Giving Services](https://www.bls.gov/oes/2023/may/naics4_813200.htm) (accessed 2026-07-22): Broader-industry occupation employment and wage mix, including management, fundraising and business operations, administrative support, communications, and community-service work.
- **S3** — [Occupational Outlook Handbook: Fundraisers](https://www.bls.gov/ooh/business-and-financial/fundraisers.htm) (accessed 2026-07-22): Fundraiser duties including donor research, appeals, online giving, campaigns, donor records, evaluation, volunteer training, reporting compliance, and relationship work.
- **S4** — [AI With Purpose: How Foundations and Nonprofits Are Thinking About and Using Artificial Intelligence](https://cep.org/report-backpacks/ai-with-purpose-how-foundations-and-nonprofits-are-thinking-about-and-using-artificial-intelligence/?finding=1) (accessed 2026-07-22): Nonprofit and foundation AI use, predominant internal-productivity and communications uses, limited staff understanding, and concerns about security, accuracy, expertise, and bias.
- **S5** — [Giving USA: Charitable Giving Rose to $617.20 Billion in 2025](https://givingusa.org/giving-usa-charitable-giving-rose-to-617-20-billion-in-2025-surpassing-the-600-billion-mark-for-the-first-time/) (accessed 2026-07-22): Current and inflation-adjusted 2025 giving by source and recipient category, including real growth in health giving and broader funding volatility.
- **S6** — [Nonprofit Mergers and Acquisitions: More Than a Tool for Tough Times](https://www.bridgespan.org/insights/nonprofit-mergers-and-acquisitions-more-than-a-too) (accessed 2026-07-22): Cross-sector nonprofit merger filing study, its 1.5 percent cumulative rate over 11 years, population limits, and omitted transaction forms.
- **S7** — [IRS Organizational Test: Internal Revenue Code Section 501(c)(3)](https://www.irs.gov/charities-non-profits/charitable-organizations/organizational-test-internal-revenue-code-section-501c3) (accessed 2026-07-22): Charitable-purpose organizational requirements and permanent dedication of assets to exempt or public purposes upon dissolution.
