# 541940 — Veterinary Services

*v5.1 Stage 1 research memo. Run `541940-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** CONDITIONAL · A 7.10 · L 3.23 · interval LOW_PRIORITY → PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Durable, repeat animal-health demand delivered through digitally enabled practices creates room for AI-assisted capacity growth without removing the veterinarian-led operator.
**Weakness:** Most labor value sits in licensed or hands-on clinical work, so documentation and front-office automation may not translate into proportionate headcount reduction or retained margin.

## Business-model lens
- Included: Veterinary clinics, animal hospitals, specialty and emergency practices, mobile and farm-animal practices, and veterinary diagnostic laboratories that serve external customers, generate recurring or repeat service revenue, and fall within the dataset-defined lower-middle-market EBITDA band.
- Excluded: Captive internal veterinary units, shells, non-control financing vehicles, research and development establishments, non-veterinary boarding or grooming, breeding and horse boarding, animal transportation, and retail-only pet supply activity. Incidental medicine or food sales inside an eligible veterinary practice remain included as ancillary revenue.
- Customer and revenue model: Customers are primarily pet owners, farms and other animal owners, with some referrals from other veterinary practices. Revenue is predominantly fee-for-service by examination, procedure, diagnostic test, treatment, hospitalization, and dispensed product; preventive, chronic-care, and follow-up needs create repeat demand, while emergency and surgical work is episodic.
- Deviation from default lens: none

## Executive view
Veterinary services combine durable repeat demand and a visible acquisition market with a credible but bounded AI labor opportunity. AI is already entering documentation, communication and diagnostic support, yet the industry's largest clinical roles remain licensed, physical and accountable. The practical thesis is workflow augmentation and capacity release across multi-role practices, not replacement of the veterinarian-led service.

## How AI changes the work
The clearest near-term uses are ambient notes, record summarization, scheduling, reception, billing support, client follow-up, inventory support, image interpretation and laboratory-result assistance [S3][S4]. These tools can reduce administrative burden and avoid incremental hires, but exams, restraint, specimen collection, anesthesia, procedures and surgery remain hands-on [S8][S9]. Clinical outputs also require review because errors, liability, privacy and skill decay constrain unattended automation [S4].

## Value capture
Itemized fee-for-service pricing gives an operator room to retain savings through avoided hiring, higher throughput and reduced clinician overtime. Retention is not complete: scarce staff may capture part through wages, added capacity may induce lower effective prices, and affordability or local competition can shift benefits to customers over time. Diagnostic laboratories and wellness plans may face faster repricing than urgent or specialty services.

## Firm availability
Most target-band operating practices should meet the recurring external-service lens, although the code spans several business models and the injected size-to-EBITDA mapping is uncertain. Broad employer-owner succession intentions and FTC-documented veterinary consolidation support a meaningful transfer pipeline [S6][S7]. Actual qualifying supply could be lower if seller intentions fail, clinics are already held inside large groups, or owner-dependent practices lack transferable teams.

## Demand durability
Animal examination, treatment, prevention and diagnostics remain operator-required because of licensure, physical care and clinical accountability [S1][S8][S9]. BLS expects above-average growth for both veterinarians and veterinary technicians, citing pet spending, treatment expansion and the growing, aging pet population [S8][S9]. The downside is that affordability pressure can defer nonurgent visits, and real service quantity may lag nominal spending.

## Risks and uncertainty
The largest measurement gaps are task-level labor savings, realized AI implementation depth, target-band firm ownership, completed control-transfer rates and long-run savings retention. The specialty AI survey may overstate readiness for general and rural practices, while employment projections are an indirect demand proxy. Clinical errors, fragmented practice systems, cybersecurity, state regulation, staff resistance, customer trust and corporate concentration can each reduce realized benefit.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.4494 | — | OBSERVED | — |
| n | — | 133 | — | ESTIMATE | — |
| a | 0.19 | 0.29 | 0.39 | PROXY | S3, S4, S8, S9 |
| rho | 0.42 | 0.62 | 0.78 | PROXY | S4, S5 |
| e | 0.7 | 0.82 | 0.92 | ESTIMATE | S1, S2 |
| s5 | 0.12 | 0.22 | 0.32 | PROXY | S6, S7 |
| q | 0.45 | 0.64 | 0.8 | ESTIMATE | S2 |
| d5 | 0.96 | 1.05 | 1.14 | PROXY | S8, S9 |
| o | 0.89 | 0.95 | 0.99 | PROXY | S4, S8, S9 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 1.43 | 3.23 | 5.47 | PROXY |
| F | 4.02 | 5.18 | 5.94 | ESTIMATE |
| C | 9.00 | 10.00 | 10.00 | ESTIMATE |
| D | 8.54 | 9.97 | 10.00 | PROXY |

## Caveats
- a: The OEWS mix is industry-specific but does not identify tasks within occupations.
- a: The AI survey covers veterinary internal-medicine specialists and may not represent general, rural, large-animal or laboratory practices.
- a: Potential labor savings are not the same as realized headcount reductions in capacity-constrained clinics.
- rho: Current use of at least one AI tool does not measure depth, reliability or enterprise-wide implementation.
- rho: The AVMA technology figures describe broad software readiness and may include practices outside the target EBITDA band.
- rho: State professional rules, vendor interoperability and clinical liability may produce large variation among practices.
- e: No source directly measures eligibility for the frozen acquisition lens.
- e: The injected firm count is inferred from SUSB size classes using a generic 15.65% margin; veterinary practices can differ materially in margins and multi-site ownership structure.
- e: NAICS 541940 mixes companion-animal, large-animal, specialty, emergency and diagnostic-laboratory models.
- s5: Gallup is cross-industry and measures intentions rather than completed transfers.
- s5: FTC evidence establishes acquisition activity but not an industry transfer rate and emphasizes specialty and emergency markets.
- s5: Corporate tuck-ins can be acquisitions of clinics or assets rather than control transfers of independently counted firms.
- q: No direct study traces veterinary AI savings into prices, wages and margins over five years.
- q: Retention differs between routine primary care, emergency care, referral specialties, farm contracts, wellness plans and laboratories.
- q: Using saved clinician time for more visits raises gross benefit but does not by itself establish retained unit economics.
- d5: Employment projections are not direct forecasts of constant-quality service volume.
- d5: BLS projections cover occupations across employers, although veterinary services employ 84% of veterinarians and 89% of veterinary technologists and technicians.
- d5: Nominal pet spending can rise even if real service quantity is flat, and affordability can suppress visits.
- o: The operator requirement varies by state scope-of-practice rules and by companion, farm, emergency, specialty and laboratory setting.
- o: Remote monitoring and direct-to-consumer triage may reduce clinic touchpoints without eliminating clinical accountability.
- o: The AI survey is attitudinal and specialist-heavy, not a direct displacement measure.

## Sources
- **S1** — [2022 NAICS Definition: 541940 Veterinary Services](https://www.census.gov/naics/?details=541940&input=541940&year=2022) (accessed 2026-07-22): Official industry scope, included veterinary medical and testing establishments, and cross-industry exclusions.
- **S2** — [NAPCS Product List for NAICS 54194: Veterinary Services](https://www2.census.gov/library/reference/napcs/product-list/web-54194-final-reformatted-edited-us082208.pdf) (accessed 2026-07-22): Service basket covering preventive care, examinations, diagnosis, treatment, surgery, imaging, laboratory services and ancillary products.
- **S3** — [Veterinary Services: May 2023 OEWS Industry-Specific Occupational Employment and Wage Estimates](https://www.bls.gov/oes/2023/may/naics5_541940.htm) (accessed 2026-07-22): Direct industry occupation counts, employment shares and wages used to anchor wage-weighted task exposure.
- **S4** — [The use of, and attitudes toward, artificial intelligence in members of the American College of Veterinary Internal Medicine and the European College of Veterinary Internal Medicine - Companion Animals](https://academic.oup.com/jvim/article/40/1/aalaf036/8431570) (accessed 2026-07-22): Veterinary specialist AI adoption, tool categories, interest, knowledge, attitudes and implementation constraints.
- **S5** — [2025 AVMA Report on the Economic State of the Veterinary Profession](https://ebusiness.avma.org/files/productdownloads/002_AVMA_SotPReport25_NoPasswordPRO.pdf) (accessed 2026-07-22): Practice adoption of management software, electronic medical records and other digital technologies.
- **S6** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Cross-industry employer-owner age and stated five-year sale or transfer intentions.
- **S7** — [FTC Approves Final Order Protecting Pet Owners from Private Equity Firm's Anticompetitive Acquisition of Veterinary Services Clinics](https://www.ftc.gov/news-events/news/press-releases/2022/08/ftc-approves-final-order-protecting-pet-owners-private-equity-firms-anticompetitive-acquisition) (accessed 2026-07-22): Evidence of veterinary clinic chain ownership, private-equity acquisition activity and consolidation scrutiny.
- **S8** — [Occupational Outlook Handbook: Veterinarians](https://www.bls.gov/ooh/healthcare/veterinarians.htm) (accessed 2026-07-22): Veterinarian duties, licensing, work setting, employment concentration, growth projection and demand drivers.
- **S9** — [Occupational Outlook Handbook: Veterinary Technologists and Technicians](https://www.bls.gov/ooh/healthcare/veterinary-technologists-and-technicians.htm) (accessed 2026-07-22): Technician physical and clinical duties, credentials, industry concentration, growth projection and demand drivers.
