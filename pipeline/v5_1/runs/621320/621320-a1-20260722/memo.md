# 621320 — Offices of Optometrists

*v5.1 Stage 1 research memo. Run `621320-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** CONDITIONAL · A 6.66 · L 3.54 · interval LOW_PRIORITY → PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Structured diagnostic, administrative, and optical workflows offer multiple AI-enabled efficiency levers around a durable recurring need for licensed eye care.
**Weakness:** Prescription portability, retail and online competition, and partial automation can separate optical economics and routine screening from the practice while licensed-clinician continuity still constrains transfers.

## Business-model lens
- Included: Independent group and multisite optometry practices in the lower-middle-market band that repeatedly provide eye examinations, refraction, disease detection and management, corrective-lens prescribing and fitting, contact-lens care, vision therapy, pre- and postoperative care, and integrated optical dispensing to external patients and payers.
- Excluded: Captive hospital, HMO, or government units; ophthalmology practices; pure optical-goods retailers without optometric practice; online eyewear or software businesses; shell or non-operating entities; non-control financing positions; and solo or owner-dependent practices that cannot support a transferable operating company or fall below the normalized EBITDA band.
- Customer and revenue model: Patients receive the service and may pay directly, while medical or vision insurers fund covered examinations and procedures. Practices may also earn product revenue from eyeglasses, contact lenses, and related optical goods. Clinical revenue is generally visit- or procedure-based, whereas optical revenue combines product margin and fitting service; repeat examinations, disease monitoring, and prescription renewals create repeat demand without guaranteed contracts.
- Deviation from default lens: none

## Executive view
Scaled optometry combines repeat licensed clinical care with structured diagnostic data, administration, and optical retail, creating a broader AI-assistance surface than many hands-on health practices. AI can improve documentation, image triage, scheduling, billing, inventory, recall, and sales support, but comprehensive examination, prescribing, disease management, fitting, and accountability remain human-led. The strongest operating form is a multi-doctor group whose payer access, brand, protocols, staff, and patient relationships survive the founder.

## How AI changes the work
Ambient documentation, test summarization, image pre-analysis, coding support, patient messaging, appointment optimization, inventory forecasting, and optical-order workflows can reduce clerical burden and avoid some hiring. Existing AI-interpreted retinal imaging demonstrates real diagnostic automation, but its narrow scope also shows the limit: comprehensive eye health, treatment choice, prescribing, exceptions, and patient communication still require licensed judgment and review.

## Value capture
Fixed clinical fees can preserve part of productivity gains, while optical operations can benefit from lower administrative cost, better inventory, and fewer errors. Capture is weakened by managed-vision pricing, vendor costs, retail competition, and federal prescription portability that lets patients buy eyewear elsewhere. The benefit depends on converting saved time into more care or lower staffing needs rather than idle capacity.

## Firm availability
The frozen LMM count is estimate-based but larger than many clinician-office categories. Medical-practice sales evidence explicitly includes optometry yet does not reveal an optometry-specific transaction rate. Actual control availability depends on owner timing, licensed clinical continuity, payer credentialing, patient retention, leases, equipment, inventory, and whether goodwill is institutional rather than personal.

## Demand durability
BLS projects optometrist employment growth, with aging, myopia and other refractive errors, digital eye strain, and diabetes supporting demand. Automation and retail or online substitution can shift where routine screening and eyewear are supplied, while disease management and complex eye care remain durable. Clinical services and optical product demand should not be assumed to move together.

## Risks and uncertainty
Key uncertainties are the true staff and revenue mix, the margin-bridged firm count, lack of a transaction denominator, uneven AI and device adoption, diagnostic liability, privacy and cybersecurity, payer reimbursement, prescription leakage, online competition, and founder dependence. Existing automation can reduce the incremental opportunity, while overreliance on narrow screening AI could harm quality or referral capture.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.4257 | — | OBSERVED | — |
| n | — | 116 | — | ESTIMATE | — |
| a | 0.2 | 0.32 | 0.45 | PROXY | S2, S5, S6 |
| rho | 0.4 | 0.65 | 0.84 | PROXY | S4, S5, S6 |
| e | 0.7 | 0.85 | 0.96 | ESTIMATE | S1, S3 |
| s5 | 0.1 | 0.2 | 0.32 | ESTIMATE | S3, S8 |
| q | 0.33 | 0.53 | 0.72 | ESTIMATE | S1, S7 |
| d5 | 0.95 | 1.04 | 1.15 | PROXY | S3, S6 |
| o | 0.62 | 0.79 | 0.91 | ESTIMATE | S2, S3, S6, S7 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 1.36 | 3.54 | 6.44 | PROXY |
| F | 3.56 | 4.88 | 5.79 | ESTIMATE |
| C | 6.60 | 10.00 | 10.00 | ESTIMATE |
| D | 5.89 | 8.22 | 10.00 | ESTIMATE |

## Caveats
- a: O*NET measures optometrist duties, not the full occupation and wage mix of NAICS 621320 offices.
- a: Ambient-scribe results come from physicians and advanced-practice practitioners rather than optometrists.
- a: Automated instruments and retinal interpretation are already present in some practices, so gross technical capability overstates the not-yet-automated share.
- rho: The AMA adoption population is physicians rather than optometrists.
- rho: The ambient-scribe study was voluntary and short-duration, and its health-system support may not transfer to independent groups.
- rho: CMS code 92229 covers a narrow retinal-imaging use case rather than broad autonomous eye care.
- e: No public source measures the share of frozen LMM firms satisfying every lens criterion.
- e: BLS occupation shares do not map cleanly to enterprise ownership or eligibility.
- e: The dataset's LMM count uses a broad healthcare-provider margin rather than observed optometry EBITDA.
- s5: BizBuySell provides medical-practice benchmarks but no optometry-only sale probability or eligible-firm denominator.
- s5: The platform's median sold practice is smaller than the target EBITDA band.
- s5: A transfer can fail economically if patients, payer panels, or optical sales follow the departing owner.
- q: Public evidence does not quantify the lens's clinical-versus-optical revenue or gross-benefit mix.
- q: The FTC rule documents prescription portability and competition but not the magnitude of AI savings passed through to patients.
- q: Freed clinician or technician capacity has little value when appointment demand is the binding constraint.
- d5: BLS projects an occupation rather than real output or visit quantity for offices of optometrists.
- d5: The occupation includes work settings outside NAICS 621320.
- d5: Product sales, clinical services, and screening can follow different demand paths.
- o: The estimate distinguishes continued need for an accountable practice from headcount per encounter.
- o: State scope-of-practice rules differ even though licensure is universal.
- o: The automated retinal-imaging precedent covers one disease-screening task and still routes positive or inconclusive cases to eye-care professionals.

## Sources
- **S1** — [2022 NAICS Manual: 621320 Offices of Optometrists](https://www.census.gov/naics/reference_files_tools/2022_NAICS_Manual.pdf) (accessed 2026-07-22): Defines 621320 as independent O.D. practices examining, diagnosing, treating, and managing visual-system disease and providing corrective lenses, vision therapy, and optician-like fitting and sales.
- **S2** — [O*NET OnLine: Optometrists (29-1041.00)](https://www.onetonline.org/link/details/29-1041.00) (accessed 2026-07-22): Provides the optometrist task and work-context map, including instrument-based eye examination, test analysis, treatment planning, prescribing, fitting, counseling, referral, daily face-to-face discussion, frequent contact, and high accuracy requirements.
- **S3** — [U.S. BLS Occupational Outlook Handbook: Optometrists](https://www.bls.gov/ooh/healthcare/optometrists.htm) (accessed 2026-07-22): Reports 47,800 optometrist jobs in 2024, work-setting shares including 54% in optometrist offices and 11% self-employed, universal state licensure, 8% projected employment growth from 2024 to 2034, and aging, refractive errors, digital eye strain, and diabetes as demand drivers.
- **S4** — [American Medical Association: 2026 Physician AI Survey](https://www.ama-assn.org/system/files/physician-ai-sentiment-report.pdf/) (accessed 2026-07-22): Reports U.S. physician AI use, including 72% incorporating at least one surveyed use case in 2026, and identifies privacy, safety, efficacy, liability, training, and oversight as adoption considerations.
- **S5** — [JAMA Network Open: Use of Ambient AI Scribes to Reduce Administrative Burden and Professional Burnout](https://jamanetwork.com/journals/jamanetworkopen/fullarticle/2839542) (accessed 2026-07-22): A 2024 pre/post quality-improvement study of 263 ambulatory clinicians across six U.S. health systems found lower documentation burden and an average-equivalent 10.8 minutes saved per workday after 30 days of ambient-scribe use, with voluntary participation and no optometry-specific sample.
- **S6** — [CMS MLN Matters MM12071: Remote Retinal Imaging CPT 92229](https://edit.cms.gov/files/document/mm12071.pdf) (accessed 2026-07-22): Describes CPT 92229 for point-of-care automated retinal-image analysis using AI to interpret the eye examination without requiring ophthalmologist interpretation as a diagnostic service, demonstrating a narrow operational automation precedent.
- **S7** — [Federal Trade Commission: Final Eyeglass Rule Updates](https://www.ftc.gov/news-events/news/press-releases/2024/06/ftc-announces-final-eyeglass-rule-implementing-updates-promote-competition-expand-consumer-choice) (accessed 2026-07-22): States that optometrists and ophthalmologists must provide a free prescription copy immediately after a refractive exam and before offering eyeglasses, enabling consumers to shop elsewhere and supporting optical-retail competition and compliance burden.
- **S8** — [BizBuySell: Medical Practice Business Valuation Benchmarks](https://www.bizbuysell.com/learning-center/valuation-benchmarks/medical-practice/) (accessed 2026-07-22): Reports transaction and valuation benchmarks for sold medical practices from 2021 through 2025 and explicitly identifies optometry among included specialties, demonstrating a transfer channel while not providing an optometry-specific probability or eligible-firm denominator.
