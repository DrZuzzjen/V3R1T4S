#!/usr/bin/env python3
"""After the workers stop: best candidate per (format, rank), re-verified, with complexity.naive filled in.
usage: finalize.py RUNDIR  -> RUNDIR/best_candidates/<format>_m<r>_cr<N>.json and RUNDIR/best_candidates/TABLE.md
naive = nnz(U)+nnz(V)+nnz(W) - 2r - n1*n3 (matches complexity.naive on 113/113 published files)."""
import glob, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import fmm_check as F
import maps

run = os.path.abspath(sys.argv[1])
out = os.path.join(run, "best_candidates")
os.makedirs(out, exist_ok=True)
ref = {}
for line in open(os.path.join(run, "data_eligibility.md"), encoding="utf-8"):
    p = [x.strip() for x in line.split("|")]
    if len(p) > 7 and p[4] == "yes":
        ref[(p[1], int(p[2]))] = (int(p[5]), p[7], p[6])
best = {}
for f in glob.glob(os.path.join(run, "attempts", "*", "output", "candidates", "*.json")):
    d = json.load(open(f, encoding="utf-8"))
    r = F.check(d)
    if not r["valid_ternary_slp"]:
        print("INVALID", f, r["error"]); continue
    k = (r["format"], r["rank"])
    if k not in ref or r["reduced_additions"] >= ref[k][0]:
        continue
    lens = f.replace("\\", "/").split("/attempts/")[1].split("/")[0]
    if k not in best or r["reduced_additions"] < best[k][0]:
        best[k] = (r["reduced_additions"], f, d, lens, r)
rows = []
for (fmt, rank), (cr, f, d, lens, r) in sorted(best.items(), key=lambda x: x[1][0] - ref[x[0]][0]):
    _, U, V, W = maps.load(f)
    d = dict(d)
    d["complexity"] = {"naive": int((U != 0).sum() + (V != 0).sum() + (W != 0).sum()) - 2 * U.shape[0] - W.shape[0],
                       "reduced": cr}
    name = "%s_m%d_cr%d_ZT_reduced.json" % (fmt, rank, cr)
    json.dump(d, open(os.path.join(out, name), "w", encoding="utf-8"))
    r2 = F.check(d)
    assert r2["valid_ternary_slp"] and r2["reduced_additions"] == cr
    rows.append("| %s | %d | %d | %d | %+d | %s | %s | %s |" % (fmt, rank, cr, ref[(fmt, rank)][0], cr - ref[(fmt, rank)][0],
                                                            lens, name, os.path.basename(f)))
tab = ["| format | rank | ours | Perminov min cr (snapshot) | gap | lens | object | source candidate |",
       "|---|---|---|---|---|---|---|---|"] + rows
open(os.path.join(out, "TABLE.md"), "w", encoding="utf-8").write("\n".join(tab) + "\n")
print("\n".join(tab))
