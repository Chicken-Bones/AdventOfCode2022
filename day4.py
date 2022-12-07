import re

if __name__ == "__main__":
    with open("input/day4.txt") as file:
        pairs = [[int(e) for e in re.match(r"(\d+)-(\d+),(\d+)-(\d+)", s.strip()).groups()] for s in file]
        print(sum(a >= c and b <= d or c >= a and d <= b for a, b, c, d in pairs))
        print(sum(not (b < c or d < a) for a, b, c, d in pairs))
