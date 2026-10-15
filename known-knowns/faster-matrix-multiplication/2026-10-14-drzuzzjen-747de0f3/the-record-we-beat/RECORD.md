# The record we beat

Cell: <4,6,7>, rank 123, reduced additions (Perminov 'reduced' convention), ternary coefficients.
Value in the table: 517, file schemes/results/addition_reduced_ZT/4x6x7_m123_cr517_cn1586_ZT_reduced.json
(sha256 8c385f50b3e85e7c750e6ace7e1e3b835e2fdf3f348f8ff9ae94931a755367dd), the only addition_reduced_ZT file for 4x6x7.
Also 517 in arXiv:2512.13365v2 (Perminov), results table, row 4x6x7 (NOVELTY panel fetch 2026-10-14T21:18:55Z).

Fetch log (one honest GET each, curl, User-Agent naming V3R1T4S; time | HTTP | sha256 of the page | URL | saved name):

2026-10-14T21:15:47Z | 200 | 71f2669d17d3636d92243b24d8b7a155ec9d9de472476a31c1a6db6d7ad2a610 | https://api.github.com/repos/dronperminov/FastMatrixMultiplication/git/trees/master?recursive=1 | perminov_tree.json
2026-10-14T21:15:48Z | 200 | 7b0761ecc0fa1988cb2ef0efeca503af974eeb6ade76d30629308ebba7e78341 | https://raw.githubusercontent.com/dronperminov/FastMatrixMultiplication/master/README.md | perminov_README.md
2026-10-14T21:15:48Z | 200 | 07fbb3249d1213b95d9a9c3069d208c0c3b4390a6b87c71325af64a2d56cd175 | https://raw.githubusercontent.com/dronperminov/FastMatrixMultiplication/master/CHANGELOG.md | perminov_CHANGELOG.md
2026-10-14T21:15:49Z | 200 | ef67c13792b0e770578de4ff01438178ce4e6ac4efd60a3580f3131e31907a5d | https://raw.githubusercontent.com/dronperminov/FastMatrixMultiplication/master/schemes/reduced_known.json | reduced_known.json
2026-10-14T21:15:49Z | 200 | d0da2c364dcf4d13c0721ea8b7c3dcd7fae4f6f3c843d22a714a1ccb9bd244c1 | https://raw.githubusercontent.com/sedoglavic/fmm_digest/master/fmm_sota.json | fmm_sota.json
2026-10-14T21:15:50Z | 200 | c2a9bd929b477acb44d4f92aa8055a0c26eab3c33121c0734be650c5c86254b7 | https://raw.githubusercontent.com/solven-eu/matmulcatalog/master/generated/COVERAGE.md | matmul_COVERAGE.md
2026-10-14T21:15:50Z | 200 | 46442ede7f2649079321c1b5f681ae6a9f962c0b34956e5da9e319ba4c8fa62b | https://fmm.univ-lille.fr/4x6x7.html | lille_4x6x7.html

Extracted values: tree truncated=false; 4x6x7 addition_reduced_ZT min cr 517; reduced_known.json has no 4x6x7 key;
README lists 4x6x7 rank 123 with no addition count; CHANGELOG has no 4x6x7 entry; fmm_sota.json 4x6x7 rank 123;
Lille 4x6x7 page cites no complexity variant; matmulcatalog COVERAGE <4,6,7> adds +1586 (naive).
