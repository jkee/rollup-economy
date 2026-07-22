# 323113 — Commercial Screen Printing

*v5.1 Stage 1 research memo. Run `323113-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** LOW_PRIORITY · A 6.29 · L 1.72 · interval STRUCTURAL_OUT → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** High-frequency artwork, quote, proof, order, scheduling, and customer workflows sit beside a relatively high labor-to-receipts base.
**Weakness:** Most shop labor remains physical, and easy-to-quote apparel work faces strong local, online, alternative-process, and offshore competition.

## Business-model lens
- Included: US lower-middle-market screen printers repeatedly serving businesses, institutions, brands, distributors, teams, schools, events, and promotional-product customers on apparel, textiles, labels, signs, stationery, invitations, components, and other purchased substrates.
- Excluded: Publishers, book printers, fabric grey-goods mills, product manufacturers whose printing is captive, pure brokers without transferable operations, hobby shops, non-control financing vehicles, and owner-dependent art practices without recurring external customer relationships.
- Customer and revenue model: Job-order and recurring-program revenue priced per design, setup, color, item, run, or fulfillment program, often including artwork, screen preparation, printing, curing, finishing, packing, online storefront, and distribution services.
- Deviation from default lens: none

## Executive view
Commercial screen printing combines labor-intensive physical production with a meaningful digital front end in artwork, quoting, proofs, order management, and customer service. AI can improve the front end, while the screen room, press, curing, reclaiming, finishing, and fulfillment remain hands-on and demand varies with apparel, promotion, event, label, and industrial end markets.

## How AI changes the work
AI can clean and adapt artwork, generate mockups, compare specifications, assist quotes, summarize proof changes, ingest orders, schedule jobs, triage exceptions, and support customers and online stores. Physical screen preparation, registration, ink handling, printing, curing, cleaning, packing, and final quality remain operator tasks.

## Value capture
Customization, turnaround, consistent placement and color, program administration, and fulfillment create service value that can protect savings. Simple apparel and promotional work is readily quoted across local shops and online platforms, so price competition will share away part of recurring gains.

## Firm availability
Census reports thousands of employer establishments, but the supplied dataset estimates only 80 firms in the target economic band, highlighting the industry's microbusiness skew and the uncertainty in the margin bridge. Transferability depends on recurring programs, staff, equipment, customer diversification, and whether art and sales relationships reside beyond the owner.

## Demand durability
Physical decorated apparel, promotional goods, labels, signs, and industrial markings should persist, but channel and technology can change. Direct-to-garment, transfers, online self-service, imports, and in-house equipment can displace conventional screen operators even without eliminating the decorated product.

## Risks and uncertainty
The largest unknowns are the six-digit labor mix, true LMM population, owner dependence, product and channel mix, current workflow software, customer concentration, and substitution among screen, digital, transfer, and offshore production. Ink and solvent controls add implementation constraints, while the supplied inputs mix vintages and apply a margin bridge.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.3117 | — | OBSERVED | — |
| n | — | 80 | — | ESTIMATE | — |
| a | 0.16 | 0.27 | 0.4 | PROXY | S1, S2 |
| rho | 0.31 | 0.51 | 0.7 | ESTIMATE | S1, S2 |
| e | 0.57 | 0.74 | 0.86 | ESTIMATE | S2 |
| s5 | 0.1 | 0.19 | 0.31 | ESTIMATE | — |
| q | 0.34 | 0.57 | 0.76 | ESTIMATE | S2 |
| d5 | 0.86 | 1 | 1.16 | ESTIMATE | S2, S4 |
| o | 0.84 | 0.94 | 0.99 | ESTIMATE | S2, S3 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.62 | 1.72 | 3.49 | ESTIMATE |
| F | 2.76 | 4.03 | 5.00 | ESTIMATE |
| C | 6.80 | 10.00 | 10.00 | ESTIMATE |
| D | 7.22 | 9.40 | 10.00 | ESTIMATE |

## Caveats
- a: BLS evidence covers all printing, not 323113.
- a: Occupation shares do not directly measure task exposure or existing automation.
- rho: This is bounded judgment rather than an observed adoption probability.
- rho: Digital-native web-store operators may implement faster than relationship-led manual shops.
- e: Census reports 5,854 employer establishments in 2023, far broader than the supplied LMM firm estimate.
- e: The provided n uses a paper-industry margin bridge that may not reflect screen-printing economics.
- s5: No comprehensive six-digit control-transfer series was found.
- s5: Asset sales and customer-book purchases without a transferable operating firm must be excluded.
- q: No source directly measures contractual sharing of AI-derived benefit.
- q: Capture differs sharply between industrial/specification work and commodity T-shirt programs.
- d5: No complete constant-price, constant-quality forecast exists for 323113.
- d5: BLS occupational decline reflects productivity and technology substitution as well as demand.
- o: Alternative physical decoration processes may displace screen printers even when decorated-product demand persists.
- o: Environmental controls and ink changes reinforce operator accountability but do not guarantee domestic demand.

## Sources
- **S1** — [Printing and Related Support Activities - May 2023 OEWS Industry-Specific Occupational Employment and Wage Estimates](https://www.bls.gov/oes/2023/may/naics3_323000.htm) (accessed 2026-07-22): BLS reports 378,410 workers in NAICS 323 in May 2023; printing workers were 138,520 (36.61%), including 90,740 press operators (23.98%), 15,330 prepress workers (4.05%), and 32,450 binding/finishing workers (8.58%).
- **S2** — [323113: Commercial Screen Printing](https://data.census.gov/profile/323113_-_Commercial_Screen_Printing?codeset=naics~323113) (accessed 2026-07-22): Census defines job-order screen printing on purchased stock and explicitly includes apparel and textile products such as T-shirts, caps, jackets, towels, and napkins; it reports 5,854 employer establishments in 2023.
- **S3** — [Monitoring Information by Industry - Printing and Publishing](https://www.epa.gov/air-emissions-monitoring-knowledge-base/monitoring-information-industry-printing-and-publishing) (accessed 2026-07-22): EPA states that printing emissions arise primarily from evaporation of organic solvents in inks, identifies press, drier, ink, cleaning, and mixing emission points, and notes use of thermal and catalytic oxidizers on screen-printing drier exhausts for solvent-borne inks.
- **S4** — [Occupational Projections and Worker Characteristics](https://www.bls.gov/emp/tables/occupational-projections-and-characteristics.htm) (accessed 2026-07-22): BLS projects printing press operator employment to decline from 150,200 in 2024 to 138,000 in 2034, an 8.1% decline, and print binding/finishing employment to decline 16.1%; these are broad occupation projections, not a screen-print demand forecast.
