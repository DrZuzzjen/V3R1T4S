# Honesty gate (run's main session, 2026-10-15T09:43:47Z)

Read all three panel files. REPRODUCE pass (own checker, all 44100 triples, 652 calibrated at 664 on Perminov's file,
deterministic, 18/18 mutants rejected, SLP executed on 20 random pairs with 652 operations). NOVELTY pass (own fetches
2026-10-15T09:36:20Z-09:40:52Z, all HTTP 200, hashes identical to the claim's 09:34Z snapshot; live minimum 664, also
664 in arXiv:2512.13365 Table 1; no lower count in Lille, matmulcatalog, werekorren, plinopt, ternary_addition_reducer,
arXiv, TROPHY_CASE or open PRs). CRITERION pass (clause by clause; no other orientation; not a rank target).

Downgrade checks: hedging panelist - no (NOVELTY's dependence on correctness is satisfied by REPRODUCE); reproduction
mismatch - none; not strictly better - no, 652 < 664; stretched criterion - no; scope wider than reproduced - no;
sample presented as complete - no; capped search as exclusion - no; table value by evasion - no; several objects
bundled - no. Panel table fetch < 6 h old. Disclosed by CRITERION and REPRODUCE: same bilinear scheme as Perminov's
file; the gain is a better U and V straight-line program (U 172 -> 167, V 198 -> 191, W unchanged).

status: CONFIRMED_SOLUTION
confirmed_scope: The file 5x6x7_m150_cr652_ZT_reduced.json is a ternary straight-line program for <5,6,7> with 150 multiplications (the fmm_sota.json best rank). It computes A*B exactly over Z with 652 additions/subtractions under Perminov's reduced convention. That is strictly fewer than 664, the minimum and only addition_reduced_ZT count for 5x6x7 rank 150, and below every count in reduced_known.json, the README, the CHANGELOG, the Lille 5x6x7 page and matmulcatalog COVERAGE.md as fetched at 2026-10-15T09:34Z. It is a re-reduction of the same bilinear scheme as Perminov's 664 file.
