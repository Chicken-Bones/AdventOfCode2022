import re
import time
from functools import *
from math import *


def ceil_div(i, d):
    return (i+d-1)//d


def parsebp(s):
    return tuple(int(e) for e in re.findall(r"(\d+)", s))


def until_afford(res, mines, cost):
    return max((ceil_div(c - r, m) if m > 0 else 1000 for r,m,c in zip(res, mines, cost) if r < c), default=0)


builds = 0
def geodes(bp, t0):
    bp_num, ore_ore, ore_clay, ore_obs, clay_obs, ore_geode, obs_geode = bp
    costs = [(ore_ore, 0, 0), (ore_clay, 0, 0), (ore_obs, clay_obs, 0), (ore_geode, 0, obs_geode)]
    max_use = [max(c[i] for c in costs) for i in range(3)]

    def build(t, res, mines, b):
        global builds
        builds += 1

        if b < 3 and res[b] == 1000:
            return 0

        cost = costs[b]
        wait = until_afford(res, mines, cost) + 1
        if wait >= t:
            return 0

        t -= wait
        res = tuple(r + m*wait - c for r,m,c in zip(res, mines, cost))

        g = t if b == 3 else 0
        mines = (mines[0] + (b == 0), mines[1] + (b == 1), mines[2] + (b == 2))

        res = tuple(r if r+m*(t-2) < cap*(t-1) else 1000 for r,m,cap in zip(res, mines, max_use))
        return g + sim(t, res, mines)

    @cache
    def sim(t, res, mines):
        return max(build(t, res, mines, i) for i in range(4))

    g = sim(t0, (0, 0, 0), (1, 0, 0))
    #print(bp_num, g)
    return g


if __name__ == "__main__":
    with open("input/day19.txt") as file:
        bps = [parsebp(s) for s in file]

        t = time.time()
        print(sum((i+1)*geodes(bp, 24) for i, bp in enumerate(bps)))
        print(f"{time.time()-t:.1f}s", builds)

        t = time.time()
        print(prod(geodes(bp, 32) for bp in bps[:3]))
        print(f"{time.time()-t:.1f}s", builds)
