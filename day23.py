from collections import Counter
from itertools import groupby, count

dirs8 = [(1, 0), (1, 1), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)]
dirs = [
    [(-1, -1), (0, -1), (1, -1)],
    [(-1, 1), (0, 1), (1, 1)],
    [(-1, -1), (-1, 0), (-1, 1)],
    [(1, -1), (1, 0), (1, 1)]
]


def add(a, b):
    ax, ay = a
    bx, by = b
    return ax+bx, ay+by


def propose(e, elves, dirs):
    if all(add(e, n) not in elves for n in dirs8):
        return e

    for dset in dirs:
        if all(add(e, n) not in elves for n in dset):
            return add(e, dset[1])

    return e


def step(elves):
    moves = [(e, propose(e, elves, dirs)) for e in elves]
    c = Counter(p for _, p in moves)
    return set(p if c[p] == 1 else e for e,p in moves)


if __name__ == "__main__":
    with open("input/day23.txt") as file:
        elves = set((i, j) for j, l in enumerate(file) for i, c in enumerate(l) if c == '#')

        for i in count(1):
            elves2 = step(elves)
            if elves2 == elves:
                print(i)
                break

            elves = elves2
            dirs = dirs[1:] + dirs[:1]

            if i == 10:
                x1 = min(x for x,y in elves)
                x2 = max(x for x,y in elves)
                y1 = min(y for x,y in elves)
                y2 = max(y for x,y in elves)
                w = x2-x1+1
                h = y2-y1+1
                print(w*h-len(elves))
