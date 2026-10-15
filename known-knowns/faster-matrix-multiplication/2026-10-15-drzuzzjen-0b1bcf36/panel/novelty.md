# novelty.md — claim 0934: <5,6,7> rank 150, ternary SLP with 652 reduced additions

(Saved verbatim by the run's main session from the subagent's returned text; subagents in this harness return
findings as text instead of writing files. work/ refers to the skeptic's own isolated scratch folder.)

Role: NOVELTY skeptic. I read only claim/ and my own web fetches. I made one plain curl per URL with UA "V3R1T4S-panel (honest client; curl)" and `-w '%{http_code}'`. There were no retries and no browser imitation. Times are `date -u` taken just before each fetch. Pages are saved under work/ with their sha256, and the log is work/FETCH_LOG.txt.

## Object under test
- Object: `5x6x7_m150_cr652_ZT_reduced.json`, sha256 0b1bcf368d3abed71e48640ef313856b4cca6087052d5114b24af614c6baea3c.
- Its stated `complexity` field is {naive: 2039, reduced: 652}, and m = 150.
- Novelty check only. I did not verify correctness; that is the other skeptics' job.

## Primary sources (all HTTP 200, none blocked)

### 1. Perminov repository tree
- URL: https://api.github.com/repos/dronperminov/FastMatrixMultiplication/git/trees/master?recursive=1
- Fetched 2026-10-15T09:36:20Z, HTTP 200, sha256 71f2669d17d3636d92243b24d8b7a155ec9d9de472476a31c1a6db6d7ad2a610
- truncated = false, 6637 entries.
- I searched every orientation of {5,6,7}. Only 5x6x7 files exist:
  - schemes/known/tensor/5x6x7_tensor.mpl
  - results/ZT/5x6x7_m150_ZT.{json,m}
  - **results/addition_reduced_ZT/5x6x7_m150_cr664_fv310_cn2039_ZT_reduced.json**. This is the only addition_reduced file for the format.
  - naive_addition_reduced_ZT/5x6x7_m150_c1994_ZT and c2039_ZT
  - 5 serendipitous_base/5x6x7_m150_* files
- No 6x5x7, 5x7x6, 6x7x5, 7x5x6 or 7x6x5 files exist.
- **Minimum cr for 5x6x7 rank 150 in addition_reduced_ZT: 664.**
- The claim's reference copy has git blob sha1 a8f2b17fe73a5232fc624087ddb899eaeff127c5. This equals the live tree blob sha, so it is the live file.
- Its stated complexity is {naive: 2039, reduced: 664}.

### 2. Perminov README, CHANGELOG and reduced_known.json
- README.md
  - URL: https://raw.githubusercontent.com/dronperminov/FastMatrixMultiplication/master/README.md
  - Fetched 2026-10-15T09:36:21Z, HTTP 200, sha256 7b0761ecc0fa1988cb2ef0efeca503af974eeb6ade76d30629308ebba7e78341
  - 5x6x7 appears only in the rank tables: ZT rank 150 (`Z/Q`), and the row "5x6x7 | 150 (?) | 150 | 150 | 2.811221917".
  - No addition count is given for 5x6x7.
- CHANGELOG.md
  - URL: https://raw.githubusercontent.com/dronperminov/FastMatrixMultiplication/master/CHANGELOG.md
  - Fetched 2026-10-15T09:36:21Z, HTTP 200, sha256 07fbb3249d1213b95d9a9c3069d208c0c3b4390a6b87c71325af64a2d56cd175
  - No 5x6x7 entry.
- schemes/reduced_known.json
  - URL: https://raw.githubusercontent.com/dronperminov/FastMatrixMultiplication/master/schemes/reduced_known.json
  - Fetched 2026-10-15T09:36:22Z, HTTP 200, sha256 ef67c13792b0e770578de4ff01438178ce4e6ac4efd60a3580f3131e31907a5d
  - Its largest key is "4x6x6-116". There is no 5x6x7 key.

### 3. fmm_sota.json
- URL: https://raw.githubusercontent.com/sedoglavic/fmm_digest/master/fmm_sota.json
- Fetched 2026-10-15T09:36:22Z, HTTP 200, sha256 d0da2c364dcf4d13c0721ea8b7c3dcd7fae4f6f3c843d22a714a1ccb9bd244c1
- createdAt 2026-10-09T11:45:48.
- Entry: {format [5,6,7], rank 150, exponent 2.811222}. So rank 150 is the best listed rank, and the claim's rank qualifies.

### 4. Lille per-format page
- URL: https://fmm.univ-lille.fr/5x6x7.html
- Fetched 2026-10-15T09:36:23Z, HTTP 200, sha256 2b1c37d144a3f5299c55cdd4dd13d3dea23a7481031bde6d24625e1b9c8ff7f2
- It lists ⟨5×6×7:150⟩ from Kauers and Wood, arXiv:2505.05896.
- The page cites no complexity or addition-count variant.

### 5. matmulcatalog COVERAGE.md
- URL: https://raw.githubusercontent.com/solven-eu/matmulcatalog/master/generated/COVERAGE.md
- Fetched 2026-10-15T09:36:23Z, HTTP 200, sha256 c2a9bd929b477acb44d4f92aa8055a0c26eab3c33121c0734be650c5c86254b7
- Row `⟨5,6,7⟩`: ✓150 Dronperminov-ZT, adds column "+2039" (naive).

### 6. V3R1T4S TROPHY_CASE.md
- URL: https://raw.githubusercontent.com/elder-plinius/V3R1T4S/main/TROPHY_CASE.md
- Fetched 2026-10-15T09:36:23Z, HTTP 200, sha256 b4f3ad52f6587e5aefdc3b555db200d99543e6b500c805012226f2042cdcc412
- There are no 5x6x7 or fmm-additive-complexity entries. The only matrix-multiplication trophies are rank records over Q for formats 13–16.

### 7. V3R1T4S open pull requests
- URL: https://api.github.com/repos/elder-plinius/V3R1T4S/pulls?state=open&per_page=100
- Fetched 2026-10-15T09:36:24Z, HTTP 200, sha256 ab715effc62366094810a75e7e8b9767485527b725c8953326f88f0bd87e8503
- 40 PRs are open (one page, under 100).
- The only fmm-additive-complexity PR is #149 by DrZuzzjen, which claims <4,6,7> rank 123 with 503 additions. That is a different cell.
- No PR title or body mentions 5x6x7 in any orientation.

The claim's sources/FETCH_LOG.md (09:34Z) gives the same sha256 as my independent fetches for every primary page.

## Literature from the last 24 months (2024-10-15 to 2026-10-15)

### arXiv API (all HTTP 200)
- q1: all:"matrix multiplication" AND all:additions, 100 results
  - Fetched 2026-10-15T09:37:24Z, sha256 0215b0bf3765d7e723eb040ce9122c590fe1fcd50742bb1a851282836cdc3267
- q2: all:"additive complexity" AND all:matrix, 26 results
  - Fetched 2026-10-15T09:40:07Z, sha256 15e223e30bbcb33a6cdc328b29cc47873b99528e8b28b5242cde2583eedc3913
- q3: abs:"fast matrix multiplication", 156 results
  - Fetched 2026-10-15T09:40:13Z, sha256 aae574f084919b6263d68d78e2405d242478d6d59226b79880f18efe7a5422e2

Relevant hits in the window:
- **3x3 only, not 5x6x7:** 2508.03857, 2512.21980, 2604.27645, 2607.28676, 2609.06588 and 2609.32388 (60, 58, 56, 55, 52 and 51 additions at rank 23).
- **Rank, flip-graph or practical papers with no 5x6x7 addition count below 664:** 2511.20317, 2512.13365, 2603.02398, 2606.02480 and 2609.12027 (4x4x4:48 in practice).
- No abstract mentions 5x6x7.

### arXiv:2512.13365v2 (Perminov, additive complexity)
- URL: https://arxiv.org/html/2512.13365
- Fetched 2026-10-15T09:37:23Z, HTTP 200, sha256 7fbf6570ffe7c946d1561d56587f53939bfb8be542f21adb1641813f2c17de3e
- Table 1, "Schemes with optimal rank achieving new SOTA addition counts", 5x6x7 row: rank 150, Naive 2039, GV 696, GP-5 691, GP-40 671, Proposed **664**.
- The best published value is therefore 664, which matches the repo file.

### arXiv:2511.20317 (ternary meta flip graphs)
- URL: https://arxiv.org/html/2511.20317
- Fetched 2026-10-15T09:40:37Z, HTTP 200, sha256 4724a50e77f0c8e2e4820c9efda3ac3177e7994223a394403a4e7dc9669fcfb6
- Row (5,6,7): rank 150, naive counts 2431 and 2039. No reduced count.

### arXiv:2606.02480
- URL: https://arxiv.org/html/2606.02480
- Fetched 2026-10-15T09:40:36Z, HTTP 200, sha256 47924458e6c33262ab977139508cd8551686ac514d9743d2bbbb1eee79d4b0d3
- No 5x6x7 hit.

### arXiv:2603.02398
- URL: https://arxiv.org/html/2603.02398
- Fetched 2026-10-15T09:40:36Z, HTTP 200, sha256 4223b911c664ac5348fd0984ddc4c5dad8e9c12ee783ce3b34196343f4a6c968
- No 5x6x7 hit.

### werekorren/fmm_add_reduction
- Tree, recursive
  - URL: https://api.github.com/repos/werekorren/fmm_add_reduction/git/trees/main?recursive=1
  - Fetched 2026-10-15T09:37:40Z, HTTP 200, sha256 dfdf1cd6a43106f75700703a917a5bb0ecdb971b27858e2bceafeb5718df1573
  - truncated = true. Because of this I listed the directories separately, one fetch each:
    - contents/algorithms: 09:38:53Z, sha256 1058ca76…
    - algorithms/hells_bells: 09:38:54Z, sha256 f3e52cb0…. Directories: 222–234, 333, 432, 532. No 567.
    - moosbauer: 09:39:02Z. Nothing above 666.
    - other: 09:39:03Z.
    - grey: 09:39:04Z.
    - other/unsorted: 09:39:12Z.
    - kauerswood: 09:39:21Z.
    - kauerswood/567: 09:39:32Z, sha256 1909dc8c…. It holds KauersWood-567-150-mod0.exp and KauersWood2-567-150-mod0.exp. These are unreduced inputs with dense non-ternary coefficients (e.g. 3*a22, -4*a12).
      - KauersWood-567-150-mod0.exp: fetched 09:39:51Z, sha256 0ea80fb4…
      - KauersWood2-567-150-mod0.exp: fetched 09:39:52Z, sha256 19bf6231…
    - kauerswood/TempNotes: 09:39:33Z. It has reduction results for 456, 457, 466 and 467 only (467: 575). There is no 567 entry.
- README.md
  - URL: https://raw.githubusercontent.com/werekorren/fmm_add_reduction/main/README.md
  - Fetched 2026-10-15T09:37:44Z, HTTP 200, sha256 37b319e0a3cb960cb612d56e1b53ac61bdfcdd673a0cd9ebafd9599cc055e842
  - No 5x6x7.

### jgdumas/plinopt
- Tree
  - URL: https://api.github.com/repos/jgdumas/plinopt/git/trees/main?recursive=1
  - Fetched 2026-10-15T09:37:45Z, HTTP 200, sha256 0fbfae75e8956781b74d61493388ffdc720d80511dd66c382e551383a59d899f
  - 407 entries, not truncated. No 5x6x7 file.
- README.md
  - URL: https://raw.githubusercontent.com/jgdumas/plinopt/main/README.md
  - Fetched 2026-10-15T09:37:46Z, HTTP 200, sha256 aaffccced2dfe5587d6406861e9a9342d26e8fd0e83aa7031153f7a65833e315
  - No 5x6x7.

### dronperminov/ternary_addition_reducer
- Tree
  - URL: https://api.github.com/repos/dronperminov/ternary_addition_reducer/git/trees/master?recursive=1
  - Fetched 2026-10-15T09:37:47Z, HTTP 200, sha256 1da19dcea3d4c0657b3bfd69503b874f1f8b96052876f8fb05c12a6b85ed8ff4
  - 14 entries. No 5x6x7.
- README.md
  - URL: https://raw.githubusercontent.com/dronperminov/ternary_addition_reducer/master/README.md
  - Fetched 2026-10-15T09:37:47Z, HTTP 200, sha256 4728b21b3a942f8327dbf286687b83e3f9d5a1aaa6197d3561042a0763ff5112
  - No 5x6x7.

### Extra check: Perminov repository open PRs
- URL: https://api.github.com/repos/dronperminov/FastMatrixMultiplication/pulls?state=open&per_page=100
- Fetched 2026-10-15T09:40:52Z, HTTP 200, sha256 953c527e335e70ba978e7f3c62053743a7ff330fb56ade8659f4bb9f069deb2f
- One open PR: #6, "Add 160-addition evaluation of the 3x4x5 rank-47 scheme". Nothing for 5x6x7.

## Prompt injection
- injection_suspected: none.
- No fetched page or claim file addressed agents.

## Verdict
- Best known reduced ternary addition count for <5,6,7> at rank 150 (the fmm_sota rank) is **664**. Sources:
  - the live Perminov addition_reduced_ZT file `5x6x7_m150_cr664_fv310_cn2039_ZT_reduced.json`, the only such file;
  - arXiv:2512.13365v2, Table 1, Proposed = 664.
- No lower count was found:
  - the Lille page cites no complexity variant;
  - matmulcatalog gives 2039 (naive);
  - werekorren, plinopt and ternary_addition_reducer have no reduced 5x6x7 result;
  - no arXiv paper from the last 24 months gives one;
  - TROPHY_CASE.md has no entry;
  - no open V3R1T4S or Perminov PR claims 5x6x7.
- Claimed 652 < 664, a strict improvement of 12. This is not a tie.
- Caveat: this verdict covers novelty only. It assumes the object really is a correct ternary SLP with 652 reduced additions. That is for the correctness and counting skeptics to confirm.

context: Claude Code Agent-tool subagent, model claude-opus-5-5, effort high, saw only a copy of claim/ plus its own web fetches
pass: true
