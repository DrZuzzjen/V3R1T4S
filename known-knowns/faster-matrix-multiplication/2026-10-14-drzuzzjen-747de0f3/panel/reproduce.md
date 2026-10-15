# reproduce.md — REPRODUCE skeptic

(Saved verbatim by the run's main session from the subagent's returned text; subagents in this harness return
findings as text instead of writing files. "../work/" paths refer to the skeptic's own isolated scratch folder next
to its copy of claim/.)

**Claim under test:** `4x6x7_m123_cr503_ZT_reduced.json` is an exact ternary SLP for <4,6,7> over Z with rank 123 and 503 reduced additions. The comparison baseline is Perminov's `reference/4x6x7_m123_cr517_cn1586_ZT_reduced.json` (517).

## 1. Definition used (quoted from sources/perminov_README.md, "Scheme File Formats")

Full format, which says how `w` relates to C:
> `* n - array [n₁, n₂, n₃] describing the dimensions (A is n₁ × n₂, B is n₂ × n₃);`
> `* w (machine-readable) - matrix encoding the linear form of Cᵀ, size m × (n₃·n₁);`

Reduced format:
> `"complexity": {"naive": x, "reduced": y}, "u_fresh": [...], "v_fresh": [...], "w_fresh": [...], "u": [...], "v": [...], "w": [...]`
> `* reduced - number of additions after elimination of common subexpressions and simplification.`
> `[{ "index": i, "value": c }, ...]`
> `* For U: original indices: 0 ... n₁·n₂ - 1, fresh indices start from: n1·n2;`
> `* For V: original indices: 0 ... n₂·n₃ - 1, fresh indices start from: n2·n3;`
> `* For W: original indices: 0 ... m - 1, fresh indices start from: m.`
> `` `u` and `v` arrays have exactly `m` rows each, `w` have `n₃·n₁` rows, and each row represents a sparse linear form ``

- **How w maps to C:** w encodes Cᵀ, so output row `j*n1+i` holds c_ij. I checked this orientation by hand on the README's full (2,2,2:7) example: c12 = m4+m5 and c21 = m6+m7 land on Cᵀ row-major columns 2 and 1.
- **Indexing of A and B:** A is row-major (`i*n2+k`) and B is row-major (`k*n3+j`).
- **Counting rule:** sum over all forms (fresh and final) of (terms-1). This rule reproduces the README's own reduced (2,2,2:7) example: 6 + 2 + 2 + 5 = 15 = its stated `"reduced": 15`.

## 2. My checker (../work/my_check.py)

I wrote it from the definition above before opening author_checker_fmm_check.py. Method:

- **Strict parse:**
  - UTF-8 strict.
  - Reject duplicate JSON keys, float or NaN literals, and bool-as-int.
  - Top-level keys must be exactly the README's ten.
  - `z2` must be false.
  - `n` must be 3 positive ints; `m` must be a positive int.
  - `complexity` must have exactly {naive, reduced} as ints.
- **Each form:**
  - must be a non-empty list of `{"index","value"}` terms with int values;
  - the coefficient must be in {-1,+1};
  - no duplicate index within a form;
  - index range: fresh form k may only reference originals or fresh < k (no self or forward reference); final forms may reference originals or any fresh.
- **Expansion:** every fresh and final form is expanded to a dense integer vector over the original variables. A zero expansion is rejected. Row counts must be u = m, v = m, w = n3·n1.
- **Ternary:** the max |coefficient| of every expanded final form and every expanded fresh form must be 1.
- **Exactness:** a full tensor identity over Z on every index triple (24 × 42 × 28 = 28224 triples, not a sample): T[a,b,c] = Σ_r U[r,a]·V[r,b]·W[c,r] must equal the <4,6,7> structure tensor, with c = j*n1+i. I computed it twice, once in int64 and once with Python big ints.
- **Secondary check:** I executed the SLP literally, step by step, on 5 fixed-seed random integer matrix pairs with entries in [-10^6, 10^6], and compared against A·B.
- **Count:** additions = Σ over all forms of (terms-1), with a per-block breakdown.
- **Negative controls:** I wrote 8 mutants of the object (in ../work/) and ran them through the checker. All were rejected:

