# 321911 — Wood Window and Door Manufacturing

*v5.1 Stage 1 research memo. Run `321911-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** LOW_PRIORITY · A 5.97 · L 1.23 · interval STRUCTURAL_OUT → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** AI-enabled configuration, inspection, scheduling, and warranty reduction in repeat custom-production relationships.
**Weakness:** The NAICS code is fundamentally product manufacturing, so only a minority of firms plausibly fit the recurring outsourced-service lens.

## Business-model lens
- Included: US lower-middle-market wood window and door manufacturers that repeatedly provide outsourced custom fabrication, configuration, prehanging, finishing, or specification-controlled production to builders, dealers, distributors, or other external customers.
- Excluded: Standard commodity product sales without an outsourced-service relationship, on-site finish carpentry, installers that do not manufacture, captive plants, distributors, software vendors, and non-control financing vehicles.
- Customer and revenue model: Eligible firms receive repeat B2B orders and earn revenue through customer-specific fabrication and production services bundled into the price of physical window and door units; standard catalog manufacturing remains product revenue and is outside the lens.
- Deviation from default lens: none

## Executive view
Wood window and door manufacturing has a larger labor intensity than many wood-product categories and several tangible AI use cases in inspection, configuration, estimating, scheduling, and warranty handling. The opportunity is constrained by physical fabrication and a service-lens mismatch: only firms whose made-to-order work genuinely functions as recurring outsourced production qualify, not the full manufacturing code.

## How AI changes the work
AI can check frame, sash, glazing, seal, hardware, and finish defects; validate configurations; speed estimating; optimize schedules and cut lists; predict maintenance; and automate documents and warranty triage. Cutting, assembly, glazing, finishing, packing, and material movement still require equipment and people, so most gains are augmentation or hiring avoidance rather than pure software substitution.

## Value capture
Custom engineering, reliable lead times, fewer defects, and lower warranty cost are relatively defensible. Direct labor savings on standardized units are easier for builders and dealers to extract through bids and program renewals. Operators retain more when AI improves hidden yield and service quality than when it simply lowers a disclosed cost line.

## Firm availability
The supplied LMM estimate of 234 firms suggests a broader target universe than many adjacent codes, but only a minority likely meets the outsourced-service lens. General small-business succession evidence supports some five-year transfer flow; a named-firm eligibility and ownership screen is still required because neither service mix nor transfer propensity is observed at six digits.

## Demand durability
New construction and remodeling drive demand. Both were soft entering 2026, and housing affordability creates near-term risk, but replacement of aging windows and doors and eventual construction normalization support a roughly stable five-year base. The physical, code-sensitive product continues to require an accountable manufacturer even as sales and production become more digital.

## Risks and uncertainty
The largest uncertainties are the share of firms truly providing outsourced custom fabrication, housing-cycle timing, material substitution, price competition, SKU complexity, and implementation evidence from smaller plants. The thesis weakens materially if eligible revenue is mostly standard product sales, if builder customers reprice all savings, or if data and controls fragmentation prevents reliable deployment.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.2145 | — | OBSERVED | — |
| n | — | 234 | — | ESTIMATE | — |
| a | 0.22 | 0.34 | 0.46 | PROXY | S2, S3, S4 |
| rho | 0.24 | 0.42 | 0.6 | ESTIMATE | S4, S5, S6 |
| e | 0.1 | 0.22 | 0.38 | ESTIMATE | S1, S7 |
| s5 | 0.09 | 0.15 | 0.23 | PROXY | S8 |
| q | 0.28 | 0.47 | 0.65 | ESTIMATE | S7 |
| d5 | 0.86 | 1.03 | 1.18 | PROXY | S7, S9, S10 |
| o | 0.88 | 0.95 | 0.99 | ESTIMATE | S1, S4, S7 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.45 | 1.23 | 2.37 | ESTIMATE |
| F | 1.82 | 3.48 | 4.93 | ESTIMATE |
| C | 5.60 | 9.40 | 10.00 | ESTIMATE |
| D | 7.57 | 9.79 | 10.00 | ESTIMATE |

## Caveats
- a: No six-digit wage-by-task study was found.
- a: Vendor-described capability is not measured labor displacement.
- a: The supplied compensation ratio uses 2024 wages over 2022 receipts and is harmonized to an IPS basis.
- rho: The only window-and-door-specific implementation evidence found is vendor-authored.
- rho: Census AI adoption data cover all nonfarm businesses, not this industry.
- rho: Custom products and frequent changeovers reduce the reliability of fixed automation assumptions.
- e: NAICS does not separate custom service-like fabrication from standard product manufacture.
- e: Repeat product orders do not automatically qualify as an outsourced service.
- e: The supplied LMM firm count is a margin-bridged estimate based on 2022 receipts and a January 2026 sector margin.
- s5: Intent is not completion.
- s5: Gallup covers all industries and small-business sizes.
- s5: Its transfer category includes gifts and rare IPOs that may not qualify.
- q: No direct five-year AI-benefit retention study exists for this industry.
- q: Owens Corning is much larger than the target firms.
- q: Capture differs materially between custom architectural products and standardized production-builder units.
- d5: Current housing data are a point in a volatile cycle.
- d5: LIRA is nominal, one-year, and not specific to windows and doors.
- d5: Public-company door commentary also includes non-wood products and markets outside the US.
- o: Insourcing and product substitution can overlap with demand change rather than operator replacement.
- o: Custom architectural windows require more accountability than standardized components.
- o: No direct customer survey measures future self-service in this category.

## Sources
- **S1** — [NAICS Code Description: 321911 Wood Window and Door Manufacturing](https://www.naics.com/naics-code-description/?code=321911&v=2022) (accessed 2026-07-22): Defines the industry as manufacturing wood or wood-clad windows, doors, frames, sash, and units, while excluding on-site fabrication.
- **S2** — [Data tables for OEWS industry charts, May 2024](https://www.bls.gov/oes/2024/may/ind_emp_chart/ind_emp_chart_data.htm) (accessed 2026-07-22): Shows the largest occupations in other wood product manufacturing are assemblers, woodworking and sawing machine operators, material movers, truck operators, supervisors, carpenters, drivers, sales representatives, and managers.
- **S3** — [O*NET: Helpers--Production Workers](https://www.onetonline.org/link/summary/51-9198.00) (accessed 2026-07-22): Documents loading, machine operation, placement, inspection, monitoring, packing, recording, and material-movement tasks in production work.
- **S4** — [AI Defect Detection for Windows and Doors](https://enaovision.com/industries/windows-and-doors) (accessed 2026-07-22): Describes AI camera inspection of frames, sash, doors, glazing, seals, finishes, and hardware across cutting, welding, glazing, and packing stations.
- **S5** — [Only 3.8% of Businesses Use AI to Produce Goods and Services](https://www.census.gov/library/stories/2023/11/businesses-use-ai.html) (accessed 2026-07-22): Reports 3.8% current US business AI use and 6.5% planned use within six months in late 2023, indicating a low starting base.
- **S6** — [BLS Table 1: Incidence rates of nonfatal occupational injuries and illnesses by industry, 2024](https://www.bls.gov/web/osh/table-1-industry-rates-national.htm) (accessed 2026-07-22): Reports a total recordable injury and illness rate of 3.3 cases per 100 full-time workers for NAICS 321911 in 2024.
- **S7** — [Owens Corning 2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/1370946/000137094626000067/oc-20251231.htm) (accessed 2026-07-22): States door demand is driven by residential construction and economic conditions; identifies service, quality, innovation, price, and customization as competitive methods; and describes near-term construction and remodeling weakness.
- **S8** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Reports 14% of working small-business owners planned a sale, IPO, or transfer within five years, rising to 17% among owners age 55 or older.
- **S9** — [Monthly New Residential Construction, May 2026](https://www.census.gov/construction/nrc/current/) (accessed 2026-07-22): Reports May 2026 housing starts at a 1.177 million annual rate, 8.7% below May 2025, and permits at 1.413 million.
- **S10** — [Leading Indicator of Remodeling Activity](https://www.jchs.harvard.edu/research-areas/remodeling/lira) (accessed 2026-07-22): Projects owner-occupied improvement and maintenance spending growth to slow sharply in early 2027 and explains that the measure is nominal and has a four-quarter horizon.
