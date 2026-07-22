# 811412 — Appliance Repair and Maintenance

*v5.1 Stage 1 research memo. Run `811412-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** LOW_PRIORITY · A 5.86 · L 1.31 · interval STRUCTURAL_OUT → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Structured service information and dispatch workflows offer an implementable AI layer around an enduring physical field service.
**Weakness:** Warranty-channel pricing, captive networks, mixed classifications, and repair-versus-replace economics can limit both firm eligibility and benefit retention.

## Business-model lens
- Included: Independent US firms repairing and servicing household appliances for external customers, including refrigerators, stoves, washing machines, clothes dryers, and room air conditioners. The screened population is limited to recurring or repeat outsourced-service firms in the lower-middle-market EBITDA band.
- Excluded: New-appliance retailers whose principal business includes repair as an ancillary service, manufacturer- or retailer-captive service units, central HVAC installation and service, commercial refrigeration repair, internal maintenance departments, shells, and non-control financing vehicles.
- Customer and revenue model: Customers include households, landlords, property managers, warranty administrators, manufacturers, and retailers. Revenue comes from diagnostic or trip charges, hourly or flat-rate labor, parts markups, service contracts, and warranty reimbursement.
- Deviation from default lens: none

## Executive view
Appliance repair combines durable physical field service with a larger information and coordination layer than many mechanical trades. AI can assist calls, work orders, scheduling, troubleshooting knowledge, billing, warranty administration, and customer communications, while an accountable operator remains necessary for most onsite repairs. The lower-middle-market pool is estimated rather than observed and captive or mixed business models reduce eligibility.

## How AI changes the work
AI can structure customer symptoms, interpret work orders and error codes, retrieve manual and parts information, draft technician guidance, schedule routes, prepare invoices, and automate follow-up. It cannot itself access an appliance, verify a physical fault, replace parts, handle refrigerant or electrical hazards, and test a completed repair.

## Value capture
Direct-pay diagnostic fees, flat-rate repairs, parts margins, improved first-time completion, and route density can preserve benefits. Warranty and retailer contracts, hourly billing, customer price comparison, and repricing can share savings externally.

## Firm availability
The frozen dataset indicates 18 estimated lower-middle-market firms. A substantial share may fit the lens, but manufacturer or retailer control, warranty economics, mixed HVAC or commercial work, subcontracting, and owner dependence require firm-level screening.

## Demand durability
BLS projects modest growth in home-appliance-repairer employment, used only as a proxy. The installed appliance and housing stock support continued need, while low-cost replacement, parts availability, product design, and remote or self-service diagnostics create downside.

## Risks and uncertainty
Key unknowns are the wage-weighted task mix, actual production AI penetration, warranty and contract pass-through, classification of captive service networks, firm eligibility, and constant-price service volumes. Product repairability and first-time-fix economics could move the outlook materially.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.4908 | — | OBSERVED | — |
| n | — | 18 | — | ESTIMATE | — |
| a | 0.12 | 0.21 | 0.32 | PROXY | S2, S3 |
| rho | 0.32 | 0.52 | 0.7 | PROXY | S4 |
| e | 0.52 | 0.7 | 0.83 | ESTIMATE | S1 |
| s5 | 0.04 | 0.1 | 0.18 | PROXY | S5 |
| q | 0.32 | 0.55 | 0.72 | ESTIMATE | — |
| d5 | 0.88 | 1.03 | 1.18 | PROXY | S6 |
| o | 0.9 | 0.97 | 1 | PROXY | S1, S2 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.75 | 2.14 | 4.40 | PROXY |
| F | 0.51 | 1.31 | 2.10 | ESTIMATE |
| C | 6.40 | 10.00 | 10.00 | ESTIMATE |
| D | 7.92 | 9.99 | 10.00 | PROXY |

## Caveats
- a: O*NET task importance is not a wage-weighted task share and does not isolate lower-middle-market operators.
- a: The BLS occupation chart is broader than NAICS 811412 and includes other repair specialties.
- rho: Census BTOS spans all industries and firm sizes and counts AI use in any business function.
- rho: The proxy does not measure the share of exposed wage work actually implemented or sustained.
- e: The injected count of 18 firms is an estimate from size-distribution and margin assumptions and is not re-estimated here.
- e: Industry classification may not cleanly separate appliance repair from mixed retail, HVAC, commercial refrigeration, or manufacturer service operations.
- s5: Gallup is cross-industry and measures planned rather than completed transfers.
- s5: No appliance-repair-specific owner demographics or completed-control-transfer series was found.
- q: No direct evidence was found on AI-enabled benefit retention in appliance repair.
- q: Warranty and retail-contract revenue may have materially different pass-through mechanics from direct-to-consumer work.
- d5: BLS reports an occupation across employers, not NAICS 811412 constant-quality service quantity.
- d5: The occupational projection does not isolate shifts between independent repair, captive networks, and self-service.
- o: The estimate concerns the current service basket rather than all future appliance-support models.
- o: O*NET task content does not directly measure customer substitution to self-service or product replacement.

## Sources
- **S1** — [North American Industry Classification System: Sector 81 Definitions](https://www.census.gov/naics/resources/archives/sect81.html) (accessed 2026-07-22): Defines 811412 as household-appliance repair and servicing without retailing new appliances and lists excluded HVAC, commercial refrigeration, and retail activities.
- **S2** — [O*NET OnLine: Home Appliance Repairers](https://www.onetonline.org/link/details/49-9031.00) (accessed 2026-07-22): Describes billing, customer and work-order intake, appliance examination, troubleshooting, and physical repair tasks.
- **S3** — [BLS OEWS Industry Charts: Personal and Household Goods Repair and Maintenance](https://www.bls.gov/oes/2024/may/ind_emp_chart/ind_emp_chart_data.htm) (accessed 2026-07-22): Reports May 2024 occupation counts in the broader repair industry, including appliance repairers, managers, and office clerks.
- **S4** — [US Census Bureau: Large Firms With at Least 20 Employees Biggest AI Users](https://www.census.gov/library/stories/2026/05/ai-use-businesses.html) (accessed 2026-07-22): Reports overall US business AI usage and expected near-term usage from December 2025 to May 2026 BTOS data.
- **S5** — [Gallup: Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Reports that 22 percent of employer-business owners planned to sell or transfer ownership within five years.
- **S6** — [BLS: Occupational Projections and Worker Characteristics](https://www.bls.gov/emp/tables/occupational-projections-and-characteristics.htm) (accessed 2026-07-22): Reports 2024 and projected 2034 employment, change, self-employment share, openings, and other characteristics for home appliance repairers.
