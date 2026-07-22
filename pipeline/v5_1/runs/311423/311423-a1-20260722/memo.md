# 311423 — Dried and Dehydrated Food Manufacturing

*v5.1 Stage 1 research memo. Run `311423-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 5.87 · L 0.54 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Specialized drying capacity and process qualification make recurring customer production physically necessary and relatively sticky.
**Weakness:** The code mixes commodity ingredients with premium niches, leaving eligibility, pricing power, and demand growth poorly measured.

## Business-model lens
- Included: U.S. lower-middle-market contract dryers, freeze-dryers, dehydrators, ingredient processors, blenders, and private-label producers supplying recurring drying, milling, blending, filling, packaging, labeling, and quality-assurance services for fruits, vegetables, soup mixes, bouillon, and related human-food ingredients.
- Excluded: Own-brand-only manufacturers, captive plants, brokers and distributors without production responsibility, pet-food-only operations, non-control financing vehicles, and processors whose primary output is classified outside NAICS 311423.
- Customer and revenue model: Food and beverage manufacturers, consumer brands, retailers, foodservice suppliers, and institutional customers purchase repeated batches or capacity under tolling, co-manufacturing, private-label, ingredient-supply, and packaging arrangements, priced by pound, batch, unit, or committed capacity.
- Deviation from default lens: none

## Executive view
The relevant segment consists of independent toll dryers, freeze-dryers, custom ingredient processors, and private-label producers that repeatedly transform customer materials or specifications. AI can improve scheduling, process analysis, quality records, maintenance, forecasting, and customer workflows, but the bulk of labor and value creation remains physical. Diverse end markets and shelf-stability benefits support modest demand growth, with imported finished ingredients and customer insourcing as important threats.

## How AI changes the work
AI can assist dryer loading and cycle analysis, energy and yield optimization, raw-material planning, recipe checks, moisture and quality-data review, maintenance diagnosis, inspection triage, specification comparison, traceability records, and order service. Physical preparation, loading, drying, sanitation, maintenance execution, milling, blending, packaging, and exception response remain operator tasks.

## Value capture
Retention is strongest where capacity is scarce, customer qualification is costly, runs are bespoke, and gains improve yield, uptime, quality, or delivery. Commodity tolling, transparent cost formulas, annual rebids, and concentrated customers expose labor savings to pass-through. Contract detail matters more than list pricing.

## Firm availability
Contract drying and co-manufacturing are visible operating models, but the code also includes branded and merchant-product firms outside the lens. Cross-industry owner intentions and food-processing deal activity make transfers plausible; the actual eligible target set still requires firm-by-firm verification.

## Demand durability
The basket spans mature dried fruit and soup mixes as well as industrial ingredients, private label, institutional meals, and expanding freeze-dried applications. Shelf life, lower weight, convenience, and specialized processing support demand, while fresh alternatives, imports, and category fashion create a wide range. Surviving demand remains highly operator-dependent because dehydration is a physical controlled process.

## Risks and uncertainty
Key risks include raw-material seasonality, energy intensity, moisture excursions, Salmonella and allergen contamination, rehydration during storage, customer concentration, equipment downtime, imported ingredients, and uncertain novelty demand. The evidence does not directly measure task exposure, eligible-firm prevalence, or category-weighted unit growth.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1044 | — | OBSERVED | — |
| n | — | 69 | — | ESTIMATE | — |
| a | 0.15 | 0.25 | 0.35 | PROXY | S2, S3, S4 |
| rho | 0.32 | 0.52 | 0.7 | PROXY | S3, S4, S5 |
| e | 0.18 | 0.34 | 0.52 | ESTIMATE | S1, S6, S7 |
| s5 | 0.12 | 0.22 | 0.34 | PROXY | S8, S9 |
| q | 0.38 | 0.58 | 0.75 | ESTIMATE | S6, S7 |
| d5 | 0.94 | 1.04 | 1.15 | ESTIMATE | S6, S7, S10 |
| o | 0.92 | 0.98 | 1 | PROXY | S4, S5, S6, S7 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.20 | 0.54 | 1.02 | PROXY |
| F | 1.47 | 2.92 | 4.15 | ESTIMATE |
| C | 7.60 | 10.00 | 10.00 | ESTIMATE |
| D | 8.65 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: OEWS is for NAICS 311400 and employers of all sizes, not 311423 LMM firms.
- a: Conventional dryers, conveyors, packaging lines, and PLC automation are not counted unless AI changes current labor tasks.
- rho: The implementation survey includes technologies other than AI and likely overrepresents larger firms.
- rho: Food-safety and moisture-control obligations slow substitution but do not prevent decision support.
- e: Company examples demonstrate that the model exists but do not measure prevalence.
- e: The provided LMM firm count is an EBITDA-band estimate and may include firms with mixed product classifications.
- s5: Stated intentions are not completed transactions.
- s5: Published deal data undercount small private transfers and overrepresent larger transactions.
- q: Bespoke freeze-drying and commodity dehydration have very different bargaining dynamics.
- q: No public evidence directly measures retained AI benefit over five years.
- d5: Public demand evidence does not cleanly isolate 311423 or contract-manufactured output.
- d5: Growth in premium freeze-dried niches may be offset by mature dried-fruit and soup-mix categories.
- o: FDA obligations support accountable physical operations, not continued outsourcing to the same operator.
- o: Imported finished ingredients can displace U.S. operators without eliminating end demand.

## Sources
- **S1** — [North American Industry Classification System: 311423 Dried and Dehydrated Food Manufacturing](https://www.census.gov/naics/resources/archives/sect31-33.html) (accessed 2026-07-22): Defines 311423 as drying or dehydrating fruits, vegetables, soup mixes and bouillon, and drying ingredients packaged with other purchased ingredients.
- **S2** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 311400](https://www.bls.gov/oes/2023/may/naics4_311400.htm) (accessed 2026-07-22): Reports the broader sector's employment and wage mix, including 50.95% production, 17.08% transportation/material moving, 9.18% maintenance, and 5.73% office support.
- **S3** — [2025 Smart Manufacturing and Operations Survey](https://www.deloitte.com/us/en/insights/industry/manufacturing-industrial-products/2025-smart-manufacturing-survey.html) (accessed 2026-07-22): Reports 7%-20% employee-productivity improvement, 10%-15% unlocked capacity, and 46% of manufacturers ranking process automation among their top two investment priorities in a 600-respondent survey.
- **S4** — [Draft Guidance for Industry: Hazard Analysis and Risk-Based Preventive Controls for Human Food](https://www.fda.gov/files/food/published/Draft-Guidance-for-Industry-Hazard-Analysis-and-Risk-Based-Preventive-Controls-for-Human-Food-Full-Guidance-01292024.pdf) (accessed 2026-07-22): Identifies freeze-drying, forced-air drying, and spray drying as primary U.S. dehydration controls and discusses shelf stability, rehydration-resistant packaging, recipe management, moisture, storage, mycotoxins, and sorting.
- **S5** — [Water Activity in Foods](https://www.fda.gov/inspections-compliance-enforcement-and-criminal-investigations/inspection-technical-guides/water-activity-aw-foods) (accessed 2026-07-22): Explains water activity measurement and states that food stability depends on reaching and maintaining suitable water activity through processing and storage.
- **S6** — [Co-Manufacturing and Contract Freeze-Drying](https://www.freeze-dry-foods.com/dienstleistung) (accessed 2026-07-22): Documents bespoke contract drying, private-label filling, sourcing, packaging, labeling, quality control, and small- or large-batch services for food-industry customers.
- **S7** — [Flatiron Food Factory Custom Freeze-Drying Solutions](https://www.flatironfood.com/) (accessed 2026-07-22): Documents U.S. custom freeze-drying, bulk ingredient processing, co-packing, recipe development, milling, tolling, storage, and production from 500 to 100,000 pounds.
- **S8** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Reports that 22% of employer-business owners planned to sell or transfer ownership within five years, based on a fall 2024 survey of 1,264 U.S. owners.
- **S9** — [Food Production Mergers and Acquisitions Update](https://www.capstonepartners.com/insights/article-food-production-mergers-acquisitions-update/) (accessed 2026-07-22): Reports 144 food-production transactions in 2024 and growth in food-processing transactions from 20 in 2023 to 52 in 2024.
- **S10** — [Peeling Open U.S. Fruit Consumption Trends](https://www.ers.usda.gov/amber-waves/2025/february/peeling-open-us-fruit-consumption-trends) (accessed 2026-07-22): Reports total U.S. fruit availability declining from 0.95 cup-equivalents per person per day in 2003 to 0.82 in 2021 and identifies dried fruit within the measured forms.
