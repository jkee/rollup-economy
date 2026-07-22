# 325910 — Printing Ink Manufacturing

*v5.1 Stage 1 research memo. Run `325910-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 5.90 · L 0.79 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Repeat specification-qualified consumable sales create switching friction and recurring demand in retained print applications.
**Weakness:** Legacy print decline and physical production constrain both demand and labor substitution.

## Business-model lens
- Included: Independent LMM manufacturers of printing and inkjet inks and cartridges with repeat external sales to printers, converters, packagers, or equipment users, including formulation and technical support.
- Excluded: Captive ink production, pure distributors, printer operations without ink manufacture, shells, and firms outside the EBITDA band.
- Customer and revenue model: Repeat B2B sales of color- and process-qualified consumables, commonly accompanied by matching, formulation, troubleshooting, inventory, and regulatory support.
- Deviation from default lens: none

## Executive view
Printing ink is a repeat-consumables niche with specification lock-in and useful knowledge-work automation, but physical plant work caps labor exposure and secular decline in parts of print clouds demand.

## How AI changes the work
AI can assist color and formulation search, specification and safety-document work, quality trend detection, scheduling, purchasing, quoting, and technical-service triage. Mixing, milling, filling, lab trials, press qualification, maintenance, and final release remain physical and accountable.

## Value capture
Customer qualification and press performance create switching friction, especially in specialty packaging and inkjet niches. Large converters, raw-material pass-through, and commodity competition allow customers to capture a meaningful portion at renewal.

## Firm availability
Most independent manufacturers should fit recurring external sales, but the estimated universe is limited. Legacy-print exposure, environmental history, site condition, customer concentration, and reliance on a few formulators can make candidates ineligible or non-transferable.

## Demand durability
The physical consumable remains necessary wherever print persists. Packaging, labels, and industrial print offset some decline in publications and office output, so target product mix is more important than the aggregate code.

## Risks and uncertainty
Key uncertainties are six-digit occupation mix, current automation, secular end-market mix, environmental liabilities, customer qualification and concentration, formula ownership, and control-transfer frequency.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1487 | — | OBSERVED | — |
| n | — | 53 | — | ESTIMATE | — |
| a | 0.16 | 0.25 | 0.36 | PROXY | S1, S2, S3 |
| rho | 0.36 | 0.53 | 0.69 | ESTIMATE | S2, S4 |
| e | 0.6 | 0.76 | 0.88 | ESTIMATE | S1, S4 |
| s5 | 0.14 | 0.24 | 0.35 | PROXY | S5 |
| q | 0.45 | 0.61 | 0.76 | ESTIMATE | S1 |
| d5 | 0.82 | 0.94 | 1.07 | ESTIMATE | S1, S6 |
| o | 0.9 | 0.96 | 0.99 | ESTIMATE | S1, S2, S4 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.34 | 0.79 | 1.48 | ESTIMATE |
| F | 2.73 | 3.81 | 4.59 | ESTIMATE |
| C | 9.00 | 10.00 | 10.00 | ESTIMATE |
| D | 7.38 | 9.02 | 10.00 | ESTIMATE |

## Caveats
- a: Occupation evidence is inferred from broader chemical manufacturing.
- a: Product and plant automation vary.
- rho: No industry-specific five-year adoption survey.
- rho: Environmental and performance accountability requires expert review.
- e: Injected firm count is a margin-bridged estimate.
- e: Industry classification alone does not prove independence or transferability.
- s5: Broad demographic proxy.
- s5: No public transfer-rate denominator was found.
- q: No public contract evidence quantifies pass-through.
- q: Inkjet and specialty packaging inks may retain more than conventional publication inks.
- d5: Official sources define and track manufacturing but do not supply a clean five-year product-volume forecast.
- d5: Mix differs sharply by target.
- o: Demand elimination is captured primarily in d5.
- o: Operator share can migrate to integrated equipment vendors or overseas suppliers.

## Sources
- **S1** — [NAICS 325910 Printing Ink Manufacturing](https://www.census.gov/naics/?details=32591&input=32591&year=2012) (accessed 2026-07-22): Census defines the industry as manufacturing printing and inkjet inks and inkjet cartridges.
- **S2** — [AP-42 Section 6.7 Printing Ink](https://www3.epa.gov/ttnchie1/ap42/ch06/final/c06s07.pdf) (accessed 2026-07-22): EPA provides printing-ink manufacturing process and emission-factor material, supporting the physical-process and environmental-accountability characterization.
- **S3** — [Chemical Manufacturing: NAICS 325](https://www.bls.gov/iag/tgs/iag325.htm) (accessed 2026-07-22): BLS provides broader chemical-manufacturing occupation context used as a task-mix proxy.
- **S4** — [Printing and Related Support Activities Sector](https://www.epa.gov/regulatory-information-sector/printing-and-related-support-activities-sector-naics-323) (accessed 2026-07-22): EPA identifies printing-sector air-toxics regulation and links process information that includes printing ink.
- **S5** — [2024 Firms in Focus chartbooks on small business data](https://www.fedsmallbusiness.org/reports/survey/2024/2024-small-business-data-chartbooks) (accessed 2026-07-22): Federal Reserve chartbooks include owner-demographic and age-of-owner evidence used only as a succession proxy.
- **S6** — [Manufacturers' Shipments, Inventories, & Orders - Historical Data](https://www.census.gov/manufacturing/m3/historical_data/index.html) (accessed 2026-07-22): Census provides historical manufacturing shipments and orders resources, supporting the proposed route for demand verification rather than a specific forecast.
