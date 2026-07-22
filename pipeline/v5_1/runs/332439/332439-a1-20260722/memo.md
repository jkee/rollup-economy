# 332439 — Other Metal Container Manufacturing

*v5.1 Stage 1 research memo. Run `332439-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 5.69 · L 0.99 · interval STRUCTURAL_OUT → CONDITIONAL · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Repeat consumption of specification-critical industrial packaging supports durable customer relationships and process data.
**Weakness:** The NAICS code is heterogeneous and the coherent industrial slice faces cyclical volume plus substitution by plastics, fiber, bulk formats, reuse, and reconditioning.

## Business-model lens
- Included: US lower-middle-market independent manufacturers supplying recurring industrial light-gauge metal shipping containers, principally steel drums, barrels, pails, bins, and vats, to external chemical, petroleum, coatings, agricultural, food, and other industrial customers.
- Excluded: Captive plants, shells, non-control financing vehicles, firms outside the EBITDA band, pure distributors and reconditioners without qualifying manufacturing, and consumer-oriented lunch boxes, tool boxes, mailboxes, garbage cans, vacuum bottles, and specialized air-cargo containers.
- Customer and revenue model: Repeat industrial packaging is supplied through purchase orders and master supply relationships, with pricing sensitive to steel, freight, capacity, specifications, quality, and service; many customers reorder standardized or configured containers as their own production volumes require.
- Deviation from default lens: Narrowed to industrial light-gauge shipping containers because the NAICS code combines recurring drums, barrels, and pails with consumer durables and air-cargo containers whose customers, production economics, demand drivers, and transferability are too different for one coherent screen.

## Executive view
The coherent industrial-container slice has repeat physical demand and a meaningful LMM supplier base, but it is cyclical and exposed to alternative materials and reuse. AI opportunity is moderate and indirect, centered on quality, maintenance, planning, inventory, order processing, and administration.

## How AI changes the work
AI can assist vision inspection, downtime prediction, production sequencing, material and inventory planning, specification control, quoting, order entry, customer service, and quality records. It will not replace pressing, forming, welding, coating, assembly, line tending, warehousing, or accountable product release within five years.

## Value capture
Local service, freight economics, qualified linings and closures, and reliable delivery provide some pricing insulation. Standardized products, steel-sensitive pricing, purchase-order competition, rebates, and plastic or fiber alternatives should transfer a substantial portion of gains to customers.

## Firm availability
Greif describes a market with large integrated suppliers and numerous smaller competitors, supporting potential LMM targets. The usable population is materially below the frozen count because the NAICS code includes excluded consumer and cargo products and because reconditioning alone is outside the manufacturing lens.

## Demand durability
Industrial drums and pails recur with chemical, petroleum, coatings, agricultural, and food production. Recent large-company metal-packaging volume weakened, and long-run demand faces cyclicality, alternative materials, larger bulk formats, and closed-loop reuse, so flat demand is more defensible than automatic growth.

## Risks and uncertainty
The main uncertainties are the product mix inside the 66-firm estimate, LMM automation baselines, contract pass-through, and new-versus-reconditioned demand. Steel costs, hazardous-goods failure, environmental liability, customer cycles, freight, capacity, and substitution can dominate AI savings.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.2341 | — | OBSERVED | — |
| n | — | 66 | — | ESTIMATE | — |
| a | 0.11 | 0.2 | 0.31 | PROXY | S1, S2, S3 |
| rho | 0.32 | 0.53 | 0.7 | ESTIMATE | S3, S4 |
| e | 0.34 | 0.53 | 0.7 | ESTIMATE | S1, S5 |
| s5 | 0.12 | 0.2 | 0.3 | PROXY | S6 |
| q | 0.29 | 0.47 | 0.64 | ESTIMATE | S5 |
| d5 | 0.82 | 0.97 | 1.15 | PROXY | S1, S5 |
| o | 0.84 | 0.93 | 0.98 | ESTIMATE | S1, S5 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.33 | 0.99 | 2.03 | ESTIMATE |
| F | 2.10 | 3.34 | 4.34 | ESTIMATE |
| C | 5.80 | 9.40 | 10.00 | ESTIMATE |
| D | 6.89 | 9.02 | 10.00 | ESTIMATE |

## Caveats
- a: The BLS source covers all fabricated metal products rather than the narrowed industrial-container lens.
- a: The frozen compensation ratio covers the full heterogeneous NAICS code, including excluded activities.
- rho: General manufacturing surveys may not represent smaller drum and pail manufacturers.
- rho: Some operational improvements attributed to AI may actually be conventional automation or lean manufacturing.
- e: The frozen firm count is margin-bridged and spans the full heterogeneous NAICS code.
- e: Reconditioners are generally classified outside 332439 and must not be counted merely because they handle the same containers.
- s5: Gallup is cross-industry and measures owner plans rather than completed control transfers.
- s5: Some sales are individual plants or assets rather than transferable lens firms.
- q: Greif is a global diversified supplier rather than a target-scale firm.
- q: Capture varies by standard drum, specialty lining or closure, short-run pail, and customer concentration.
- d5: Greif's segment is global and its reported dollar volume effect is not a direct constant-quality unit index.
- d5: The narrowed lens excludes consumer and air-cargo categories that may have different demand trajectories.
- o: The estimate includes elimination by alternative formats and reuse, not only software self-service.
- o: A shift to another manufacturer does not reduce operator requirement even if it harms an incumbent.

## Sources
- **S1** — [2022 Economic Census Survey: Other Metal Container Manufacturing](https://bhs.econ.census.gov/ombpdfs2022/export/2022_MC-33243_su.pdf) (accessed 2026-07-22): Identifies 332439 as light-gauge metal container manufacturing including barrels, drums, and mailboxes and distinguishes it from metal cans, heavy-gauge tanks, and other adjacent fabrication.
- **S2** — [Fabricated Metal Product Manufacturing: NAICS 332](https://www.bls.gov/iag/tgs/iag332.htm) (accessed 2026-07-22): Provides broader-subsector evidence on the importance of physical fabrication occupations including assemblers, welders, machinists, press operators, and production supervisors.
- **S3** — [2026 Roadmap on Artificial Intelligence and Machine Learning for Smart Manufacturing](https://www.nist.gov/publications/2026-roadmap-artificial-intelligence-and-machine-learning-smart-manufacturing) (accessed 2026-07-22): Documents industrial AI applications and the data, integration, explainability, reliability, availability, and safety barriers to deployment.
- **S4** — [Shaping the AI-Powered Factory of the Future](https://documents.nam.org/tech/Shaping-the-AI-Powered-Factory-of-the-Future-Report.pdf) (accessed 2026-07-22): Reports only 18% of surveyed manufacturers have a formal operations AI strategy and highlights data, skill, culture, and legacy-system barriers.
- **S5** — [Greif, Inc. 2025 Form 10-KT](https://investor.greif.com/static-files/d2ea05ba-ddb1-46dc-b477-ad119ecc73bc) (accessed 2026-07-22): Describes steel drums sold to chemical, petroleum, agricultural, and coatings customers; numerous large and small competitors; cyclical price-sensitive markets; purchase-order and master-supply contracting; and a $70.7 million adverse 2025 volume effect in Durable Metal Solutions.
- **S6** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Gallup reports that 22% of US employer-business owners planned a sale, transfer, or public offering within five years and 52.3% of employer businesses are owned by people age 55 or older.
