# 541350 — Building Inspection Services

*v5 Stage 1 research memo. Run `541350-a1-20260722`, model `gpt-5.6-terra`, 2026-07-22, attempt 1.*

**Base tier:** CONDITIONAL · A 6.09 · L 2.69 · interval LOW_PRIORITY → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Report and workflow automation can improve productive capacity while physical inspection and accountable judgment remain required.
**Weakness:** Transferability and recurring revenue are not measured in public NAICS data and may be weak for principal-dependent, transaction-driven firms.

## Business-model lens
- Included: Independent, external-customer building and home inspection providers in the lower-middle-market band that earn repeat or recurring outsourced work, including repeat work generated through real-estate, property-owner, insurer, or construction relationships.
- Excluded: Government code-enforcement units, captive inspection departments, pest and hazardous-material inspections classified elsewhere, one-person practices without transferable operations, and businesses outside the lower-middle-market band.
- Customer and revenue model: Typically a client-specific inspection engagement documented in a report; repeat demand may come from referral networks, property portfolios, construction milestones, or recurring customer relationships. Fees and scope are set in a pre-inspection agreement.
- Deviation from default lens: none

## Executive view
Building Inspection Services is a field-intensive professional service with useful AI assistance around documents and workflow, but not a clear path to replacing the accountable inspection. The central commercial question is whether firms have transferable referral relationships and staff beyond the principal inspector. [S1][S2]

## How AI changes the work
AI can assist plan review, report drafting, image and log organization, intake, scheduling, and customer communication. BLS describes inspectors as spending most time at worksites while also reviewing blueprints, writing reports, and scheduling; it also describes physical examination and testing tasks, which limits substitution. [S2][S3]

## Value capture
Home-inspection agreements address scope, fee, payment timing, report ownership, and liability, consistent with per-engagement pricing rather than an automatic cost-plus pass-through. Savings can be retained initially, but competitive local markets may later return some benefit to customers through price or added service. [S5]

## Firm availability
The NAICS definition covers external building and home inspection services and excludes code-enforcement activity classified elsewhere. Within the supplied lower-middle-market count, eligibility and transfer likelihood remain uncertain because public statistics do not identify customer concentration, staff depth, normalized EBITDA, or ownership succession. [S1]

## Demand durability
BLS projects total construction and building inspector employment to decline 1 percent from 2024 to 2034, citing remote inspections as a reducing force while safety and construction quality support demand. That evidence supports a near-flat, uncertain demand outlook rather than a strong secular growth claim. [S2]

## Risks and uncertainty
The occupation proxy contains government and construction roles outside private NAICS 541350, and the industry has no observed task-time, ownership-transfer, or AI-retention series in the reviewed sources. Licensing, professional standards, liability, local housing cycles, and referral concentration could materially alter the result. [S2][S4][S5]

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.4974 | — | OBSERVED | — |
| n | — | 40 | — | ESTIMATE | — |
| a | 0.2 | 0.32 | 0.45 | PROXY | S2, S3, S4 |
| rho | 0.35 | 0.52 | 0.68 | ESTIMATE | S2, S4 |
| e | 0.45 | 0.6 | 0.75 | ESTIMATE | S1, S2 |
| s5 | 0.1 | 0.18 | 0.28 | ESTIMATE | S2 |
| q | 0.45 | 0.6 | 0.75 | PROXY | S5 |
| d5 | 0.9 | 0.995 | 1.08 | PROXY | S2 |
| o | 0.74 | 0.84 | 0.92 | ESTIMATE | S2, S4 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 1.39 | 3.31 | 6.09 | ESTIMATE |
| F | 1.66 | 2.69 | 3.60 | ESTIMATE |
| C | 9.00 | 10.00 | 10.00 | PROXY |
| D | 6.66 | 8.36 | 9.94 | ESTIMATE |

## Caveats
- a: The occupational proxy includes government and construction roles outside this NAICS industry.
- a: No NAICS-specific task-time or wage-by-task dataset was located.
- rho: This is a five-year judgment rather than a measured adoption rate.
- rho: State and locality rules vary, and the source evidence does not measure AI deployment.
- e: NAICS establishment definitions do not identify recurring revenue, normalized EBITDA, or transferability.
- e: The supplied firm-count estimate is not re-estimated here.
- s5: No NAICS-specific longitudinal ownership-transfer series was obtained.
- s5: Occupational self-employment statistics are not a measure of control transfers for lower-middle-market firms.
- q: The agreement is a member resource and is not representative pricing evidence.
- q: The figure concerns retained implemented benefit, not revenue growth or demand effects.
- d5: Occupational employment is an imperfect proxy for paid service quantity.
- d5: The source includes large public-sector and construction-employer populations outside the lens.
- o: This is a judgment about future accountability, not a measured software displacement rate.
- o: Remote-inspection growth may vary sharply by property type and jurisdiction.

## Sources
- **S1** — [U.S. Census Bureau NAICS definition: 541350 Building Inspection Services](https://www.census.gov/naics/?details=541350&input=541350&year=2017) (accessed 2026-07-22): Industry scope: building or home inspection services for property-condition reports, and exclusions for pest, hazardous-material, and code-enforcement activities.
- **S2** — [BLS Occupational Outlook Handbook: Construction and Building Inspectors](https://www.bls.gov/ooh/construction-and-extraction/construction-and-building-inspectors.htm) (accessed 2026-07-22): Duties, worksite versus office work, credential requirements, employment mix, and the 2024-2034 national employment projection.
- **S3** — [O*NET OnLine: Construction and Building Inspectors (47-4011.00)](https://www.onetonline.org/link/details/47-4011.00) (accessed 2026-07-22): Occupation task and knowledge profile used as the AI-exposure proxy.
- **S4** — [InterNACHI Home Inspection Standards of Practice](https://www.nachi.org/sop.htm) (accessed 2026-07-22): A home inspection is a fee-paid, non-invasive visual examination with a written report on observed material defects.
- **S5** — [InterNACHI Home Inspection Contracts for Member Use](https://www.nachi.org/newagreement.htm) (accessed 2026-07-22): Standard agreement topics include inspection scope, fee, payment due date, report ownership, and liability provisions.
