# Run it yourself

From this folder, in a fresh shell (any OS with sh and Python 3.8+):

    sh verify-it-yourself/run_checks.sh

Expected output: one JSON line with "format": "5x6x7", "rank": 150, "total": 652, "tensor_CT_mismatches": 0,
"random_fail_CT": 0, "pass": true, then `format 5x6x7 rank 150 additions 652 exact True`, then `PASS`.

Optional calibration against the record: download Perminov's
schemes/results/addition_reduced_ZT/5x6x7_m150_cr664_fv310_cn2039_ZT_reduced.json and run
`python3 -I verify-it-yourself/indep_check.py <that file>`; expected total 664 (= its stated complexity.reduced).

Rebuild the object: how-we-built-it/ holds the search code (numpy, numba; Windows supervisor). The object came from
the 'transpose' lens: greedy common-subexpression elimination on the transposed U and V maps of Perminov's 664 file
followed by transposition of the resulting linear program (lens_ops.reduce_by_transposition), with iterated
randomized restarts (worker.py --lens transpose). The search is randomized; rerunning finds programs of similar
length, not necessarily this exact file.
