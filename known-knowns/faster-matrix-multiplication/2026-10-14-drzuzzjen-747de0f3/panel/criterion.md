# CRITERION skeptic: claim fmm-additive-complexity-records, <4,6,7> rank 123, 503 reduced additions

(Saved verbatim by the run's main session from the subagent's returned text; subagents in this harness return
findings as text instead of writing files. Scratch scripts referenced below lived in the skeptic's own isolated work/
folder outside claim/.)

**Verdict: pass.** I went through the criterion one clause at a time. My checks ran against the saved sources only. I had no network access, so I could not re-fetch anything live. I wrote and ran my own scripts, work/tree.py, work/check.py and work/check2.py. I did not read or run the author's checker.

## C1. Explicit SLP (linear forms on the inputs, r products, linear forms producing the outputs): MET
- The object uses Perminov's reduced JSON layout with these fields: n=[4,6,7], m=123, u_fresh/u, v_fresh/v, w_fresh/w.
- The fresh variables are topologically ordered:
  - forward_refs=0 and unused_fresh=0 on U, V and W.
  - No form is empty.
  - No form repeats an index.
- Every literal coefficient is in {-1, 1}.
- After full expansion, every coefficient of U, V and W is in {-1, 1}, and no fresh variable expands to zero.

## C2. max(n,m,p) <= 8: MET
max(4,6,7) = 7.

## C3. Rank equals the best rank in fmm_sota.json (unordered/sorted format matching): MET
- fmm_sota.json has 5456 entries, createdAt 2026-10-09T11:45:48. Its description says entries are "indexed by unordered ... formats (sorted ascending by convention)".
- No entry is unsorted. The only entry with sorted format [4,6,7] is `{'format': [4, 6, 7], 'rank': 123, 'exponent': 2.817458}`.
- The object has m = 123 and exactly 123 u rows and 123 v rows.

## C4. Verified symbolically exact over Z: MET
I checked the Brent equations exactly over the integer coefficient tensor, which is equivalent to the polynomial identity over Z.

| File | layout C^T (w row = k*n1+i, as README says: w has n3*n1 rows) | layout C |
|---|---|---|
| object | exact: True, nterms 168 (= 4*6*7) | exact: False |
| reference (517 file) | exact: True | exact: False |

The same layout works for both files, which calibrates the layout check.

## C5. Counted under Perminov's 'reduced' convention exactly: MET
Each form costs (terms - 1). Negation is free. No other scalars appear.

| File | U (fresh + final) | V (fresh + final) | W (fresh + final) | TOTAL | stated |
|---|---|---|---|---|---|
| object | 62 + 59 = 121 | 96 + 61 = 157 | 119 + 106 = 225 | **503** | complexity.reduced 503 |
| reference | 53 + 75 = 128 | 71 + 93 = 164 | 119 + 106 = 225 | **517** | complexity.reduced 517 |

- My counter reproduces Perminov's own 517 exactly, so it is calibrated and not inflated.

**Stretched-counting hunt.** The object has 57 single-term u_fresh entries and 46 single-term v_fresh entries.
- Every one is a copy of another fresh variable: 0 point to original inputs, 57 and 46 point to fresh variables.
- 10 (U) and 15 (V) of them are negations.
- Under the convention these are a free alias or a free negation. They hide no operation and lower no count.
- Counting them only adds 0.

**Other checks:**
- No form contains a scalar other than ±1.
- No intermediate value expands to a coefficient other than ±1.
- The naive count recomputed from the expanded scheme is 1586, matching both files.

## C6. Strictly less than the MINIMUM cr over all addition_reduced_ZT files for the format and rank: MET
- Tree snapshot: commit sha f0efd4f6..., truncated=False, 6637 entries.
- Paths matching any orientation of {4,6,7}:
  - schemes/known/tensor/4x6x7_tensor.mpl
  - results/ZT/4x6x7_m123_ZT.{json,m}
  - results/addition_reduced_ZT/4x6x7_m123_cr517_cn1586_ZT_reduced.json
  - results/naive_addition_reduced_ZT/4x6x7_m123_c1562_ZT.{json,m}
  - results/naive_addition_reduced_ZT/4x6x7_m123_c1586_ZT.{json,m}
  - results/serendipitous_base/4x6x7_m123_1c38....json
