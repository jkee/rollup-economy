# 331492 — Secondary Smelting, Refining, and Alloying of Nonferrous Metal (except Copper and Aluminum)

*v5.1 Stage 1 research memo. Run `331492-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 5.33 · L 0.26 · interval STRUCTURAL_OUT → STRUCTURAL_OUT · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Domestic critical-material recycling investment and repeat feedstock/offtake contracts can support growing, operator-required processing demand.
**Weakness:** Environmental liabilities and metal-price-distorted economics sharply reduce the pool of safely transferable recurring-service firms.

## Business-model lens
- Included: Independent US secondary smelters, refiners, and alloyers that repeatedly recover lead, nickel, cobalt, precious, tin, titanium, zinc, or other nonferrous metals from customer or contracted scrap streams, or toll-alloy purchased metal, with transferable operations in the target band.
- Excluded: Copper and aluminum recyclers, scrap brokers and sorting facilities without smelting or refining, captive internal recovery operations, speculative inventory vehicles, dormant assets, project shells, and non-control interests.
- Customer and revenue model: Revenue combines toll or treatment charges, recovery-value sharing, and sales of ingot, billet, alloy, powder, or other primary forms, generally under recurring feedstock and offtake relationships with metal-price formulas.
- Deviation from default lens: The code mixes outsourced recovery/toll processing with commodity metal production from owned scrap. The lens retains repeat external recovery, refining, and alloying relationships because speculative and captive operations are not coherent recurring services.

## Executive view
Secondary nonferrous recovery has durable physical demand and emerging critical-material tailwinds, but a coherent roll-up lens includes only repeat toll and contracted recovery, not speculative scrap ownership or captive plants. AI affects administrative, assay, planning, maintenance, and compliance work rather than the furnace-centered core.

## How AI changes the work
Useful workflows include feedstock classification, assay reconciliation, settlement support, production scheduling, maintenance knowledge, quality certificates, emissions and waste records, procurement, and customer communication. Physical preparation, smelting, refining, sampling, dust control, and product release remain operator-accountable.

## Value capture
Treatment and recovery formulas can protect processing economics, while scarce permits and specialized streams add differentiation. Feedstock suppliers and offtakers are sophisticated counterparties, so efficiency gains face repricing and recovery-sharing pressure.

## Firm availability
The injected pool may be distorted by metal-price receipts. Eligible firms need repeat external streams, reliable assays and recoveries, transferable permits, manageable liabilities, independent management, and target-band processing economics.

## Demand durability
Lead-acid battery recycling is mature, while battery, electronics, titanium, nickel, tin, precious, and critical-metal recovery is expanding. The range remains wide because new projects, technologies, commodity cycles, and feedstock availability can shift volumes rapidly.

## Risks and uncertainty
Key risks are environmental and remediation liabilities, worker exposure, volatile assays and prices, feedstock concentration, commissioning failure, alternate hydrometallurgy, classification ambiguity, legacy controls, and the lack of six-digit occupation and transfer data.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1082 | — | OBSERVED | — |
| n | — | 81 | — | ESTIMATE | — |
| a | 0.07 | 0.14 | 0.22 | PROXY | S1, S2 |
| rho | 0.24 | 0.43 | 0.62 | ESTIMATE | S2, S3 |
| e | 0.12 | 0.29 | 0.48 | ESTIMATE | S2, S3 |
| s5 | 0.09 | 0.18 | 0.29 | PROXY | S4 |
| q | 0.22 | 0.42 | 0.63 | ESTIMATE | S2, S5 |
| d5 | 0.94 | 1.12 | 1.34 | PROXY | S5, S6, S7 |
| o | 0.95 | 0.99 | 1 | ESTIMATE | S2, S3, S6 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.07 | 0.26 | 0.59 | ESTIMATE |
| F | 1.01 | 2.66 | 4.03 | ESTIMATE |
| C | 4.40 | 8.40 | 10.00 | ESTIMATE |
| D | 8.93 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: Four-digit occupation data mix primary and secondary processes.
- a: Current automation in assay labs, furnace controls, sorting, and emissions monitoring is not observed.
- rho: No six-digit AI implementation study was located.
- rho: Emerging battery-recycling processes may be more digital than mature secondary lead plants.
- e: Public data do not distinguish treatment services from commodity metal sales.
- e: Metal-price pass-through can inflate receipts and distort the injected EBITDA-band bridge.
- s5: Cross-industry intentions are not realized transaction probabilities.
- s5: Corporate battery-recycling projects and strategic joint ventures may fall outside the LMM control lens.
- q: No source directly measures pass-through of AI-derived savings.
- q: Accounting margins can move with metal inventories even when processing economics are unchanged.
- d5: USGS totals include metals and recycling routes outside this NAICS.
- d5: Battery and electronics recovery may use processes or classifications different from traditional secondary smelting.
- o: Operator requirement is distinct from labor intensity.
- o: Technology substitution among physical recovery routes belongs partly in d5.

## Sources
- **S1** — [Nonferrous Metal (except Aluminum) Production and Processing - May 2023 OEWS Industry-Specific Occupational Employment and Wage Estimates](https://www.bls.gov/oes/2023/may/naics4_331400.htm) (accessed 2026-07-22): Broader-industry occupation mix: 53.18% production and 7.66% installation, maintenance, and repair.
- **S2** — [NAICS 331492 Definition](https://www.census.gov/naics/resources/archives/sect31-33.html) (accessed 2026-07-22): Official scope: alloying purchased nonferrous metals or recovering them from scrap and making primary forms through smelting or refining.
- **S3** — [Secondary Lead Smelting NESHAP](https://www.epa.gov/stationary-sources-air-pollution/secondary-lead-smelting-national-emissions-standards-hazardous-air) (accessed 2026-07-22): Physical and regulated process scope for a major segment: batteries and other lead scrap are recycled through furnaces, refining kettles, dryers, buildings, and fugitive-emissions controls.
- **S4** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Cross-industry succession proxy: 52.3% of employer businesses have owners age 55 or older and 22% planned a five-year sale or transfer.
- **S5** — [Employment and output by industry](https://www.bls.gov/emp/tables/industry-employment-and-output.htm) (accessed 2026-07-22): BLS projects broader NAICS 331400 real output growth of 2.4% annually over 2024-34.
- **S6** — [Mineral Commodity Summaries 2026](https://pubs.usgs.gov/periodicals/mcs2026/mcs2026.pdf) (accessed 2026-07-22): USGS estimates $46 billion of old scrap was domestically recycled in 2025 and documents new US nickel, tin, precious-metal, titanium, battery, and mixed-metal recovery facilities.
- **S7** — [Sector Spotlight: Critical Materials](https://www.energy.gov/edf/articles/sector-spotlight-critical-materials) (accessed 2026-07-22): DOE describes large projected demand growth for key battery minerals and financing for domestic closed-loop critical-material recycling and processing.
