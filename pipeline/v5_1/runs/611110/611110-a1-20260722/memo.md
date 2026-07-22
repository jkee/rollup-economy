# 611110 — Elementary and Secondary Schools

*v5.1 Stage 1 research memo. Run `611110-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** CONDITIONAL · A 7.32 · L 2.39 · interval STRUCTURAL_OUT → PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Large payroll-weighted planning and administrative workloads create a meaningful, though bounded, opportunity for AI-assisted capacity and avoided hiring.
**Weakness:** Religious and nonprofit governance sharply reduces the share of schools that can undergo a conventional qualifying control transfer.

## Business-model lens
- Included: Privately operated elementary and secondary schools providing recurring instruction and related school services to enrolled students, with tuition, contracted public funding, or other repeat customer revenue, and with approximately $1-10M normalized EBITDA.
- Excluded: Public school systems, standalone tutoring or test-preparation providers classified elsewhere, homeschooling households, software-only products, captive school units, non-control financing vehicles, and schools without transferable operations.
- Customer and revenue model: Families and, for some operators, public agencies pay tuition or contracted per-pupil funding for an academic-year service; enrollment commonly renews annually and revenue is largely fixed-fee or per-student rather than hourly.
- Deviation from default lens: none

## Executive view
Elementary and secondary schools combine a large labor base with repeat annual enrollment, but the economically implementable AI opportunity is concentrated in preparation, assessment, communications, records, and back-office work. Live teaching, supervision, safeguarding, and institutional accountability remain operator-intensive. The more severe constraint is firm availability: much of private K-12 is religious or nonprofit and not conventionally transferable.

## How AI changes the work
AI can generate lesson materials, draft differentiated activities, assist rubric-based assessment, summarize student information, prepare parent communications, and automate admissions, billing, scheduling, and compliance workflows. It is less suited to unsupervised instruction, classroom management, special-needs judgment, child safeguarding, and high-stakes decisions. Implementation should be measured as avoided hiring and reclaimed capacity with documented human review, not nominal tool adoption.

## Value capture
Tuition and per-pupil funding are generally set for a term or academic year, so workflow savings are not automatically rebated. An operator can retain savings initially, but repeated enrollment decisions and annual price setting encourage sharing through moderated tuition, aid, staff investment, or service improvements. Capture will be strongest where demand is stable and automation improves responsiveness without weakening the school experience.

## Firm availability
NCES shows that two-thirds of private schools have a religious orientation, and legal or sponsor governance can prevent an ordinary control acquisition. Even among nonsectarian schools, nonprofit status, founder dependence, campus-level rather than firm-level data, and subscale economics narrow the pool. Broad baby-boomer transition pressure exists, but a school-specific control-transfer dataset is missing.

## Demand durability
K-12 education remains compulsory and socially important, yet the number of students is not growing nationally. NCES projected private enrollment down 12% from 2019 to 2030 and public enrollment down 4% from 2020 to 2030. School-choice policy and local migration can create pockets of growth, but the base case is modest real quantity contraction with an accountable school operator still required for nearly all remaining service.

## Risks and uncertainty
The occupation data mix public and private schools, the AI adoption study covers public teachers, private-enrollment projections are dated and historically less accurate, and orientation is only a rough proxy for transferable ownership. Privacy, bias, hallucination, parent trust, labor relations, and inconsistent state rules could slow implementation. A poor result would arise if eligible schools are much rarer than estimated, enrollment declines accelerate, or AI savings must be fully reinvested to preserve outcomes.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.4943 | — | OBSERVED | — |
| n | — | 2678 | — | ESTIMATE | — |
| a | 0.14 | 0.22 | 0.31 | PROXY | S1, S2 |
| rho | 0.35 | 0.55 | 0.72 | PROXY | S2, S8 |
| e | 0.18 | 0.29 | 0.4 | PROXY | S3, S4 |
| s5 | 0.09 | 0.15 | 0.23 | PROXY | S5 |
| q | 0.45 | 0.6 | 0.75 | ESTIMATE | S3, S6 |
| d5 | 0.91 | 0.96 | 1.01 | PROXY | S6, S7 |
| o | 0.9 | 0.96 | 0.99 | PROXY | S8, S9 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.97 | 2.39 | 4.41 | PROXY |
| F | 6.10 | 7.67 | 8.86 | ESTIMATE |
| C | 9.00 | 10.00 | 10.00 | ESTIMATE |
| D | 8.19 | 9.22 | 10.00 | PROXY |

## Caveats
- a: OEWS is NAICS 611100 and includes government schools, whereas the economic lens is private six-digit establishments.
- a: RAND covers public-school ELA, mathematics, and science teachers and reports use, not technically substitutable task share.
- a: The frozen compensation ratio has a 2024-wage/2022-receipts vintage mismatch and an IPS harmonization adjustment.
- rho: Current usage is not equivalent to operational labor realization.
- rho: RAND's public-school sample may not represent private schools' procurement autonomy or technology resources.
- rho: Implementation excludes revenue, tuition pricing, enrollment, and valuation effects.
- e: Religious orientation is not a legal-form or transferability measure.
- e: The NCES school universe includes many schools far below the frozen LMM band and counts campuses rather than necessarily firms.
- e: The frozen firm count is a margin-bridged estimate and may not align with school-campus counts.
- s5: The source is an exit-planning industry organization and its population and methodology are broader than this lens.
- s5: School transactions are often asset, nonprofit affiliation, or sponsor changes that may not qualify as control transfers.
- s5: No industry-specific denominator of eligible firms was found.
- q: No source directly measures retention of AI-derived gross benefit in K-12 schools.
- q: Voucher, charter-contract, nonprofit, and family-paid tuition models can have materially different pass-through dynamics.
- q: Enrollment decline is treated in d5, not again in this estimate.
- d5: The NCES projection was prepared with historical data through 2019 or 2020 and explicitly notes pandemic uncertainty.
- d5: Private-school five-year projection errors have historically been materially larger than public-school errors.
- d5: National enrollment can mask strong local growth and decline.
- o: Regulation varies materially by state and does not always require teacher certification or accreditation.
- o: The proxy supports operator accountability qualitatively rather than measuring a quantity share.
- o: Rapid policy change or acceptance of software-led schooling could lower the operator-required share.

## Sources
- **S1** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 611100 Elementary and Secondary Schools](https://www.bls.gov/oes/2023/may/naics4_611100.htm) (accessed 2026-07-22): Occupation mix and wages: 8,600,970 total jobs; 65.79% educational instruction/library, 44.80% classroom-teacher group, 12.94% teaching assistants, 5.92% office/administrative support, and 4.58% management.
- **S2** — [Uneven Adoption of Artificial Intelligence Tools Among U.S. Teachers and Principals in the 2023-2024 School Year](https://www.rand.org/content/dam/rand/pubs/research_reports/RRA100/RRA134-25/RAND_RRA134-25.pdf) (accessed 2026-07-22): Nationally representative public-school evidence on teacher AI adoption, frequency, use cases, principal concerns, and the 18% prevalence of school or district guidance.
- **S3** — [Number and percentage distribution of private schools, students, and FTE teachers, by religious or nonsectarian orientation: 2021-22](https://nces.ed.gov/surveys/pss/tables/TABLE02fl2122.asp) (accessed 2026-07-22): Private-school universe totals: 29,727 schools, 4,731,303 students, 19,628 religious schools (66.0%), and 10,099 nonsectarian schools (34.0%).
- **S4** — [Number and percentage distribution of private schools, by school level and selected characteristics: 2021-22](https://nces.ed.gov/surveys/pss/tables/TABLE16fl2122.asp) (accessed 2026-07-22): School-level composition of the 29,727-school private universe and confirmation of the religious/nonsectarian mix across elementary, secondary, and combined schools.
- **S5** — [State of Owner Readiness Research](https://exit-planning-institute.org/state-of-owner-readiness) (accessed 2026-07-22): Broad-market proxy stating 51% of the American business market is baby-boomer owned and set to transition over zero to ten years, while only 20-30% of businesses brought to market sell.
- **S6** — [Projections of Education Statistics to 2030: Elementary and Secondary Enrollment](https://nces.ed.gov/programs/PES/section-1.asp) (accessed 2026-07-22): Enrollment projections: private K-12 from 5.5 million in 2019 to 4.8 million in 2030 (down 12%) and public enrollment down 4% from 2020 to 2030, with forecast accuracy limitations.
- **S7** — [Projections of Education Statistics to 2030: About This Report](https://nces.ed.gov/programs/PES/about.asp) (accessed 2026-07-22): Projection scope, pandemic-era limitations, and historical five-year mean absolute percentage errors, including 8.5% for private preK-12 enrollment.
- **S8** — [Guidance for Generative AI in Education and Research](https://www.unesco.org/en/articles/guidance-generative-ai-education-and-research) (accessed 2026-07-22): Human-centered, age-appropriate AI use, data-privacy safeguards, ethical validation, and pedagogical design requirements in education.
- **S9** — [Selected U.S. Supreme Court Rulings Related to Private and Home Schools](https://www.ed.gov/birth-grade-12-education/school-choice/selected-us-supreme-court-rulings-related-private-and-home-schools) (accessed 2026-07-22): Private education is recognized in all 50 states within compulsory-attendance statutes, and states retain authority to impose reasonable basic-education regulation.
