#!/usr/bin/env python3
# SPDX-License-Identifier: AGPL-3.0-or-later
"""Exact verification of one finite-decimal sphere packing. Python 3.9+, stdlib only."""
import argparse
from decimal import Decimal, localcontext
from fractions import Fraction
import hashlib
import json
from math import lcm
from pathlib import Path
import sys

BOUND = '0.0725678002281956999999999'
EXPECTED_N = 385


def exact_decimal(value):
    if not isinstance(value, str):
        raise ValueError('Coordinates must be decimal strings, never binary floats')
    number = Decimal(value)
    if not number.is_finite():
        raise ValueError('Nonfinite coordinate')
    return Fraction(number)


def verify(path):
    raw = path.read_bytes()
    data = json.loads(raw)
    rows = data.get('centers') if isinstance(data, dict) else data
    if not isinstance(rows, list) or len(rows) != EXPECTED_N:
        raise ValueError('Expected exactly 385 centers')
    if any(not isinstance(row, list) or len(row) != 3 for row in rows):
        raise ValueError('Every center must have three coordinates')
    points = [[exact_decimal(value) for value in row] for row in rows]
    bound = Fraction(Decimal(BOUND))
    scale = lcm(2, bound.denominator, *(v.denominator for row in points for v in row))
    integer_points = [[int(v * scale) for v in row] for row in points]
    integer_radius = int(bound * scale)
    half = scale // 2
    minimum_wall = None
    failed_walls = 0
    wall_constraints = 0
    for row in integer_points:
        for coordinate in row:
            for clearance in (half - coordinate, half + coordinate):
                wall_constraints += 1
                failed_walls += clearance < integer_radius
                minimum_wall = clearance if minimum_wall is None else min(minimum_wall, clearance)
    minimum_squared_distance = None
    failed_pairs = 0
    pairs = 0
    witness = None
    for i, left in enumerate(integer_points):
        for j in range(i + 1, len(integer_points)):
            right = integer_points[j]
            distance_squared = sum((a - b) ** 2 for a, b in zip(left, right))
            pairs += 1
            failed_pairs += distance_squared < 4 * integer_radius ** 2
            if minimum_squared_distance is None or distance_squared < minimum_squared_distance:
                minimum_squared_distance, witness = distance_squared, [i + 1, j + 1]
    with localcontext() as context:
        context.prec = 80
        wall_decimal = Decimal(minimum_wall) / Decimal(scale)
        pair_decimal = Decimal(minimum_squared_distance).sqrt() / (2 * Decimal(scale))
        feasible_decimal = min(wall_decimal, pair_decimal)
    return {
        'object_sha256': hashlib.sha256(raw).hexdigest(),
        'N': len(points),
        'cube': '[-1/2,1/2]^3',
        'certified_radius_lower_bound': BOUND,
        'arithmetic': 'exact integers after common scaling of finite decimal rationals',
        'tolerance': 'none',
        'pairs_checked': pairs,
        'individual_wall_constraints_checked': wall_constraints,
        'failed_pair_constraints': failed_pairs,
        'failed_wall_constraints': failed_walls,
        'minimum_wall_clearance': str(wall_decimal),
        'minimum_half_pair_distance_approx_80_digits': str(pair_decimal),
        'feasible_radius_approx_80_digits': str(feasible_decimal),
        'closest_pair_one_based': witness,
        'geometry_pass': not failed_pairs and not failed_walls,
        'novelty': 'unresolved; geometry verification does not establish priority or acceptance',
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('coordinates', nargs='?', default=str(Path(__file__).parent / 'object/centers.json'))
    args = parser.parse_args()
    try:
        result = verify(Path(args.coordinates))
    except (ValueError, OSError, TypeError, ArithmeticError) as error:
        print(json.dumps({'geometry_pass': False, 'error': str(error)}))
        print('FAIL')
        return 1
    print(json.dumps(result, indent=2))
    print('PASS' if result['geometry_pass'] else 'FAIL')
    return 0 if result['geometry_pass'] else 1


if __name__ == '__main__':
    sys.exit(main())
