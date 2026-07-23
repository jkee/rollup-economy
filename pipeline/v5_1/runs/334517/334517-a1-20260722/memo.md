# 334517 — Irradiation Apparatus Manufacturing

*v5.1 Stage 1 research memo. Run `334517-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** STRUCTURAL_OUT · A 5.90 · L 0.89 · interval STRUCTURAL_OUT → LOW_PRIORITY · readiness MODEL_CONDITIONED · action VALIDATE_ASSUMPTIONS

**Driver:** A high-value engineering, software, regulatory, test, and service-document layer creates more AI-addressable work than typical physical manufacturing.
**Weakness:** A small candidate pool and stringent safety, validation, and regulatory requirements slow implementation and transactions.

## Business-model lens
- Included: US lower-middle-market manufacturers repeatedly supplying medical diagnostic and therapeutic, industrial, research, and scientific irradiation apparatus, tubes, components, upgrades, and associated configured systems to external healthcare, laboratory, industrial, OEM, and research customers.
- Excluded: Hospitals and imaging-service operators, radioactive-isotope producers, captive internal engineering units, software-only vendors without accountable physical apparatus, pure distributors, non-control financing vehicles, and operations that cannot transfer independently of the owner.
- Customer and revenue model: Capital-equipment, component, tube, upgrade, replacement, and configured-system revenue under purchase orders, tenders, OEM programs, service-linked installed-base relationships, and regulated product lifecycles.
- Deviation from default lens: none

## Executive view
Irradiation apparatus combines a large engineering, software, quality, and regulatory labor layer with physical safety-critical hardware. AI can improve traceability, documentation, testing support, service knowledge, and planning, but regulation, validation, and expert accountability constrain implementation.

## How AI changes the work
AI can assist requirements and revision review, test-case generation, code review, risk and regulatory document assembly, complaint and service knowledge, procurement, configuration, and planning. Physics design, hardware integration, assembly, calibration, radiation measurement, verification, installation, and final safety release remain expert and physical.

## Value capture
Clearances, performance standards, installed interfaces, uptime, training, and service history protect value. OEM sourcing, hospital procurement, GPOs, tenders, capital-budget pressure, and reimbursement still force some benefit into customer economics.

## Firm availability
The supplied dataset estimates 45 firms in the economic band. Actual eligibility depends on independence, recurring products or installed-base revenue, valid clearances and quality systems, customer concentration, key-person risk, and normalized earnings; many apparent participants may be large strategic subsidiaries.

## Demand durability
Diagnostic imaging, therapy, industrial inspection, scientific research, tubes, upgrades, and service-linked replacements require physical apparatus. Equipment longevity and capital constraints temper demand, while upgrades, installed-base aging, and clinical or industrial needs support it.

## Risks and uncertainty
The largest unknowns are six-digit occupation mix, medical versus industrial product mix, regulatory status, product liability, customer concentration, installed-base economics, current software automation, and true LMM margins. The supplied inputs mix vintages and use a computers/peripherals margin bridge.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.1957 | — | OBSERVED | — |
| n | — | 45 | — | ESTIMATE | — |
| a | 0.18 | 0.3 | 0.43 | PROXY | S1, S2 |
| rho | 0.2 | 0.38 | 0.57 | ESTIMATE | S2, S3, S4 |
| e | 0.48 | 0.65 | 0.79 | ESTIMATE | S2 |
| s5 | 0.07 | 0.15 | 0.26 | ESTIMATE | — |
| q | 0.43 | 0.66 | 0.83 | ESTIMATE | S2, S3 |
| d5 | 0.95 | 1.1 | 1.28 | ESTIMATE | S2, S3, S4 |
| o | 0.96 | 0.99 | 1 | ESTIMATE | S2, S3, S4 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.28 | 0.89 | 1.92 | ESTIMATE |
| F | 1.48 | 2.71 | 3.74 | ESTIMATE |
| C | 8.60 | 10.00 | 10.00 | ESTIMATE |
| D | 9.12 | 10.00 | 10.00 | ESTIMATE |

## Caveats
- a: Occupation evidence covers all navigational, measuring, electromedical, and control instruments, not 334517.
- a: Exposure does not imply autonomous engineering or regulatory approval.
- rho: This is bounded judgment rather than an observed implementation probability.
- rho: Medical requirements do not apply identically to industrial and research apparatus.
- e: The supplied n relies on receipts and a computers/peripherals margin bridge rather than observed EBITDA.
- e: The industry includes medical, industrial, and research products with different qualification and revenue patterns.
- s5: No comprehensive six-digit control-transfer series was found.
- s5: Technology licenses, product-line asset sales, and internal reorganizations must be excluded unless operating control transfers.
- q: No source directly measures sharing of AI-derived benefit.
- q: Pricing power differs sharply between proprietary cleared systems, OEM components, and competitive research apparatus.
- d5: No complete constant-price five-year forecast was found for 334517.
- d5: Medical imaging dominates available evidence but the NAICS definition also includes therapy, industrial, research, and scientific apparatus.
- o: Software may change clinical or industrial workflows without eliminating the physical radiation source.
- o: Domestic suppliers can be displaced even when US end demand persists.

## Sources
- **S1** — [Navigational, Measuring, Electromedical, and Control Instruments Manufacturing - May 2023 OEWS](https://www.bls.gov/oes/2023/may/naics4_334500.htm) (accessed 2026-07-22): BLS reports NAICS 334500 occupation shares of 17.58% engineering, 14.10% computer/mathematical, 10.15% business/financial, 12.47% management, 7.77% office support, and 26.89% production in May 2023.
- **S2** — [NAICS 334517 Irradiation Apparatus Manufacturing](https://www.census.gov/naics/resources/archives/sect31-33.html) (accessed 2026-07-22): Census defines the industry as manufacturing irradiation apparatus and tubes for medical diagnostic, medical therapeutic, industrial, research, and scientific evaluation using beta, gamma, X-ray, or other ionizing radiation.
- **S3** — [Medical X-ray Imaging](https://www.fda.gov/radiation-emitting-products/medical-imaging/medical-x-ray-imaging) (accessed 2026-07-22): FDA states that X-ray manufacturers are regulated under EPRC and medical-device provisions and must meet records, defect notification, repair/replacement, import, radiation-safety performance, and medical-device requirements.
- **S4** — [How Does FDA Regulate CT Systems?](https://www.fda.gov/radiation-emitting-products/medical-x-ray-imaging/how-does-fda-regulate-ct-systems) (accessed 2026-07-22): FDA states that CT systems are regulated as radiation-emitting products and Class II medical devices, requiring manufacturer registration/listing, 510(k) notification, quality-system practices, controls, certification, labeling, and performance information.
