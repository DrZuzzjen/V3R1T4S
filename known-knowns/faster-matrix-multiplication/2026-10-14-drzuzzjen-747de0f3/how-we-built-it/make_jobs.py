#!/usr/bin/env python3
"""Build the job list for the supervisor from the run's eligibility table.
usage: make_jobs.py RUNDIR OUT.json
Each eligible format gets its minimum-cr file (the reference file). Jobs: lens x file x seed, ordered so that the
three lenses are interleaved and the most promising cells (p1 3x3x3, small formats, formats where our greedy was
within 3 of the reference in calibration) come first."""
import json, os, re, sys

run = os.path.abspath(sys.argv[1])
out = sys.argv[2]
rows = []
for line in open(os.path.join(run, "data_eligibility.md"), encoding="utf-8"):
    p = [x.strip() for x in line.split("|")]
    if len(p) > 7 and p[4] == "yes":
        rows.append({"format": p[1], "rank": int(p[2]), "ref": int(p[5]), "file": p[7]})


def dims(f):
    return tuple(map(int, f.split("x")))


def prio(r):
    d = dims(r["format"])
    if r["format"] == "3x3x3":
        return 0
    return max(d) * 10 + sum(d)


rows.sort(key=prio)
jobs = []
seed = 1
for lens, nseeds in (("cse", 1), ("transpose", 1), ("flipwalk", 1)):
    for r in rows:
        if r["format"] == "2x2x2":
            continue  # 15 is proved optimal
        d = dims(r["format"])
        if lens == "flipwalk" and max(d) > 5:
            continue  # the walk's quick scoring is too slow on the largest maps for this cycle
        jobs.append({"lens": lens, "file": os.path.join(run, "data", "addition_reduced_ZT", r["file"]), "ref": r["ref"],
                     "seed": seed, "out": os.path.join("attempts", lens, "output"), "format": r["format"],
                     "minutes": 22})
        seed += 1
# extra seeds for p1 (3x3x3) on every lens, running for the whole window
for lens in ("cse", "transpose", "flipwalk"):
    r = next(x for x in rows if x["format"] == "3x3x3")
    for _ in range(2):
        jobs.append({"lens": lens, "file": os.path.join(run, "data", "addition_reduced_ZT", r["file"]), "ref": r["ref"],
                     "seed": seed, "out": os.path.join("attempts", lens, "output"), "format": "3x3x3", "minutes": 100})
        seed += 1
# interleave lenses so that early slots cover all three
by = {}
for j in jobs:
    by.setdefault(j["lens"], []).append(j)
order = []
while any(by.values()):
    for lens in ("cse", "transpose", "flipwalk"):
        if by.get(lens):
            order.append(by[lens].pop(0))
json.dump(order, open(out, "w", encoding="utf-8"), indent=1)
print(len(order), "jobs;", {k: sum(1 for j in order if j["lens"] == k) for k in ("cse", "transpose", "flipwalk")})
