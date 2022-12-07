import operator
from itertools import *
from math import *
from functools import *
from collections import *
import re

dirs8 = [(1, 0), (1, 1), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)]
def neighbours_8(x, y):
    return ((x + dx, y + dy) for dx, dy in dirs8)


dirs4 = [(1, 0), (-1, 0), (0, 1), (0, -1)]
def neighbours_4(x, y):
    return ((x + dx, y + dy) for dx, dy in dirs4)

#min, max, key, pwd = re.match(r"(\d+)-(\d+) (\w): (\w+)", s).groups()

if __name__ == "__main__":
    with open("input/day1.txt") as file:
        food = [sum(int(s) for s in elf.splitlines()) for elf in file.read().split("\n\n")]
        print(max(food))
        print(sum(sorted(food, reverse=True)[:3]))
