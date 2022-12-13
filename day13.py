from math import *
from functools import *


def cmp(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a - b

    if isinstance(a, int): a = [a]
    if isinstance(b, int): b = [b]

    for _a, _b in zip(a, b):
        c = cmp(_a, _b)
        if c != 0:
            return c

    return len(a) - len(b)


if __name__ == "__main__":
    with open("input/day13.txt") as file:
        pairs = [[eval(e) for e in s.split()] for s in file.read().split("\n\n")]

        print(sum(i+1 for i, p in enumerate(pairs) if cmp(*p) <= 0))

        keys = [[[2]], [[6]]]
        l = [e for p in pairs for e in p] + keys
        l.sort(key=cmp_to_key(cmp))
        print(prod(l.index(k) + 1 for k in keys))