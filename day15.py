import re

import numpy as np


def dist(s_x, s_y, b_x, b_y):
    return abs(b_x - s_x) + abs(b_y - s_y)


if __name__ == "__main__":
    with open("input/day15.txt") as file:
        beacons = set()
        sensors = []

        y = 2000000
        xs = set()
        for s in file:
            s_x, s_y, b_x, b_y = re.match(r".+?([-\d]+).+?([-\d]+).+?([-\d]+).+?([-\d]+)", s).groups()
            s_x = int(s_x)
            s_y = int(s_y)
            b_x = int(b_x)
            b_y = int(b_y)

            d = dist(s_x, s_y, b_x, b_y)
            sensors.append((s_x, s_y, d))
            beacons.add((b_x, b_y))

            d -= abs(s_y - y)
            for x in range(s_x - d, s_x + d + 1):
                xs.add(x)

        n = len(xs)
        n -= sum(b_y == y for b_x, b_y in beacons)
        print(n)

        px, py = (0, 0)
        for sx1, sy1, d1 in sensors:
            for sx2, sy2, d2 in sensors:
                if sx2 < sx1:
                    continue

                if d1+d2+2 == dist(sx1, sy1, sx2, sy2):
                    if sy2 > sy1:
                        py += sy1+sx1+d1+1
                        px += sy1+sx1+d1+1
                        # y+x = sy1+sx1+d1+1
                    else:
                        py += sy1-sx1-d1-1
                        px -= sy1-sx1-d1-1
                        # y-x = sy1-sx1-d1-1

        px//=2
        py//=2
        print(px, py)
        print(px*4000000 + py)


        diamond = []
        for sx1, sy1, d1 in sensors:
            for sx2, sy2, d2 in sensors:
                if d1+d2+2 == dist(sx1, sy1, sx2, sy2):
                    diamond.append((sx1, sy1, d1))

        def clear(x, y):
            return all(dist(x, y, sx, sy) == d + 1 for sx,sy,d in diamond)

        sx, sy, d = diamond[0]
        for x in range(sx-d-1, sx+d+1):
            dy = d+1 - abs(x - sx)
            y = sy+dy
            if clear(x, y):
                print(x, y)
                print(x*4000000 + y)

            y = sy - dy
            if clear(x, y):
                print(x, y)
                print(x*4000000 + y)


