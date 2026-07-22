# 541940 — Veterinary Services

*v5 Stage 1 research memo. Run `541940-a1-20260722`, model `gpt-5.6-terra`, 2026-07-22, attempt 1.*

**Base tier:** CONDITIONAL · A 6.70 · L 2.42 · interval STRUCTURAL_OUT → PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Repeat, clinically necessary animal-health services remain dependent on accountable operators while administrative workflow is amenable to AI assistance.
**Weakness:** No direct industry evidence measures realized AI labor savings or completed lower-middle-market control transfers, so both are bounded judgments or proxies.

## Business-model lens
- Included: Independent lower-middle-market veterinary practices and veterinary testing providers delivering repeat animal prevention, diagnosis, treatment, surgery, laboratory, and related care to pet owners, livestock owners, and referring practices.
- Excluded: Captive animal-care units, internal corporate departments, shell entities, non-control financing vehicles, and operators whose economics are primarily pet retail, boarding, grooming, or real estate rather than veterinary services.
- Customer and revenue model: External customers purchase recurring preventive care and episodic medically necessary services, generally through direct practice fees and related inventory sales; referring practices may purchase testing services.
- Deviation from default lens: none

## Executive view
Veterinary Services is a clinically anchored external service business with repeat demand and meaningful operational administration, but its core care delivery remains hands-on and professionally accountable. The strongest AI case is relieving documentation and back-office friction rather than replacing veterinary medicine.

## How AI changes the work
The industry has a large observed mix of veterinarians, technicians, assistants, and office staff. AI is most relevant to records, scheduling, intake, communications, billing support, inventory, and clinical information triage; examination, procedures, specimen handling, and final clinical judgment remain limiting tasks.

## Value capture
Direct service revenue is the largest practice revenue category, so workflow gains need not be automatically passed through under cost-plus contracts. Retention is nevertheless uncertain because local competition, client affordability, staffing pressure, and the need to reinvest gains can share benefits with customers and employees.

## Firm availability
The industry contains many small practices and has an active succession and consolidation environment. A published projection of practices coming to market supports transfer potential, but listings are not closed sales and one- or two-doctor practices may be difficult to transfer.

## Demand durability
BLS expects veterinarian employment growth driven by pet spending, expanded treatment options, and a growing, aging pet population. That is a favorable demand proxy, though affordability pressure and normalization after unusually strong demand can weaken actual visit volume.

## Risks and uncertainty
The main evidence gaps are direct measurements of AI deployment, task time, completed lower-middle-market transactions, and constant-dollar service volumes. Clinical quality, privacy, liability, practice-system integration, state scope rules, and fragmented practice types make broad extrapolation hazardous.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.4494 | — | OBSERVED | — |
| n | — | 133 | — | ESTIMATE | — |
| a | 0.18 | 0.28 | 0.4 | ESTIMATE | S1, S2, S3, S4 |
| rho | 0.3 | 0.48 | 0.65 | ESTIMATE | S4 |
| e | 0.8 | 0.9 | 0.97 | ESTIMATE | S7, S4 |
| s5 | 0.1 | 0.16 | 0.25 | PROXY | S6 |
| q | 0.5 | 0.68 | 0.82 | ESTIMATE | S4 |
| d5 | 0.97 | 1.05 | 1.12 | PROXY | S5 |
| o | 0.82 | 0.91 | 0.97 | ESTIMATE | S2, S3, S5 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.97 | 2.42 | 4.67 | ESTIMATE |
| F | 3.95 | 4.83 | 5.64 | ESTIMATE |
| C | 10.00 | 10.00 | 10.00 | ESTIMATE |
| D | 7.95 | 9.55 | 10.00 | ESTIMATE |

## Caveats
- a: OEWS excludes self-employed workers and is a 2023 wage snapshot.
- a: O*NET describes occupations across employers, not the veterinary-services industry alone.
- a: AI capability and quality for veterinary workflows are evolving faster than the source vintages.
- rho: Technology enthusiasm is not measured deployment or sustained productivity.
- rho: The AVMA practice-owner sample may not represent the lower-middle-market subset.
- e: The industry definition does not report lens eligibility or firm-level normalized EBITDA.
- e: Establishment counts can differ from firm counts for multi-site operators.
- s5: The cited projection concerns practices put up for sale rather than closed transactions.
- s5: The cited source discusses general and specialty practice markets, whereas the lens covers all eligible lower-middle-market veterinary services.
- s5: The underlying Packaged Facts projection predates the later slowdown in consolidation described by AAHA.
- q: The AVMA revenue categories do not measure contractual pass-through or the incidence of AI savings.
- q: Retention can differ substantially by companion, food-animal, equine, emergency, and specialty practice type.
- d5: Occupation employment is not the same construct as service quantity and includes employment outside NAICS 541940.
- d5: The BLS projection spans ten years and is not adjusted here using an observed industry productivity series.
- o: The estimate does not separately model companion, livestock, mobile, testing, and specialty providers.
- o: Software-assisted service can still reduce operator time without eliminating the accountable operator.

## Sources
- **S1** — [BLS May 2023 OEWS Industry-Specific Occupational Employment and Wage Estimates: Veterinary Services](https://www.bls.gov/oes/2023/may/naics5_541940.htm) (accessed 2026-07-22): Observed NAICS 541940 occupation employment shares and wages, including veterinarians, veterinary technologists and technicians, veterinary assistants, animal caretakers, and office support.
- **S2** — [O*NET Job Duties: Veterinarians](https://www.onetonline.org/search/task/choose/29-1131.00) (accessed 2026-07-22): Veterinarian tasks include treatment, inoculation, examination, specimen collection, diagnostic equipment use, client counseling, and advice.
- **S3** — [O*NET Details: Veterinary Technologists and Technicians](https://www.onetonline.org/link/details/29-2056.00) (accessed 2026-07-22): Technician work includes documentation, patient care, imaging, specimen work, equipment handling, close physical proximity, and material consequences of error.
- **S4** — [American Veterinary Medical Association 2025 Report on the Economic State of the Veterinary Profession](https://ebusiness.avma.org/files/productdownloads/002_AVMA_SotPReport25_NoPasswordPRO.pdf) (accessed 2026-07-22): Practice size, ownership, revenue-category, owner-time, technology-attitude, and productivity evidence for United States veterinary practices.
- **S5** — [BLS Occupational Outlook Handbook: Veterinarians](https://www.bls.gov/ooh/Healthcare/Veterinarians.htm) (accessed 2026-07-22): Veterinarian duties, concentration in veterinary services, and projected employment growth with stated demand drivers.
- **S6** — [AAHA Trends: Practice Ownership Exit and Entry Strategies](https://www.aaha.org/trends-magazine/july-2024/practice-ownership-exit-and-entry-strategies/) (accessed 2026-07-22): Published discussion of veterinary practice sales, a Packaged Facts projection of practices put up for sale, consolidation, and transfer constraints by practice size and geography.
- **S7** — [U.S. Census Bureau Profile: NAICS 541940 Veterinary Services](https://data.census.gov/profile/541940_-_Veterinary_services?codeset=naics~541940) (accessed 2026-07-22): NAICS 541940 definition covering licensed veterinary medical, dental, surgical, and testing establishments.
