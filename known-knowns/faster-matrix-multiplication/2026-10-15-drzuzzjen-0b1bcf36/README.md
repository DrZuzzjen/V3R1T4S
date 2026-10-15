# <5,6,7> rank 150: a ternary straight-line program with 652 additions (record table: 664)

## What

The file 5x6x7_m150_cr652_ZT_reduced.json is a ternary straight-line program for <5,6,7> with 150 multiplications (the fmm_sota.json best rank). It computes A*B exactly over Z with 652 additions/subtractions under Perminov's reduced convention. That is strictly fewer than 664, the minimum and only addition_reduced_ZT count for 5x6x7 rank 150, and below every count in reduced_known.json, the README, the CHANGELOG, the Lille 5x6x7 page and matmulcatalog COVERAGE.md as fetched at 2026-10-15T09:34Z. It is a re-reduction of the same bilinear scheme as Perminov's 664 file.

## Check it yourself

    sh verify-it-yourself/run_checks.sh

Expected last line: `PASS` (standard-library Python 3; a few seconds on a laptop). The checker was written from the
definition in Perminov's README by an independent context; it checks the full tensor identity over Z, executes the
program on 24 random integer matrix pairs, enforces coefficients in {-1,0,1} after expansion and counts additions as the
sum over every form of (terms - 1).

## Compared to

| table | cell | value | URL | fetched (UTC) |
|---|---|---|---|---|
| Perminov, FastMatrixMultiplication, addition_reduced_ZT | 5x6x7 rank 150 | 664 | https://github.com/dronperminov/FastMatrixMultiplication | 2026-10-15T09:34:31Z (panel re-fetch 09:36:20Z) |
| Perminov, arXiv:2512.13365v2, results table | 5x6x7 rank 150 | 664 | https://arxiv.org/abs/2512.13365 | 2026-10-15T09:37:23Z |
| fmm_sota.json (best rank) | 5x6x7 | rank 150 | https://raw.githubusercontent.com/sedoglavic/fmm_digest/master/fmm_sota.json | 2026-10-15T09:34:33Z |
| Lille catalogue | 5x6x7 | rank 150, no complexity variant cited | https://fmm.univ-lille.fr/5x6x7.html | 2026-10-15T09:34:34Z |
| matmulcatalog COVERAGE 'adds' | <5,6,7> | +2039 (naive count) | https://raw.githubusercontent.com/solven-eu/matmulcatalog/master/generated/COVERAGE.md | 2026-10-15T09:34:33Z |

Details and page hashes: the-record-we-beat/RECORD.md.

## Not claimed

- No new rank: the bilinear scheme is Perminov's own rank-150 ternary scheme (its expanded U, V, W are unchanged); only
  the straight-line program for the U and V maps is shorter (U 172 -> 167, V 198 -> 191; W unchanged at 294).
- No claim about total operations, practical speed or any other format. Other cells found in the same run are
  unpanelled and not part of this package.
- No optimality claim; the search was randomized and time-capped.

## Credits

- A. I. Perminov: the rank-150 ternary scheme and its 664-addition reduced program, the reduced-scheme format and the
  counting convention (https://github.com/dronperminov/FastMatrixMultiplication, arXiv:2512.13365, arXiv:2511.20317).
- M. Kauers and I. Wood: the rank-150 <5,6,7> algorithm cited by the Lille catalogue (arXiv:2505.05896).
- A. Sedoglavic and the Lille FMM catalogue (https://fmm.univ-lille.fr/, fmm_digest).
- solven-eu/matmulcatalog (coverage table).
- The transposition principle (Tellegen; Bordewijk), used here to search for the U and V programs.
