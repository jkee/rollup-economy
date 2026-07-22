# v5.1 cross-sector canary report

**Date:** 2026-07-22  
**Status:** ready for Victor's fleet-approval gate; not approved  
**Contract:** `aab2c9e92e78bce09e2d306b237ffda9ce828ae72772be3c11cbfbf6d8786763`

## Gate summary

All ten frozen canary codes completed fresh attempt-1 research, deterministic
validation/finalization/check, and isolated review. All ten reviews passed
`build.py validate-review` against the exact artifact bytes. Outcomes were
10 `publishable_with_caveats`, 0 `publishable`, 0 `reject`, and 0 `invalid`.
There were no material findings, no remediations, and no exclusions. The
predeclared pause trigger did not fire.

The canary used 20 model sessions: 10 research and 10 review, against the
launch-fixed ceiling of 1,400. Research ran as `claude-sonnet-5`; review ran
as `claude-fable-5`, matching the committed launch record.

**Recommendation:** approve the fleet without a territory descope. The frozen
lens remained useful as a screen: it allowed goods industries to screen out
for explicit weakest-link economics, and it allowed agriculture and public
administration to return an honest evidence-first result instead of forcing a
private-company opportunity. The caveats below remain binding; approval does
not turn estimates into observed evidence.

## Record outcomes

| NAICS | Territory | Base tier | Tier interval | Base H | Readiness / action | Review |
|---|---|---|---|---:|---|---|
| 238910 | Site preparation | `STRUCTURAL_OUT` | `STRUCTURAL_OUT`–`LOW_PRIORITY` | 0.73 | `MODEL_CONDITIONED / VALIDATE_ASSUMPTIONS` | accepted with caveats |
| 311612 | Meat processing | `STRUCTURAL_OUT` | `STRUCTURAL_OUT` | 0.39 | `MODEL_CONDITIONED / VALIDATE_ASSUMPTIONS` | accepted with caveats |
| 332710 | Machine shops | `LOW_PRIORITY` | `STRUCTURAL_OUT`–`CONDITIONAL` | 1.17 | `MODEL_CONDITIONED / VALIDATE_ASSUMPTIONS` | accepted with caveats |
| 423840 | Industrial-supplies wholesale | `STRUCTURAL_OUT` | `STRUCTURAL_OUT`–`LOW_PRIORITY` | 0.66 | `MODEL_CONDITIONED / VALIDATE_ASSUMPTIONS` | accepted with caveats |
| 445110 | Grocery retail | `STRUCTURAL_OUT` | `STRUCTURAL_OUT`–`LOW_PRIORITY` | 0.50 | `MODEL_CONDITIONED / VALIDATE_ASSUMPTIONS` | accepted with caveats |
| 484110 | Local freight trucking | `LOW_PRIORITY` | `STRUCTURAL_OUT`–`CONDITIONAL` | 1.28 | `MODEL_CONDITIONED / VALIDATE_ASSUMPTIONS` | accepted with caveats |
| 522310 | Loan brokers | `PRIORITY` | `CONDITIONAL`–`HIGHEST_PRIORITY` | 5.76 | `MODEL_CONDITIONED / VALIDATE_ASSUMPTIONS` | accepted with caveats |
| 621111 | Physician offices | `CONDITIONAL` | `LOW_PRIORITY`–`PRIORITY` | 3.45 | `MODEL_CONDITIONED / VALIDATE_ASSUMPTIONS` | accepted with caveats |
| 111998 | Miscellaneous crop farming | no base | `STRUCTURAL_OUT`–`HIGHEST_PRIORITY` | — | `STRESS_TEST_ONLY / EVIDENCE_FIRST` | accepted with caveats |
| 921190 | General government support | no base | `STRUCTURAL_OUT`–`HIGHEST_PRIORITY` | — | `STRESS_TEST_ONLY / EVIDENCE_FIRST` | accepted with caveats |

Aggregate base tiers were 4 `STRUCTURAL_OUT`, 2 `LOW_PRIORITY`, 1
`CONDITIONAL`, 1 `PRIORITY`, and 2 without a base. Eight records were
`MODEL_CONDITIONED / VALIDATE_ASSUMPTIONS`; two were
`STRESS_TEST_ONLY / EVIDENCE_FIRST`. Validators recorded 66 caveats in total,
all non-material under the frozen tier-or-action test.

## Required canary reads

### A. Is H informative where labor share is structurally small?

Yes. The goods/construction/trade records did not fail mechanically or collapse
into arbitrary narratives; they screened out through the stated economics.
Site preparation, meat processing, industrial-supplies wholesale, and grocery
retail all had strong breadth aggregates but base H below 0.75, making labor
opportunity the explicit weakest link. Machine shops and local trucking also
had low base H (1.17 and 1.28) and landed `LOW_PRIORITY`. This is the expected
behavior of a compensation-to-receipts screen in physical, inventory-heavy,
or COGS-heavy industries, not evidence noise. By contrast, loan brokers and
physician offices produced materially higher H (5.76 and 3.45), so the factor
still differentiates territories rather than merely suppressing the whole
canary.

The limitation is unchanged: task exposure and five-year implementation were
mostly proxies or estimates. H explains the screen result; it is not a claim
about EBITDA uplift.

### B. Do q and s5 find real evidence outside services?

They found real directional evidence, but not denominator-matched measurement.
For the eight scored records, `q` was honestly labeled `ESTIMATE`; `s5` was a
disclosed `PROXY`. The sources supported contract mechanics, owner-age and
succession context, transaction examples, and deal-flow direction. Validators
reopened every cited source and found no material unsupported mechanism.

The recurring caveat was consistent across territories: none of those sources
directly measured five-year retained AI benefit or completed qualifying control
transfers for the exact LMM lens. That makes these primitives useful bounded
screen inputs, not observed rates. The government-support record correctly used
`MISSING` for both rather than inventing a commercial retention or transfer
market.

### C. Is the frozen lens coherent for goods and public-sector codes?

Yes as a prioritization screen, with disclosed edge cases. It did not require
goods industries to resemble subscription software. Repeat project work,
processing programs, purchase orders, replenishment, local freight, and medical
or brokerage transactions supplied coherent repeat-service units. Meat
processing and crop farming disclosed heterogeneous-code narrowings rather than
shopping for a favorable population.

The hardest cases were grocery retail, miscellaneous crop farming, and general
government support. Grocery's eligible outsourced-service subset is rare; crop
farming had to narrow to genuine fee-paid production-contract growers; and
government support identified no verified commercial external-customer or
transferable-firm population. Those are economically informative negative or
evidence-first results, not forced positive constructs. Reviewers accepted all
three with caveats and no material finding. No territory currently meets the
plan's descoping test, although the corresponding fleet block reports should
continue to call out these structural limitations rather than interpret an
unscored record as neutral.

### D. Does the declared-gap path route and render honestly?

Yes. `111998` and `921190` both received dataset-injected `MISSING` H and F
inputs, no base A/L or tier, the full semantic tier interval, and
`STRESS_TEST_ONLY / EVIDENCE_FIRST`. `921190` additionally kept commercial
retention and transfer primitives `MISSING`. Neither record converted a gap to
zero, and both memos rendered the evidence-first state. Their reviews passed
the exact-byte gate and explicitly confirmed that the missing anchors prevented
a forced conclusion.

## Gate decision requested

Victor should either:

- approve fleet work by adding and committing `canary_approved` in
  `pipeline/v5_1/campaign_state.json` (and updating the plan mirror in the same
  commit); or
- stop/redirect with a stated reason.

Until that committed record exists, every fleet block remains gated and no
fleet research may start.
