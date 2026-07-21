# v3.1.2 isolated research-runner brief

Own at most two codes. Do not spawn, delegate or read another runner's packet.
Fleet research must run as `gpt-5.6-terra`; golden research must run as
`gpt-5.6-sol`. A golden runner may not read `golden_set.json`, prior golden
records/reviews/conclusions or another model's result.

For each assigned code:

1. Read only its frozen prompt in `pipeline/prompts_v3_1_2/<naics>.md`, its
   deterministic dataset and its block/source hints. Replace the four runtime
   placeholders with the exact model/date/run identity supplied by the
   orchestrator. `PROMPT_VERSION` is exactly `v3.1.2-text-first-1`; any other
   value is a fatal mechanics error.
2. Research the industry and write exactly one canonical packet to
   `pipeline/packets/<naics>/<run-id>.json`. Do not write scores or prose
   anywhere else and do not modify prior-version artifacts.
3. Reopen every score-driving source. Material factual/numeric support must be
   real; exact quotation and forensic scope metadata are optional. State broad
   proxies, old sources and scope mismatches as score-input caveats.
4. Validate with `research_packet_v3_1_2.schema.json`, then run:

   `python3 pipeline/build/finalize_run_v3_1_2.py --packet <packet> --dataset <dataset> --kind fleet|golden --output <run> --memo <memo>`

   Fleet output is `pipeline/runs/<naics>/<run-id>.json`; golden output is
   `pipeline/golden_v3_1_2/<naics>/<run-id>.json`; both use
   `pipeline/memos/<naics>/<run-id>.md`. Never use an overwrite flag and never
   hand-edit the final record or memo.
5. Independently reload the packet/run/memo and verify exact identity, role
   membership, source-ID references, dataset equality, finite inputs, zero
   arithmetic mismatch and fresh finalizer/memo equality. Self-report is not
   acceptance; the orchestrator repeats every check.

For attempt 2 only, the orchestrator supplies the exact prior Sol findings.
Set `attempt: 2` and `remediates_run_id`; write a new run ID. Fix only the
record-specific material/fatal findings. No third attempt is permitted.
