# Run it yourself

From this folder, in a fresh shell (any OS with sh and Python 3.8+):

    sh verify-it-yourself/run_checks.sh

Expected output: one JSON line with "format": "4x6x7", "rank": 123, "total": 503, "tensor_CT_mismatches": 0,
"random_fail_CT": 0, "pass": true, then `format 4x6x7 rank 123 additions 503 exact True`, then `PASS`.

Optional calibration against the record: download Perminov's
schemes/results/addition_reduced_ZT/4x6x7_m123_cr517_cn1586_ZT_reduced.json and run
`python3 -I verify-it-yourself/indep_check.py <that file>`; expected total 517 (= its stated complexity.reduced).

Rebuild the object: how-we-built-it/ holds the search code (numpy, numba; Windows supervisor). The object came from
the 'transpose' lens: greedy common-subexpression elimination on the transposed U and V maps of Perminov's 517 file
followed by transposition of the resulting linear program (lens_ops.reduce_by_transposition), with iterated
randomized restarts (worker.py --lens transpose). The search is randomized; rerunning finds programs of similar
length, not necessarily this exact file.