```
mut_coef2.json VALID= False u[0]: coefficient 2 not in {-1,1}
mut_dupindex.json VALID= False w[0]: duplicate index 3
mut_emptyform.json VALID= False w[0]: empty form
mut_forwardref.json VALID= False v_fresh[3]: index 52 out of allowed range [0,45) (forward/self ref or out of range)
mut_rowcount.json VALID= False u: 122 final rows, expected 123
mut_selfref.json VALID= False v_fresh[3]: index 45 out of allowed range [0,45) (forward/self ref or out of range)
mut_signflip.json VALID= False mismatches=4
mut_windex.json VALID= False mismatches=44
```

## 3. My checker: real output

Command, from claim/:
`python -I ../work/my_check.py reference/4x6x7_m123_cr517_cn1586_ZT_reduced.json 4x6x7_m123_cr503_ZT_reduced.json`

I ran it twice. `cmp run1.txt run2.txt` reported IDENTICAL, so the output is deterministic.

```
{"VALID": true, "additions": 517, "additions_breakdown": {"u": 75, "u_fresh": 53, "v": 93, "v_fresh": 71, "w": 106, "w_fresh": 119}, "count_equals_stated_reduced": true, "exact_over_Z": true, "expanded_final_ternary": true, "expanded_maxabs_final": [1, 1, 1], "expanded_maxabs_fresh": [1, 1, 1], "file": "reference/4x6x7_m123_cr517_cn1586_ZT_reduced.json", "format": "4x6x7", "fresh_counts": [53, 71, 119], "keys": ["complexity", "m", "n", "u", "u_fresh", "v", "v_fresh", "w", "w_fresh", "z2"], "m": 123, "products_unused_in_W": [], "sha256": "8c385f50b3e85e7c750e6ace7e1e3b835e2fdf3f348f8ff9ae94931a755367dd", "slp_execution_5_random_ok": true, "stated_complexity": {"naive": 1586, "reduced": 517}, "tensor_mismatches": 0, "tensor_mismatches_objectint": 0, "triples_checked": 28224}
{"VALID": true, "additions": 503, "additions_breakdown": {"u": 59, "u_fresh": 62, "v": 61, "v_fresh": 96, "w": 106, "w_fresh": 119}, "count_equals_stated_reduced": true, "exact_over_Z": true, "expanded_final_ternary": true, "expanded_maxabs_final": [1, 1, 1], "expanded_maxabs_fresh": [1, 1, 1], "file": "4x6x7_m123_cr503_ZT_reduced.json", "format": "4x6x7", "fresh_counts": [119, 125, 119], "keys": ["complexity", "m", "n", "u", "u_fresh", "v", "v_fresh", "w", "w_fresh", "z2"], "m": 123, "products_unused_in_W": [], "sha256": "747de0f311caaf359538b14522c33523b83bf154bea1255cb02b2e8de977c5a0", "slp_execution_5_random_ok": true, "stated_complexity": {"naive": 1586, "reduced": 503}, "tensor_mismatches": 0, "tensor_mismatches_objectint": 0, "triples_checked": 28224}
```

- **Calibration:** on Perminov's own file my count is 517, equal to its stated `complexity.reduced`.
- **Object:**

  | Property | Result |
  |---|---|
  | Exact over Z | yes, 0 mismatches out of 28224 triples |
  | Ternary | yes, every expanded fresh and final form has max \|coef\| = 1, and every step coefficient is ±1 |
  | Rank | 123; every product has a non-zero u and v form and is used in W |
  | Additions | 503 |
  | Literal SLP execution | correct |
  | Format | 4x6x7, z2 false |

## 4. sha256

`sha256sum` output:
```
747de0f311caaf359538b14522c33523b83bf154bea1255cb02b2e8de977c5a0 *4x6x7_m123_cr503_ZT_reduced.json
8c385f50b3e85e7c750e6ace7e1e3b835e2fdf3f348f8ff9ae94931a755367dd *reference/4x6x7_m123_cr517_cn1586_ZT_reduced.json
```
Both match CLAIM_SHA256.txt exactly.

## 5. Extra checks on how the count is reached

Term-length statistics (../work/stats.py):

