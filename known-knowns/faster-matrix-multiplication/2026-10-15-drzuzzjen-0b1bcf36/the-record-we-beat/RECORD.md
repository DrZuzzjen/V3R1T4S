# The record we beat

Cell: <5,6,7>, rank 150, reduced additions (Perminov 'reduced' convention), ternary coefficients.
Value in the table: 664, file schemes/results/addition_reduced_ZT/5x6x7_m150_cr664_fv310_cn2039_ZT_reduced.json
(sha256 ee197c7c8fa4d02aa282ed9273a0cb6cd76ab27e1b7019b338beefa8ef763ffb), the only addition_reduced_ZT file for 5x6x7.
Also 664 in arXiv:2512.13365v2 (Perminov), results table, row 5x6x7 (NOVELTY panel fetch 2026-10-15T09:37:23Z).

Fetch log (one honest GET each, curl, User-Agent naming V3R1T4S; time | HTTP | sha256 of the page | URL | saved name):

2026-10-15T09:34:31Z | 200 | 71f2669d17d3636d92243b24d8b7a155ec9d9de472476a31c1a6db6d7ad2a610 | https://api.github.com/repos/dronperminov/FastMatrixMultiplication/git/trees/master?recursive=1 | perminov_tree.json
2026-10-15T09:34:31Z | 200 | 7b0761ecc0fa1988cb2ef0efeca503af974eeb6ade76d30629308ebba7e78341 | https://raw.githubusercontent.com/dronperminov/FastMatrixMultiplication/master/README.md | perminov_README.md
2026-10-15T09:34:32Z | 200 | 07fbb3249d1213b95d9a9c3069d208c0c3b4390a6b87c71325af64a2d56cd175 | https://raw.githubusercontent.com/dronperminov/FastMatrixMultiplication/master/CHANGELOG.md | perminov_CHANGELOG.md
2026-10-15T09:34:32Z | 200 | ef67c13792b0e770578de4ff01438178ce4e6ac4efd60a3580f3131e31907a5d | https://raw.githubusercontent.com/dronperminov/FastMatrixMultiplication/master/schemes/reduced_known.json | reduced_known.json
2026-10-15T09:34:33Z | 200 | d0da2c364dcf4d13c0721ea8b7c3dcd7fae4f6f3c843d22a714a1ccb9bd244c1 | https://raw.githubusercontent.com/sedoglavic/fmm_digest/master/fmm_sota.json | fmm_sota.json
2026-10-15T09:34:33Z | 200 | c2a9bd929b477acb44d4f92aa8055a0c26eab3c33121c0734be650c5c86254b7 | https://raw.githubusercontent.com/solven-eu/matmulcatalog/master/generated/COVERAGE.md | matmul_COVERAGE.md
2026-10-15T09:34:34Z | 200 | 2b1c37d144a3f5299c55cdd4dd13d3dea23a7481031bde6d24625e1b9c8ff7f2 | https://fmm.univ-lille.fr/5x6x7.html | lille_5x6x7.html
2026-10-15T09:34:35Z | 200 | ab715effc62366094810a75e7e8b9767485527b725c8953326f88f0bd87e8503 | https://api.github.com/repos/elder-plinius/V3R1T4S/pulls?state=open&per_page=100 | v3r1t4s_open_prs.json

Extracted values: tree truncated=false; 5x6x7 addition_reduced_ZT min cr 664; reduced_known.json has no 5x6x7 key;
README lists 5x6x7 rank 150 with no addition count; CHANGELOG has no 5x6x7 entry; fmm_sota.json 5x6x7 rank 150;
Lille 5x6x7 page cites no complexity variant; matmulcatalog COVERAGE <5,6,7> adds +2039 (naive).
