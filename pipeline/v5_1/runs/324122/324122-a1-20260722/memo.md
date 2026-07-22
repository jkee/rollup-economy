# 324122 — Asphalt Shingle and Coating Materials Manufacturing

*v5.1 Stage 1 research memo. Run `324122-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 4.71 · L 0.45 · interval STRUCTURAL_OUT → STRUCTURAL_OUT · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Continuous, data-rich production lines create repeatable opportunities in inspection, maintenance, scheduling, yield, and service administration.
**Weakness:** Nearly all industry revenue is product manufacturing rather than recurring outsourced service, leaving few plausible LMM eligible firms.

## Business-model lens
- Included: US lower-middle-market manufacturers of asphalt shingles, roll roofing, saturated felts, roof and waterproofing coatings, and related asphalt materials that serve recurring external distributors, contractors, private-label customers, or genuine contract-manufacturing accounts.
- Excluded: Roofing installation contractors, building-material distributors, captive internal manufacturing units, integrated plants outside the EBITDA band, shells, and non-control financing vehicles.
- Customer and revenue model: Primarily per-unit, bundle, roll, gallon, or truckload product sales through distributors and contractor channels; qualifying outsourced-service revenue is limited to private-label or contract manufacturing with repeat external customers.
- Deviation from default lens: none

## Executive view
Asphalt roofing materials offer practical AI applications in quality inspection, maintenance, planning, forecasting, and administration, but most businesses are manufacturers of branded products rather than outsourced-service providers. The likely eligible contract-manufacturing subset is small, and physical production keeps direct labor substitution bounded.

## How AI changes the work
AI can detect surface and dimensional defects, predict line failures, optimize schedules and changeovers, forecast demand, support formulation analysis, reconcile production records, and automate routine distributor service. Hot-material handling, maintenance, environmental control, laboratory release, packaging equipment, and warranty accountability remain operator-led.

## Value capture
Differentiated brands, reliable supply, and warranties can retain some gains, while private-label bids, distributor concentration, retailer negotiations, transparent asphalt inputs, rebates, and competition pass savings through. Contract manufacturers are likely to face faster repricing than branded producers.

## Firm availability
The frozen count should be screened aggressively rather than treated as an addressable target list. Only recurring private-label, toll, or contract manufacturing clearly fits the service lens, and every candidate needs verification of ownership, permits, warranties, environmental exposure, customer concentration, and normalized EBITDA.

## Demand durability
Replacement of aging and storm-damaged roofs supports recurring demand, while new housing and commercial construction add cyclicality. Competing materials, building codes, insurance practices, interest rates, and product longevity can shift quantity, but remaining physical roofing demand continues to require accountable manufacturing.

## Risks and uncertainty
Key risks are service-lens ineligibility, firm-count error, branded-market concentration, distributor power, raw-material volatility, warranty and product-liability claims, environmental compliance, plant scale, housing cyclicality, and substitution toward other roofing systems.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1015 | — | OBSERVED | — |
| n | — | 49 | — | ESTIMATE | — |
| a | 0.1 | 0.2 | 0.33 | PROXY | S1, S2 |
| rho | 0.35 | 0.55 | 0.72 | ESTIMATE | S1, S3 |
| e | 0.03 | 0.11 | 0.26 | ESTIMATE | S1, S3 |
| s5 | 0.07 | 0.14 | 0.24 | PROXY | S4 |
| q | 0.22 | 0.4 | 0.6 | ESTIMATE | S1, S3 |
| d5 | 0.86 | 0.99 | 1.12 | PROXY | S5 |
| o | 0.9 | 0.96 | 0.99 | ESTIMATE | S1, S3 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.14 | 0.45 | 0.96 | ESTIMATE |
| F | 0.16 | 0.90 | 2.25 | ESTIMATE |
| C | 4.40 | 8.00 | 10.00 | ESTIMATE |
| D | 7.74 | 9.50 | 10.00 | ESTIMATE |

## Caveats
- a: No six-digit occupational or task dataset was located.
- a: Coatings plants and high-speed shingle lines have different labor mixes, making an industry aggregate imprecise.
- rho: Process digitization indicates feasibility but does not measure AI implementation success.
- rho: Warranty and product-liability risk can keep human approval in place even when models perform well.
- e: The frozen firm count is an ESTIMATE and the paper/forest-products margin bridge may not match roofing-product economics.
- e: Repeat distributor sales remain product revenue and do not automatically satisfy the outsourced-service lens.
- s5: Gallup is neither industry- nor size-specific and measures intentions rather than consummated transfers.
- s5: A plant acquisition by a strategic manufacturer may be an asset purchase rather than a qualifying firm control transfer.
- q: No representative contracts or pass-through study were located.
- q: Brand strength and channel concentration can move retention far outside the industry range.
- d5: No current public six-digit shipment forecast or reroofing-volume series was located.
- d5: Storm incidence, insurance practices, housing turnover, interest rates, and material substitution can materially shift demand.
- o: An accountable manufacturer can remain necessary while production consolidates into large firms outside the lens.
- o: Operator requirement does not imply current labor intensity or preserve independent contract-manufacturer demand.

## Sources
- **S1** — [AP-42 Chapter 11.2: Asphalt Roofing](https://nepis.epa.gov/Exe/ZyPURL.cgi?Dockey=P100RGXZ.TXT) (accessed 2026-07-22): Describes asphalt roofing products and six main operations: felt saturation, coating, mineral surfacing, cooling and drying, finishing including cutting and laminating, and packaging, plus asphalt, filler, and granule support operations.
- **S2** — [Petroleum and Coal Products Manufacturing: NAICS 324](https://www.bls.gov/iag/tgs/iag324.htm) (accessed 2026-07-22): Provides broader-subsector occupational context, including 5,230 mixing and blending machine setters, operators, and tenders and 4,980 first-line production supervisors in 2025.
- **S3** — [Asphalt Processing and Asphalt Roofing Manufacture: New Source Performance Standards](https://www.epa.gov/stationary-sources-air-pollution/asphalt-processing-and-asphalt-roofing-manufacture-new-source) (accessed 2026-07-22): States that asphalt processing and roofing manufacture significantly contribute to air pollution and requires new, modified, and reconstructed facilities to use demonstrated continuous-emission-reduction systems.
- **S4** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Fall 2024 US survey found 22% of employer-business owners planned to sell or transfer ownership within five years, while 5% planned closure and 5% had no plan.
- **S5** — [Monthly New Residential Construction, May 2026](https://www.census.gov/construction/nrc/current/) (accessed 2026-07-22): Reports May 2026 privately owned housing starts at a seasonally adjusted annual rate of 1.177 million, 8.7% below May 2025, and building permits at 1.413 million.
