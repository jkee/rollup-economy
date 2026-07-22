# 524291 — Claims Adjusting

*v5.1 Stage 1 research memo. Run `524291-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** PRIORITY · A 7.96 · L 5.65 · interval CONDITIONAL → HIGHEST_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** High-volume claims workflows contain many structured cognitive tasks while severe and complex losses preserve a need for accountable human operators.
**Weakness:** Carrier-controlled automation can disintermediate vendors on routine claims and use procurement leverage to capture much of the remaining efficiency benefit.

## Business-model lens
- Included: US lower-middle-market independent adjusting firms that repeatedly investigate, appraise, document, negotiate, and settle claims for insurance carriers, self-insured organizations, or their administrators.
- Excluded: Carrier-employed or captive adjusting units, public adjusters representing policyholders on contingency economics, pure third-party claims administrators classified in 524292, shell entities, non-control financing vehicles, and firms outside the approximately $1–10M normalized EBITDA band.
- Customer and revenue model: Carriers, self-insured organizations, and administrators outsource daily, specialty, field, desk, or catastrophe adjusting under per-claim, fee-schedule, daily-rate, time-and-expense, or managed-service arrangements.
- Deviation from default lens: Narrowed to insurer-side and self-insured outsourced adjusting because public adjusters represent claimants under materially different contingency-fee incentives and customer acquisition economics; combining the models would make commercial retention and operator-required demand incoherent.

## Executive view
Independent adjusting has substantial document, image, estimation, and workflow exposure, and carrier clients are already exploring the relevant technologies. The opportunity is constrained because the same tools can let carriers or policyholders bypass outside adjusters on routine claims, while carrier procurement can reclaim savings.

## How AI changes the work
AI can extract loss documents, summarize files and interviews, analyze damage imagery, suggest estimates and reserves, screen fraud, draft correspondence, and automate quality checks. Human operators remain central for field facts, ambiguity, severe exposure, negotiation, litigation, exceptions, and accountable settlement decisions.

## Value capture
Fixed per-claim and fee-schedule arrangements can preserve some productivity gains, but time-based work cannot. Large carrier customers can reset fees, demand service improvements, or shift claims in-house as technology matures.

## Firm availability
The insurer-side independent-adjusting lens likely covers a majority, but not all, of the supplied LMM population. Broader insurance-services M&A confirms buyer activity without establishing a claims-adjusting transfer rate; public-adjuster and owner-dependent firms are material exclusions.

## Demand durability
Loss investigation and settlement remain necessary, and complex or physical claims continue to need accountable field and negotiation capability. Routine claims face straight-through processing, self-service, carrier internalization, and image-based estimation; catastrophes add both durable need and sharp volume volatility.

## Risks and uncertainty
The largest uncertainties are claim-mix segmentation, carrier versus vendor control of technology and data, fee-model mix, regulatory and litigation exposure, catastrophe cyclicality, contractor dependence, customer concentration, and the absence of claims-adjusting-specific M&A and eligibility data. A firm concentrated in routine desk claims could be structurally impaired rather than merely made more efficient.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.6871 | — | OBSERVED | — |
| n | — | 217 | — | ESTIMATE | — |
| a | 0.42 | 0.6 | 0.75 | PROXY | S2, S3 |
| rho | 0.48 | 0.72 | 0.88 | PROXY | S4 |
| e | 0.55 | 0.75 | 0.9 | ESTIMATE | S1 |
| s5 | 0.1 | 0.2 | 0.32 | ESTIMATE | S5 |
| q | 0.3 | 0.5 | 0.68 | ESTIMATE | — |
| d5 | 0.87 | 0.97 | 1.1 | PROXY | S3 |
| o | 0.42 | 0.64 | 0.82 | ESTIMATE | S2, S3, S4 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 5.54 | 10.00 | 10.00 | PROXY |
| F | 4.12 | 5.65 | 6.68 | ESTIMATE |
| C | 6.00 | 10.00 | 10.00 | ESTIMATE |
| D | 3.65 | 6.21 | 9.02 | ESTIMATE |

## Caveats
- a: Occupation data span employers and claim types outside the narrowed lens and do not provide task time shares.
- a: Catastrophe, auto, property, liability, and specialty workflows have very different automation ceilings.
- a: Existing carrier automation may already have removed some easy tasks before work reaches an independent firm.
- rho: The NAIC percentages combine use, plans, and exploration and are not workflow implementation rates.
- rho: The source population is insurers rather than independent adjusting firms.
- rho: Regulatory acceptance and contractual audit requirements vary by state, line, and decision type.
- e: No source measures the insurer-side outsourced share within the supplied LMM firm estimate.
- e: Establishment classifications may not cleanly distinguish public adjusting, independent adjusting, and claims administration.
- e: The supplied count is estimated and may be sensitive to margin assumptions and multi-establishment structures.
- s5: The cited M&A category is much broader than NAICS 524291 and is not a direct transfer-rate observation.
- s5: Small private sales and internal successions may be missing, while platform add-ons may be overrepresented.
- s5: No observed owner-age distribution is available for the narrowed lens.
- q: No public source quantifies billing-model mix or benefit pass-through for independent adjusting firms.
- q: Catastrophe surge pricing and routine daily claims can have opposite retention economics.
- q: Carrier concentration and rebid frequency vary widely by firm.
- d5: Employment is not constant-price, constant-quality demand and spans carrier staff, government, and other employers.
- d5: The occupational forecast embeds productivity and substitution effects that conceptually overlap with operator requirement.
- d5: Catastrophe frequency and severity make year-five volume unusually volatile.
- o: The narrowed LMM vendor mix may skew toward difficult claims and therefore retain operators more than the overall occupation.
- o: Carrier adoption evidence does not reveal whether technology complements vendors or disintermediates them.
- o: Legal accountability, licensing, and physical inspection requirements vary across jurisdictions and claim types.

## Sources
- **S1** — [North American Industry Classification System: Sector 52](https://www.census.gov/naics/resources/archives/sect52.html) (accessed 2026-07-22): Defines 524291 as establishments primarily engaged in investigating, appraising, and settling insurance claims and distinguishes third-party administration.
- **S2** — [O*NET OnLine: Claims Adjusters, Examiners, and Investigators](https://www.onetonline.org/link/details/13-1031.00) (accessed 2026-07-22): Lists coverage and file review, data verification, investigation, interviews, payment and reserve entry, damage estimation, complex-claim resolution, litigation coordination, and evidence handling.
- **S3** — [BLS Occupational Outlook Handbook: Claims Adjusters, Appraisers, Examiners, and Investigators](https://www.bls.gov/ooh/business-and-financial/claims-adjusters-appraisers-examiners-and-investigators.htm) (accessed 2026-07-22): Reports a 5% 2024–2034 employment decline and 21,600 annual openings, documents office and field work, and explains that image-evaluation software and AI raise productivity while disasters influence demand.
- **S4** — [NAIC: Artificial Intelligence](https://content.naic.org/insurance-topics/artificial-intelligence) (accessed 2026-07-22): Reports insurer use, planning, or exploration of AI or machine learning in 88% of surveyed auto insurers, 70% of home insurers, and 92% of health insurers; identifies claims uses including accident-image analysis, settlement-value estimation, and fraud detection and describes governance expectations.
- **S5** — [OPTIS Partners: Year-End 2025 Agent and Broker M&A Report](https://optisins.com/wp/wp-content/uploads/2026/01/Year-End-2025-MA-Report-2.pdf) (accessed 2026-07-22): Reports 695 announced North American insurance-distribution and related-service deals in 2025, including 640 retail, wholesale, and TPA transactions, but does not isolate claims adjusting.
