# 316110 — Leather and Hide Tanning and Finishing

*v5.1 Stage 1 research memo. Run `316110-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 5.22 · L 0.73 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Durable need for a compliant physical processor supporting repeat specialty B2B workflows.
**Weakness:** The eligible contract-processing population is unmeasured and probably small within a structurally pressured domestic industry.

## Business-model lens
- Included: Independent US contract tanneries and leather finishers that repeatedly process customer-owned hides, skins, wet-blue stock, or leather to customer specifications for business customers.
- Excluded: Tanneries selling only their own finished leather, converters that merely own and arrange processing, captive processing units, fur dressing that is not repeat outsourced work, shells, and non-control financing vehicles.
- Customer and revenue model: Recurring or repeat B2B processing revenue, generally quoted by hide, skin, lot, area, or specified finishing job, with the customer retaining ownership of the input material.
- Deviation from default lens: The NAICS industry combines product manufacturers, converters, and contract processors. The lens is narrowed to contract tanning and finishing because only that model supplies the recurring outsourced service specified by the fixed screen.

## Executive view
The relevant opportunity is a narrow subset of a small, specialized manufacturing industry: contract tanneries and finishers processing customer-owned material. Physical production and environmental accountability make the operator durable, but they also cap direct AI labor substitution and raise integration risk.

## How AI changes the work
AI is most useful around the plant: translating customer specifications into job tickets, quoting, scheduling, matching recipes and colors, drafting compliance records, assisting visual quality inspection, and handling customer communication. The core wet and dry processing steps remain equipment- and labor-mediated, so avoided hiring is more plausible than broad labor replacement.

## Value capture
Per-hide, per-lot, or job-based pricing lets a processor retain savings until a bid or renewal resets economics. Specialty quality, short runs, and compliance can protect margin, while concentrated buyers, transparent conversion pricing, and offshore alternatives accelerate sharing.

## Firm availability
Eligibility is the central gating issue because NAICS 316110 includes regular product-selling tanneries and converters as well as contract processors. General employer-owner evidence suggests meaningful five-year transfer intent, but the eligible pool implied by the frozen 26-firm estimate may contain only a handful of firms.

## Demand durability
Domestic demand faces synthetics, imports, environmental burdens, and a long history of facility decline. The remaining specialty work may be defensible, and almost all surviving tanning or finishing demand still needs an accountable physical operator, but a modest real-volume decline is the base case.

## Risks and uncertainty
The largest uncertainties are the current share of LMM firms that truly process customer-owned material, contract-level pricing power, end-market concentration, environmental liabilities, and whether plant data are sufficient for machine vision and workflow automation. A single large customer loss or remediation obligation can overwhelm modest labor savings.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.2204 | — | OBSERVED | — |
| n | — | 26 | — | ESTIMATE | — |
| a | 0.08 | 0.15 | 0.24 | PROXY | S2, S3 |
| rho | 0.35 | 0.55 | 0.72 | ESTIMATE | S3 |
| e | 0.12 | 0.25 | 0.42 | ESTIMATE | S1, S6 |
| s5 | 0.14 | 0.22 | 0.31 | PROXY | S5 |
| q | 0.3 | 0.5 | 0.7 | ESTIMATE | S6 |
| d5 | 0.72 | 0.9 | 1.08 | PROXY | S3, S4 |
| o | 0.91 | 0.97 | 1 | ESTIMATE | S3, S6 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.25 | 0.73 | 1.52 | ESTIMATE |
| F | 0.58 | 1.43 | 2.38 | ESTIMATE |
| C | 6.00 | 10.00 | 10.00 | ESTIMATE |
| D | 6.55 | 8.73 | 10.00 | ESTIMATE |

## Caveats
- a: BLS publishes this occupation chart for the full industry, not the narrowed contract-processing lens.
- a: The top-ten occupation chart does not provide a complete wage-weighted task distribution.
- a: Visual defect detection is technically plausible but plant-specific image data, lighting, and handling integration can dominate feasibility.
- rho: No current industry adoption survey was found.
- rho: Small plants may lack MES/ERP data and staff needed to maintain integrations.
- rho: Environmental and customer-quality accountability slows implementation even when a model works in a trial.
- e: The NAICS definition includes converters that outsource their own material; those firms do not necessarily supply an external service.
- e: EPA's structural evidence is old and may not describe the much smaller current industry.
- e: Mixed-model firms may have both proprietary leather sales and contract-processing revenue.
- s5: Survey intentions are not completed transactions.
- s5: The survey spans all employer industries and business sizes.
- s5: Very small eligible-firm counts make realized transfer rates volatile.
- q: No public contract-pricing dataset was found.
- q: Retention varies sharply between commodity wet processing and scarce specialty finishing.
- q: This estimate excludes demand loss and implementation friction, which belong in other primitives.
- d5: Sectoral output is nominal and covers product sellers as well as contract processors.
- d5: EPA's explanation of long-run decline is dated.
- d5: End markets differ: luxury, military, automotive, footwear, and industrial leather can move in different directions.
- o: The operator may consolidate across fewer, larger plants even if the service quantity remains.
- o: This is a judgment about the need for an accountable operator, not the number of workers required.
- o: Customers that vertically integrate finishing would reduce the eligible outsourced operator share.

## Sources
- **S1** — [2022 NAICS definition: Leather and Hide Tanning and Finishing](https://www.census.gov/naics/?details=316&input=316&year=2022) (accessed 2026-07-22): Defines NAICS 316110 as tanning, currying, and finishing hides and skins, having others process them on contract, and dyeing or dressing furs; supports the industry's mixed business models and lens narrowing.
- **S2** — [BLS OEWS Data Tables for Industry Employment Charts, May 2024](https://www.bls.gov/oes/2024/may/ind_emp_chart/ind_emp_chart_data.htm) (accessed 2026-07-22): Reports the ten largest occupations and employment counts in leather and hide tanning and finishing, including 690 shoe/leather workers, 210 production supervisors, 180 other textile/apparel workers, 150 dyeing-machine operators, and 150 material movers.
- **S3** — [EPA AP-42 Section 9.15: Leather Tanning](https://www3.epa.gov/ttn/chief/ap42/ch09/final/c9s15.pdf) (accessed 2026-07-22): Describes the many physical and chemical stages of tanning and finishing, reports that chrome tanning was about 90% of US production, and notes long-run facility decline associated with synthetic substitutes, imports, and environmental regulation.
- **S4** — [BLS via FRED: Sectoral Output for Leather and Hide Tanning and Finishing](https://fred.stlouisfed.org/series/IPUEN3161T300000000) (accessed 2026-07-22): Reports nominal annual sectoral output of $1,238.741 million in 2021, $1,189.322 million in 2022, $1,217.642 million in 2023, and $1,196.484 million in 2024, and defines the series.
- **S5** — [Gallup: Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Reports from a fall 2024 US survey that 22% of employer-business owners planned to sell or transfer ownership within five years, rising to 30% among employer owners age 55 or older; also reports 52.3% of employer businesses are owned by people 55 or older.
- **S6** — [EPA Assessment of Industrial Hazardous Waste Practices: Leather Tanning and Finishing Industry](https://nepis.epa.gov/Exe/ZyPURL.cgi?Dockey=9101U9X6.TXT) (accessed 2026-07-22): Distinguishes regular tanneries, converters, and contract tanneries; defines contract tanneries as processors of material owned by another party and states that contract leather finishers made up the largest segment of contract operations.
