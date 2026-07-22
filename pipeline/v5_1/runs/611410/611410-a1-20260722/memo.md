# 611410 — Business and Secretarial Schools

*v5.1 Stage 1 research memo. Run `611410-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 5.98 · L 0.00 · interval STRUCTURAL_OUT → STRUCTURAL_OUT · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Digitizable instructional content and administrative workflows create implementable labor-saving potential.
**Weakness:** The supplied data estimate zero target-band firms, and durable demand for operator-led generic secretarial training is uncertain.

## Business-model lens
- Included: Privately owned providers of repeat or recurring employer-contracted instruction in office procedures, administrative support, reception, communications, word processing, and related secretarial skills.
- Excluded: Consumer-only tuition programs, degree-granting business education, computer training classified in 611420, captive employer training units, public institutions, shells, and non-control financing vehicles.
- Customer and revenue model: Employer-paid cohort, seat, subscription, or fixed-fee training sold repeatedly to external organizations; learner-paid tuition without a repeat organizational customer is excluded.
- Deviation from default lens: The NAICS definition spans consumer career schools and employer training, which have materially different buyers and recurrence. The lens is narrowed to employer-contracted repeat instruction so the recurring outsourced-service screen is coherent.

## Executive view
The coherent recurring-service opportunity is employer-contracted office-skills training, a narrow subset of a small and heterogeneous NAICS. AI can reduce content, support, and administrative labor, but the supplied dataset estimates no firms in the target EBITDA band and the underlying secretarial-training demand is pressured by on-the-job learning and self-service technology.

## How AI changes the work
AI can draft and refresh course materials, generate exercises and assessments, personalize practice, answer routine learner questions, summarize interactions, and automate enrollment, scheduling, marketing, and billing. Humans remain important for needs diagnosis, live facilitation, motivation, exceptions, quality assurance, and employer accountability.

## Value capture
Fixed-fee and per-seat arrangements can preserve savings at first. Over renewals, transparent digital delivery and abundant substitutes should push a meaningful share of the benefit to customers through lower prices, broader scope, or higher service levels.

## Firm availability
Availability is the central constraint. The frozen firm-count input is zero in the target EBITDA band, while only a minority of any firms would have recurring employer contracts rather than consumer tuition revenue. Any apparent target would require direct verification of NAICS classification, size, recurrence, and ownership.

## Demand durability
Employers will continue to need some administrative reskilling, especially for specialized workflows and changing software. Traditional general clerical and secretarial preparation is vulnerable because entry often requires only a high-school credential and short on-the-job training, while AI and digital tools increasingly perform or simplify the tasks being taught.

## Risks and uncertainty
The strongest evidence is only available at broader industry or occupation level. Material risks include an empty target universe, falling relevance of stand-alone secretarial credentials, migration to vendor tutorials and AI tutors, aggressive renewal repricing, and weak implementation capacity in very small schools.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 1.4969 | — | OBSERVED | — |
| n | — | 0 | — | ESTIMATE | — |
| a | 0.3 | 0.46 | 0.62 | PROXY | S1, S2 |
| rho | 0.35 | 0.55 | 0.72 | ESTIMATE | S2, S5 |
| e | 0.02 | 0.08 | 0.2 | ESTIMATE | S3 |
| s5 | 0.08 | 0.18 | 0.32 | ESTIMATE | — |
| q | 0.3 | 0.5 | 0.7 | ESTIMATE | S3, S4 |
| d5 | 0.65 | 0.82 | 0.98 | PROXY | S4, S5 |
| o | 0.3 | 0.48 | 0.7 | PROXY | S3, S6 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 6.29 | 10.00 | 10.00 | ESTIMATE |
| F | 0.00 | 0.00 | 0.00 | ESTIMATE |
| C | 6.00 | 10.00 | 10.00 | ESTIMATE |
| D | 1.95 | 3.94 | 6.86 | PROXY |

## Caveats
- a: The occupation distribution is for NAICS 611400 and includes computer and management training.
- a: Anthropic usage is product-specific observed use, not a capability ceiling or a wage-weighted industry measure.
- a: The estimate excludes tasks already automated by learning-management and office software.
- rho: No 611410 adoption study was found.
- rho: Implementation capacity may be unusually weak because the frozen dataset estimates no firms in the target EBITDA band.
- e: The supplied n equals zero and is itself an ESTIMATE, so even a positive eligibility share implies zero expected targets at its base.
- e: NAICS descriptions do not reveal customer mix or firm-level consolidation.
- s5: No observed 611410 control-transfer denominator was available.
- s5: Because the dataset estimates zero band firms, a conditional transfer probability may not correspond to any actual target.
- q: The NAICS definition permits many delivery modes but does not measure contract structures.
- q: The lens excludes learner-paid tuition, whose pricing dynamics may differ.
- d5: Occupational employment is not training spend or constant-quality service quantity.
- d5: The five-year conversion is judgmental and does not isolate employer-funded programs.
- d5: Medical-secretary demand is stronger than generic and legal-secretary demand, creating mix uncertainty.
- o: Degree-granting distance-learning participation is a broad population proxy.
- o: Remote delivery can still retain an accountable operator; it is not identical to operator elimination.

## Sources
- **S1** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 611400](https://www.bls.gov/oes/2023/may/naics4_611400.htm) (accessed 2026-07-22): Broader-industry occupation mix: 83,320 jobs, including 28.88% business and financial operations, 17.39% management, 14.31% office support, and 14.25% educational instruction.
- **S2** — [Anthropic Economic Index: Tracking AI's role in the US and global economy](https://www.anthropic.com/research/economic-index-geography) (accessed 2026-07-22): Observed Claude use mapped to O*NET tasks; educational instruction and office/administrative tasks are represented, and automation reached 49.1% of classified interactions in the reported sample.
- **S3** — [North American Industry Classification System: Sector 61 Educational Services](https://www.census.gov/naics/resources/archives/sect61.html) (accessed 2026-07-22): Defines 611410 around office procedures and secretarial skills and distinguishes it from computer training, degree business education, and other technical training.
- **S4** — [Occupational Outlook Handbook: Secretaries and Administrative Assistants](https://www.bls.gov/ooh/office-and-administrative-support/secretaries-and-administrative-assistants.htm) (accessed 2026-07-22): Documents duties, short on-the-job training, 0% projected 2024-34 employment change overall, divergent specialty projections, and AI/digital tools enabling staff to prepare their own documents.
- **S5** — [Occupational Outlook Handbook: General Office Clerks](https://www.bls.gov/ooh/office-and-administrative-support/general-office-clerks.htm) (accessed 2026-07-22): Reports short on-the-job training, a 7% projected 2024-34 decline, and continued automation of document preparation, filing, and clerical work.
- **S6** — [NCES Fast Facts: Distance learning](https://nces.ed.gov/fastfacts/display.asp?id=80) (accessed 2026-07-22): Shows broad acceptance of remote postsecondary delivery: 61% of undergraduates took at least one distance course in fall 2021 and 28% studied exclusively at a distance.
