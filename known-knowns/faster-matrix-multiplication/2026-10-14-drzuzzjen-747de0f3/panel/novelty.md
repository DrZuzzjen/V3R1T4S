# novelty.md: <4,6,7> rank 123, ternary SLP, 503 additions (claim: 4x6x7_m123_cr503_ZT_reduced.json)

(Saved verbatim by the run's main session from the subagent's returned text; subagents in this harness return
findings as text instead of writing files. "work/" refers to the skeptic's own isolated scratch folder.)

skeptic: NOVELTY
object sha256: 747de0f311caaf359538b14522c33523b83bf154bea1255cb02b2e8de977c5a0 (matches CLAIM_SHA256.txt)
claimed value: 503 reduced additions, rank 123, coefficients {-1,0,1}
reference to beat: min cr of the live addition_reduced_ZT files for 4x6x7 rank 123, plus reduced_known.json, README, CHANGELOG, Lille cited variant, matmulcatalog 'adds', literature, TROPHY_CASE and open PRs

## Access method
I made one plain request per URL with curl -sS -A "V3R1T4S-panel (honest client; curl)". I did not retry anything, imitate a browser or use a browser. Every request returned HTTP 200, so I hit no block or challenge page. Each fetch time comes from `date -u` taken just before the request. Each page is saved under work/ with its sha256.

## Primary sources (fresh fetches by this skeptic)

| time (UTC) | HTTP | sha256 | URL | value found |
|---|---|---|---|---|
| 2026-10-14T21:17:26Z | 200 | 71f2669d17d3636d92243b24d8b7a155ec9d9de472476a31c1a6db6d7ad2a610 | https://api.github.com/repos/dronperminov/FastMatrixMultiplication/git/trees/master?recursive=1 | truncated=false, 6637 entries. 4x6x7 files: schemes/known/tensor/4x6x7_tensor.mpl; schemes/results/ZT/4x6x7_m123_ZT.json and .m; schemes/results/addition_reduced_ZT/4x6x7_m123_cr517_cn1586_ZT_reduced.json; schemes/results/naive_addition_reduced_ZT/4x6x7_m123_c1562_ZT.json/.m and 4x6x7_m123_c1586_ZT.json/.m; schemes/results/serendipitous_base/4x6x7_m123_1c38c2b939f13535874e3ac958e2816f7de62e8a_ZT.json. No permuted-format files (4x7x6, 6x4x7, 6x7x4, 7x4x6, 7x6x4). addition_reduced_ZT for 4x6x7 rank 123: exactly one file, so **min cr = 517**. Byte-identical to the claim's sources copy. |
| 2026-10-14T21:17:50Z | 200 | 8c385f50b3e85e7c750e6ace7e1e3b835e2fdf3f348f8ff9ae94931a755367dd | https://raw.githubusercontent.com/dronperminov/FastMatrixMultiplication/master/schemes/results/addition_reduced_ZT/4x6x7_m123_cr517_cn1586_ZT_reduced.json | n=[4,6,7], m=123, complexity {naive:1586, reduced:517}. Identical to claim/reference. |
| 2026-10-14T21:17:27Z | 200 | 7b0761ecc0fa1988cb2ef0efeca503af974eeb6ade76d30629308ebba7e78341 | https://raw.githubusercontent.com/dronperminov/FastMatrixMultiplication/master/README.md | 4x6x7 appears only as rank 123 (line 397, ZT scheme link; line 1018, rank table). No addition count is given for 4x6x7. |
| 2026-10-14T21:17:28Z | 200 | 07fbb3249d1213b95d9a9c3069d208c0c3b4390a6b87c71325af64a2d56cd175 | https://raw.githubusercontent.com/dronperminov/FastMatrixMultiplication/master/CHANGELOG.md | No 4x6x7 entry of any kind. The "Reduced additions improvement" entries cover only 2x2x6..2x4x6, 3x3x4, 3x3x5 and 3x4x4. The latest "Additions reducing" entry is the 3x3x3 58-addition scheme. The newest changelog entry is 09/10/2026. |
| 2026-10-14T21:17:28Z | 200 | ef67c13792b0e770578de4ff01438178ce4e6ac4efd60a3580f3131e31907a5d | https://raw.githubusercontent.com/dronperminov/FastMatrixMultiplication/master/schemes/reduced_known.json | No 4x6x7 key. The largest keys are 4x5x6-93 and 4x6x6-116. |
| 2026-10-14T21:17:29Z | 200 | d0da2c364dcf4d13c0721ea8b7c3dcd7fae4f6f3c843d22a714a1ccb9bd244c1 | https://raw.githubusercontent.com/sedoglavic/fmm_digest/master/fmm_sota.json | createdAt 2026-10-09T11:45:48. Entry {"format":[4,6,7],"rank":123,"exponent":2.817458}, so **best rank = 123**. The candidate's rank equals it, which makes this an additions target and not a rank target. |
| 2026-10-14T21:17:29Z | 200 | 46442ede7f2649079321c1b5f681ae6a9f962c0b34956e5da9e319ba4c8fa62b | https://fmm.univ-lille.fr/4x6x7.html | <4x6x7:123>, taken from Kauers and Wood, "Consequences of the Moosbauer-Poole algorithms", arXiv:2505.05896. No complexity variant and no addition count is cited. |
| 2026-10-14T21:17:30Z | 200 | c2a9bd929b477acb44d4f92aa8055a0c26eab3c33121c0734be650c5c86254b7 | https://raw.githubusercontent.com/solven-eu/matmulcatalog/master/generated/COVERAGE.md | Row `⟨4,6,7⟩`: 123 (Dronperminov-ZT), adds column **+1586**. This is a naive count, nz(U)+nz(V)+nz(W)-2r-n·p. |
| 2026-10-14T21:17:30Z | 200 | b4f3ad52f6587e5aefdc3b555db200d99543e6b500c805012226f2042cdcc412 | https://raw.githubusercontent.com/elder-plinius/V3R1T4S/main/TROPHY_CASE.md | 0 matches for 4x6x7 or 4,6,7. No addition-count entries. The fast-matrix-multiplication rows are rank records for <13..15,14..16,14..16> only. |
| 2026-10-14T21:17:31Z | 200 | 3594fbc71fa6f6431ed1294f268386545d32dc2f499f7ec85b5165ed8b54bc0a | https://api.github.com/repos/elder-plinius/V3R1T4S/pulls?state=open&per_page=100 | 28 open PRs, so the list is not truncated. None mentions 4x6x7 or <4,6,7>. None is an addition-count claim. The only FMM PR is #130, a rank claim for (13,15,15) rank 1763. |

All 7 primary sources I fetched hash identically to the copies in claim/sources/ (FETCH_LOG.md). The table did not change between the author's fetch (21:15:47Z–21:15:50Z) and mine.

## Literature, last 24 months (2024-10-14 to 2026-10-14)

### arXiv API queries
| time (UTC) | HTTP | sha256 | query |
|---|---|---|---|
| 2026-10-14T21:18:31Z | 200 | 32c6b9be7f28e1b50868f22b07beac9701811424b93c4e41e4750733ee8fd546 | https://export.arxiv.org/api/query?search_query=abs:"additive complexity" AND abs:"matrix multiplication" (sorted by date, max 50) |
| 2026-10-14T21:18:32Z | 200 | b71da81d5eae4268704b19d15ec1576a1d60097f753786ef636bfda96ef5078c | https://export.arxiv.org/api/query?search_query=abs:"matrix multiplication" AND abs:additions AND abs:scheme (max 50) |
| 2026-10-14T21:18:33Z | 200 | 813b6d628f4b2aba23cc7a611743d85a520ff84d4a1fb03b57df43ad2b25fbf2 | https://export.arxiv.org/api/query?search_query=all:"fast matrix multiplication" AND all:"common subexpression" (max 50) |
| 2026-10-14T21:20:40Z | 200 | 720d11363cc817781fe1c9f9ec93b1996737a01f93dcb2853ae563410fe40287 | https://export.arxiv.org/api/query?search_query=abs:"matrix multiplication" AND (abs:"number of additions" OR abs:"additive cost" OR abs:"linear operations" OR abs:"straight-line program") (max 50) |

Relevant hits:
- **arXiv:2512.13365v2**, Perminov, "Parallel Heuristic Exploration for Additive Complexity Reduction in Fast Matrix Multiplication". I fetched the full HTML once: https://arxiv.org/html/2512.13365v2 at 2026-10-14T21:18:55Z, HTTP 200, sha256 7fbf6570ffe7c946d1561d56587f53939bfb8be542f21adb1641813f2c17de3e. Its results table row for 4x6x7 reads: rank 123, naive 1586, GV 535, GP 533, GP 518, proposed **517**. So 517 is the published best and matches the repository.
- arXiv:2511.20317v2, Perminov, "Fast Matrix Multiplication via Ternary Meta Flip Graphs". This is about ranks and naive additive complexity, and gives no reduced count for 4x6x7.
- arXiv:2512.21980 (3x3x3, 58 additions), arXiv:2604.27645 (Sun, 3x3x3, 56 additions) and arXiv:2508.03857 (3x3x3, 60 additions) cover 3x3 only. None gives a 4x6x7 count.
- arXiv:2505.05896, Kauers–Wood, is the rank source cited by Lille. It gives no addition count.
- Other hits (secure, distributed, homomorphic, LLM and hardware matrix multiplication) are not relevant. None of the four query result sets mentions 4x6x7 in an abstract.

### GitHub (search API and repository READMEs/trees)
| time (UTC) | HTTP | sha256 | URL | finding |
|---|---|---|---|---|
| 2026-10-14T21:19:01Z | 200 | 05197b5046b3e80e0bf37278fa1f3ac3737dcd4ed2599ca09b84d306803d250e | https://api.github.com/search/repositories?q=matrix+multiplication+addition+reduction&per_page=50 | 15 repos. Relevant: ErikMaartensson/fmm_add_reduction, dronperminov/ternary_addition_reducer, 22naresn/GEMM (a hardware accelerator, not a scheme source). |
| 2026-10-14T21:19:02Z | 200 | 46cfa1c2c39027a272bd05278b2b116c0a7dcafd3e3444ae7b9ee6035cc40170 | https://api.github.com/search/repositories?q=additive+complexity+matrix+multiplication&per_page=50 | 1 repo: dronperminov/linear-expressions-optimization, pushed 2026-10-12. |
| 2026-10-14T21:18:56Z | 200 | 37b319e0a3cb960cb612d56e1b53ac61bdfcdd673a0cd9ebafd9599cc055e842 | https://raw.githubusercontent.com/werekorren/fmm_add_reduction/main/README.md | No 4x6x7 count. The README describes the greedy-potential tool (ACDA25, "Number of the Beast"). |
| 2026-10-14T21:18:56Z | 200 | dfdf1cd6a43106f75700703a917a5bb0ecdb971b27858e2bceafeb5718df1573 | https://api.github.com/repos/werekorren/fmm_add_reduction/git/trees/main?recursive=1 | The recursive listing was truncated, so I listed the subtree separately (next row). |
| 2026-10-14T21:19:28Z | 200 | 9f8e64021463ac5ae0982b037485de1389176842dbc7af162ab07508ea0dab1f | https://api.github.com/repos/werekorren/fmm_add_reduction/git/trees/74fd1431aae47cea715c0ef699c282bc2c651849 | algorithms/hells_bells format directories: 222, 223, 224, 225, 226, 227, 228, 233, 234, 333, 432, 532. algorithms/grey covers formats up to 4x4x2 and 5x2x2. **No 4x6x7 in any orientation.** |
| 2026-10-14T21:19:00Z | 200 | aaffccced2dfe5587d6406861e9a9342d26e8fd0e83aa7031153f7a65833e315 | https://raw.githubusercontent.com/jgdumas/plinopt/main/README.md | No 4x6x7. |
| 2026-10-14T21:20:08Z | 200 | 0fbfae75e8956781b74d61493388ffdc720d80511dd66c382e551383a59d899f | https://api.github.com/repos/jgdumas/plinopt/git/trees/main?recursive=1 | 407 entries, not truncated. No 4x6x7 file in any orientation. |
| 2026-10-14T21:19:01Z | 200 | 4728b21b3a942f8327dbf286687b83e3f9d5a1aaa6197d3561042a0763ff5112 | https://raw.githubusercontent.com/dronperminov/ternary_addition_reducer/master/README.md | No 4x6x7 count. The only example is a rank-164 scheme, reduced to 715. |
| 2026-10-14T21:20:09Z | 200 | 1da19dcea3d4c0657b3bfd69503b874f1f8b96052876f8fb05c12a6b85ed8ff4 | https://api.github.com/repos/dronperminov/ternary_addition_reducer/git/trees/master?recursive=1 | 14 entries. No scheme files. |
| 2026-10-14T21:19:54Z | 200 | 99cbffbbe281d02d76f606bab243624b941843deae99f0e4da4f02307e69ac9c | https://raw.githubusercontent.com/dronperminov/linear-expressions-optimization/master/README.md | Framework description only. No counts. |
| 2026-10-14T21:19:55Z | 200 | 60f71e4332ec4f805d3baacb84f631cccd023d36546cefd0c01017409475750e | https://api.github.com/repos/dronperminov/linear-expressions-optimization/git/trees/master?recursive=1 | 120 entries: source code and examples only. No 4x6x7 results. |
| 2026-10-14T21:19:56Z | 200 | 66b845afbceac9a21c0ff5f4875b7e30983d330a1b77ee7a2125ad39399bef28 | https://raw.githubusercontent.com/ErikMaartensson/fmm_add_reduction/main/README.md | No 4x6x7. |
| 2026-10-14T21:19:56Z | 200 | b32c8ceec632370e3320cd37cde23a678c2be82f809da9a753af7cedf42d498f | https://api.github.com/repos/ErikMaartensson/fmm_add_reduction/git/trees/main?recursive=1 | 91 entries. No 4x6x7 in any orientation. |
| 2026-10-14T21:20:28Z | 200 | 9af3b97c700fa9bcc7be6065033b48b40464816bc48cfc55ebc5279ffa00cf6e | https://api.github.com/repos/matyasstoch/cloudroom-math/git/trees/HEAD?recursive=1 | This source was merged into Perminov's repo on 09/10/2026. 99 entries. No 4x6x7 and no addition-reduced files. |
| 2026-10-14T21:20:29Z | 200 | f25a290fcb035c0a0b1df06f5baccbd99653698ed38b1abcc49807da335e8c37 | https://api.github.com/repos/MerlijnW70/fmm-schemes/git/trees/HEAD?recursive=1 | This source was merged into Perminov's repo on 02/10/2026. 39 entries. No 4x6x7 and no addition-reduced files. |

## Coefficient-class comparison
The candidate is ternary, with coefficients in {1,-1} only; I enumerated every coefficient in the file. The class used for comparison is therefore ternary / ZT. The Lille rank 123 (Kauers–Wood) is also available as a ternary scheme (Perminov ZT). Lille gives no complexity variant, so no Q-class count needs comparing either.

I found no published 4x6x7 rank-123 SLP with <= 503 additions, in the ternary class or any other. The lowest published count is 517 (Perminov, live addition_reduced_ZT file and arXiv:2512.13365 Table). Next come 518, 533 and 535 (other heuristics in the same table). The naive counts are 1562 and 1586.

## Counter sanity (not a correctness verdict)
I counted (number of terms - 1) over every form in u_fresh, u, v_fresh, v, w_fresh and w:
- Candidate: 62+59+96+61+119+106 = **503**, equal to its stated complexity.reduced.
- Perminov's file: 53+75+71+93+119+106 = **517**, equal to its stated value.

This calibration matches. The w_fresh/w part is identical in count (225) to Perminov's, so the whole saving of 14 is on the U/V encoding side.

Two points for the correctness panel, which I did not check: I did no symbolic verification of the product. The candidate's u_fresh has 119 entries contributing only 62 additions, so some fresh variables are single-term (aliases or negations, which cost 0 under this convention).

## Prompt-injection scan
I scanned the fetched pages for agent-directed text. The only hit is Perminov README line 539: "new matrix multiplication algorithms found by AI agents". It is a benign attribution and contains no instruction.
injection_suspected: none

## Verdict
- Live minimum for 4x6x7 rank 123 under the reduced convention: 517.
- Candidate: 503.
- Margin: -14. This is a strict improvement and not a tie.
- Lille cites no complexity variant.
- matmulcatalog shows +1586 (naive).
- reduced_known.json, README and CHANGELOG have no 4x6x7 entry.
- Literature from the last 24 months, TROPHY_CASE.md and the 28 open V3R1T4S PRs contain no count at or below 503.

novelty: 503 < 517. Strictly beats everything known to this skeptic as of 2026-10-14T21:21:06Z (all primary sources read with HTTP 200).
This verdict covers novelty only. It depends on the correctness skeptic confirming the SLP is exact over Z and valid under the stated counting convention.

context: Claude Code Agent-tool subagent, model claude-opus-5-5, effort high, saw only a copy of claim/ plus its own web fetches
pass: true
