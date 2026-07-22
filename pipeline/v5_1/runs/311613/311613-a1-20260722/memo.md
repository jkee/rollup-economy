# 311613 — Rendering and Meat Byproduct Processing

*v5.1 Stage 1 research memo. Run `311613-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 5.66 · L 0.43 · interval STRUCTURAL_OUT → STRUCTURAL_OUT · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Route-dense recurring collection and mission-critical physical conversion of unavoidable perishable byproducts.
**Weakness:** A small, consolidated firm universe and commodity-linked economics leave eligibility, transfer supply, and benefit retention poorly measured.

## Business-model lens
- Included: Lower-middle-market independent renderers that repeatedly collect and process animal byproducts, mortalities, meat scraps, or grease from external slaughterhouses, food processors, farms, retailers, restaurants, and institutions.
- Excluded: Captive rendering within integrated meatpacking plants, firms principally processing only internally generated material, pure commodity traders, shells, and non-control financing vehicles.
- Customer and revenue model: Recurring route-based collection and byproduct handling for external generators, often economically supported by sale of recovered fats, protein meals, and grease and sometimes bundled with grease-trap or wastewater services.
- Deviation from default lens: The lens is narrowed to independent external-source rendering because the code combines recurring outsourced collection/processors with captive integrated plants; their eligibility and value-capture mechanics are materially different.

## Executive view
Independent rendering is a genuine recurring outsourced operation: it collects perishable byproducts from many external generators and converts them into saleable fats and proteins. AI is most relevant to routing, receiving, controls, maintenance, quality, compliance, and administration; the already-mechanized thermal core and low labor-to-receipts ratio limit the absolute labor pool.

## How AI changes the work
Vision and sensors can classify incoming material and flag contamination, optimization can improve pickup routes and cooker settings, predictive models can reduce equipment failure, and language tools can streamline manifests, customer service, and compliance records. Harsh plants, legacy controls, variable feedstock, fleet work, and environmental obligations constrain rollout.

## Value capture
The operator sits between generators and commodity buyers. Better routes, yield, energy use, and uptime create value, but generators can seek higher rebates or lower service prices and end-product buyers pay market-linked prices, so a meaningful portion of gains is competed away.

## Firm availability
Independent offsite-source renderers fit the lens; captive integrated plants do not. The addressable count is small and current ownership data are weak, while permits, routes, and local density make viable assets strategically valuable but environmental liabilities can impair transferability.

## Demand durability
Meat and food systems continue to generate material that must be managed quickly, and feed plus biomass-diesel markets provide outlets. Demand is durable but volatile because renewable-fuel policy, imports, livestock cycles, feed substitution, and reintegration can change both product values and outsourced volumes.

## Risks and uncertainty
The largest unknowns are the current independent share of LMM firms, true revenue architecture, and transaction frequency. Odor, wastewater, emissions, animal-disease rules, contamination, fleet incidents, energy costs, commodity spreads, and customer or supplier concentration can overwhelm AI savings.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.0826 | — | OBSERVED | — |
| n | — | 30 | — | ESTIMATE | — |
| a | 0.18 | 0.29 | 0.42 | PROXY | S1, S2 |
| rho | 0.28 | 0.45 | 0.62 | ESTIMATE | S2 |
| e | 0.35 | 0.55 | 0.75 | PROXY | S3, S6, S7 |
| s5 | 0.1 | 0.18 | 0.28 | ESTIMATE | — |
| q | 0.4 | 0.6 | 0.78 | PROXY | S4, S5, S6 |
| d5 | 0.95 | 1.05 | 1.16 | PROXY | S4, S5, S7 |
| o | 0.94 | 0.98 | 1 | PROXY | S2, S3, S6, S7 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.17 | 0.43 | 0.86 | ESTIMATE |
| F | 1.15 | 2.22 | 3.20 | ESTIMATE |
| C | 8.00 | 10.00 | 10.00 | PROXY |
| D | 8.93 | 10.00 | 10.00 | PROXY |

## Caveats
- a: The occupation source covers all NAICS 311600 and is employment-weighted rather than wage-weighted.
- a: EPA's process description establishes mechanization but does not measure AI exposure or current software adoption.
- rho: Continuous process equipment does not imply modern data infrastructure.
- rho: The range combines relatively easy digital workflows with much harder physical and control-system changes.
- e: The independent-versus-integrated count is from 1992 and is establishment-based, not firm-based.
- e: Independent firms may still earn primarily commodity product revenue rather than explicit service fees.
- s5: Only 30 LMM-band firms are estimated, so a few transfers materially change the rate.
- s5: Plant acquisitions and route purchases are not necessarily qualifying firm-control transfers.
- q: Revenue can sit on either side of the feedstock transaction depending on material value and local disposal alternatives.
- q: Biofuel and feed prices can swamp the commercial effect of operating savings.
- d5: The strongest demand evidence is historical growth, not a five-year forecast.
- d5: Rendered inputs compete with vegetable oils, imported used cooking oil, and other feed proteins.
- o: Alternative disposal and processing methods can replace the eligible operator without replacing demand for byproduct management.
- o: Integrated rendering would preserve physical demand but move it outside the lens.

## Sources
- **S1** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 311600](https://www.bls.gov/oes/2023/may/naics4_311600.htm) (accessed 2026-07-22): Broader-industry occupation mix: production 59.77%, transportation and material moving 18.43%, maintenance and repair 6.47%, and office support 4.31%.
- **S2** — [AP-42 Section 9.5.3: Meat Rendering Plants](https://www.epa.gov/sites/default/files/2020-10/documents/c9s05-3_0.pdf) (accessed 2026-07-22): EPA describes batch and continuous rendering, conveyors, cookers, presses, pumps, centrifuges, storage, feedstock variability, and process conditions.
- **S3** — [Final Background Document for Meat Rendering Plants, Section 9.5.3](https://www3.epa.gov/ttn/chief/ap42/ch09/bgdocs/b09s05-3.pdf) (accessed 2026-07-22): EPA distinguishes integrated and independent renderers, lists offsite source types, and reports a 1992 estimate of 150 independent and 100 integrated U.S. plants.
- **S4** — [Growing Biomass-Based Diesel Production Drives Demand for Animal Fats, Waste Oils, and Grease](https://www.ers.usda.gov/data-products/charts-of-note/109680) (accessed 2026-07-22): USDA reports biomass-based diesel output rising from 1.8 billion gallons in 2016 to 4.6 billion in 2023 and almost 12 billion pounds of animal fats and greases used in 2023.
- **S5** — [Energy and Nutrient Digestibility in Four Sources of Meat and Bone Meal and Animal Protein Blends Fed to Growing Pigs](https://www.ars.usda.gov/research/publications/publication/?seqNo115=335390) (accessed 2026-07-22): USDA ARS reports 4.5 million tons of animal-derived protein products, about 85% used as animal-feed ingredients, and documents variation in product energy value.
- **S6** — [Darling International Investor Presentation](https://www.sec.gov/Archives/edgar/data/916540/000119312511081529/dex991.htm) (accessed 2026-07-22): Public-company filing describes external-source rendering, spent-cooking-oil collection, grease-trap services, supplier types, recovered products, traceability, rapid processing, and outsourcing by integrated meat processors.
- **S7** — [After Action Report: Rendering Workshop](https://www.aphis.usda.gov/sites/default/files/rendering-report.pdf) (accessed 2026-07-22): USDA reports 170 U.S. facilities processing more than 56 billion pounds of animal byproduct and describes source materials, output uses, process controls, and industry structure.
