# v4.2 rejection record

**Status:** rejected at the preregistered five-record development gate. The
v4.2 holdout and full Phase 4 campaign were not run.

This is an outcome-blind change-control decision. It is based on evidence
feasibility and contract/tooling failures, not on any named score, rank, color,
verdict, or movement from an earlier version. The governing rules are
`V4_2_METHODOLOGY.md` §12 and
`pipeline/v4_2/change_control.json`.

## Frozen authority

The accepted development campaign is
`pipeline/v4_2/campaigns/v42-regression-20260721-freeze8.json`:

- commit: `8de38c5aa9437e77beb696e46099c02a960b242e`
- signed tag: `v4.2-freeze-2026-07-21-8`
- tag object: `d59d8734c5fec59a2eef5d101795db7060f5748f`
- freeze root: `1f1fedba7760aad8f4589d40d0f984c7d73359557f3839efa4c2104dc0a475a2`
- freeze manifest SHA-256:
  `48e6fb425e8f03b147f540bce83c04b6689bad49ecb57d6d26d94eb6db806f43`
- campaign manifest SHA-256:
  `0ef90270215ad94dc1394ded16a3be34bded65ddc9ccc4bc521538debb9830bc`
- issuance plan: `pipeline/v4_2/issuance/v42-regression-20260721-freeze8.json`
  (`2f1e4e851ec584b4bcab086864c8e222df194b24ab91ee295b6f4df526a4b79b`)

The campaign manifest binds the exact datasets, specifications, prompts,
envelopes, packets, records, memos, reviews, model routes, and freeze
authorization. Earlier v4.2 campaign attempts are not authority for this
decision.

## Exact five-record result

`missing` is the length of
`decision.evidence_readiness.missing_critical_inputs` in the exact record.
Every record is therefore `critical_unbounded` under
`pipeline/build/build_gate_report_v4_2.py`.

| NAICS | Entry | Record SHA-256 | Review SHA-256 | Binding SHA-256 | Review outcome | Missing |
|---|---|---|---|---|---|---:|
| 238220 | `entry_v42_89401bc7221634caeabb94b5_a1` | `f470d76ddffdfee5eeebc1f488ed4e03ba4ea2cc4d511675ca8e4b553251da64` | `1172a4010445ff4443d55aa2891d68fa3cc89a150fde5d32de8d29be82125efe` | `9b0a79c8ec8e74e9cca41b23fcb550e18d14408902889f1539bfe97c200590d1` | `reject` | 27 |
| 541214 | `entry_v42_37b45406f68349e7329e3e6b_a1` | `6209221b749c5428c74a4f2ef3bbed6e004ba64266864e0a813c7921b1f3437f` | `647f75f29c653dd602d663dc41f109fe87ac1f080a4e6a0c8e0167581b92cc8b` | `30147a3af67eb93325a68d0749a78ea693a02fd43f5cc8ce813bd5c68490c305` | `publishable_with_caveats` | 27 |
| 541511 | `entry_v42_9628272b84d1db0c9b13bdf8_a1` | `04a2ce3ef18e4bda919024c1a50068453805ff28f73d27937a7cefd244abfc2b` | `835fc10667c8796b614c5be586dd77a2755f223d79b50e57f4dd916a6320564b` | `7c1392061ad3e4b0d9c7ef9577133ecf49986f7a5b07cef1fc5707a310de4c21` | `publishable_with_caveats` | 27 |
| 541512 | `entry_v42_82883d45dde1e583f40100c1_a1` | `d3ef6693c083d89a439df1141ddded908b6f5c5284e6715ec655349e27fb2b52` | `2802c6635d0292ccb3b6e5d69a6d5aa111a86c0f321754246db78711c40accab` | `0fcb0fd41d8bb1e488c99f7fd17a3e5ba6cbf128957ee04ba8750425021adaf5` | `reject` | 27 |
| 541930 | `entry_v42_c2d98b424aa61ca1c8b8c259_a1` | `ba7c2a5c7da4c51dee8289c2ec2eb78f65987987c634348ab7a63d309d1e1b57` | `11167ebf6cec0264dd1d7a2a61b3f3f63b7c599ecc4e0d77f090a7e5b965c27e` | `0a608c5965d8dfaaab3bd6cc4a490e69cd1eaae12685147763e867eadfadab1a` | `publishable_with_caveats` | 30 |

