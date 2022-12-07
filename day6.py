from itertools import *


if __name__ == "__main__":
    with open("input/day6.txt") as file:
        s = file.read().strip()
        print(next(i for i in count() if len(set(s[i-4:i])) == 4))
        print(next(i for i in count() if len(set(s[i-14:i])) == 14))
