# 621512 — Diagnostic Imaging Centers

*v5.1 Stage 1 research memo. Run `621512-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** CONDITIONAL · A 7.59 · L 2.90 · interval LOW_PRIORITY → PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** Digitized images, high administrative friction, and a large regulated radiology-AI ecosystem support workflow and throughput improvement across repeat procedure volume.
**Weakness:** Patient-facing acquisition, expensive equipment, professional accountability, and payer-controlled reimbursement prevent software from removing most operator cost or demand.

## Business-model lens
- Included: Lower-middle-market diagnostic imaging firms repeatedly producing patient images on practitioner referral through MRI, CT, X-ray, mammography, ultrasound, PET, and nuclear-medicine services, including patient scheduling and preparation, image acquisition, technical operations, interpretation coordination, reporting, billing, collections, and referral support.
- Excluded: Captive hospital and physician-practice imaging departments, equipment manufacturers and repair businesses, software vendors without an operated imaging service, radiation-therapy providers, shells, subscale hobby businesses, and non-control financing vehicles.
- Customer and revenue model: Patients are generally referred by physicians, while commercial insurers, managed-care organizations, Medicare, Medicaid, hospitals, physician groups, and patients fund services. Revenue is mainly per procedure under negotiated commercial rates or government fee schedules, with some capitation and management-fee arrangements; repeat referrals and recurring payer or physician relationships support volume.
- Deviation from default lens: none

## Executive view
Diagnostic imaging centers have a mature AI supply base and substantial digital administrative and clinical-support workflows, but the service remains anchored to capital equipment, patient handling, safety, and accountable interpretation. The best opportunity is to improve throughput, worklists, reporting, authorization, and collections across a network rather than to replace the center itself.

## How AI changes the work
AI can assist scheduling, referral intake, prior authorization, protocol selection, scan acceleration, reconstruction, image-quality checks, worklist triage, cancer detection, report drafting, coding, denial management, and collections. Technologists still prepare and position patients, administer contrast, operate equipment, manage radiation and safety, and acquire diagnostically adequate images, while radiologists retain professional responsibility.

## Value capture
Negotiated commercial rates and government fee schedules can leave initial labor and throughput gains with the operator, particularly under multi-year contracts. Capitation, payer renegotiation, competitive pricing, PFS changes, professional-reading fees, utilization management, and AI licensing or integration costs limit long-run retention.

## Firm availability
The frozen population is large and the cited strategic buyer completed repeated imaging-center acquisitions, demonstrating demand for local density, equipment, modalities, payer access, and referral networks. Transferability is weakened by joint ventures, radiology-group agreements, payer enrollment, equipment debt and leases, referral concentration, and asset-only transaction structures.

## Demand durability
Aging, chronic disease, cancer screening, falls, and expanding advanced-imaging applications support modest real procedure growth. Physical image acquisition remains necessary, but payers can constrain utilization and referrals may shift toward hospitals, physician groups, mobile services, or denser regional platforms.

## Risks and uncertainty
Key risks are reimbursement cuts, payer and referral concentration, capital intensity, equipment downtime and obsolescence, technologist shortages, radiologist alignment, regulatory and cybersecurity failures, false-positive or biased AI, integration cost, and overestimating labor removal when AI mainly adds capacity. A center with weak modality mix, aging equipment, poor contracts, or no referral density may not capture the operational benefit.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.3714 | — | OBSERVED | — |
| n | — | 859 | — | ESTIMATE | — |
| a | 0.21 | 0.31 | 0.43 | PROXY | S2, S3, S4, S5 |
| rho | 0.45 | 0.63 | 0.78 | PROXY | S4, S5 |
| e | 0.55 | 0.72 | 0.85 | ESTIMATE | S1, S5 |
| s5 | 0.1 | 0.18 | 0.28 | PROXY | S5, S7 |
| q | 0.35 | 0.54 | 0.7 | PROXY | S5, S6 |
| d5 | 0.98 | 1.05 | 1.12 | PROXY | S3, S5, S6 |
| o | 0.88 | 0.94 | 0.99 | PROXY | S1, S3, S4, S5 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 1.40 | 2.90 | 4.98 | PROXY |
| F | 6.24 | 7.59 | 8.57 | ESTIMATE |
| C | 7.00 | 10.00 | 10.00 | PROXY |
| D | 8.62 | 9.87 | 10.00 | PROXY |

## Caveats
- a: BLS publishes only a combined 621500 occupation mix, requiring judgment to remove medical-laboratory work and reconstruct the imaging-center mix.
- a: Most authorized radiology AI products assist rather than replace accountable clinicians, so device counts do not measure labor substitution.
- a: Equipment-related acceleration may increase scan capacity and demand rather than proportionally reduce staffing.
- rho: The FDA list establishes authorization, not utilization, workflow coverage, or economic benefit.
- rho: RadNet is the largest U.S. freestanding imaging operator and also owns a digital-health segment, unlike a typical LMM center group.
- rho: Implementation varies by modality, vendor, PACS and RIS architecture, radiology-group relationship, and state requirements.
- e: No source measures default-lens eligibility among the frozen LMM-band firms.
- e: The 859-firm count is margin-bridged with a broad hospitals and healthcare-facilities margin that may not fit freestanding imaging centers with different equipment, lease, and professional-fee structures.
- e: Imaging-site counts, joint ventures, management companies, and legal firms are not interchangeable denominators.
- s5: Gallup is cross-industry and measures intentions rather than completed qualifying transfers.
- s5: RadNet's disclosed transactions are one buyer's asset acquisitions and do not provide an industry denominator.
- s5: Joint-venture interests, professional radiology practices, management entities, and imaging-center operating companies have different transfer mechanics.
- q: Neither source measures five-year retention of implemented AI benefit for LMM diagnostic imaging firms.
- q: Technical fees, professional fees, management fees, commercial fee-for-service, government payment, and capitation transmit benefit differently.
- q: RadNet's density and scale create procurement, utilization, and payer advantages unavailable to many LMM operators.
- d5: Occupational employment is not procedure volume, and the BLS projection spans ten years rather than the five-year horizon.
- d5: RadNet's reported growth includes acquisitions, price, and modality mix and is not a constant-price national demand series.
- d5: Demand varies sharply across MRI, CT, mammography, ultrasound, X-ray, PET, and nuclear medicine.
- o: Operator-required service does not guarantee that the current independent center retains the referral or payer contract.
- o: Remote interpretation can centralize professional labor without eliminating the local physical imaging site.
- o: The operator-required share differs by modality and could fall faster for standardized screening and image-review workflows.

## Sources
- **S1** — [North American Industry Classification System, United States, 2022](https://www.census.gov/naics/reference_files_tools/2022_NAICS_Manual.pdf) (accessed 2026-07-22): Defines NAICS 621512 as diagnostic imaging centers producing patient images generally on practitioner referral and lists CT, radiological, X-ray, ultrasound, and MRI centers.
- **S2** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: NAICS 621500](https://www.bls.gov/oes/2023/may/naics4_621500.htm) (accessed 2026-07-22): Reports the combined medical-and-diagnostic-laboratory occupation mix and wages, including radiologic, MRI, sonography, nuclear-medicine, clinical-laboratory, administrative, billing, customer-service, management, and business occupations.
- **S3** — [Occupational Outlook Handbook: Radiologic and MRI Technologists](https://www.bls.gov/ooh/healthcare/radiologic-technologists.htm) (accessed 2026-07-22): Describes patient preparation, positioning, scanner operation, image evaluation, recordkeeping, safety, certification and licensing, and projects 5 percent employment growth from 2024 to 2034 based on aging and chronic-disease diagnostic demand.
- **S4** — [Artificial Intelligence-Enabled Medical Devices](https://www.fda.gov/medical-devices/software-medical-device-samd/artificial-intelligence-enabled-medical-devices) (accessed 2026-07-22): Provides the FDA list of AI-enabled devices authorized for U.S. marketing, including a large radiology category, and explains that listed devices met applicable premarket safety and effectiveness requirements.
- **S5** — [RadNet, Inc. 2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/790526/000162828026013337/rdnt-20251231.htm) (accessed 2026-07-22): Discloses imaging modalities, AI uses and deployment, payer and contract structures, reimbursement pressure, physical and professional operating roles, procedure growth, and eleven 2025 plus nine 2024 imaging-center asset acquisitions.
- **S6** — [Medicare Physician Fee Schedule](https://www.cms.gov/medicare/payment/fee-schedules/physician) (accessed 2026-07-22): States that Medicare uses the Physician Fee Schedule to pay radiology services and diagnostic tests other than clinical laboratory tests.
- **S7** — [Most Small-Business Owners Lack a Succession Plan](https://news.gallup.com/poll/657362/small-business-owners-lack-succession-plan.aspx) (accessed 2026-07-22): Reports that 22 percent of U.S. employer-business owners planned to sell, transfer, or take public within five years and documents the intent-based survey population.
