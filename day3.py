import string

import operator
from itertools import *
from math import *
from functools import *
from collections import *
import re

def prio(c):
    return 1 + string.ascii_letters.index(c)


if __name__ == "__main__":
    with open("input/day3.txt") as file:
        lines = [s.strip() for s in file]

        sacks = [(s[:len(s)//2], s[len(s)//2:]) for s in lines]
        common = [set(a) & set(b) for a, b in sacks]
        print(sum(prio(next(iter(c))) for c in common))

        groups = [lines[i:i+3] for i in range(0, len(lines), 3)]
        badges = [set(a) & set(b) & set(c) for a, b, c in groups]
        print(sum(prio(next(iter(c))) for c in badges))