The exact records are under `pipeline/v4_2/runs/` and the exact reviews are
under `pipeline/v4_2/reviews/`, using each entry's run ID as the filename.

## Decisive evidence gate

The deterministic gate rule in `pipeline/build/build_gate_report_v4_2.py` is:

- pass only when at most one of five records is critical-unbounded;
- reject when at least two of five are critical-unbounded; and
- require a replacement methodology version on rejection.

The observed count is **5/5**, against the rejection threshold of **2/5**.
The individual missing-critical counts are **27, 27, 27, 27, and 30**. This
alone activates the preregistered `preregistered_evidence_infeasibility`
change-control trigger. No threshold or named result may be tuned to reverse
it.

## Review-contract finding

The isolated reviews expose an ambiguity in
`pipeline/template/validator_brief_v4_2.md`: it says both that unsupported
critical evidence cannot receive a publishable disposition and that an honest
low-readiness result may be publishable. All five records honestly map missing
or assumption-backed primitives to `UNPROVEN`, yet two reviewers returned
`reject` and three returned `publishable_with_caveats`. The contract does not
state a reproducible materiality boundary that resolves those instructions.
This is a review/evidence-contract failure, independent of the decisive 5/5
gate rejection.

Two reject findings are also genuine record-specific archetype defects, not
merely this ambiguity:

- In `pipeline/v4_2/reviews/v42_89401bc7221634caeabb94b5_a1.json`, the 238220
  low/high archetype counts and coverage endpoints come from an unsupported
  common 0.75x–1.25x revenue-to-firm-count heuristic. The registered sources
  support neither that bridge nor its endpoints.
- In `pipeline/v4_2/reviews/v42_82883d45dde1e583f40100c1_a1.json`, the 541512
  archetype claims transfer broad channel/all-size product statistics into the
  frozen target band without an evidenced bridge; two registered sources were
  not reopenable. The affected bases and range endpoints are not supported.

## Frozen tooling defects

Two independent frozen-toolchain defects prevent treating the campaign as a
successful gate even apart from evidence infeasibility:

1. The attempt-2 path in the tagged
   `pipeline/build/issue_campaign_v4_2.py` requires the predecessor campaign's
   `issuance_plan` reference to contain `path`, `sha256`, and `byte_length`.
   The canonical manifest produced and validated by
   `pipeline/build/campaign_v4_2.py` contains only `path` and `sha256`, as seen
   in the exact freeze8 campaign. Thus the frozen remediation issuer rejects
   its own valid predecessor manifest before it can authorize bounded
   remediation.
2. `pipeline/build/build_gate_report_v4_2.py` freezes per-module sentinel
   counts totaling **133**, while the seven frozen sentinel modules actually
   run **136** tests. The suite passes, but gate-report construction fails
   closed on the stale expected counts, so no valid gate certificate can be
   issued.

These defects require a new frozen version; patching them in place would alter
the authority under which the records were issued.

## Change-control disposition

v4.2 is rejected. No v4.2 holdout was opened, no v4.2 full fleet was issued,
and no v4.2 Phase 4 publication was produced. A successor must use a new
version, clarify the review materiality rule, fix and test remediation/gate
issuance before freezing, and select a newly salted untouched holdout as
required by `pipeline/v4_2/change_control.json`.

All v4.2 packets, records, memos, reviews, claims, issuance plans, campaign
manifests, tags, and receipts are preserved as audit evidence. They must not be
deleted, overwritten, reinterpreted as a completed Phase 4, or silently
promoted into a successor version.
