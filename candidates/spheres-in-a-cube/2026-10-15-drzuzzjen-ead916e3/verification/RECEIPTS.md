# Verification receipts

Executed on Mac at 2026-10-15T14:39:06.580951+00:00.

`python3 -I verify.py` checked all 73920 pairs and 2310 individual wall constraints with exact integer inequalities, with zero violations. Last line: `PASS`. The complete result is exact-integer-result.json.

The supplied 50-decimal mpmath checker independently returned claimed_feasible=true and feasible_radius=0.0725678002281957; see mp50-result.json. Its closest-pair indices are zero-based; the exact checker reports one-based indices.

Negative controls: coincident centers rejected, center outside the cube rejected. Both produced exit 1 and FAIL; only temporary copies were modified.
