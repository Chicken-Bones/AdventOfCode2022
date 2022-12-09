from math import *

dirs4 = [(1, 0), (-1, 0), (0, 1), (0, -1)]

if __name__ == "__main__":
    with open("input/day8.txt") as file:
        g = [[int(c) for c in s.strip()] for s in file]
        v = [[False for _ in r] for r in g]

        w = len(g[0])
        h = len(g)

        def view(t, x, y, dx, dy):
            if x < 0 or y < 0 or x >= w or y >= h:
                return

            l = g[y][x]
            if l > t:
                t = l
                v[y][x] = True

            view(t, x + dx, y + dy, dx, dy)

        for x in range(0, w):
            view(-1, x, 0, 0, 1)
            view(-1, x, h - 1, 0, -1)

        for y in range(0, h):
            view(-1, 0, y, 1, 0)
            view(-1, w - 1, y, -1, 0)

        print(sum(c for r in v for c in r))


        def see(t, x, y, dx, dy):
            x += dx
            y += dy
            if x < 0 or y < 0 or x >= w or y >= h:
                return 0

            if g[y][x] < t:
                return 1 + see(t, x, y, dx, dy)

            return 1


        def score(x, y):
            return prod(see(g[y][x], x, y, dx, dy) for dx, dy in dirs4)


        print(max(score(x, y) for x in range(0, w) for y in range(0, h)))
