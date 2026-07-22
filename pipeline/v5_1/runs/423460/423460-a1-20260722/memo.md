# 423460 — Ophthalmic Goods Merchant Wholesalers

*v5.1 Stage 1 research memo. Run `423460-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 5.27 · L 1.00 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** High-penetration, recurring vision-correction purchases create repeat information, fulfillment, and support workflows that AI can streamline.
**Weakness:** Integrated optical and direct channels can preserve end demand while eliminating the independent wholesaler from the value chain.

## Business-model lens
- Included: Independent lower-middle-market ophthalmic goods distributors that repeatedly provide external optometry, ophthalmology, optical-retail, institutional, or consumer-channel customers with outsourced inventory, prescription-order fulfillment, product and frame curation, tracing or recall support, returns, practice support, or equipment-related service.
- Excluded: Product-only frame or lens wholesalers without a recurring or repeat outsourced service, lens and frame manufacturers, optical laboratories classified as manufacturing, integrated retailers' captive units, eye-care practices, marketplaces, shells, and non-control financing vehicles.
- Customer and revenue model: Customers buy frames, lenses, contact lenses, instruments, accessories, and replenishment at distribution margins; eligible firms layer repeat fulfillment, inventory, prescription workflow, customer support, returns, traceability, curation, or equipment support onto those sales.
- Deviation from default lens: The small code mixes commodity replenishment, fashion frames, prescription products, instruments, and product-only wholesalers. It is narrowed to firms with a material repeat or recurring outsourced-service obligation so merchant resale is not mistaken for service delivery.

## Executive view
The defensible subset is a small group of ophthalmic distributors with real fulfillment, inventory, prescription-workflow, practice-support, or equipment-service obligations. Demand for vision correction is recurrent, but the independent wholesale channel faces unusually strong integrated, online, and supplier-concentrated alternatives.

## How AI changes the work
AI can improve product and frame search, catalog enrichment, quote and order capture, prescription-data validation support, reorder prediction, return authorization, customer response, purchasing exceptions, and back-office reconciliation. Humans remain needed for quality control, exception resolution, physical fulfillment, instrument work, sensitive customer issues, and accountability for prescribed-product errors.

## Value capture
Savings are most retainable in internal overhead and contracted fulfillment or service. Standard contacts, frames, and lenses are transparent and competitively shopped, so online sellers, integrated players, suppliers, and optical customers are likely to capture part of any productivity gain.

## Firm availability
The frozen LMM population is only 95 firms and includes product-only wholesalers that fail the lens. Broad owner-age evidence suggests succession potential, but the eligible count and control-transfer rate are not observed and are highly sensitive to a few firms.

## Demand durability
Vision correction has high penetration and frequent replacement, while aging increases vision needs. The concern is channel durability rather than end demand: retail chains, manufacturers, captive labs, and direct-to-consumer platforms can internalize or bypass independent wholesale functions.

## Risks and uncertainty
Principal risks include supplier concentration, brand and fashion cycles, online price competition, prescription and recordkeeping errors, inventory obsolescence, customer concentration, retailer integration, and a very small acquisition universe. Proxy evidence is much stronger on consumer eyewear need than on independent distributor service economics.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1687 | — | OBSERVED | — |
| n | — | 95 | — | ESTIMATE | — |
| a | 0.17 | 0.29 | 0.42 | PROXY | S1, S2, S3 |
| rho | 0.31 | 0.51 | 0.69 | ESTIMATE | S3, S8 |
| e | 0.07 | 0.19 | 0.36 | ESTIMATE | S6, S7, S10 |
| s5 | 0.1 | 0.18 | 0.29 | PROXY | S4, S5 |
| q | 0.32 | 0.53 | 0.72 | ESTIMATE | S6, S7 |
| d5 | 0.97 | 1.09 | 1.23 | PROXY | S6, S9, S11 |
| o | 0.49 | 0.71 | 0.87 | ESTIMATE | S7, S8 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.36 | 1.00 | 1.96 | ESTIMATE |
| F | 0.82 | 2.33 | 3.85 | ESTIMATE |
| C | 6.40 | 10.00 | 10.00 | ESTIMATE |
| D | 4.75 | 7.74 | 10.00 | ESTIMATE |

## Caveats
- a: BLS occupation data are at 423400, not 423460.
- a: General AI research measures exposure or use rather than economically removable labor.
- a: The service-rich subset may have a different labor mix from the full six-digit code.
- rho: No representative implementation study for 423460 was found.
- rho: Contact-lens rules do not govern all ophthalmic goods.
- rho: Small firms may lack the data quality and integrations needed for high implementation.
- e: The frozen n is margin-bridged from broad distributor economics and is only ESTIMATE quality.
- e: Retail filings illustrate channels and outsourced fulfillment but not the prevalence of eligible independent wholesalers.
- e: Repeat delivery alone is insufficient without an outsourced-service component.
- s5: Broad and demographic-subgroup age data do not observe transaction timing.
- s5: No six-digit deal denominator was found.
- s5: With only 95 frozen-band firms, a few events materially change the rate.
- q: Retailer filings are directional channel evidence, not direct measures of wholesaler benefit retention.
- q: Fashion frames and prescribed contacts have different pricing dynamics.
- q: Supplier rebates, exclusivity, and private-label terms can dominate operating savings.
- d5: Warby Parker market estimates come from an interested retailer and cover consumer eyewear rather than six-digit wholesale output.
- d5: Vision impairment prevalence is not the same as purchases of corrective goods.
- d5: Integrated labs, retailer consolidation, and direct channels can disconnect end demand from wholesaler demand.
- o: The lens selects service-bearing firms, which raises operator dependence relative to the full code.
- o: Operator-required demand can persist while moving away from firms of the lens's kind.
- o: Automation of prescription verification may reduce labor without eliminating seller responsibility.

## Sources
- **S1** — [Data tables for OEWS industry charts, May 2024](https://www.bls.gov/oes/2024/may/ind_emp_chart/ind_emp_chart_data.htm) (accessed 2026-07-22): Observed largest occupations and counts for the broader NAICS 423400 industry, used to anchor the labor-mix proxy.
- **S2** — [GPTs are GPTs: An early look at the labor market impact potential of large language models](https://openai.com/index/gpts-are-gpts/) (accessed 2026-07-22): General U.S. task-exposure benchmark: about 80% of workers could have at least 10% of tasks affected and 19% could have at least 50% affected.
- **S3** — [The Anthropic Economic Index](https://www.anthropic.com/news/the-anthropic-economic-index) (accessed 2026-07-22): Observed Claude task-use evidence, including 57% augmentation and 43% automation, with explicit representativeness caveats.
- **S4** — [Business Owners' Ages](https://www.census.gov/content/dam/Census/library/visualizations/2020/comm/business-owners-ages.pdf) (accessed 2026-07-22): 2019 Annual Business Survey graphic reporting 51% of responding employer-business owners were age 55 or older.
- **S5** — [The Metamorphosis of Women Business Owners: A Focus on Age](https://www2.census.gov/ces/wp/2024/CES-WP-24-71.pdf) (accessed 2026-07-22): Census evidence that older employer owners are prominent in wholesale trade, used only as a succession proxy.
- **S6** — [Warby Parker Inc. 2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/1504776/000150477626000006/wrby-20251231.htm) (accessed 2026-07-22): Eyewear-market size, vision-correction penetration, replenishment frequency, contact-lens recurrence, competitive channels, independent-retailer share, and supply-chain structure.
- **S7** — [National Vision Holdings, Inc. 2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/1710155/000162828026014379/eye-20260103.htm) (accessed 2026-07-22): Third-party contact-lens fulfillment, centralized laboratory operations, and supplier concentration including 96% of contact-lens spend across three vendors and 86% of lens spend with one vendor.
- **S8** — [The Contact Lens Rule: A Guide for Prescribers and Sellers](https://www.ftc.gov/business-guidance/resources/contact-lens-rule-guide-prescribers-sellers) (accessed 2026-07-22): Seller prescription-verification procedures, required request information, eight-business-hour response framework, prohibited practices, and three-year recordkeeping.
- **S9** — [Vision Impairment and Chronic Health Conditions](https://www.cdc.gov/vision-health/php/chronic-conditions-vision/index.html) (accessed 2026-07-22): CDC finding that 13.6% of national survey respondents age 65 or older reported vision impairment and that aging is expected to increase the public-health burden.
- **S10** — [2022 NAICS definition: 423460 Ophthalmic Goods Merchant Wholesalers](https://www.census.gov/naics/?input=423460&year=2022&details=423460) (accessed 2026-07-22): Official industry classification scope anchoring the merchant-wholesale population and narrower service-bearing lens.
- **S11** — [Taking Care of Your Eyes](https://www.cdc.gov/vision-health/prevention/taking-care-of-your-eyes.html) (accessed 2026-07-22): CDC evidence that refractive errors are common, an estimated 11 million Americans age 12 or older could see better with corrective lenses or surgery, and older adults have greater vision needs.
