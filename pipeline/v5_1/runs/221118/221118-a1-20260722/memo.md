# 221118 — Other Electric Power Generation

*v5.1 Stage 1 research memo. Run `221118-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** CONDITIONAL · A 6.36 · L 2.11 · interval LOW_PRIORITY → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Contracted or market-priced recurring power revenue can retain gains from analytics, availability, maintenance, and reporting improvements.
**Weakness:** A tiny heterogeneous residual category with many asset entities makes eligible-firm identification and transferable operating-platform quality unusually uncertain.

## Business-model lens
- Included: US lower-middle-market operators of electric power generation facilities using technologies outside hydroelectric, fossil fuel, nuclear, solar, wind, geothermal, and biomass, selling recurring electricity, capacity, or ancillary services to utilities, organized markets, aggregators, or contracted commercial and industrial offtakers.
- Excluded: The specifically classified generation technologies, transmission and distribution utilities, equipment vendors, developers without operating assets, captive self-generation without external sales, municipal or internal departments, passive asset shells, tax-equity vehicles, and non-control financing vehicles.
- Customer and revenue model: Recurring wholesale electricity, capacity, renewable or environmental attribute, and ancillary-service revenue through long-term power purchase agreements, utility contracts, regulated or market-based rates, and organized spot or forward markets; revenue depends on dispatched or contracted output, availability, price, and compliance.
- Deviation from default lens: none

## Executive view
Other electric power generation offers focused AI opportunities in monitoring analytics, maintenance, market operations, settlements, reporting, and administration, but core plant control is already automated and remains safety-critical. The residual NAICS definition and prevalence of project entities make population quality a larger issue than software feasibility.

## How AI changes the work
AI can prioritize alarms, detect degrading equipment, forecast output and price, assist bids and dispatch plans, reconcile settlements, draft regulatory submissions, search technical records, and plan work. Humans still control or oversee equipment, perform rounds and repairs, respond to emergencies, and remain accountable for grid, safety, and environmental performance.

## Value capture
Fixed-price contracts and market prices can preserve gains through a contract term, especially when better availability creates incremental output. Cost-based structures, shared savings, penalties, merchant competition, and contract renewals reduce retained benefit.

## Firm availability
The frozen firm estimate is small and likely includes independent operators alongside captive facilities, public entities, project shells, and passive financed assets. A credible target must contain operating people and capabilities, external recurring revenue, transferable permits and contracts, and normalized LMM earnings.

## Demand durability
US electricity use is growing, but 221118 is a tiny, mixed residual category and cannot inherit the system forecast mechanically. Niche resources may benefit from capacity, resiliency, environmental attributes, or specialized inputs, while substitution, contract expiry, and plant retirement create substantial technology-specific dispersion.

## Risks and uncertainty
Residual-code classification, project-shell prevalence, single-offtaker exposure, PPA and interconnection transfer, market prices, forced outages, environmental compliance, cybersecurity, input supply, technology obsolescence, and capital intensity are material. Evidence is weakest on eligible operating firms, task weights, direct AI adoption, qualifying transfers, and technology-specific five-year demand.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.655 | — | OBSERVED | — |
| n | — | 32 | — | ESTIMATE | — |
| a | 0.13 | 0.22 | 0.32 | PROXY | S1 |
| rho | 0.42 | 0.58 | 0.72 | ESTIMATE | S1, S2 |
| e | 0.2 | 0.37 | 0.55 | ESTIMATE | S2, S3 |
| s5 | 0.14 | 0.23 | 0.34 | PROXY | S3, S6 |
| q | 0.52 | 0.68 | 0.82 | ESTIMATE | S2, S3 |
| d5 | 0.92 | 1.04 | 1.16 | PROXY | S4, S5 |
| o | 0.96 | 0.99 | 0.999 | ESTIMATE | S1, S2 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 1.43 | 3.34 | 6.04 | ESTIMATE |
| F | 1.03 | 2.11 | 3.13 | ESTIMATE |
| C | 10.00 | 10.00 | 10.00 | ESTIMATE |
| D | 8.83 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: The occupation source covers utilities broadly and includes distribution and nuclear roles outside 221118.
- a: The frozen compensation-to-receipts ratio is high for an asset-intensive industry and may be distorted by the small residual population or vintage mismatch.
- rho: No direct five-year adoption survey for 221118 was found.
- rho: Implementation varies sharply across fuel cells, waste-derived sources, storage-like facilities, purchased-steam systems, and other residual technologies.
- e: The frozen 32-firm estimate is margin-bridged and may count asset entities rather than operating platforms.
- e: NAICS is a residual category whose establishments can have materially different technologies and ownership structures.
- s5: Cross-industry intentions are not completed power-industry transactions.
- s5: Power-project asset and affiliate transfers can look like firm sales but fail the lens's operating-platform requirement.
- q: No public contract sample isolates automation pass-through.
- q: Retention differs substantially between merchant, fixed-price PPA, cost-based, and behind-the-meter arrangements.
- d5: Total electricity growth is not demand for the residual technology basket.
- d5: EIA energy-source categories do not map cleanly to establishment NAICS and may include storage or fuels classified elsewhere.
- o: The accountable entity may consolidate across many facilities, reducing local staffing without eliminating an operator.
- o: Storage and behind-the-meter systems may shift responsibility to customers or aggregators more readily than combustion or process-based generators.

## Sources
- **S1** — [Power Plant Operators, Distributors, and Dispatchers](https://www.bls.gov/ooh/production/power-plant-operators-distributors-and-dispatchers.htm) (accessed 2026-07-22): Lists monitoring, control, equipment checks, adjustment, start and stop, field rounds, troubleshooting, and emergency-relevant duties; reports 46,600 jobs in 2024 and a projected 10 percent employment decline through 2034 as technology and modernized control rooms improve efficiency.
- **S2** — [Electric Quarterly Reports](https://www.ferc.gov/power-sales-and-markets/electric-quarterly-reports-eqr) (accessed 2026-07-22): Explains that EQR data include contractual terms and transaction information for short- and long-term market-based and cost-based power sales, grounding recurring revenue models, reporting workflows, and contract heterogeneity.
- **S3** — [Electric Market-Based Rates](https://www.ferc.gov/power-sales-and-markets/electric-market-based-rates) (accessed 2026-07-22): Describes authorization for wholesale energy, capacity, and ancillary-service sellers and required initial, change-in-status, triennial, tariff, succession, and cancellation filings, grounding compliance and ownership-transfer considerations.
- **S4** — [EIA forecasts strongest four-year growth in U.S. electricity demand since 2000, fueled by data centers](https://www.eia.gov/pressroom/releases/press582.php) (accessed 2026-07-22): Forecasts US electricity use growth of 1 percent in 2026 and 3 percent in 2027 and shows other energy sources at 1 percent of generation in 2025, 2026, and 2027, used as a broad demand proxy rather than a 221118 forecast.
- **S5** — [Electricity in the United States](https://www.eia.gov/energyexplained/electricity/electricity-in-the-us.php) (accessed 2026-07-22): Reports other gases and other sources at about 0.2 percent of 2025 utility-scale generation and identifies other sources as including pumped storage, non-biogenic municipal waste, batteries, hydrogen, purchased steam, sulfur, tire-derived fuel, and miscellaneous sources, illustrating small scale and category heterogeneity.
- **S6** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Reports that 22 percent of employer-business owners surveyed in fall 2024 planned to sell or transfer ownership within five years, used as a cross-industry transfer proxy.
