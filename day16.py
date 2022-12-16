import re
import time
from collections import defaultdict
from functools import cache


if __name__ == "__main__":
    with open("input/day16.txt") as file:
        valves = {}
        for line in file:
            v, rate, to = re.match(r"Valve (\w\w) has flow rate=(\d+);.+valves? ([\w, ]+)", line).groups()
            rate = int(rate)
            to = to.split(", ")

            valves[v] = (rate, to)

    dist = defaultdict(lambda: 100000)
    for v, (_, to) in valves.items():
        for t in to:
            dist[(v, t)] = 1

    for k in valves.keys():
        for i in valves.keys():
            for j in valves.keys():
                l = dist[(i, k)] + dist[(k, j)]
                if dist[(i, j)] > l:
                    dist[(i, j)] = l

    # reduce to just the important nodes
    flow = {v: f for v, (f, _) in valves.items()}
    important = [v for v, f in flow.items() if f > 0]
    dist = {(a, b): v for (a, b), v in dist.items() if (flow[a] > 0 or a == 'AA') and flow[b] > 0}
    print("distances computed")

    def cost(a, b):
        return dist[(a, b)] + 1

    @cache
    def path(v, m, rem: frozenset):
        if m <= 0:
            return 0

        rem -= {v}
        return m*flow[v] + max((path(n, m-cost(v, n), rem) for n in rem), default=0)

    @cache
    def path2(v, m, rem: frozenset):
        if m > 0:
            # take this node yourself and recurse
            rem = rem - {v}
            return m * flow[v] + max((path2(n, m-cost(v, n), rem) for n in rem), default=0)
        else:
            # give the rest to the elephant
            return path('AA', 26, rem)

    print(path('AA', 30, frozenset(important)))

    t = time.time()
    print(path2('AA', 26, frozenset(important)))
    print(f"{time.time() - t:.2f}s")

