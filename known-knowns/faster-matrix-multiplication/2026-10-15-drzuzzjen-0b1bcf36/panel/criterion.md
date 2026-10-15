# Criterion skeptic verdict: 5x6x7 rank-150 reduced-addition claim (652 vs 664)

(Saved verbatim by the run's main session from the subagent's returned text; subagents in this harness return
findings as text instead of writing files. work/ paths refer to the skeptic's own isolated scratch folder.)

I wrote my own checker first, in work/check.py, work/run_slp.py, work/compare.py, work/tree_scan.py, work/sota.py and work/misc.py. I read and ran the author's checker only after that.

## Integrity of the evidence
- sha256 of the object and the reference both match CLAIM_SHA256.txt. Object: 0b1bcf36...a3c. Reference: ee197c7c...ffb.
- The sha256 of every saved source matches its FETCH_LOG.md line: tree 71f2669d..., README 7b0761ec..., CHANGELOG 07fbb324..., reduced_known ef67c131..., fmm_sota d0da2c36..., COVERAGE c2a9bd92..., Lille 2b1c37d1...
- The reference file's git blob sha1 (computed locally) is a8f2b17fe73a5232fc624087ddb899eaeff127c5, size 42699. This equals the tree entry for `schemes/results/addition_reduced_ZT/5x6x7_m150_cr664_fv310_cn2039_ZT_reduced.json`, so reference/ is the live file byte for byte.
- Tree: `truncated: False`, 6637 entries, commit tree sha f0efd4f6....
- FETCH_LOG also lists a `v3r1t4s_open_prs.json` that is not in sources/. It is irrelevant to the criterion.

## Clause by clause
1. **Explicit SLP.** PASS. u_fresh/u, v_fresh/v and w_fresh/w define every intermediate as a signed sum of earlier variables. I found no forward or self references, no duplicate indices, no empty forms and no unused fresh variables. I executed the program literally on 200 random pairs of 5x6 and 6x7 matrices with entries up to 10^30. All results were exact, and the run used exactly 652 binary +/- operations. The reference run used 664.
2. **max dim <= 8.** PASS. n = [5,6,7].
3. **Rank equals the fmm_sota.json best rank.** PASS. fmm_sota.json (createdAt 2026-10-09T11:45:48) has entry 1425 `{"format": [5, 6, 7], "rank": 150}`, and it is the only 5x6x7 entry. The object has m = 150. All 150 products are distinct and all are used in W, so the effective rank is 150 and not lower. This is therefore not a rank target.
4. **Exact over Z.** PASS, checked myself.
   - I expanded every form to integer coefficient vectors and checked the full trilinear identity for all 35 outputs, with W read as C^T row-major (row = j*5 + i). Result: `bad_outputs: 0`.
   - The reference verifies under the same mapping. Under plain C row-major, both files fail 32 of 35 outputs, so the convention is the repository's own and the same one is applied to both files.
   - Every expanded coefficient is in {-1,0,1} (max |c| = 1). z2 = false. No product factor is zero.
5. **Counting convention (Perminov "reduced").** PASS, nothing stretched.
   - Each form costs (number of terms - 1).
   - The same formula reproduces 664 on Perminov's own file and 15 on the README's 2x2x2 example (2+2+2+2+2+5), so it is his convention.
   - Object breakdown: u_fresh 101, u 66, v_fresh 115, v 76, w_fresh 145, w 149. Total **652**, equal to the stated complexity.reduced 652.
   - The only unusual feature is 103 single-term fresh variables (U: 55, of which 13 are negations; V: 48, of which 13 are negations). All of them alias earlier fresh variables. Each costs 0 under the formula and is a genuine 0-operation copy or free negation under the criterion's rule ("multiplication by -1 is free"), so this is not a hidden undercount.
   - All coefficients are exactly +1 or -1, with no other scalars.
   - The author's checker gives an identical result: `adds_U 167, adds_V 191, adds_W 294, reduced_additions 652, exact_over_Z true, valid_ternary_slp true`. For the reference it gives 664.
6. **Strictly below the MINIMUM cr over all addition_reduced_ZT files for this format and rank, in any orientation.** PASS.
   - In the live tree, the only file whose name is any permutation of {5,6,7} under `addition_reduced_ZT/` is `5x6x7_m150_cr664_fv310_cn2039_ZT_reduced.json`.
   - The other 5x6x7 files are `naive_addition_reduced_ZT/` c1994 and c2039, results/ZT, and serendipitous_base. None has a smaller reduced count.
   - Minimum = 664, and 652 < 664.
7. **reduced_known.json.** PASS. It has no 5x6x7 key in any orientation. Its largest entries are 4x6x6-116 and 4x5x6-93.
8. **README.** PASS. 5x6x7 appears only in the ZT rank table (150, `Z/Q`) and in the research table (`150 (?) | 150 | 150`). No addition count is given for 5x6x7.
9. **CHANGELOG, all headings.** PASS. I checked every "Reduced additions improvement" block (26/08 to 05/09/2026) and the older "Additions reducing" block (3x3x3, 58). None mentions 5x6x7 or any permutation of it. A grep of the whole file finds no 5x6x7 permutation at all.
10. **Lille cited complexity variant.** PASS, vacuously. The live 5x6x7 page cites only ⟨5×6×7:150⟩ from Kauers–Wood (arXiv 2505.05896) with Maple encodings. It gives no addition or complexity count and no complexity variant.
11. **matmulcatalog COVERAGE.md "adds".** PASS. The ⟨5,6,7⟩ row shows "✓ 150 Dronperminov-ZT … +2039". No other orientation row exists. 652 < 2039.
12. **Coefficient class.** PASS. Rank 150 is attained with ternary coefficients: Perminov's ZT file and COVERAGE's "Dronperminov-ZT". The object is ternary, so the comparison is within the same class.
13. **Not a rank target; not a partial win.** Rank is equal to 150, not below it. The claim is made against the full criterion, not p1, p2 or p3, and it meets the full criterion.
14. **Live re-fetch timing.** PASS on the record.
    - All sources were fetched 2026-10-15T09:34:31Z to 09:34:35Z with HTTP 200.
    - The claim folder files are stamped 09:35:33Z, about one minute later. My check finished at about 09:39Z the same day.
    - I had no network and could not re-fetch myself. The orchestrator must re-fetch again before any external claim.
15. **Tie or subsumption.** No tie (652 ≠ 664) and no lower published count in any listed source.
    - Disclosure: the object is the **same bilinear scheme** as Perminov's 664 file. All 150 (U,V) product pairs match up to factor sign. The expanded nnz U/V/W is 798/824/752 for both files (naive 2039).
    - The W part (w_fresh and w) is byte-identical to the reference. The 12-addition gain is entirely a better common-subexpression schedule for U (172→167) and V (198→191).
    - The criterion counts additions of an SLP for the format and rank, not scheme novelty, so this is within the criterion. It should be described as a re-reduction of Perminov's scheme, not a new scheme.
16. **Null model / residual risk.**
    - The baseline is Perminov's own reducer output on the same scheme. The gain is real but small (1.8%).
    - Perminov's README lists werekorren/fmm_add_reduction as an external source. That repository is outside the criterion's enumerated sources, was not fetched, and is not checked here.

confirmed_scope: The file 5x6x7_m150_cr652_ZT_reduced.json is a ternary straight-line program for <5,6,7> with 150 multiplications (the fmm_sota.json best rank). It computes A*B exactly over Z with 652 additions/subtractions under Perminov's reduced convention. That is strictly fewer than 664, the minimum and only addition_reduced_ZT count for 5x6x7 rank 150, and below every count in reduced_known.json, the README, the CHANGELOG, the Lille 5x6x7 page and matmulcatalog COVERAGE.md as fetched at 2026-10-15T09:34Z. It is a re-reduction of the same bilinear scheme as Perminov's 664 file.
context: Claude Code Agent-tool subagent, model claude-opus-5-5, effort high, saw only a copy of claim/
pass: true
