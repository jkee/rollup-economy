# 423440 — Other Commercial Equipment Merchant Wholesalers

*v5.1 Stage 1 research memo. Run `423440-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 6.20 · L 0.91 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Physical installed equipment generates repeat service and parts workflows whose information and coordination layer is amenable to AI.
**Weakness:** Eligibility is uncertain because 423440 is fundamentally a heterogeneous merchant-wholesale category rather than a recurring-service category.

## Business-model lens
- Included: Independent commercial-equipment distributors in the lower-middle-market EBITDA band that repeatedly serve external restaurant, food-retail, institutional, or other commercial customers with equipment specification, project coordination, installation, preventive maintenance, repair, parts, or related accountable service.
- Excluded: Product-only catalog sellers, manufacturers and captive sales branches, consumer retailers, pure rental companies, commission-only agents, internal maintenance units, shells, and non-control financing vehicles.
- Customer and revenue model: Customers purchase commercial machines, fixtures, shelving, scales, and related equipment at product margins, then buy repeat project, installation, maintenance, repair, parts, or annual-service work through contracts and work orders.
- Deviation from default lens: The code is heterogeneous across restaurant equipment, store fixtures, shelving, scales, and other commercial machines, and many establishments are product-only. The lens is narrowed to distributors with a material recurring or repeat accountable service component to keep the screen coherent.

## Executive view
The coherent target is a service-bearing commercial-equipment distributor, not a product-only catalog wholesaler. AI can improve a large information and coordination layer, while the physical installed base preserves technician and project accountability; the main constraint is that many firms in the code will not meet the service lens.

## How AI changes the work
High-value workflows include product and parts identification, quote and submittal drafting, order entry, project scheduling, service intake, dispatch support, technician knowledge search, warranty documentation, purchasing, invoice matching, and customer updates. Installation, diagnosis in ambiguous field conditions, repair execution, and safety sign-off remain human work.

## Value capture
Retention should be strongest in fixed-price annual maintenance, bundled projects, urgent repair, and internal overhead. Transparent equipment bids and catalog sales will pass more savings to customers because online, manufacturer-direct, and large-distributor alternatives make comparison easy.

## Firm availability
The frozen firm count covers an equipment-wholesale code with varied niches and business models. Older-owner evidence supports a succession pipeline, but neither the eligible service share nor the five-year qualifying-transfer rate is directly observed.

## Demand durability
Commercial kitchens, stores, and institutions continue to need equipment uptime, parts, repair, compliance, and replacement. Equipment purchases are cyclical and currently soft in one major foodservice proxy, while service demand tied to the installed base should be steadier.

## Risks and uncertainty
Key risks are product-only firms inside the code, thin or cyclical equipment margins, working-capital exposure, tariffs, manufacturer channel control, technician scarcity, and fragmented legacy data. AI may improve throughput without allowing headcount removal if branches remain subscale or service quality is brittle.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1573 | — | OBSERVED | — |
| n | — | 443 | — | ESTIMATE | — |
| a | 0.17 | 0.29 | 0.41 | PROXY | S1, S2, S3, S6 |
| rho | 0.31 | 0.5 | 0.68 | ESTIMATE | S3, S6 |
| e | 0.1 | 0.24 | 0.41 | ESTIMATE | S5, S7 |
| s5 | 0.11 | 0.18 | 0.29 | PROXY | S4, S5 |
| q | 0.44 | 0.64 | 0.8 | ESTIMATE | S6, S7 |
| d5 | 0.88 | 1.03 | 1.21 | ESTIMATE | S7, S8 |
| o | 0.75 | 0.88 | 0.96 | ESTIMATE | S6, S7 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.33 | 0.91 | 1.75 | ESTIMATE |
| F | 2.85 | 4.83 | 6.41 | ESTIMATE |
| C | 8.80 | 10.00 | 10.00 | ESTIMATE |
| D | 6.60 | 9.06 | 10.00 | ESTIMATE |

## Caveats
- a: Occupation evidence is at 423400, not six-digit 423440.
- a: Global Industrial spans broader industrial products and is much larger than the target firms.
- a: General AI evidence measures exposure or use, not removable labor.
- rho: No representative 423440 implementation study was found.
- rho: AI use observed on consumer chat products may not transfer to field-service systems.
- rho: Small distributors may lack clean product and service data.
- e: The frozen n is derived using broad distributor margins that may misclassify service-rich firms by EBITDA band.
- e: Manufacturer service models demonstrate the activity but not its prevalence among independent wholesalers.
- e: Eligibility likely varies sharply by equipment niche.
- s5: Broad and subgroup-specific age data are weak predictors of transaction timing.
- s5: No denominator-complete six-digit deal series was found.
- s5: Family succession and manufacturer dealer-authorizations may affect transferability.
- q: Public manufacturer and distributor economics are only directional for independent LMM dealers.
- q: Gross margin is not direct evidence of AI-benefit retention.
- q: Emergency repair and bid equipment sales have very different pricing power.
- d5: Middleby is a global manufacturer, not a U.S. merchant wholesaler.
- d5: Reported sales include price, currency, acquisition, and share effects.
- d5: The code combines end markets with different cycles.
- o: The service lens selects activities with intrinsically high operator requirement.
- o: Remote diagnostics and connected equipment could reduce truck rolls.
- o: Manufacturers may internalize service and displace independent distributors without eliminating operator work.

## Sources
- **S1** — [Data tables for OEWS industry charts, May 2024](https://www.bls.gov/oes/2024/may/ind_emp_chart/ind_emp_chart_data.htm) (accessed 2026-07-22): Observed largest occupations and employment counts for the broader NAICS 423400 professional and commercial equipment wholesale industry.
- **S2** — [GPTs are GPTs: An early look at the labor market impact potential of large language models](https://openai.com/index/gpts-are-gpts/) (accessed 2026-07-22): General U.S. task-exposure benchmark: about 80% of workers could have at least 10% of tasks affected and about 19% could have at least 50% affected.
- **S3** — [The Anthropic Economic Index](https://www.anthropic.com/news/the-anthropic-economic-index) (accessed 2026-07-22): Observed Claude task use across occupations, including 57% augmentation and 43% automation, with stated representativeness limitations.
- **S4** — [Business Owners' Ages](https://www.census.gov/content/dam/Census/library/visualizations/2020/comm/business-owners-ages.pdf) (accessed 2026-07-22): 2019 Annual Business Survey graphic reporting that 51% of responding employer-business owners were 55 or older.
- **S5** — [The Metamorphosis of Women Business Owners: A Focus on Age](https://www2.census.gov/ces/wp/2024/CES-WP-24-71.pdf) (accessed 2026-07-22): Census evidence that older employer owners are prominent in wholesale trade, used only as an owner-age proxy for succession.
- **S6** — [Global Industrial Company 2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/945114/000162828026012945/gic-20251231.htm) (accessed 2026-07-22): Distributor channel competition, customer buying criteria, service model, and workforce composition: 36% customer-facing, 26% distribution and fulfillment, and 37% administrative.
- **S7** — [Illinois Tool Works 2025 Annual Report](https://www.sec.gov/Archives/edgar/data/49826/000119312526127630/2026_ars_filing.pdf) (accessed 2026-07-22): Commercial food-equipment products and integrated service model, including installation, annual service contracts, maintenance, repair, parts, and customer acceptance.
- **S8** — [The Middleby Corporation 2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/769520/000076952026000011/midd-20260103.htm) (accessed 2026-07-22): Commercial foodservice equipment demand proxy: 2025 sales decreased 1.7% excluding acquisition and currency effects, with weaker chain traffic and replacement demand cited.
- **S9** — [2022 NAICS definition: 423440 Other Commercial Equipment Merchant Wholesalers](https://www.census.gov/naics/?input=423440&year=2022&details=423440) (accessed 2026-07-22): Official scope of merchant wholesale distribution of commercial machines and equipment generally used in restaurants and stores.