**Object:**
```
  u_fresh rows 119 len-hist {1: 57, 2: 62} single(+1) 47 single(-1) 10
  v_fresh rows 125 len-hist {1: 46, 2: 66, 3: 10, 4: 2, 5: 1} single(+1) 31 single(-1) 15
  w_fresh rows 119 len-hist {2: 119}
  u rows 123 len-hist {1: 65, 2: 57, 3: 1}
  v rows 123 len-hist {1: 66, 2: 53, 3: 4}
  w rows 28 len-hist {2: 2, 3: 8, 4: 3, 5: 5, 6: 6, 7: 1, 8: 2, 10: 1}
  no unused fresh variables, no unused originals
```

**Reference:** u_fresh 53 and v_fresh 71, all of length 2. Its final u and v rows also contain single-term -1 forms (u: 2, v: 11), so Perminov's own file treats negation as free.

- **w side:** `w_fresh` and `w` are byte-for-byte identical to the reference's. All 14 saved additions are on the A and B sides: u is 121 vs 128 and v is 157 vs 164.
- **Single-term fresh forms:** the object has 57 in u_fresh and 46 in v_fresh. They are pure aliases (+1) or negations (-1), cost 0 under the stated convention, and cannot hide an operation.
- **Aliases hiding repeats:** I resolved aliases to their root variable and checked for duplicates within each form (../work/alias.py), to rule out x + alias(x) = 2x or a hidden cancellation. Result: 0 forms in the object, 0 in the reference. Coefficient 2 is in any case already excluded by the expanded-ternary check.

## 6. Author's checker (run only after the above, exactly as REPRODUCE.md says)

`python -X utf8 author_checker_fmm_check.py 4x6x7_m123_cr503_ZT_reduced.json reference/4x6x7_m123_cr517_cn1586_ZT_reduced.json`

Python 3.12.6. I ran it twice and the outputs were IDENTICAL.

```
{"format": "4x6x7", "rank": 123, "adds_U": 121, "adds_V": 157, "adds_W": 225, "reduced_additions": 503, "nonternary_coeffs": [], "exact_over_Z": true, "valid_ternary_slp": true, "stated_reduced": 503, "count_matches_stated": true, "error": null, "file": "4x6x7_m123_cr503_ZT_reduced.json"}
{"format": "4x6x7", "rank": 123, "adds_U": 128, "adds_V": 164, "adds_W": 225, "reduced_additions": 517, "nonternary_coeffs": [], "exact_over_Z": true, "valid_ternary_slp": true, "stated_reduced": 517, "count_matches_stated": true, "error": null, "file": "4x6x7_m123_cr517_cn1586_ZT_reduced.json"}
```

The author's checker agrees with mine on every block:

| Block | Object (author) | Object (mine) | Reference (author) | Reference (mine) |
|---|---|---|---|---|
| U | 121 | 62 + 59 = 121 | 128 | 53 + 75 = 128 |
| V | 157 | 96 + 61 = 157 | 164 | 71 + 93 = 164 |
| W | 225 | 119 + 106 = 225 | 225 | 119 + 106 = 225 |
| Total | 503 | 503 | 517 | 517 |

Its Cᵀ orientation (`c = k*n1+i`) and its validity rules are the same as mine. It matches the expected output in REPRODUCE.md.

## 7. Baseline, from the saved sources only (no network; I did not re-fetch)

- **Perminov tree** (sources/perminov_tree.json): the only `addition_reduced_ZT` path for 4x6x7 is `4x6x7_m123_cr517_cn1586_ZT_reduced.json`. The other 4x6x7 paths are results/ZT, naive_addition_reduced_ZT (c1562, c1586), serendipitous_base and known/tensor.
- **reduced_known.json:** 0 matches for 4x6x7.
- **fmm_sota.json:** `{'format': [4, 6, 7], 'rank': 123, ...}`.
- **matmul_COVERAGE.md:** ⟨4,6,7⟩ 123, adds column +1586.
- **README:** lists 4x6x7 rank 123 with no addition count.
- **Lille page:** ⟨4×6×7:123⟩. I only grepped the saved page and saw no complexity figure.

So, on these snapshots, 503 < 517 is the minimum reduced count. Whether these sources are still current is for the other skeptics to judge.

## 8. Discrepancies

None. Every property in the claim reproduced exactly with my own independent checker: format, rank 123, exact over Z on all 28224 triples, ternary, 503 additions (calibrated at 517 on the reference), sha256, and determinism. The author's checker gives identical numbers.

context: Claude Code Agent-tool subagent, model claude-opus-5-5, effort high, saw only a copy of claim/

pass: true
