# How we found it (contributor text, unverified)

Brief: the bank target asks for fewer additions than Perminov's addition-reduced ternary schemes at the best rank.
We wrote an exact checker, calibrated it on all 113 published schemes with max dimension <= 8, and split each scheme
into its three linear maps (U on A, V on B, W from products to outputs), which can be optimized independently.

What failed: plain randomized pair-greedy CSE and ternary flip-graph walks tie Perminov on every small format (max
dimension <= 4) and on 3x3x3 (58), and stay above him on most large ones.

What worked: running the same greedy on the TRANSPOSED map and transposing the resulting linear program back
(transposition principle). On mid-sized formats this landscape is different enough to find shorter programs for U and
V. In about two hours on 28 CPU threads it went strictly below the table on several formats; this package carries
only the largest margin, 4x6x7 rank 123: 503 vs 517.
