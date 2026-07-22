# 313320 — Fabric Coating Mills

*v5.1 Stage 1 research memo. Run `313320-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 5.89 · L 1.00 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Qualified repeat coating programs can retain value from better inspection, process knowledge, uptime, traceability, and overhead automation.
**Weakness:** Legacy chemical and environmental liabilities can make an otherwise attractive operating business difficult or impossible to transfer.

## Business-model lens
- Included: US lower-middle-market mills repeatedly coating, laminating, varnishing, waxing, or rubberizing textile fabrics or apparel for external B2B customers under toll-coating, approved-supplier, or recurring production programs.
- Excluded: Captive coating lines inside integrated manufacturers, own-account commodity product operations without an outsourced-service relationship, textile dyeing and finishing mills, paper or non-textile coating, nonrecurring experimental work without repeat revenue, shells, and non-control financing vehicles.
- Customer and revenue model: Per-yard, per-roll, per-pound, per-lot, or program pricing for toll coating and conversion, plus product margins where mills purchase substrate or chemistry. Customers span industrial, automotive, defense, protective, outdoor, furnishings, and other technical-textile markets; approvals, performance specifications, recipes, and qualification histories support repeat orders but seldom subscription contracts.
- Deviation from default lens: The code includes both toll coaters serving external customers and own-account coated-fabric manufacturers. The lens is narrowed to repeat external-customer coating programs so that outsourced-service and product-manufacturing economics are not combined.

## Executive view
Fabric coating is a physical, specification-driven B2B process with credible AI opportunities in inspection, formulation search, process monitoring, planning, traceability, maintenance, quoting, and administration. Qualified technical programs can support repeat revenue and pricing durability, but the small firm population, weak broader output trend, capital intensity, and chemical or PFAS liabilities are material constraints.

## How AI changes the work
Machine vision and anomaly detection can improve surface inspection and process consistency; language and analytical tools can assist specifications, certificates, regulatory records, formulation knowledge, scheduling, maintenance, purchasing, and customer communication. Coating-line setup, materials, curing, sampling, maintenance, functional testing, and hazardous-process accountability remain operator-intensive.

## Value capture
Efficiency gains can remain with the operator because programs are usually quoted per yard, roll, or lot rather than on transparent labor hours. Qualification histories, recipes, performance testing, technical support, and domestic sourcing can protect retention. Commodity competition, open-book costing, and rebids will pass savings to customers over time.

## Firm availability
Repeat toll-coating programs and transferable technical know-how make many independent mills conceptually eligible. Actual supply is narrowed by own-account manufacturers, captive lines, customer concentration, owner dependence, specialized aging equipment, site and permit complexity, and environmental history. Broad owner succession evidence supports some turnover but not a dependable wave of clean acquisitions.

## Demand durability
The physical process remains operator-required, and coated textiles serve a wide set of technical end markets. Broader finishing-and-coating output has contracted, so commodity demand should not be assumed stable. Specialty industrial, protective, automotive, and defense programs provide resilience, while PFAS phaseouts may both eliminate legacy formulations and create reformulation work.

## Risks and uncertainty
The best public occupation and output data combine coating with finishing. Critical diligence includes toll versus own-account revenue, end-market mix, customer approvals and concentration, recipe ownership, equipment and site condition, existing vision and process controls, air and water permits, PFAS and other chemical use, historical releases, remediation exposure, and the cost and timing of customer requalification.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1794 | — | OBSERVED | — |
| n | — | 55 | — | ESTIMATE | — |
| a | 0.18 | 0.29 | 0.41 | PROXY | S2, S3, S4 |
| rho | 0.3 | 0.48 | 0.67 | PROXY | S3, S4, S5 |
| e | 0.58 | 0.75 | 0.88 | ESTIMATE | S1, S5 |
| s5 | 0.09 | 0.18 | 0.29 | PROXY | S5, S6 |
| q | 0.4 | 0.6 | 0.76 | ESTIMATE | S7, S8 |
| d5 | 0.76 | 0.93 | 1.11 | PROXY | S7, S8, S9 |
| o | 0.93 | 0.98 | 0.995 | ESTIMATE | S1, S5, S9 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.39 | 1.00 | 1.97 | PROXY |
| F | 2.18 | 3.43 | 4.36 | ESTIMATE |
| C | 8.00 | 10.00 | 10.00 | ESTIMATE |
| D | 7.07 | 9.11 | 10.00 | ESTIMATE |

## Caveats
- a: OEWS combines NAICS 313310 and 313320 and therefore is not a six-digit occupation mix.
- a: The inspection system source is demonstrated on woven-fabric production rather than coated fabric and does not measure labor savings.
- a: Exposure denotes substitutable tasks or avoided hiring, not whole-job removal.
- rho: The MLC sample is broad manufacturing and may skew toward digitally mature or larger respondents.
- rho: Vision systems include conventional automation as well as AI and may not be deployed on coating lines.
- rho: Customer and environmental validation can prevent technically feasible process changes from being implemented.
- e: No public dataset measures lens eligibility for NAICS 313320 in the specified EBITDA band.
- e: The provided LMM firm count is an estimate and may include facilities whose margins are temporarily in range.
- e: Environmental liabilities can impair transferability independently of operating performance.
- s5: The succession evidence covers employer businesses across industries and sizes.
- s5: Stated plans may not be completed and can include transfers that do not convey control.
- s5: Undiscovered environmental liabilities can turn a planned transfer into a closure or asset sale.
- q: No public evidence measures five-year retained AI benefit for fabric coaters.
- q: Defense and specialty programs may retain materially more than commodity coated fabrics.
- q: The estimate excludes demand loss and implementation failure to avoid double counting.
- d5: The industrial-production series combines finishing and coating.
- d5: Specialty and defense growth may not benefit the current customer baskets of all screened firms.
- d5: Chemical restrictions can destroy legacy product demand even while creating demand for reformulated coatings.
- o: This estimate is conditional on year-five demand and does not reapply the d5 decline.
- o: Some formulation, inspection, and documentation tasks can move to customers even though physical coating cannot.
- o: A chemistry ban can eliminate a current coating specification rather than merely change its operator.

## Sources
- **S1** — [2022 NAICS Definition: 313320 Fabric Coating Mills](https://www.census.gov/naics/?details=313320&input=313320&year=2022) (accessed 2026-07-23): Defines the industry as establishments primarily engaged in coating, laminating, varnishing, waxing, and rubberizing textiles and apparel.
- **S2** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: Textile and Fabric Finishing and Fabric Coating Mills](https://www.bls.gov/oes/2023/may/naics4_313300.htm) (accessed 2026-07-23): Reports the broader group's occupation mix, including office support at 12.81%, sales at 4.11%, production at 56.59%, inspectors at 5.14%, and coating-machine operators at 6.16%.
- **S3** — [WiseEye: AI-based Textile Material Inspection System](https://www.polyu.edu.hk/kteo/knowledge-transfer/innovations-and-technologies/technology-search/5-textile-and-fashion/5_itc_39_0319/?sc_lang=en) (accessed 2026-07-23): Describes real-time AI machine-vision inspection across fabric width, detecting around 40 defect types at a reported detection rate above 90%.
- **S4** — [Shaping the AI-Powered Factory of the Future: Survey Report](https://manufacturingleadershipcouncil.com/wp-content/uploads/2025/05/Shaping-the-AI-Powered-Factory-of-the-Future-Report.pdf) (accessed 2026-07-23): Reports broad manufacturer use of vision systems and machine learning, increased investment intent, but only 18% with a formal operations AI strategy and major data, skills, ROI, trust, and legacy-system barriers.
- **S5** — [Multi-Industry PFAS Study: 2021 Preliminary Report](https://www.epa.gov/system/files/documents/2021-09/multi-industry-pfas-study_preliminary-2021-report_508_2021.09.08.pdf) (accessed 2026-07-23): Documents fabric coating and laminating within regulated textile-mill processes, PFAS use to impart performance properties, coating application routes, sparse monitoring, and observed PFAS in some textile-mill wastewater discharges.
- **S6** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-23): Reports that 52.3% of US employer businesses are owned by people age 55 or older and that 22% of employer-business owners planned to sell or transfer ownership within five years; provides survey methods.
- **S7** — [Industrial Production: Textile and Fabric Finishing and Fabric Coating Mills (NAICS 3133)](https://fred.stlouisfed.org/series/IPG3133A) (accessed 2026-07-23): Federal Reserve real-output index for the broader group: 66.3922 in 2022, 61.8800 in 2024, and 60.3558 in 2025.
- **S8** — [SelectUSA Textiles Industry](https://www.trade.gov/selectusa-textiles-industry) (accessed 2026-07-23): Describes growth and broad applications in specialty and industrial fabrics, including automotive, protective, filtration, insulation, hoses, tires, and composites, and reports textile-mill shipments of $25.3 billion in 2023.
- **S9** — [Berry Amendment Implementation](https://www.trade.gov/berry-amendment-implementation) (accessed 2026-07-23): States Defense Department domestic-source restrictions covering synthetic fabric and coated synthetic fabric, as well as tents, tarpaulins, covers, canvas products, and specified clothing materials.
