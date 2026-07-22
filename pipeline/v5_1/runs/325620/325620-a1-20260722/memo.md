# 325620 — Toilet Preparation Manufacturing

*v5.1 Stage 1 research memo. Run `325620-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 6.61 · L 0.91 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Repeat physical consumption plus document-intensive formulation and compliance workflows creates a usable AI opportunity.
**Weakness:** Contract repricing and extreme business-model heterogeneity can erode retention and comparability.

## Business-model lens
- Included: Independent LMM manufacturers and contract manufacturers that repeatedly formulate, blend, fill, package, and support perfumes, hair and skin preparations, lotions, sunscreens, and other cosmetics for external brands or channels.
- Excluded: Brand-only marketers with no operating manufacturing service, captive plants, shell entities, distributors, and firms outside the EBITDA band.
- Customer and revenue model: Repeat B2B contract-manufacturing and private-label revenue, plus repeat wholesale sales of owned formulations, with formulation, compliance, testing, filling, and packaging support.
- Deviation from default lens: The industry mixes consumer-brand product companies and outsourced contract manufacturers. The lens retains manufacturers with recurring external B2B production or repeat wholesale relationships and excludes brand-only marketing entities so operator economics remain coherent.

## Executive view
This is a sizable but heterogeneous LMM field combining physical repeat manufacturing with knowledge-heavy formulation, compliance, customer, and brand workflows. AI opportunity is meaningful, while value capture depends strongly on whether the target owns differentiated formulations or faces procurement-led contract pricing.

## How AI changes the work
Likely uses include label and claims checking, product-listing preparation, safety-document retrieval, formulation and ingredient search, demand planning, customer support, quoting, artwork variants, and quality trend analysis. Mixing, filling, laboratory testing, sanitation, maintenance, warehousing, and final release remain operator-led.

## Value capture
Formulation know-how, reliable regulatory execution, speed, and switching costs protect part of the savings. Large brands and retailers can re-bid contracts or demand price concessions, while owned brands may retain more but bear marketing and fashion risk.

## Firm availability
The injected population is relatively large, but genuine eligibility requires operating manufacturing, repeat external revenue, compliance maturity, and transferable customer relationships. Founder-centric brands and marketing shells should not be treated like contract manufacturers.

## Demand durability
The underlying service produces consumable physical goods and is resistant to software elimination. Demand should be broadly durable, though category cycles, channel shifts, imports, and rapid SKU turnover create meaningful target-level variance.

## Risks and uncertainty
Business-model heterogeneity is the largest analytical risk. Other uncertainties include current software adoption, customer concentration, retailer power, product liability, claims compliance, safety substantiation, SKU economics, and whether estimated firms are truly in the EBITDA band.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1285 | — | OBSERVED | — |
| n | — | 186 | — | ESTIMATE | — |
| a | 0.2 | 0.31 | 0.43 | PROXY | S1, S2 |
| rho | 0.4 | 0.57 | 0.73 | ESTIMATE | S3, S4, S5 |
| e | 0.5 | 0.68 | 0.82 | ESTIMATE | S2, S3 |
| s5 | 0.14 | 0.24 | 0.36 | PROXY | S6 |
| q | 0.43 | 0.6 | 0.76 | ESTIMATE | S2, S4 |
| d5 | 0.96 | 1.08 | 1.22 | ESTIMATE | S2, S4 |
| o | 0.87 | 0.94 | 0.98 | ESTIMATE | S2, S3, S5 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.41 | 0.91 | 1.61 | ESTIMATE |
| F | 4.25 | 5.54 | 6.47 | ESTIMATE |
| C | 8.60 | 10.00 | 10.00 | ESTIMATE |
| D | 8.35 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: Public occupation data are broader than 325620.
- a: Business-model mix drives large dispersion.
- rho: Regulatory sources establish workflow requirements, not adoption rates.
- rho: Generative outputs need qualified review.
- e: The supplied firm count is margin-bridged and estimated.
- e: FDA registration does not prove LMM size, independence, or external recurring revenue.
- s5: Economy-wide demographic proxy.
- s5: No public five-year transfer denominator for this code.
- q: No public contract sample measures automation pass-through.
- q: Owned-brand and contract-manufacturing economics differ sharply.
- d5: Official sources define products and requirements but do not forecast real demand.
- d5: Category growth and product lifecycles vary widely.
- o: Operator share may migrate among domestic contract manufacturers, brands, and foreign suppliers.
- o: This is not an employment-retention estimate.

## Sources
- **S1** — [Chemical Manufacturing: NAICS 325](https://www.bls.gov/iag/tgs/iag325.htm) (accessed 2026-07-22): BLS includes Soap, Cleaning Compound, and Toilet Preparation Manufacturing (3256) in its industry overview and provides common-occupation context.
- **S2** — [NAICS 325620 Toilet Preparation Manufacturing](https://www.census.gov/naics/?details=325620&input=325620&year=2017) (accessed 2026-07-22): Census defines the industry as preparing, blending, compounding, and packaging products including perfumes, shaving and hair preparations, creams, lotions, sunscreens, and cosmetics.
- **S3** — [Registration & Listing of Cosmetic Product Facilities and Products](https://www.fda.gov/cosmetics/registration-listing-cosmetic-product-facilities-and-products) (accessed 2026-07-22): FDA describes Cosmetics Direct data entry, validation, and submission workflows for facility registration and cosmetic product listing.
- **S4** — [Cosmetics Labeling](https://www.fda.gov/cosmetics/cosmetics-labeling) (accessed 2026-07-22): FDA states labeling is important to market entry and regulated under the FD&C Act and Fair Packaging and Labeling Act, while firms remain responsible for product safety.
- **S5** — [Product Testing of Cosmetics](https://www.fda.gov/cosmetics/cosmetics-science-research/product-testing-cosmetics) (accessed 2026-07-22): FDA states cosmetics must be safe under labeled or customary use and that it can act when reliable information shows a product does not meet safety requirements.
- **S6** — [2024 Firms in Focus chartbooks on small business data](https://www.fedsmallbusiness.org/reports/survey/2024/2024-small-business-data-chartbooks) (accessed 2026-07-22): Federal Reserve chartbooks include firm breakdowns by owner demographics and an age-of-owner chartbook, used as broad succession evidence.
