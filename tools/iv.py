# SPDX-License-Identifier: MIT
"""Compute sampled Pmax and optional efficiency from voltage_v,current_a CSV."""
import argparse
import csv
import json
import math


def summarize(rows, irradiance=None, area_cm2=None):
    points = [(float(r['voltage_v']), float(r['current_a'])) for r in rows]
    if len(points) < 2 or any(not math.isfinite(v) or not math.isfinite(i) for v, i in points):
        raise ValueError('Need at least two finite V/I samples')
    generating = [(v*i, v, i) for v, i in points if v >= 0 and i >= 0]
    if not generating:
        raise ValueError('No first-quadrant samples; check the current sign convention')
    power, v, i = max(generating)
    result = dict(samples=len(points), sampled_pmax_w=power, vmp_v=v, imp_a=i)
    if irradiance is not None or area_cm2 is not None:
        if not all(x is not None and math.isfinite(x) and x > 0 for x in (irradiance, area_cm2)):
            raise ValueError('Supply both positive measured irradiance and active area')
        result['sampled_efficiency_percent'] = 100*power/(irradiance*area_cm2/10000)
    return result


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('csv')
    p.add_argument('--irradiance-w-m2', type=float)
    p.add_argument('--area-cm2', type=float)
    a = p.parse_args()
    with open(a.csv, newline='', encoding='utf-8-sig') as f:
        print(json.dumps(summarize(csv.DictReader(f), a.irradiance_w_m2, a.area_cm2), indent=2))
