# reproduce.md — REPRODUCE skeptic

(Saved verbatim by the run's main session from the subagent's returned text; subagents in this harness return
findings as text instead of writing files. work/ paths refer to the skeptic's own isolated scratch folder.)

Claim: `5x6x7_m150_cr652_ZT_reduced.json` is a ternary straight-line program (SLP). It computes <5,6,7> exactly over Z with rank 150 and 652 reduced additions. That is below 664, the count of Perminov's only addition_reduced_ZT file for 5x6x7 rank 150.

## 1. Definition relied on (sources/perminov_README.md, quoted verbatim)

Full scheme format (fixes the meaning of u/v/w and the C^T convention):
- line 567: "* `n` - array `[n₁, n₂, n₃]` describing the dimensions (`A` is `n₁ × n₂`, `B` is `n₂ × n₃`);"
- line 572: "* `u` (machine-readable) - matrix encoding the linear form of `A`, size `m × (n₁·n₂)`;"
- line 573: "* `v` (machine-readable) - matrix encoding the linear form of `B`, size `m × (n₂·n₃)`;"
- line 574: "* `w` (machine-readable) - matrix encoding the linear form of `Cᵀ`, size `m × (n₃·n₁)`;"
- The 2x2x2 example (lines 579-628) confirms row-major A/B (`m4 = (a11 + a12) * (b22)` has u row `[1, 1, 0, 0]`). It also confirms C^T: m4 appears in c11 (-1) and c12 (+1), and its w row is `[-1, 0, 1, 0]`. So the w index for c_ij is j*n1+i.

Reduced scheme format:
- line 652: "* `n`, `m`, `z2` - these fields have the same meaning as in the full scheme format"
- line 656: "* `reduced` - number of additions after elimination of common subexpressions and simplification."
- line 665: `[{ "index": i, "value": c }, ...]`
- lines 670-672: "* For `U`: original indices: `0 ... n₁·n₂ - 1`, fresh indices start from: n1·n2;" / "* For `V`: original indices: `0 ... n₂·n₃ - 1`, fresh indices start from: n2·n3;" / "* For `W`: original indices: `0 ... m - 1`, fresh indices start from: m."
- line 679: "`u` and `v` arrays have exactly `m` rows each, `w` have `n₃·n₁` rows, and each row represents a sparse linear form:"

How w relates to C^T: in the reduced format, w has n3·n1 rows, one per entry of C^T in row-major order (row j*n1+i = c_ij). Each row is a form over products 0..m-1 and the w fresh variables.

Counting convention (CLAIM.md, under the bank's 'reduced' convention): "every form costs (number of terms - 1); negation free; only coefficients +-1."

## 2. Method (my checker written before opening the author's)

I wrote work/my_check.py from the definitions above before opening author_checker_fmm_check.py.

**Strict parse.** The parser rejects:
- duplicate JSON keys, float literals, NaN/Infinity, and booleans used as integers;
- a key set other than exactly {n,m,z2,complexity,u_fresh,v_fresh,w_fresh,u,v,w};
- z2 other than false;
- wrong row counts (u≠m, v≠m, w≠n3·n1).

**Each form.** A form must:
- be a non-empty list;
- contain only {index,value} terms with integer values in {-1,+1};
- use no index twice;
- reference only originals or earlier fresh variables (forward, self and out-of-range references are rejected);
- not expand to the zero form.

**Exact tensor identity over Z.** Fresh and final forms are expanded to integer vectors over the originals. I accumulate T[a,b,c] = Σ_k U[k][a]·V[k][b]·W[c][k]. I then compare it densely over every index triple (n1n2)·(n2n3)·(n3n1) = 30·42·35 = 44100 against δ(i,i')δ(l,l')δ(j,j'), with c = j'·n1 + i'. This is exhaustive, not a sample.

**Ternary.** Every coefficient written in the file is ±1, and every expanded coefficient (fresh and final) has |x| ≤ 1.

**Count.** The count is Σ over all u_fresh, v_fresh, w_fresh, u, v and w forms of (terms − 1).

**Calibration**
- README reduced 2x2x2 example (z2=true, so checked mod 2): count 15 = stated 15; exact under C^T; fails under plain C (8 mismatches). This confirms the convention.
- reference/: count 664 = stated complexity.reduced 664; exact over Z.

**Independent second method (work/evalslp.py).** This runs the SLP on 20 random integer 5x6 / 6x7 matrices with entries up to 1e6, counts each executed binary +/- (negation free), and compares against the naive A·B.

## 3. Real outputs

### my_check.py (run 1; run 2 is byte-identical: `cmp` → IDENTICAL; exit 0 both runs)
```
{"VALID": true, "arith": "Z", "cost_parts": {"u": 172, "v": 198, "w": 294}, "count_matches_stated": true, "exact": true, "expected_triples": 44100, "file": "reference/5x6x7_m150_cr664_fv310_cn2039_ZT_reduced.json", "first_mismatch": null, "format": "5x6x7", "fresh_counts": {"u": 79, "v": 86, "w": 145}, "max_abs_expanded_coef": {"u": 1, "v": 1, "w": 1}, "max_abs_expanded_fresh_coef": {"u": 1, "v": 1, "w": 1}, "mismatches": 0, "my_reduced_count": 664, "nonzero_tensor_entries": 210, "rank": 150, "stated_complexity": {"naive": 2039, "reduced": 664}, "ternary_expanded": true, "triples_checked": 44100, "unused_fresh": {"u": 0, "v": 0, "w": 0}, "w_convention": "C^T (row j*n1+i = c_ij)", "z2_flag": false}
{"VALID": true, "arith": "Z", "cost_parts": {"u": 167, "v": 191, "w": 294}, "count_matches_stated": true, "exact": true, "expected_triples": 44100, "file": "5x6x7_m150_cr652_ZT_reduced.json", "first_mismatch": null, "format": "5x6x7", "fresh_counts": {"u": 147, "v": 156, "w": 145}, "max_abs_expanded_coef": {"u": 1, "v": 1, "w": 1}, "max_abs_expanded_fresh_coef": {"u": 1, "v": 1, "w": 1}, "mismatches": 0, "my_reduced_count": 652, "nonzero_tensor_entries": 210, "rank": 150, "stated_complexity": {"naive": 2039, "reduced": 652}, "ternary_expanded": true, "triples_checked": 44100, "unused_fresh": {"u": 0, "v": 0, "w": 0}, "w_convention": "C^T (row j*n1+i = c_ij)", "z2_flag": false}
```
210 = 5·6·7 nonzero tensor entries, as required. The object under the plain-C convention is rejected (first mismatch at ((0,0),(0,1),(0,1)), got 0, want 1).

### README example calibration
```
{"VALID": true, "arith": "mod 2", "cost_parts": {"u": 4, "v": 4, "w": 7}, "count_matches_stated": true, "exact": true, "expected_triples": 64, ... "my_reduced_count": 15, ... "stated_complexity": {"naive": 24, "reduced": 15}, ... "w_convention": "C^T (row j*n1+i = c_ij)", "z2_flag": true}
--no-transpose: {"VALID": false, ... "mismatches": 8, ... "w_convention": "C (row i*n3+j = c_ij)"}
```

### Direct SLP evaluation (evalslp.py)
```
5x6x7_m150_cr652_ZT_reduced.json all 20 random trials correct: True | executed +/- ops: [652]
5x6x7_m150_cr664_fv310_cn2039_ZT_reduced.json all 20 random trials correct: True | executed +/- ops: [664]
```

### Structure (stats.py)
```
5x6x7_m150_cr652_ZT_reduced.json products used in w: 150 / 150 | distinct (U,V) pairs up to sign: 150 | single-term fresh forms: {'u': 55, 'v': 48, 'w': 0} | single-term final rows: {'u': 87, 'v': 79, 'w': 0}
5x6x7_m150_cr664_fv310_cn2039_ZT_reduced.json products used in w: 150 / 150 | distinct (U,V) pairs up to sign: 150 | single-term fresh forms: {'u': 0, 'v': 0, 'w': 0} | single-term final rows: {'u': 63, 'v': 49, 'w': 0}
product pairs shared with reference (up to sign): 150
```
- **Single-term fresh forms.** The object has 55 in u (42 with +1, 13 with −1) and 48 in v (35 with +1, 13 with −1). They are aliases or negations and cost 0, which matches both the convention and the direct operation count above.
- **Same products as the reference.** The object uses the same 150 bilinear products as Perminov's scheme, up to sign, and the identical W cost (294). It is a re-reduction of the U/V linear forms of the same rank-150 decomposition: U 172→167, V 198→191.
- **Rank.** All 150 products are used and pairwise distinct, so the rank is truly 150, not lower.

### Hashes
```
sha256sum -c CLAIM_SHA256.txt
5x6x7_m150_cr652_ZT_reduced.json: OK
reference/5x6x7_m150_cr664_fv310_cn2039_ZT_reduced.json: OK
```
(0b1bcf36...baea3c and ee197c7c...763ffb, also re-checked after all runs. One post-run check was accidentally run from the wrong directory and reported "No such file"; re-run from claim/ it gives OK for both.)

### Mutants (all rejected by my_check.py, exit 1)
```
flip_sign_u0             exit=1 VALID=False  exact=False mism=144 count=652 stated=652
coef_2_in_w              exit=1 VALID=False  w[3]: coefficient 2 not in [-1, 1]
empty_form_v5            exit=1 VALID=False  v[5]: empty form
dup_index_u7             exit=1 VALID=False  u[7]: duplicate index 132
forward_ref_ufresh0      exit=1 VALID=False  u_fresh[0]: forward/self/out-of-range reference index 35 (allowed < 30)
self_ref_vfresh10        exit=1 VALID=False  v_fresh[10]: forward/self/out-of-range reference index 52 (allowed < 52)
zero_coef_term           exit=1 VALID=False  u_fresh[2]: coefficient 0 not in [-1, 1]
w_row_missing            exit=1 VALID=False  w has 34 rows, expected n3*n1=35
u_row_missing            exit=1 VALID=False  u has 149 rows, expected m=150
stated_651               exit=1 VALID=False  exact=True mism=0 count=652 stated=651
z2_true                  exit=1 VALID=False  z2 is not false
extra_product_in_w0      exit=1 VALID=False  exact=False mism=4 count=653 stated=652
swap_u_rows              exit=1 VALID=False  exact=False mism=345 count=652 stated=652
w_out_of_range           exit=1 VALID=False  w[0]: forward/self/out-of-range reference index 295 (allowed < 295)
float_value              exit=1 VALID=False  float literal 1.0
dup_json_key             exit=1 VALID=False  duplicate JSON key 'm'
extra_key                exit=1 VALID=False  key set mismatch: missing [], extra ['extra']
zero_expanded_vfresh1    exit=1 VALID=False  v_fresh[1]: expands to the zero form
```

### Author's checker, exactly as in REPRODUCE.md
Command: `python -X utf8 author_checker_fmm_check.py 5x6x7_m150_cr652_ZT_reduced.json reference/5x6x7_m150_cr664_fv310_cn2039_ZT_reduced.json`, run with Python 3.12.6 from the venv. Run twice: exit 0 both times, outputs byte-identical.
```
{"format": "5x6x7", "rank": 150, "adds_U": 167, "adds_V": 191, "adds_W": 294, "reduced_additions": 652, "nonternary_coeffs": [], "exact_over_Z": true, "valid_ternary_slp": true, "stated_reduced": 652, "count_matches_stated": true, "error": null, "file": "5x6x7_m150_cr652_ZT_reduced.json"}
{"format": "5x6x7", "rank": 150, "adds_U": 172, "adds_V": 198, "adds_W": 294, "reduced_additions": 664, "nonternary_coeffs": [], "exact_over_Z": true, "valid_ternary_slp": true, "stated_reduced": 664, "count_matches_stated": true, "error": null, "file": "5x6x7_m150_cr664_fv310_cn2039_ZT_reduced.json"}
```
This matches the expected output in REPRODUCE.md. The per-block splits (167/191/294 and 172/198/294) are identical to mine.

Author's checker on some of my mutants:
```
mut_flip_sign_u0.json False False 652 True None []
mut_coef_2_in_w.json False False 652 True None ['2', 'expanded:2']
mut_forward_ref_ufresh0.json False False None None fresh[0]: forward/invalid reference 35 (have 30 vars) []
mut_w_row_missing.json False False 644 False row counts: U 150 V 150 W 34, expected 150 150 35 []
mut_stated_651.json True True 652 False None []
mut_zero_expanded_vfresh1.json False False None None fresh[1] expands to the zero form []
```
Columns are: exact_over_Z, valid_ternary_slp, reduced_additions, count_matches_stated, error, nonternary_coeffs. The mut_stated_651 result is correct behaviour: the author's checker reports the true count 652 and flags count_matches_stated=false.

### Context facts from the saved sources
- **sources/ hashes.** All seven sources/ files match the sha256 values in sources/FETCH_LOG.md (all HTTP 200, 2026-10-15T09:34Z).
- **Best rank.** fmm_sota.json entries for {5,6,7}: `[{'format': [5, 6, 7], 'rank': 150, 'exponent': 2.811222}]`. Rank 150 is the best listed.
- **Perminov's directory.** perminov_tree.json has exactly one addition_reduced_ZT file for 5x6x7, or for any permutation of (5,6,7): `schemes/results/addition_reduced_ZT/5x6x7_m150_cr664_fv310_cn2039_ZT_reduced.json`. The minimum cr is 664. The reference/ copy is that file, and its stated reduced count, 664, is reproduced exactly.
- **Other Perminov sources.** reduced_known.json has no 5x6x7 entry. README mentions 5x6x7 only as rank 150 (lines 414, 1096), with no reduced count. CHANGELOG has no 5x6x7 mention.
- **Lille.** lille_5x6x7.html gives ⟨5×6×7:150⟩ (Kauers–Wood, arXiv 2505.05896) and cites no addition-count variant.
- **matmulcatalog.** COVERAGE.md row `⟨5,6,7⟩`: 150, adds `+2039`.
- **Conclusion.** 652 < 664 and 652 < 2039. No lower count for this format and rank appears in any saved source.

## 4. Discrepancies
- Object and claim: none. My checker and the author's checker agree on every reported field, for both files. Both are deterministic across two runs.
- Minor, author's checker only: it does not check `z2 == false` or reject extra or duplicate JSON keys. The object passes those checks in my checker, so this does not affect the verdict.
- Minor, outside the claim's evidence: sources/FETCH_LOG.md lists an 8th fetch (`v3r1t4s_open_prs.json`) that is not present in sources/. It is not used by the claim.
- Observation, not a defect: the object uses the same 150 products as Perminov's rank-150 scheme. The improvement is purely additive (U and V forms re-reduced). This is consistent with the target, which is an addition-count record at the best rank, not a rank record.
- Limits of this check: I verified against the saved snapshots only (no network). Whether these are still the live minima now is for the other skeptics.

context: Claude Code Agent-tool subagent, model claude-opus-5-5, effort high, saw only a copy of claim/

pass: true
