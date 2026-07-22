# 512199 — Other Motion Picture and Video Industries

*v5.1 Stage 1 research memo. Run `512199-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 6.46 · L 0.31 · interval STRUCTURAL_OUT → STRUCTURAL_OUT · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Fragile physical media and preservation-grade capture requirements keep specialized outsourced laboratories relevant even as digital workflow stages automate.
**Weakness:** The addressable lower-middle-market population is extremely small and classification uncertainty can remove much of it before transfer probability is considered.

## Business-model lens
- Included: U.S. lower-middle-market motion-picture film laboratories and film-preservation service firms that repeatedly provide external archives, studios, libraries, museums, government bodies, rights owners, and producers with inspection, stabilization, cleaning, repair, scanning, laboratory processing, digitization, restoration, preservation masters, access copies, and exhibition or distribution derivatives.
- Excluded: Stock-footage libraries and pure footage licensors, captive archive departments, public repositories performing work only in-house, teleproduction and postproduction services classified in 512191, production, distribution, exhibition, sound studios, mass duplication, storage-only providers, independent freelancers without a transferable operating firm, and shell entities.
- Customer and revenue model: Customers buy project-based preservation and laboratory work, collection batches, multi-phase digitization programs, restoration engagements, repeat access or exhibition derivatives, and occasional custody or managed-file services. Fees are commonly based on footage, format, condition, capture specification, labor, deliverables, storage, and special handling.
- Deviation from default lens: The code combines film laboratories and preservation services with stock-footage libraries. The screen retains laboratory and preservation firms because they supply an outsourced service, and excludes footage libraries because rights and asset licensing is a different business model that would make one set of primitives incoherent.

## Executive view
The residual code is heterogeneous, so the coherent outsourced-service lens is film laboratory and preservation work rather than stock-footage licensing. Physical media risk and specialized capture sustain operator demand, while the tiny supplied firm count makes market availability the dominant uncertainty.

## How AI changes the work
AI can assist metadata creation, catalog search, defect detection, restoration suggestions, routine color and audio cleanup, quality-control triage, derivative generation, and administration. Humans remain necessary for physical inspection, cleaning, repair, scanning, chemistry, calibration, custody, archival judgment, authenticity, and final preservation quality.

## Value capture
Per-footage and project bids allow initial retention of digital-stage efficiencies. Institutional tenders, grant constraints, customer demands for higher quality, specialist software and compute, managed storage, and mandatory review push part of the benefit into price or scope.

## Firm availability
The code contains only a few dataset-estimated LMM firms and mixes service providers with footage libraries. Eligibility and transfer flow are therefore fragile to classification, margin assumptions, ownership, and whether a transaction preserves a functioning specialist team and facility.

## Demand durability
Deterioration, obsolete playback equipment, access needs, and preservation standards support continuing digitization and restoration. Demand remains lumpy because budgets are institutional, backlogs are finite, and some large archives can build internal capacity.

## Risks and uncertainty
The largest risks are the residual-code business-model mix, a three-firm dataset estimate, the generic margin bridge, broad occupation data, scarce transaction evidence, project and grant cycles, obsolete equipment, key-person dependence, archive insourcing, and uncertain productivity from AI under preservation-grade review.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.862 | — | OBSERVED | — |
| n | — | 3 | — | ESTIMATE | — |
| a | 0.22 | 0.38 | 0.58 | PROXY | S1, S2, S3, S4 |
| rho | 0.3 | 0.52 | 0.72 | PROXY | S3, S4, S6 |
| e | 0.28 | 0.5 | 0.72 | ESTIMATE | S1 |
| s5 | 0.06 | 0.14 | 0.26 | ESTIMATE | — |
| q | 0.35 | 0.56 | 0.74 | ESTIMATE | S3, S4 |
| d5 | 0.86 | 1.04 | 1.22 | PROXY | S3, S4, S5 |
| o | 0.68 | 0.84 | 0.95 | ESTIMATE | S3, S4, S5, S6 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 2.28 | 6.81 | 10.00 | PROXY |
| F | 0.08 | 0.31 | 0.72 | ESTIMATE |
| C | 7.00 | 10.00 | 10.00 | ESTIMATE |
| D | 5.85 | 8.74 | 10.00 | ESTIMATE |

## Caveats
- a: OEWS covers the full 512100 motion-picture and video industry rather than the narrow laboratory and preservation lens.
- a: The public preservation guidance describes workflows and standards but does not report labor shares.
- a: Film laboratory, analog-video transfer, high-end restoration, and archive metadata projects have materially different task mixes.
- rho: Adobe's editing features are not designed as an independent measure of archival-preservation adoption.
- rho: NARA specifications describe required outcomes rather than private-vendor implementation rates.
- rho: AI adoption can improve quality or discovery without reducing labor, especially when every output still receives frame-level review.
- e: The exact mix of film laboratories, preservation vendors, and stock-footage libraries in the supplied count is unavailable.
- e: The supplied n is only three firms, so classification or margin error can move eligibility substantially.
- e: The Information Services margin bridge may not represent equipment-intensive laboratories or project-funded preservation work.
- s5: No public exact-industry transfer rate or owner-succession series was found.
- s5: Equipment auctions, archive donations, closures, and purchases of film or footage assets are not qualifying transfers of a continuing service firm.
- s5: With very few eligible firms, idiosyncratic owner decisions dominate a population probability.
- q: No source measures the retained share of implemented AI benefit in film preservation.
- q: Grant-funded, government, studio, museum, and private-collector customers have different procurement and price-sharing behavior.
- q: Savings may be reinvested in higher capture quality or more manual restoration rather than appearing as margin.
- d5: NARA guidance establishes need and workflow, not a representative commercial demand forecast.
- d5: Preservation demand depends on institutional and grant budgets and can be delayed despite physical urgency.
- d5: The narrowed lens excludes stock-footage licensing, so broader growth in video usage does not automatically raise this service quantity.
- o: No source directly measures year-five operator-required demand for the narrowed lens.
- o: Routine born-digital media management is more substitutable than fragile-film handling and preservation-master creation.
- o: Equipment simplification may enable archive insourcing even if the work still requires a human operator.

## Sources
- **S1** — [2022 NAICS Manual: 512199 Other Motion Picture and Video Industries](https://www.census.gov/naics/reference_files_tools/2022_NAICS_Manual.pdf) (accessed 2026-07-22): Exact residual-industry scope and illustrative examples of motion-picture film laboratories, stock-footage film libraries, and film-preservation services.
- **S2** — [May 2023 OEWS: Motion Picture and Video Industries](https://www.bls.gov/oes/2023/may/naics4_512100.htm) (accessed 2026-07-22): Broader-industry occupation shares and wages used as a disclosed labor-mix proxy.
- **S3** — [Reformatting Audio, Video, and Motion Picture Records](https://www.archives.gov/preservation/holdings-maintenance/considerations/audio-video) (accessed 2026-07-22): Need for reformatting and digitization, preservation and access copies, specialized knowledge and equipment, outside vendors, and managed storage.
- **S4** — [Digital Output from Motion Picture Film Source](https://www.archives.gov/preservation/products/reformatting/mopix-digital) (accessed 2026-07-22): Preservation-grade film capture requirements, products for deteriorating or obsolete sources, restoration masters, access derivatives, and high-quality managed outputs.
- **S5** — [Film-Based Negatives and Positives](https://www.archives.gov/preservation/holdings-maintenance/film-based) (accessed 2026-07-22): Physical film deterioration, vinegar syndrome, cold-storage and reformatting priorities, careful handling, specialist consultation, and digitization needs.
- **S6** — [Introducing new AI-powered features and workflow enhancements in Premiere Pro and After Effects 25.2](https://blog.adobe.com/en/publish/2025/04/02/introducing-new-ai-powered-features-workflow-enhancements-premiere-pro-after-effects) (accessed 2026-07-22): Available AI-assisted media workflows for footage search, caption translation, clip generation, and automatic color handling, used as a proxy for digital-stage automation.
