# <4,6,7> rank 123: a ternary straight-line program with 503 additions (record table: 517)

## What

The file 4x6x7_m123_cr503_ZT_reduced.json is a ±1-coefficient straight-line program for <4,6,7> with 123 products (the fmm_sota.json best rank) that my own Brent-equation check confirms computes A*B exactly over Z with 503 additions/subtractions under Perminov's reduced convention (recounted with the same counter that reproduces 517 on Perminov's file), strictly below the 517 of the only 4x6x7 addition_reduced_ZT file in the saved 2026-10-14T21:15:47Z tree snapshot (commit f0efd4f), with no count at or below 503 in the saved reduced_known.json, README, CHANGELOG, Lille 4x6x7 page or matmulcatalog COVERAGE.md (adds +1586).

## Check it yourself

    sh verify-it-yourself/run_checks.sh

Expected last line: `PASS` (standard-library Python 3; a few seconds on a laptop). The checker was written from the
definition in Perminov's README by an independent context; it checks the full tensor identity over Z, executes the
program on 24 random integer matrix pairs, enforces coefficients in {-1,0,1} after expansion and counts additions as the
sum over every form of (terms - 1).

## Compared to

| table | cell | value | URL | fetched (UTC) |
|---|---|---|---|---|
| Perminov, FastMatrixMultiplication, addition_reduced_ZT | 4x6x7 rank 123 | 517 | https://github.com/dronperminov/FastMatrixMultiplication | 2026-10-14T21:15:47Z (panel re-fetch 21:17:26Z) |
| Perminov, arXiv:2512.13365v2, results table | 4x6x7 rank 123 | 517 | https://arxiv.org/abs/2512.13365 | 2026-10-14T21:18:55Z |
| fmm_sota.json (best rank) | 4x6x7 | rank 123 | https://raw.githubusercontent.com/sedoglavic/fmm_digest/master/fmm_sota.json | 2026-10-14T21:15:49Z |
| Lille catalogue | 4x6x7 | rank 123, no complexity variant cited | https://fmm.univ-lille.fr/4x6x7.html | 2026-10-14T21:15:50Z |
| matmulcatalog COVERAGE 'adds' | <4,6,7> | +1586 (naive count) | https://raw.githubusercontent.com/solven-eu/matmulcatalog/master/generated/COVERAGE.md | 2026-10-14T21:15:50Z |

Details and page hashes: the-record-we-beat/RECORD.md.

## Not claimed

- No new rank: the bilinear scheme is Perminov's own rank-123 ternary scheme (its expanded U, V, W are unchanged); only
  the straight-line program for the U and V maps is shorter (U 128 -> 121, V 164 -> 157; W unchanged at 225).
- No claim about total operations, practical speed or any other format. Other cells found in the same run are
  unpanelled and not part of this package.
- No optimality claim; the search was randomized and time-capped.

## Credits

- A. I. Perminov: the rank-123 ternary scheme and its 517-addition reduced program, the reduced-scheme format and the
  counting convention (https://github.com/dronperminov/FastMatrixMultiplication, arXiv:2512.13365, arXiv:2511.20317).
- M. Kauers and I. Wood: the rank-123 <4,6,7> algorithm cited by the Lille catalogue (arXiv:2505.05896).
- A. Sedoglavic and the Lille FMM catalogue (https://fmm.univ-lille.fr/, fmm_digest).
- solven-eu/matmulcatalog (coverage table).
- The transposition principle (Tellegen; Bordewijk), used here to search for the U and V programs.
