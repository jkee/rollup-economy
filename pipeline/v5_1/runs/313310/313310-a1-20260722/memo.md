# 313310 — Textile and Fabric Finishing Mills

*v5.1 Stage 1 research memo. Run `313310-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** LOW_PRIORITY · A 6.23 · L 1.65 · interval STRUCTURAL_OUT → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Repeat outsourced finishing programs contain measurable quality, rework, scheduling, documentation, and administrative workflows that AI can augment.
**Weakness:** Contracting domestic output and potentially severe environmental liabilities can overwhelm otherwise credible operating efficiencies.

## Business-model lens
- Included: US lower-middle-market firms repeatedly providing dyeing, bleaching, printing, washing, preshrinking, mercerizing, napping, scouring, cleaning, and other textile or fabric finishing to external B2B customers, including converters with durable repeat finishing programs.
- Excluded: Captive finishing inside integrated mills, converters whose economics are principally speculative wholesale inventory rather than repeat customer programs, fabric coating mills, apparel manufacturing, one-off project shops without repeat demand, shells, and non-control financing vehicles.
- Customer and revenue model: Mostly per-yard, per-pound, per-lot, per-garment, or program-based job finishing for fabric mills, apparel manufacturers, brands, and industrial-textile customers; converter revenue may include a wholesale spread on purchased grey fabric. Specifications, approved recipes, color matching, compliance, and turnaround create repeat relationships but limited contractual subscription revenue.
- Deviation from default lens: NAICS 313310 combines outsourced finishers with converters that buy grey goods, outsource finishing, and resell at wholesale. The lens is narrowed to repeat external-customer finishing programs so those distinct operating models are not treated as one service population.

## Executive view
Textile finishing is an externally supplied, repeat B2B process in much of the industry, which supports customer continuity and operating transferability. AI can improve color and defect inspection, scheduling, recipe and process analysis, documentation, quoting, and administration, but physical process work remains dominant. Weak real output and potentially material wastewater or PFAS liabilities are the central concerns.

## How AI changes the work
The implementable opportunity spans computer-vision inspection, color and shade analysis, anomaly detection, predictive maintenance, production scheduling, specification parsing, compliance records, purchasing, billing, and customer communication. Physical dyeing and finishing, sample handling, changeovers, maintenance, chemical management, and exception resolution limit whole-job substitution.

## Value capture
Lower shade failures, scrap, rework, chemical use, and turnaround time can improve margins without an immediately observable labor-price linkage. Per-yard rebids and procurement competition will share savings over time, while differentiated recipes, qualifications, specialty effects, speed, and strong compliance can preserve retention.

## Firm availability
The estimated LMM population is larger than in many niche textile codes, and the NAICS definition explicitly includes contract finishing. Transferable supply is nevertheless reduced by converter economics, integrated or captive operations, concentrated customer books, aging equipment, owner dependence, and environmental diligence. Broad employer-business transition plans support some deal flow but not a large annual wave.

## Demand durability
A physical operator remains necessary wherever finishing demand survives, but domestic real output for the finishing-and-coating group has declined materially. Commodity work can move offshore with fabric production; quick-turn, specialty, traceable, regulated, or customer-qualified work is more defensible.

## Risks and uncertainty
Public occupation and output data combine finishing with coating, and there is no direct public evidence for the LMM lens. Diligence must resolve contract versus converter revenue, process and end-market mix, customer concentration, recipe ownership, existing automation, permit status, wastewater treatment, PFAS history, deferred maintenance, and the cost of qualifying process changes.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.2405 | — | OBSERVED | — |
| n | — | 118 | — | ESTIMATE | — |
| a | 0.21 | 0.33 | 0.45 | PROXY | S2, S3 |
| rho | 0.32 | 0.52 | 0.7 | PROXY | S3, S4, S5 |
| e | 0.68 | 0.82 | 0.92 | ESTIMATE | S1, S5 |
| s5 | 0.11 | 0.2 | 0.31 | PROXY | S5, S6 |
| q | 0.36 | 0.56 | 0.74 | ESTIMATE | S1, S3 |
| d5 | 0.72 | 0.87 | 1.03 | PROXY | S1, S7 |
| o | 0.91 | 0.97 | 0.995 | ESTIMATE | S1, S5 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.65 | 1.65 | 3.03 | PROXY |
| F | 3.68 | 4.85 | 5.70 | ESTIMATE |
| C | 7.20 | 10.00 | 10.00 | ESTIMATE |
| D | 6.55 | 8.44 | 10.00 | ESTIMATE |

## Caveats
- a: OEWS is for NAICS 313300 and therefore includes fabric coating mills.
- a: Published occupation shares are employment-weighted; wage weighting is approximated from the displayed wage structure rather than observed at 313310.
- a: The defect-detection review demonstrates technical capability across textiles, not realized labor substitution in US finishing mills.
- rho: The small-business survey spans industries and measures generative-AI use or plans rather than production automation.
- rho: Labor savings may be absorbed as throughput or quality capacity rather than headcount reduction.
- rho: Customer qualification and environmental controls can slow otherwise feasible deployments.
- e: No public source measures lens eligibility in the specified EBITDA band.
- e: The provided LMM firm count is an estimate and may include integrated or converter operations.
- e: Environmental liabilities can impair transferability even when customer revenue is otherwise eligible.
- s5: Gallup covers employer businesses across industries and sizes, not NAICS 313310 or the LMM EBITDA band.
- s5: Owner plans may not be completed and may involve partial or non-control changes.
- s5: A family transfer qualifies only if control and the operating business actually transfer.
- q: No public evidence measures five-year retained AI benefit for textile finishers.
- q: Converter wholesale margins behave differently from contract finishing fees, which is why the lens is narrowed.
- q: Environmental or energy savings may be shared differently from direct labor savings.
- d5: The output series includes NAICS 313320 fabric coating mills.
- d5: Industrial production is realized US output rather than direct demand for the frozen service basket.
- d5: Future trade policy and customer reshoring decisions are not forecast explicitly.
- o: This estimate is conditional on the demand represented in d5; it does not reapply volume decline.
- o: Some laboratory, color-development, inspection, and documentation work can be self-served even though the physical process remains external.
- o: Environmental compliance makes an accountable operator necessary but can also push customers toward alternative supply.

## Sources
- **S1** — [313310: Textile and Fabric Finishing Mills - Census Bureau Profile](https://data.census.gov/profile/313310_-_Textile_and_Fabric_Finishing_Mills?codeset=naics~313310) (accessed 2026-07-23): Defines the industry as textile, fabric, and apparel finishing plus converters buying grey goods, having them contract-finished, and wholesaling them; lists core finishing processes.
- **S2** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: Textile and Fabric Finishing and Fabric Coating Mills](https://www.bls.gov/oes/2023/may/naics4_313300.htm) (accessed 2026-07-23): Reports the broader group's occupation mix, including production at 56.59%, office support at 12.81%, bleaching and dyeing operators at 17.10%, and inspectors at 5.14%.
- **S3** — [Artificial Intelligence Driving Innovation in Textile Defect Detection](https://www.mdpi.com/2673-7248/5/2/12) (accessed 2026-07-23): 2025 review documenting computer vision, image processing, and machine learning for faster and more reliable textile defect detection, with continuing implementation challenges.
- **S4** — [U.S. Bank 2025 Small Business Survey](https://ir.usbank.com/news-events/news/news-details/2025/U-S--Bank-Small-Business-Survey-Finds-More-Than-One-Third-of-Gen-Z-and-Millennial-Owners-Plan-to-Acquire-a-Business-From-a-Retiring-Owner--But-Many-Older-Owners-Arent-Ready/default.aspx) (accessed 2026-07-23): Reports that 57% of surveyed small-business owners currently use or plan to implement GenAI within a year, led by content, data and information, and marketing uses; gives survey population and methodology.
- **S5** — [Textile Mills Effluent Guidelines](https://www.epa.gov/eg/textile-mills-effluent-guidelines) (accessed 2026-07-23): Describes finishing processes and regulated pollutants, and states EPA is studying PFAS use and discharge because some textile-mill wastewater samples contain PFAS and most mills are not monitoring for it.
- **S6** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-23): Reports that 22% of employer-business owners planned to sell, transfer, or take public their business within five years, rising to 30% among employer owners age 55 or older; provides survey methods.
- **S7** — [Industrial Production: Textile and Fabric Finishing and Fabric Coating Mills (NAICS 3133)](https://fred.stlouisfed.org/series/IPG3133A) (accessed 2026-07-23): Federal Reserve real-output index for the broader industry: 66.3922 in 2022, 61.8800 in 2024, and 60.3558 in 2025.
