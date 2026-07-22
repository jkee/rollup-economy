# 311991 — Perishable Prepared Food Manufacturing

*v5.1 Stage 1 research memo. Run `311991-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 6.39 · L 0.42 · interval STRUCTURAL_OUT → STRUCTURAL_OUT · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Recurring customer demand for safe, fresh, convenient food creates a persistent outsourced operator role with valuable scheduling, order, quality, and waste workflows for AI.
**Weakness:** Most payroll supports physical production and cold-chain execution, while the eligible share and retained benefit rely on broad or company-specific proxies rather than six-digit measurement.

## Business-model lens
- Included: Lower-middle-market U.S. manufacturers repeatedly producing short-shelf-life prepared meals, salads, sandwiches, fresh pizza and pasta, peeled or cut vegetables, and similar refrigerated foods for external retailers, brands, meal platforms, institutions, or foodservice customers under private-label, co-packing, contract-production, or customized supply relationships.
- Excluded: Own-brand-only food companies without recurring outsourced production, restaurant or grocery in-store kitchens classified outside manufacturing, captive commissaries, shelf-stable or frozen products outside 311991, shells, and non-control financing vehicles.
- Customer and revenue model: Recurring business-to-business unit sales and manufacturing programs, often customer-specific or private label, with high-frequency ordering, strict freshness and service windows, retailer or foodservice specifications, and revenue tied to cases, units, or meals delivered.
- Deviation from default lens: none

## Executive view
Perishable prepared food contains a clear outsourced manufacturing model for retailers, brands, institutions, and meal platforms, with a large estimated LMM cohort and structurally durable convenience demand. The constraint is that most labor remains physical, local, time-sensitive, and safety-critical, so AI's implementable contribution is concentrated in planning, order flow, waste control, documentation, and selected inspection rather than full production substitution.

## How AI changes the work
AI can improve short-horizon forecasting, menu and ingredient planning, labor scheduling, order intake, customer communication, specification review, environmental and quality trend detection, vision inspection, route planning, and maintenance triage. It cannot directly replace most preparation, assembly, sanitation, packaging intervention, cold-chain handling, and accountable product release.

## Value capture
Fixed case prices and superior freshness or service allow temporary retention, but large retailers and foodservice buyers exert substantial leverage. Over repeated annual and multi-year renewals, gains will be shared through lower bids, productivity expectations, tighter service levels, or customer migration.

## Firm availability
Private-label and food-as-a-service platforms demonstrate eligibility, and the 2024 transfer of a fresh-cut prepared-food business to a co-packing partner demonstrates that operating platforms can change control. Actual availability is constrained by customer concentration, leases, labor, food-safety history, and the need to transfer programs without interrupting daily service.

## Demand durability
Convenience, fresh-food positioning, and customer outsourcing support modest five-year unit growth across grocery and foodservice. Short shelf life, high waste, price sensitivity, demand swings, and retailer or restaurant insourcing can offset that growth, but software cannot eliminate the need to make and move physical food.

## Risks and uncertainty
Listeria and other environmental pathogens are central tail risks; one failure can cause recalls, lost customers, plant downtime, and liability that overwhelms labor savings. Forecast error creates spoilage or service misses. The evidence is weakest on six-digit task exposure, the LMM eligible share, and contract-level pass-through, while current AI adoption evidence mostly reflects augmentation rather than reduced staffing.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1527 | — | OBSERVED | — |
| n | — | 240 | — | ESTIMATE | — |
| a | 0.1 | 0.18 | 0.27 | PROXY | S2, S3 |
| rho | 0.2 | 0.38 | 0.58 | PROXY | S4, S5 |
| e | 0.27 | 0.44 | 0.62 | PROXY | S1, S6, S7 |
| s5 | 0.11 | 0.22 | 0.35 | PROXY | S7, S8, S9 |
| q | 0.34 | 0.54 | 0.72 | PROXY | S7, S10 |
| d5 | 0.96 | 1.07 | 1.16 | PROXY | S6, S11, S12, S13 |
| o | 0.94 | 0.98 | 1 | ESTIMATE | S5, S14 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.12 | 0.42 | 0.96 | PROXY |
| F | 3.37 | 5.13 | 6.39 | ESTIMATE |
| C | 6.80 | 10.00 | 10.00 | PROXY |
| D | 9.02 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: The occupation table is four-digit NAICS 311900, not six-digit 311991.
- a: The estimate cannot observe the baseline of conventional automation, robotics, and software already in use.
- a: Waste and throughput improvements may create economic value without substituting wage hours and therefore are not counted in a.
- rho: BTOS measures broad business-function use, including drafting and search that may not generate labor savings.
- rho: FDA requirements do not prohibit AI but require monitoring, verification, corrective action, and records around safety-critical controls.
- rho: Rapidly changing daily menus and short data histories can make models fragile.
- e: No public dataset reports the eligible firm share at six digits.
- e: FreshRealm is a prominent scaled platform, not a representative LMM firm.
- e: Private-label sales qualify only when they reflect a repeat outsourced operating capability for an external customer.
- s5: One strategic asset sale does not measure annual transfer probability.
- s5: The owner-age evidence is old, broad, and limited to linked single-unit firms.
- s5: Internal reorganizations, closures, and asset liquidations without a transferable operating business are excluded.
- q: The fixed-price contract evidence is older and from value-added salads rather than the entire six-digit industry.
- q: Retention varies between differentiated custom meal programs and easily rebid fresh-cut commodities.
- q: The estimate excludes volume loss, waste benefits, and implementation difficulty.
- d5: Convenience-food research spans frozen, shelf-stable, restaurant, and other products outside 311991.
- d5: Real foodservice spending does not isolate constant-quality perishable prepared-food units.
- d5: FreshRealm's capacity and reach are company-provided figures and may represent share shift rather than category growth.
- o: No source directly measures operator-required year-five quantity.
- o: Insourcing changes the operator's identity and may remove volume from the lens even though physical work persists.
- o: Automation could sharply reduce staffing without eliminating the accountable manufacturing entity.

## Sources
- **S1** — [North American Industry Classification System: 311991 Perishable Prepared Food Manufacturing](https://www.census.gov/naics/?details=311&input=311&year=2022) (accessed 2026-07-23): Defines 311991 as manufacturing perishable prepared foods such as salads, sandwiches, prepared meals, fresh pizza, fresh pasta, and peeled or cut vegetables.
- **S2** — [Other Food Manufacturing: May 2023 OEWS Industry-Specific Occupational Employment and Wage Estimates](https://www.bls.gov/oes/2023/may/naics4_311900.htm) (accessed 2026-07-23): Reports 259,650 jobs in NAICS 311900, including 43.62% production, 20.91% transportation/material moving, 7.15% office support, 6.04% maintenance, 5.69% management, and 3.64% business/financial operations.
- **S3** — [Generative AI and Jobs: A Refined Global Index of Occupational Exposure](https://www.ilo.org/publications/generative-ai-and-jobs-refined-global-index-occupational-exposure) (accessed 2026-07-23): Finds clerical occupations remain the most exposed to GenAI and that transformation rather than full replacement is the most likely impact for most occupations.
- **S4** — [The Microstructure of AI Diffusion: Evidence from Firms, Business Functions, and Worker Tasks](https://www.census.gov/library/working-papers/2026/adrm/CES-WP-26-25.html) (accessed 2026-07-23): Reports 18% firm AI use and 32% employment-weighted use in late 2025/early 2026, narrow adoption breadth, augmentation-only use for 66% of users, and AI-related employment decreases at 2% of firms.
- **S5** — [Environmental Sampling](https://www.fda.gov/food/sampling-protect-food-supply/environmental-sampling) (accessed 2026-07-23): Explains that food processors must prevent environmental contamination, monitor and verify controls, initiate corrective action, and maintain records, with Listeria frequently associated with ready-to-eat food environments.
- **S6** — [FreshRealm: A Food-as-a-Service Company](https://freshrealm.com/) (accessed 2026-07-23): Describes outsourced product development, ingredient manufacturing, production, fulfillment, and customized brand and retailer programs, with claimed built capacity of 15 million meals per week and 99% population reach.
- **S7** — [Calavo Growers, Inc. 2024 Form 10-K](https://www.sec.gov/Archives/edgar/data/1133470/000155837025000209/cvgw-20241031x10k.htm) (accessed 2026-07-23): Describes store-brand and private-label prepared products, top-ten customers at 50% of 2024 sales, risks from customer order changes, and the $83 million 2024 sale of the Fresh Cut business.
- **S8** — [Calavo Growers, Inc. Form 8-K: Sale of Fresh Cut Prepared Food Business](https://www.sec.gov/Archives/edgar/data/1133470/000155837024012417/cvgw-20240815x8k.htm) (accessed 2026-07-23): Documents the 2024 acquisition by a co-packing partner of the fresh-cut and prepared-food business, including sandwiches, salads, parfaits, snacks, fresh fruit and vegetables, as a going concern with assumed operating liabilities and leases.
- **S9** — [A Comparison of Firm Age in the Survey of Business Owners and the Longitudinal Business Database](https://www2.census.gov/ces/tn/CES-TN-2020-08.pdf) (accessed 2026-07-23): Reports 49.55% of primary owners above age 54 in its linked single-unit employer-firm 2007 sample.
- **S10** — [Chiquita Brands International, Inc. 2014 Form 10-K](https://www.sec.gov/Archives/edgar/data/101063/000010106315000026/cqb10-k.htm) (accessed 2026-07-23): Describes packaged ready-to-eat salads under branded and private labels and annual or multi-year fixed-price-per-case retail contracts with fuel-index surcharges.
- **S11** — [U.S. Households' Demand for Convenience Foods](https://ers.usda.gov/publications/80653) (accessed 2026-07-23): Reports that U.S. demand for convenience foods grew over four decades and analyzes prepared, ready-to-eat, and ready-to-cook purchasing.
- **S12** — [Food Service Industry: Market Segments](https://ers.usda.gov/topics/food-markets-prices/food-service-industry/market-segments) (accessed 2026-07-23): Reports inflation-adjusted foodservice sales of $1.41 trillion in 2025 versus $818 billion in 1997 and food away from home at 56.3% of nominal U.S. food spending in 2025.
- **S13** — [U.S. Population Growth Slows Due to Historic Decline in Net International Migration](https://www.census.gov/newsroom/press-releases/2026/population-growth-slows.html) (accessed 2026-07-23): Reports U.S. population growth of 1.8 million, or 0.5%, from July 2024 to July 2025.
- **S14** — [Outbreak Investigation of Listeria monocytogenes: Ready-to-Eat Foods, May 2025](https://www.fda.gov/food/outbreaks-foodborne-illness/outbreak-investigation-listeria-monocytogenes-ready-eat-foods-may-2025) (accessed 2026-07-23): Documents a ready-to-eat sandwich and snack outbreak tied to environmental samples, with 10 illnesses, 10 hospitalizations, one death, a recall, and corrective and preventive actions.