- addition_reduced_ZT holds 195 files. Exactly one is for 4x6x7 (cr517).
- No 4x7x6, 6x4x7, 6x7x4, 7x4x6 or 7x6x4 file exists anywhere, so the hidden orientation quantifier is empty.
- **Minimum cr = 517. 503 < 517, a margin of 14.**
- The saved reference copy is byte-identical to the file in the tree. Its git blob sha1 is b9dd8d31a4f0810eed115d34d3e497d949e34fe7, matching the tree entry, size 33713.

## C7. Below reduced_known.json, README and CHANGELOG: MET
- **reduced_known.json:** no 4x6x7 key; the 4x6 entries stop at 4x6x6-116. Its blob sha1 fe2053...e92f matches the tree.
- **README:** 4x6x7 appears only at line 397 (rank 123, Z/Q) and line 1018 (rank table). Neither line gives an addition count. Blob sha1 adcfd6... matches the tree.
- **CHANGELOG:** no 4x6x7 mention in any notation. Blob sha1 454e1e... matches the tree.
- **Small inaccuracy in CLAIM.md:** it says the last 'Additions reducing' entry is 25.12.2025.
  - That is true for that exact heading.
  - Later entries use the heading "Reduced additions improvement", the newest on 05/09/2026.
  - None of them concerns 4x6x7, so the verdict is unaffected.

## C8. Lille per-format page's cited complexity variant: MET (vacuously)
- lille_4x6x7.html shows ⟨4×6×7:123⟩ taken from Kauers and Wood, arXiv:2505.05896.
- It gives an algorithm-type polynomial and maple links, but cites no complexity variant and no addition count.

## C9. matmulcatalog COVERAGE.md 'adds': MET
- The header's 'adds' column is defined as nz(U)+nz(V)+nz(W) − 2r − n·p.
- The row ⟨4,6,7⟩ shows 123 and adds +1586. 503 < 1586.

## C10. Coefficient-class rule: NOT TRIGGERED, applied correctly
- Rank 123 is attained with ternary coefficients. The README lists 4x6x7 123 under ZT, and the reference file itself is ternary at rank 123.
- So the Lille rank is not attained "only with non-ternary coefficients". In any case, the comparison is ZT against ZT, the same class.

## C11. "A scheme that also lowers the rank is a rank target": NOT A RANK TARGET
- Rank 123 equals the SOTA, so it does not lower the rank.
- The expanded bilinear scheme is identical to Perminov's 517 file: U, V and W are equal and the triads are in the same order.
- The w and w_fresh arrays are byte-identical to the reference.
- So the object is Perminov's own rank-123 scheme with better shared-subexpression reuse on the U and V sides: U 128 → 121, V 164 → 157. This is a genuine reduced-addition improvement for an existing scheme, not a new rank result.

## C12. Live, re-fetched immediately before claiming: MET as far as the saved data shows
- All 7 sources in FETCH_LOG were fetched between 2026-10-14T21:15:47Z and 21:15:50Z, each with HTTP 200.
- I recomputed the sha256 of every saved file, and every value matches the log.
- The packaged claim files carry mtime 2026-10-14T21:16:32Z, about 42 s later. The local timezone is +0200; the files show 23:16 local.
- **Caveat:** without network access I cannot confirm that the snapshot still matches the live sites. My check is limited to the log being internally consistent: the sha256 values match, and the blob sha1s of the reference, README, CHANGELOG and reduced_known.json match the tree listing.

## C13. Tie / subsumption / partial-win confusion
- **Not a tie:** 503 is strictly below 517.
- **Not subsumed:** no source lists any 4x6x7 rank-123 count at or below 503. The only counts present are 517 (reduced) and 1586 / 1562 (naive).
- **Not p1, p2 or p3:** the criterion is satisfied by a single eligible format, which is exactly what is claimed.

confirmed_scope: The file 4x6x7_m123_cr503_ZT_reduced.json is a ±1-coefficient straight-line program for <4,6,7> with 123 products (the fmm_sota.json best rank) that my own Brent-equation check confirms computes A*B exactly over Z with 503 additions/subtractions under Perminov's reduced convention (recounted with the same counter that reproduces 517 on Perminov's file), strictly below the 517 of the only 4x6x7 addition_reduced_ZT file in the saved 2026-10-14T21:15:47Z tree snapshot (commit f0efd4f), with no count at or below 503 in the saved reduced_known.json, README, CHANGELOG, Lille 4x6x7 page or matmulcatalog COVERAGE.md (adds +1586).
context: Claude Code Agent-tool subagent, model claude-opus-5-5, effort high, saw only a copy of claim/
pass: true
