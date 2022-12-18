from collections import *


def adj(x, y, z):
    yield x + 1, y, z
    yield x - 1, y, z
    yield x, y + 1, z
    yield x, y - 1, z
    yield x, y, z + 1
    yield x, y, z - 1


if __name__ == "__main__":
    with open("input/day18.txt") as file:
        pts = {tuple(int(s) for s in l.split(',')) for l in file}

        print(sum(a not in pts for p in pts for a in adj(*p)))

        minx = min(x for x,y,z in pts)-1
        miny = min(y for x,y,z in pts)-1
        minz = min(z for x,y,z in pts)-1
        maxx = max(x for x,y,z in pts)+1
        maxy = max(y for x,y,z in pts)+1
        maxz = max(z for x,y,z in pts)+1

        q = deque()
        q.append((minx, miny, minz))
        w = set()

        while len(q) > 0:
            p = q.pop()
            if p in w or p in pts:
                continue

            w.add(p)
            for x, y, z in adj(*p):
                if minx <= x <= maxx and miny <= y <= maxy and minz <= z <= maxz:
                    q.append((x, y, z))

        print(sum(a in w for p in pts for a in adj(*p)))
