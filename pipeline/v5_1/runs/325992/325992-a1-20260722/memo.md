# 325992 — Photographic Film, Paper, Plate, Chemical, and Copy Toner Manufacturing

*v5.1 Stage 1 research memo. Run `325992-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 5.35 · L 0.54 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Repeat physical consumables and specialty coating or chemical know-how keep accountable operators necessary while AI improves supporting workflows.
**Weakness:** Legacy print and toner volume decline and a very small, heterogeneous firm universe can overwhelm incremental operating gains.

## Business-model lens
- Included: US manufacturers in the LMM band that repeatedly supply photographic or motion-picture film, sensitized paper or plates, photographic chemicals, copy toner, toner cartridges, or closely related contract coating and processing to external customers.
- Excluded: Captive production, shell entities, pure software or IP licensing, equipment-only businesses without repeat consumables or processing revenue, and non-control financing vehicles.
- Customer and revenue model: Recurring or repeat B2B sale of physical consumables and contract manufacturing or processing; some plate and consumables relationships are contract-based, while other volumes follow customers' print, imaging, and film usage.
- Deviation from default lens: none

## Executive view
This is a heterogeneous physical-consumables industry: legacy print and toner volumes are pressured, but repeat film, chemical, plate, cartridge, and contract-coating work remains operator-intensive. AI is more likely to improve planning, documentation, quality inspection, maintenance, and customer workflows than to remove core coating and chemical production labor.

## How AI changes the work
The largest near-term opportunities are scheduling and inventory decisions, specifications and batch-record review, sales and service support, predictive maintenance, machine-vision inspection, and anomaly detection. Chemical operations already have substantial automation, and application-specific data, capital, validation, and safety requirements slow conversion from technical exposure to implemented labor savings.

## Value capture
Proprietary formulations, installed bases, repeat consumables, and contract production can preserve savings, but powerful buyers, competitive bids, input-cost mechanisms, and recurring contract renewals will share part of the benefit. Savings that improve yield, uptime, or quality are more retainable than visible reductions in direct labor per unit.

## Firm availability
The injected population is only 24 estimated LMM-band firms. Many firms should have repeat external revenue, but equipment-only, captive, licensing-heavy, concentrated, or nonrecurring development businesses reduce eligibility. Cross-industry employer-owner evidence suggests a meaningful five-year transfer pool, but industry-specific completed-deal evidence is absent.

## Demand durability
Commercial print plates and electrophotographic toner face continuing digital substitution and volume decline. Motion-picture and specialty film, photographic chemicals, repeat installed-base consumables, and emerging contract coating or specialty-material applications can offset part of that decline, leaving a mixed and product-dependent outlook.

## Risks and uncertainty
The principal risks are accelerated print substitution, dependence on a few customers or installed platforms, raw-material volatility, environmental and product-quality obligations, legacy equipment, and a small eligible target universe. The evidence is dominated by broader-industry occupation data and a large public-company proxy rather than LMM 325992 observations.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1087 | — | OBSERVED | — |
| n | — | 24 | — | ESTIMATE | — |
| a | 0.14 | 0.24 | 0.36 | PROXY | S2, S3, S4 |
| rho | 0.35 | 0.52 | 0.68 | ESTIMATE | S4 |
| e | 0.48 | 0.65 | 0.79 | ESTIMATE | S1, S5 |
| s5 | 0.13 | 0.22 | 0.32 | PROXY | S6 |
| q | 0.42 | 0.6 | 0.75 | ESTIMATE | S5 |
| d5 | 0.76 | 0.91 | 1.08 | PROXY | S1, S5 |
| o | 0.85 | 0.93 | 0.98 | ESTIMATE | S1, S5 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.21 | 0.54 | 1.06 | ESTIMATE |
| F | 1.47 | 2.39 | 3.15 | ESTIMATE |
| C | 8.40 | 10.00 | 10.00 | ESTIMATE |
| D | 6.46 | 8.46 | 10.00 | ESTIMATE |

## Caveats
- a: The occupation distribution is NAICS 325 rather than 325992 and is not wage-weighted here.
- a: LLM exposure is not equivalent to labor substitution and does not identify tasks already automated.
- a: The code spans film, plates, chemicals, and toner, whose plant automation and technical labor differ.
- rho: The DOE evidence concerns chemical and thermal processing broadly, not photographic materials or toner specifically.
- rho: The range assumes modern tools can connect to enough plant and ERP data without a full equipment replacement cycle.
- e: No source measures eligibility among the injected LMM-firm population.
- e: Some qualifying revenue may be product sales rather than conventionally labeled outsourced services.
- e: The injected firm count is an estimate derived from size-class receipts and an industry margin bridge.
- s5: Gallup is cross-industry and includes firms far smaller than the LMM EBITDA band.
- s5: Surveyed intentions are not completed qualifying control transfers.
- s5: Internal family transfers and gifts may or may not meet the screen's control-transfer definition.
- q: Kodak is a large public-company proxy and may have bargaining power unlike LMM firms.
- q: Retention varies sharply between proprietary film or formulations, contract coating, commodity toner, and plates.
- q: The estimate excludes demand loss and implementation failure, which are represented elsewhere.
- d5: Public data do not isolate constant-quality quantities for each product within 325992.
- d5: Kodak's portfolio includes activities outside 325992 and company-specific restructuring.
- d5: The range is sensitive to the weight of declining commercial print versus resilient film and emerging specialty applications.
- o: The value is conditional on the demand remaining in d5; eliminated legacy demand is not counted twice.
- o: A few large customers may vertically integrate or switch to substitute technologies faster than assumed.

## Sources
- **S1** — [U.S. Census Bureau NAICS 325992 industry definition](https://www2.census.gov/econ2012/Reference_materials/htm%20files/32599n.htm) (accessed 2026-07-22): Defines 325992 as manufacturing sensitized film, paper, cloth and plates, toner and toner cartridges, and photographic chemicals.
- **S2** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 325 Chemical Manufacturing](https://www.bls.gov/oes/2023/may/naics3_325000.htm) (accessed 2026-07-22): Reports production occupations at 39.02% of chemical-manufacturing employment, including chemical-equipment operators at 12.28%, packaging and filling operators at 6.43%, and inspectors/testers at 3.33%.
- **S3** — [GPTs are GPTs: An Early Look at the Labor Market Impact Potential of Large Language Models](https://arxiv.org/abs/2303.10130) (accessed 2026-07-22): Finds about 15% of US worker tasks could be completed significantly faster with an LLM alone and 47%-56% with LLM-powered software, while explicitly not predicting adoption timing.
- **S4** — [DOE Advanced Manufacturing Office: Thermal Process Intensification Workshop Report](https://www.energy.gov/sites/default/files/2022-05/TPI%20Workshop%20Report_AMO.pdf) (accessed 2026-07-22): Documents AI and sensor opportunities in industrial process control and identifies chemical-manufacturing barriers including application-specific algorithms, complex data acquisition, capital intensity, testing, scale-up, disruption risk, and regulatory approval.
- **S5** — [Eastman Kodak Company 2024 Annual Report on Form 10-K](https://www.sec.gov/Archives/edgar/data/31235/000114036125013173/ny20046139x3_ars.pdf) (accessed 2026-07-22): Describes two-year recurring plate contracts, repeat ink and consumables, film and chemical lines, toner-based solutions, contract coating, print volume and pricing pressure, customer concentration, and physical production and quality obligations.
- **S6** — [Gallup: Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Reports 52.3% of US employer businesses are owned by people age 55 or older; 22% of employer owners planned a sale or transfer within five years, rising to 30% among employer owners age 55 or older.
