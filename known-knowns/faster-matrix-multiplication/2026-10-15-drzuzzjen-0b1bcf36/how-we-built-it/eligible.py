#!/usr/bin/env python3
"""Join Perminov reduced counts (recounted by fmm_check), fmm_sota best ranks and matmulcatalog adds.
Usage: eligible.py RUN_DATA_DIR  -> markdown table on stdout."""
import json, re, sys, glob, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import fmm_check as F
D = sys.argv[1]
sota = {tuple(sorted(e["format"])): e["rank"] for e in json.load(open(os.path.join(D, "fmm_sota.json")))["entries"]}
cov = {}
for line in open(os.path.join(D, "matmul_COVERAGE.md"), encoding="utf-8"):
    m = re.match(r"\|\s*`⟨(\d+),(\d+),(\d+)⟩`\s*\|.*\|\s*\+(\d+)\s*\|[^|]*\|\s*$", line)
    if m:
        cov[tuple(sorted(map(int, m.groups()[:3])))] = int(m.group(4))
best = {}
for f in glob.glob(os.path.join(D, "addition_reduced_ZT", "*.json")):
    r = F.check(json.load(open(f, encoding="utf-8")))
    if not r["valid_ternary_slp"]:
        continue
    k = (r["format"], r["rank"])
    if k not in best or r["reduced_additions"] < best[k][0]:
        best[k] = (r["reduced_additions"], os.path.basename(f))
print("| format | perminov rank | sota best rank | eligible (rank==sota) | perminov min cr | matmulcatalog adds | file |")
print("|---|---|---|---|---|---|---|")
for (fmt, rank), (cr, fn) in sorted(best.items(), key=lambda x: (tuple(map(int, x[0][0].split("x"))), x[0][1])):
    key = tuple(sorted(map(int, fmt.split("x"))))
    s = sota.get(key)
    print("| %s | %d | %s | %s | %d | %s | %s |" % (fmt, rank, s, "yes" if s == rank else "no", cr, cov.get(key, "-"), fn))
