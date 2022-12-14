from math import *
from functools import *


def cmp(a: int | list, b: int | list):
    match (a, b):
        case (int(), int()): return a - b

        case (int(), _): return cmp([a], b)
        case (_, int()): return cmp(a, [b])

        case ([a_head, *a_rest], [b_head, *b_rest]):
            c = cmp(a_head, b_head)
            return c if c != 0 else cmp(a_rest, b_rest)

        case _: return len(a) - len(b)


if __name__ == "__main__":
    with open("input/day13.txt") as file:
        pairs = [[eval(e) for e in s.split()] for s in file.read().split("\n\n")]

        print(sum(i+1 for i, p in enumerate(pairs) if cmp(*p) <= 0))

        keys = [[[2]], [[6]]]
        l = [e for p in pairs for e in p] + keys
        l.sort(key=cmp_to_key(cmp))
        print(prod(l.index(k) + 1 for k in keys))