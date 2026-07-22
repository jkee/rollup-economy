# 516110 — Radio Broadcasting Stations

*v5.1 Stage 1 research memo. Run `516110-a1-20260722`, model `claude-sonnet-5`, 2026-07-22, attempt 1.*

**Base tier:** no base (evidence-first) · A — · L — · interval STRUCTURAL_OUT → PRIORITY · readiness STRESS_TEST_ONLY · action EVIDENCE_FIRST

**Driver:** A large combined share of media production, sales, and administrative work is addressable by AI, with surveyed radio managers already moving from discussion toward use and policy formation.
**Weakness:** Demand for core terrestrial advertising is structurally weak and younger-listener share is lower, while the missing lower-middle-market firm count makes total target availability unmeasurable.

## Business-model lens
- Included: Commercial radio broadcasting stations serving external listeners and advertisers through over-the-air programming and station-operated streaming, digital advertising, sponsorship, and related recurring local marketing services, viewed at lower-middle-market EBITDA scale.
- Excluded: Noncommercial and public stations without a commercial revenue model, internet-only audio services without terrestrial station operations, podcast-only businesses, networks without station operations, and businesses whose principal activity is advertising agency work rather than radio broadcasting.
- Customer and revenue model: Stations aggregate listener attention and sell recurring local and national advertising, sponsorship, political advertising, digital marketing, streaming inventory, events, and related services. Revenue is externally paid and often repeat, but cyclical, audience-sensitive, and exposed to advertiser migration across media.
- Deviation from default lens: none

## Executive view
Radio stations offer meaningful AI-addressable production, sales, and administrative work, and industry managers are actively exploring adoption. The economic setting is less favorable than the task exposure: terrestrial spot revenue and younger-listener share are under pressure, while digital revenue provides only a partial offset. FCC-licensed operations and local relationships support persistence, but the missing firm count prevents a reliable aggregate availability conclusion.

## How AI changes the work
AI can assist copywriting, voice tracking, editing, transcription, scheduling, research, prospecting, proposals, traffic, and administration. Realization will be moderated by local authenticity, editorial and copyright risk, brand trust, live programming, engineering, client relationships, and the gap between adoption plans and production deployment.

## Value capture
Stations can retain savings where licenses, audience franchises, local personalities, and bundled advertiser relationships differentiate the offering. Advertiser bargaining, digital alternatives, direct use of AI by clients, declining core revenue, and required digital investment limit retention.

## Firm availability
FCC rules permit transfers subject to prior approval, so station assets are transaction-capable, but no denominator-supported lower-middle-market seller rate is available. Cluster ownership also makes stations and firms difficult to map one-for-one, and n is missing in the supplied dataset.

## Demand durability
Radio still commands a majority of ad-supported audio listening time and remains locally relevant, but younger audiences allocate materially less time to radio and spot-revenue forecasts decline. Streaming and broader digital marketing services mitigate rather than eliminate the structural pressure.

## Risks and uncertainty
Key uncertainties are the missing firm count, use-versus-plan ambiguity in AI adoption, occupation-to-task translation, nominal revenue proxies for real demand, political-ad cycles, digital-service economics, format differences, cluster ownership, and regulatory transaction friction.

## Scorecard

| Primitive | Low | Base | High | Evidence | Sources |
|---|---|---|---|---|---|
| l | — | 0.2525 | — | ESTIMATE | — |
| n | — | — | — | MISSING | — |
| a | 0.34 | 0.5 | 0.66 | PROXY | S2, S3 |
| rho | 0.28 | 0.48 | 0.67 | PROXY | S3 |
| e | 0.5 | 0.68 | 0.82 | ESTIMATE | S1, S5 |
| s5 | 0.04 | 0.09 | 0.16 | ESTIMATE | S5 |
| q | 0.3 | 0.49 | 0.66 | ESTIMATE | S3, S7 |
| d5 | 0.72 | 0.86 | 1 | PROXY | S4, S6, S7 |
| o | 0.48 | 0.65 | 0.8 | ESTIMATE | S1, S4, S5 |

| Factor | Low | Base | High | Evidence |
|---|---|---|---|---|
| H | 0.96 | 2.42 | 4.47 | ESTIMATE |
| F | — | — | — | MISSING |
| C | 6.00 | 9.80 | 10.00 | ESTIMATE |
| D | 3.46 | 5.59 | 8.00 | ESTIMATE |

