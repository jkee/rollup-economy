# 541120 — Offices of Notaries

*v5 Stage 1 research memo. Run `541120-a1-20260722`, model `gpt-5.6-terra`, 2026-07-22, attempt 1.*

**Base tier:** no base (evidence-first) · A — · L — · interval STRUCTURAL_OUT → PRIORITY · readiness STRESS_TEST_ONLY · action EVIDENCE_FIRST

**Driver:** Document-processing workflows have real automation exposure while the formal act remains accountable and regulated.
**Weakness:** There is no defensible public evidence for eligible LMM-firm share or five-year qualifying transfer probability in this narrow NAICS.

## Business-model lens
- Included: US lower-middle-market independent offices that repeatedly provide external customers with the NAICS-defined services of drafting, approving, executing, receiving, indexing, or storing legal documents.
- Excluded: Law firms, title abstract and settlement offices, internal corporate units, financing vehicles, and signature-only notary public services that NAICS places in 541199.
- Customer and revenue model: External customers pay per document matter or under a repeat service relationship; this screen excludes one-off consumer stamp-only work unless the firm also supplies the NAICS-defined document service on a repeat outsourced basis.
- Deviation from default lens: none

## Executive view
Offices of Notaries is an unusually narrow and poorly measured NAICS category. Its defined work combines legal-document processing with accountable execution and custody, but the ordinary signature-only notary market belongs in another industry. The missing firm-eligibility and transfer evidence is a central limitation.

## How AI changes the work
AI can support intake, document classification, drafting assistance, retrieval, and customer communication. A legal-services task proxy suggests material exposure, yet the formal act still depends on accurate review and a person responsible for identity and execution.

## Value capture
Per-matter pricing offers some initial retention of workflow savings, but standardized remote platforms and regulated fee rules create pass-through pressure. A Florida online notarial act is capped at $25, while related platform services may be billed separately.

## Firm availability
No reliable public evidence identifies firms in the frozen EBITDA band that also have repeat outsourced revenue, nor does it measure qualifying control transfers. This is not treated as a zero opportunity; it remains missing evidence.

## Demand durability
The broad legal-services outlook is slow but positive, supporting a near-flat demand proxy. Remote authorization in 47 states and the District of Columbia changes delivery rather than eliminating the legal-document need, although platform substitution can reduce operator volume.

## Risks and uncertainty
The NAICS definition and the common meaning of notary do not align cleanly: signature-only notary services are classified in 541199. State-specific rules, error liability, identity requirements, customer acceptance, and sparse industry data make extrapolation particularly uncertain.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.4487 | — | ESTIMATE | — |
| n | — | — | — | MISSING | — |
| a | 0.25 | 0.38 | 0.5 | PROXY | S1, S2 |
| rho | 0.2 | 0.32 | 0.45 | ESTIMATE | S3, S4 |
| e | — | — | — | MISSING | — |
| s5 | — | — | — | MISSING | — |
| q | 0.12 | 0.22 | 0.35 | ESTIMATE | S5 |
| d5 | 0.92 | 1.01 | 1.08 | PROXY | S2 |
| o | 0.45 | 0.62 | 0.78 | ESTIMATE | S3, S4 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.90 | 2.18 | 4.04 | ESTIMATE |
| F | — | — | — | MISSING |
| C | 2.40 | 4.40 | 7.00 | ESTIMATE |
| D | 4.14 | 6.26 | 8.42 | ESTIMATE |

## Caveats
- a: No current occupation or task mix is published for this suppressed and unusually narrow NAICS industry.
- a: The legal-profession proxy includes lawyers and paralegals with work unlike this lens.
- rho: The state-law evidence establishes permitted technology and controls, not actual AI adoption or savings in this NAICS.
- rho: Requirements vary by state and document type.
- e: The frozen n input is unavailable by instruction and must remain dataset-injected MISSING.
- e: NAICS classification alone does not establish recurring revenue or normalized EBITDA.
- s5: General small-business exit statistics would not distinguish transfers from closures or internal reorganizations.
- q: Florida's fee rule is not a national fee survey and does not govern non-notarial document work.
- q: Actual fee structure and competition vary by state and customer type.
- d5: Legal-services employment is a broader population and is not a volume measure.
- d5: A direct five-year forecast for this NAICS was not found.
- o: The evidence is about remote notarization generally, while this NAICS excludes signature-only notary services and includes broader document work.
- o: Future changes in state law or identity technology could alter the operator requirement.

## Sources
- **S1** — [Census Bureau NAICS Sector 54 definition](https://www.census.gov/naics/resources/archives/sect54.html) (accessed 2026-07-22): Defines 541120 as offices drafting, approving, executing, receiving, indexing, and storing legal documents; states that signature-only notary public services are classified in 541199.
- **S2** — [BLS: Incorporating AI impacts in employment projections](https://www.bls.gov/opub/mlr/2025/article/incorporating-ai-impacts-in-bls-employment-projections.htm) (accessed 2026-07-22): Reports a study estimating 44 percent of legal-profession tasks susceptible to automation and projects legal-services employment growth of 1.6 percent from 2023 to 2033; also describes continuing legal-review needs.
- **S3** — [National Association of Secretaries of State: Remote Electronic Notarization](https://www.nass.org/initiatives/remote-electronic-notarization) (accessed 2026-07-22): States that 47 states and the District of Columbia allow remote e-notarization and describes personal appearance, identity verification, audiovisual communication, credential analysis, and privacy standards.
- **S4** — [Florida Statutes Section 117.265, Online notarization procedures](https://www.flsenate.gov/Laws/Statutes/2025/117.265) (accessed 2026-07-22): Requires online identity confirmation, audiovisual communication, remote government identification presentation, credential analysis, identity proofing, and secure communication for Florida online notarizations.
- **S5** — [Florida Statutes Section 117.275, Fees for online notarization](https://www.flsenate.gov/Laws/Statutes/2025/117.275) (accessed 2026-07-22): Caps the fee for an online notarial act at $25 and permits separate charges for services other than the act, including a RON service provider.
