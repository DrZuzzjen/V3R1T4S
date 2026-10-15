# PREREG (frozen 2026-10-14T18:21:12Z UTC, before any attack output)

## Criterion (verbatim): see target.md (copied from repo/bank/targets.json). Partial wins p1, p2, p3 verbatim there.

## Statistic and checker
- Object: a scheme JSON in Perminov layout (n, m, u_fresh/u, v_fresh/v, w_fresh/w).
- Checker: checker/fmm_check.py (exact integer tensor identity over Z, all 3 maps; outputs indexed C^T row-major as
  calibrated on 113/113 published files). Statistic: reduced_additions = sum(len(form)-1) over all forms; any
  coefficient outside {-1,+1} => invalid.
- Eligibility: format max dim <= 8, rank == fmm_sota.json rank for the sorted format (data/fmm_sota.json, re-fetched
  before claiming).
- Reference: minimum cr over ALL live addition_reduced_ZT files for that format and rank, recounted by the same
  checker; also reduced_known.json, README, CHANGELOG, Lille per-format page and matmulcatalog COVERAGE adds.

## Thresholds
- Candidate: reduced_additions <= reference - 1 (strict), exact_over_Z true, ternary true, rank equal.
- A tie (== reference) is recorded as a rediscovery, never a claim.
- p1: 3x3x3 rank 23 with <= 57. p3: three distinct eligible formats each strictly below.
- p2 is out of scope for this cycle's tools unless a rank-48 rational 4x4x4 operation count is found; not claimed.

## Null design
null_test: not needed because the claim is an explicit object checked by a deterministic exact checker against a
table value (no search statistic or "beats chance" claim is involved).

## Independent verification plan
Any candidate gets an independent recount in a second representation (lens skeptic) and then three fresh-context
skeptics (Claude Code subagents) that see only claim/.
