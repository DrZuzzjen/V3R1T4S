# PREREG (frozen 2026-10-15T09:35:12Z UTC, before any attack output of this run)

## Criterion (verbatim): see target.md (copied from repo/bank/targets.json). Partial wins p1, p2, p3 verbatim there.

## Statistic and checker
- Object: a scheme JSON in Perminov's reduced layout. Checker: checker/fmm_check.py (exact integer tensor identity over
  Z, C^T output layout per README, strict validation; reduced_additions = sum over all forms of (terms - 1)).
- Eligibility: max dim <= 8 and rank == fmm_sota.json rank of the sorted format (data/fmm_sota.json).
- Reference: minimum cr over all live addition_reduced_ZT files for that format and rank, recounted by the checker,
  plus reduced_known.json, README, CHANGELOG, the Lille per-format page and matmulcatalog COVERAGE adds; re-fetched
  immediately before any claim.

## Thresholds
- Candidate: reduced_additions <= reference - 1, exact_over_Z true, valid_ternary_slp true, rank equal. A tie is a
  rediscovery, never a claim. One cell per claim; the panel sees one object.
- An improvement of one of OUR earlier cells is only a claim if it is strictly below the live table value (our own
  unpublished values are not the reference; a lower value of ours just replaces the carried object).

## Null design
null_test: not needed because each claim is an explicit object checked by a deterministic exact checker against a
table value (no search statistic or "beats chance" claim is involved).