## Caveats
- a: The BLS table is May 2023 and measures occupations rather than tasks.
- a: Radio groups increasingly sell digital services whose labor mix may not be fully represented in the station occupation table.
- a: The injected labor-intensity value is inherited from ancestor sector 51 and is LOW quality, so it may misstate radio stations' compensation-to-receipts structure.
- rho: The survey reports manager responses and does not audit implementation or savings.
- rho: The phrase roughly half combines current users with stations merely planning adoption.
- rho: Survey participants may be more digitally engaged than the full station population.
- e: The NAICS definition establishes broadcasting activity but not commercial status, profitability, independence, or transaction size.
- e: FCC approval makes license transfers possible but does not show the fraction that is economically eligible.
- e: The firm-count input n is a declared dataset gap and must remain MISSING; this estimate does not replace or infer n.
- s5: FCC transfer rules establish process, not historical seller incidence.
- s5: A license transfer may involve a single station, a cluster, or a broader company and therefore does not map cleanly to firms.
- s5: Distressed station transfers may not represent recurring positive-EBITDA acquisition opportunities.
- q: Neither source directly measures the share of labor savings retained in station EBITDA.
- q: Digital revenue growth can require third-party product costs and additional specialist labor.
- q: Local market concentration, ratings, format, and advertiser mix produce wide station-level variation.
- d5: Spot-ad revenue is nominal and does not directly measure constant-price service demand.
- d5: S&P's spot forecasts exclude some digital and non-spot station revenue.
- d5: Audio listening shares measure time, not advertiser spending or station profitability.
- d5: Political advertising creates material cycle effects.
- o: The estimate concerns the need for an operating entity, not preservation of current station employment.
- o: Local news, talk, sports, and emergency-oriented formats may persist more strongly than music formats.
- o: A station can remain licensed while much programming and production is centralized elsewhere.

## Sources
- **S1** — [2022 NAICS Definition: 516110 Radio Broadcasting Stations](https://www.census.gov/naics/?details=516110&input=516110&year=2022) (accessed 2026-07-22): Defines establishments broadcasting aural programs to the public using station studios and broadcasting facilities.
- **S2** — [May 2023 National Industry-Specific Occupational Employment and Wage Estimates: Radio Broadcasting Stations](https://www.bls.gov/oes/2023/may/naics5_516110.htm) (accessed 2026-07-22): Provides radio-station employment shares across media, announcer, sales, administrative, management, and other occupations used to bridge to task exposure.
- **S3** — [2025 Benchmarking Report: Radio's Digital Sales Exceed $2 Billion](https://www.rab.com/unusual/BorrellReport2025/BorrellDigitalBenchmark_FINAL.pdf) (accessed 2026-07-22): Reports a 2024 survey of 221 radio managers, including generative-AI use or plans, AI discussion, best-practice policies, and digital-sales context.
- **S4** — [The Record: Q1 2025 U.S. Audio Listening Trends](https://www.edisonresearch.com/the-record-q1-2025-u-s-audio-listening-trends/) (accessed 2026-07-22): Reports radio's share of ad-supported audio time overall and the large age split between listeners 18-34 and 35 and older.
- **S5** — [FCC Memorandum Opinion and Order Applying Section 310(d) Transfer Requirements](https://docs.fcc.gov/public/attachments/DA-24-9A1.pdf) (accessed 2026-07-22): Documents prior-consent and public-interest requirements for substantial assignment or transfer of station licenses and distinguishes pro forma changes.
- **S6** — [Broadcast Outlook 2025: Challenges, Opportunities Facing US TV, Radio Stations](https://www.spglobal.com/market-intelligence/en/news-insights/research/2025/10/broadcast-outlook-2025-challenges-opportunities-facing-us-tv-radio-stations) (accessed 2026-07-22): Provides forecasts for national and core local radio spot revenue through 2030 and notes cyclical political advertising.
- **S7** — [U.S. Local Radio Revenue Projected at $12.3 Billion in 2025](https://www.rab.com/public/pr/pr_detail.cfm?id=981) (accessed 2026-07-22): Provides BIA's 2025 local radio revenue projection including over-the-air and digital revenue and describes radio's local reach and trust.
