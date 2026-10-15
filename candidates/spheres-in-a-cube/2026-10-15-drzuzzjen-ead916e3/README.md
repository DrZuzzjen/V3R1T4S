# Candidate: 385 equal spheres in a unit cube

**Status: PROMISING — geometry verified; novelty and Packomania priority unresolved.**

## Construction

The 385 finite-decimal centers in `object/centers.json` admit a common sphere radius of at least **0.0725678002281956999999999** in the cube **[-1/2,1/2]^3**. The minimum wall clearance is exactly 0.0725678002281957; every pair distance is at least twice the stated conservative bound.

This is a public, reproducible candidate released for review. The original research gate remains PROMISING. It is not a CONFIRMED_SOLUTION, an accepted Packomania record or a claim of optimality, method novelty or priority over earlier private submissions. It is intentionally placed under `candidates/`, outside the confirmed-result collection.

## Check it yourself

Python 3.9 or later, standard library only:

    python3 -I verify.py

Expected last line: `PASS`. The checker parses decimal strings exactly, converts every coordinate and the claimed radius to integers at one common scale, and checks all 73,920 pairs and 2,310 individual wall constraints with no tolerance. The object hash is printed. Verification takes about a second on the publishing machine.

Optional original MP50 replay, with mpmath from requirements-optional.txt:

    python3 verification/mp50_checker.py object/centers.json --claimed 0.0725678002281956999999999 --baseline 0.072542024034581654580005481314

The numerical result, exact certificate output and negative-control receipts are in `verification/`. `SHA256SUMS` identifies every other file in this candidate bundle.

## Comparison and unresolved novelty

The successful saved public radius capture from 2026-10-14 at 19:24:40 UTC gives N=385 radius **0.072542024034581654580005481314**. The conservative candidate bound exceeds it by more than 1e-11. The HTML table viewed on 2026-10-15 still displays that comparison value: https://packomania.com/scu/scu.html.

The pending page still lists the **26-Sep-2026 Moki & Julio, category *many*, 4666 candidates** bundle without its per-category/per-N contents: https://packomania.com/pending-requests.html. We cannot determine whether it contains an equal or better N=385 arrangement. The full novelty/queue condition of the approved research protocol has therefore not passed. A later live comparison remains required; the older successful TXT capture is not presented as a new final-claim fetch.

The original independent geometry reviewers also found the complete sorted distance multiset different from the supplied posted N=385 object. That comparison establishes non-isometry to that saved configuration; it does not settle the unseen queue. This minimal bundle reproduces the candidate's geometry; the original full comparative reviewer artifacts remain archived by the contributor.

## Research review and publication status

The original three-context panel recorded REPRODUCE pass=true, NOVELTY pass=false and CRITERION pass=false. Its gate is preserved verbatim in `verification/original-research-gate.md`. These outcomes have not been upgraded. This candidate publication was specifically authorized while novelty remains pending; it is not a confirmed-result outbox package and is not claimed to pass the kit's confirmed-package gate.

## Provenance and credits

Contributor: **Jean Francois Gutierrez / [@DrZuzzjen](https://github.com/DrZuzzjen)**.

The construction was obtained on 2026-10-14 from Packomania's public N=384 seed by local insertion and constraint optimization. The exact retained center file is unchanged; SHA256 `ead916e395b86b40de9e796239c9ab8397096e32a4700753a84d10d0ff56747a`.

- **Eckard Specht / Packomania**: the public N=384 seed, catalogue and source data, https://packomania.com/scu/scu.html.
- **David W. Cantrell**: author of the posted N=385 comparison configuration.
- **Xiangjing Lai, Jin-Kao Hao, Renbin Xiao and Fred Glover**, perturbation-based thresholding search (2023), https://leria-info.univ-angers.fr/~jinkao.hao/papers/LaietalJOC2023.pdf.
- **Salvatore Torquato and Yang Jiao**, packing optimization precedents (2010), https://arxiv.org/abs/1008.2747.
- **Milos Tatarevic**, close-packing perturbation precedents (2015), https://arxiv.org/abs/1503.07933.

The frozen preregistration is in `provenance/PREREG.v2.md`. Search notes here describe a derived construction, not a new mathematical method. The exact object and its geometric verification are reproducible from this bundle; it is not a claim of byte-for-byte search regeneration.
