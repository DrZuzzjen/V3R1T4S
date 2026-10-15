"""Independent decimal check of equal spheres in the centered unit cube."""
import argparse
import json
from pathlib import Path
import mpmath as mp

mp.mp.dps = 50

def read_centers(path):
    path = Path(path)
    if path.suffix == '.json':
        value = json.loads(path.read_text())
        value = value.get('centers', value) if isinstance(value, dict) else value
        rows = [[mp.mpf(str(v)) for v in row] for row in value]
    else:
        rows = []
        for line in path.read_text().splitlines():
            if not line.strip() or line.lstrip().startswith('#'):
                continue
            parts = line.split()
            if len(parts) == 4:
                parts = parts[1:]
            rows.append([mp.mpf(v) for v in parts])
    if not rows or any(len(row) != 3 for row in rows):
        raise ValueError('Expected nonempty three-dimensional center coordinates')
    if any(not mp.isfinite(v) for row in rows for v in row):
        raise ValueError('Nonfinite coordinate')
    return rows

def check(rows, claimed=None, baseline=None):
    walls = [mp.mpf('0.5') - abs(v) for row in rows for v in row]
    wall_radius = min(walls)
    pair_radius = mp.inf
    closest = None
    for i, left in enumerate(rows):
        for j in range(i + 1, len(rows)):
            right = rows[j]
            radius = mp.sqrt(mp.fsum((a-b)**2 for a,b in zip(left,right))) / 2
            if radius < pair_radius:
                pair_radius, closest = radius, [i,j]
    feasible = min(wall_radius,pair_radius)
    answer = {'n':len(rows), 'digits':mp.mp.dps,
              'feasible_radius':mp.nstr(feasible,50),
              'wall_radius':mp.nstr(wall_radius,50),
              'pair_radius':mp.nstr(pair_radius,50),'closest_pair':closest,
              'centers_inside_cube':wall_radius >= 0}
    if claimed is not None:
        radius=mp.mpf(str(claimed))
        answer['claimed_radius']=mp.nstr(radius,50)
        answer['claimed_feasible']=bool(radius > 0 and feasible >= radius)
    if baseline is not None:
        gap=feasible-mp.mpf(str(baseline))
        answer['gap_to_table']=mp.nstr(gap,50)
        answer['meets_numeric_improvement']=bool(gap >= mp.mpf('1e-11'))
    return answer

if __name__ == '__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('coordinates')
    parser.add_argument('--claimed')
    parser.add_argument('--baseline')
    args=parser.parse_args()
    result=check(read_centers(args.coordinates),args.claimed,args.baseline)
    print(json.dumps(result,indent=2))
    if args.claimed and not result['claimed_feasible']:
        raise SystemExit(1)
