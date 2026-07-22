# 561730 — Landscaping Services

*v5 Stage 1 research memo. Run `561730-a1-20260722`, model `gpt-5.6-terra`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 7.13 · L 0.92 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Recurring outsourced maintenance demand combined with attainable AI support for estimating, dispatch, customer service, and administration.
**Weakness:** Most labor is site-specific physical work, sharply limiting direct AI substitution and leaving key values dependent on estimates rather than industry-matched measurements.

## Business-model lens
- Included: US lower-middle-market firms in NAICS 561730 providing externally purchased recurring lawn, grounds, tree, irrigation, snow, and landscape-maintenance services, plus repeat work for commercial and residential customers.
- Excluded: Captive property-maintenance units, pure landscape architecture, landscape-material retail, one-off construction-only work without a repeat outsourced-service relationship, shells, and financing vehicles.
- Customer and revenue model: Commercial and residential customers, principally route-based or contracted maintenance with project and seasonal add-on work; repeat outsourced service is required by the lens.
- Deviation from default lens: none

## Executive view
Landscaping Services is a physical, locally delivered service with a substantial base of repeat maintenance revenue, but its AI opportunity is concentrated in the smaller administrative and supervisory portion of the cost base rather than in field crews.

## How AI changes the work
OEWS reports landscaping and groundskeeping workers at 60.88% of NAICS employment, and O*NET's listed work is predominantly mowing, pruning, planting, spraying, irrigation, and equipment operation. AI is therefore most relevant to estimating, scheduling, routing support, customer communication, documentation, bookkeeping, and supervisory planning.

## Value capture
Recurring maintenance contracts can preserve some back-office productivity during a term, but local bid competition and renewal repricing should share a material portion with customers. Field labor should not be counted as broadly substitutable AI value.

## Firm availability
BizBuySell documents a transaction channel: its benchmark page analyzes 945 sold landscaping and yard-service listings and its 2025 sector table reports 173 transactions. Those data are substantially smaller than the frozen LMM band, so they indicate transferability without measuring the qualifying transfer rate.

## Demand durability
The physical service remains needed at homes, commercial properties, institutions, and green spaces. BLS projects 4% growth in grounds-maintenance employment from 2024 to 2034 and cites homeowner, institutional, and urban-green-space demand, though this is an occupational proxy rather than a real-output forecast.

## Risks and uncertainty
Seasonality, weather, local labor availability, pesticide rules, fragmented field data, and nonrecurring installation revenue can weaken implementation and retention. Marketplace transaction statistics do not match the frozen EBITDA band, and no source directly measures AI adoption, contractual pass-through, or repeat-service revenue share for LMM NAICS 561730 firms.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.4087 | — | OBSERVED | — |
| n | — | 593 | — | ESTIMATE | — |
| a | 0.08 | 0.14 | 0.22 | ESTIMATE | S1, S2 |
| rho | 0.25 | 0.4 | 0.55 | ESTIMATE | S2, S4 |
| e | 0.55 | 0.75 | 0.85 | ESTIMATE | S3 |
| s5 | 0.2 | 0.35 | 0.5 | ESTIMATE | S3, S5 |
| q | 0.45 | 0.6 | 0.75 | ESTIMATE | S3 |
| d5 | 0.99 | 1.02 | 1.05 | PROXY | S4 |
| o | 0.85 | 0.93 | 0.97 | ESTIMATE | S2, S4 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.33 | 0.92 | 1.98 | ESTIMATE |
| F | 6.75 | 8.13 | 8.90 | ESTIMATE |
| C | 9.00 | 10.00 | 10.00 | ESTIMATE |
| D | 8.41 | 9.49 | 10.00 | ESTIMATE |

## Caveats
- a: OEWS employment shares are a 2023 establishment survey rather than payroll shares and include work outside the frozen repeat-service subset.
- a: Task lists do not measure task time or AI technical performance.
- rho: No source measures five-year AI implementation in the frozen LMM population.
- rho: Licensing varies by state and task.
- e: BizBuySell's marketplace category is not the NAICS universe or the injected EBITDA band.
- e: Recurring revenue does not by itself prove transferable operations or customer-contract assignability.
- s5: The reported transactions have median revenue of $755,359 and median cash flow of $201,392, below the frozen LMM EBITDA band, so they cannot produce a direct transfer rate.
- s5: Marketplace data undercount off-market and larger brokered sales and include an unknown listing-selection effect.
- q: No cited source reports contractual pass-through or post-AI pricing for this industry.
- q: Commercial and residential pricing behavior can differ sharply by local market.
- d5: The source covers the broader occupation and a ten-year horizon, not the specific LMM repeat-service lens.
- d5: Employment demand is not identical to service-quantity demand when equipment productivity or staffing intensity changes.
- o: The task evidence is occupational and does not quantify future robotics adoption.
- o: The assessment excludes demand growth, which is represented separately in d5.

## Sources
- **S1** — [BLS May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 561730](https://www.bls.gov/oes/2023/may/naics5_561730.htm) (accessed 2026-07-22): Reports 915,720 total NAICS 561730 employment; 76.87% in building and grounds cleaning and maintenance occupations; 60.88% in landscaping and groundskeeping workers; and 6.70% in office and administrative support occupations.
- **S2** — [O*NET Job Duties: Landscaping and Groundskeeping Workers](https://www.onetonline.org/search/task/choose/37-3011.00) (accessed 2026-07-22): Lists field tasks including hand-tool and powered-equipment use, watering, pruning, spraying, lawn care, planting, mowing, irrigation maintenance, snow removal, and repairs.
- **S3** — [BizBuySell Landscaping and Yard Service Business Valuation Multiples and Financial Benchmarks](https://www.bizbuysell.com/learning-center/valuation-benchmarks/landscaping-yard-service/) (accessed 2026-07-22): States that most listed and sold businesses rely on yard maintenance for consistent recurring revenue; reports 945 sold listings analyzed, 2025 median revenue of $755,359 and owner earnings of $201,392, and transaction benchmarks for 2021 through 2025.
- **S4** — [BLS Occupational Outlook Handbook: Grounds Maintenance Workers](https://www.bls.gov/ooh/building-and-grounds-cleaning/grounds-maintenance-workers.htm) (accessed 2026-07-22): Projects 4% grounds-maintenance employment growth from 2024 to 2034 and attributes need for landscaping and groundskeeping workers to demand from homeowners, institutions, and urban green spaces; describes physical outdoor duties and pesticide-application licensing.
- **S5** — [BizBuySell Insight Report Data Tables](https://www.bizbuysell.com/insight-report-data-tables/) (accessed 2026-07-22): The full-year 2025 sector table reports 173 landscaping and yard-service transactions, with $755,359 average revenue and $201,392 median cash flow in the displayed row.
