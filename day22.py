import re

dirs4 = [(1, 0), (0, 1), (-1, 0), (0, -1)]
def add(a, b):
    ax, ay = a
    bx, by = b
    return ax+bx, ay+by


if __name__ == "__main__":
    with open("input/day22.txt") as file:
        map, path = file.read().split("\n\n")
        map = {(i, j): c for j, l in enumerate(map.split("\n")) for i, c in enumerate(l) if c != ' '}

        def wrap2d(p, f):
            rev = dirs4[f^2]
            while add(p, rev) in map:
                p = add(p, rev)

            return p, f


        wrap3d = {}
        def join_seams(p, f1, f2):
            p1 = p2 = p
            while True:
                g1 = (f1-1)%4
                g2 = (f2+1)%4
                for _ in range(50):
                    p1 = add(p1, dirs4[f1])
                    p2 = add(p2, dirs4[f2])
                    assert p1 in map
                    assert p2 in map

                    o1 = add(p1, dirs4[g1])
                    o2 = add(p2, dirs4[g2])
                    assert o1 not in map
                    assert o2 not in map

                    wrap3d[(o1, g1)] = (p2, g2^2)
                    wrap3d[(o2, g2)] = (p1, g1^2)

                turn1 = add(p1, dirs4[f1]) not in map
                turn2 = add(p2, dirs4[f2]) not in map
                if turn1 == turn2:
                    return

                if turn1:
                    f1 = g1^2
                    p1 = add(p1, dirs4[f1^2])

                if turn2:
                    f2 = g2^2
                    p2 = add(p2, dirs4[f2^2])

        join_seams((50, 100), 3, 2)
        join_seams((49, 149), 1, 0)
        join_seams((99, 49), 1, 0)

        def walk(p, f, n, wrap_func):
            for _ in range(n):
                p2, f2 = add(p, dirs4[f]), f
                if p2 not in map:
                    p2, f2 = wrap_func(p2, f)

                if map[p2] == '#':
                    break

                p, f = p2, f2

            return p, f

        def go(wrap_func):
            pos = (min(x for x,y in map if y == 0), 0)
            f = 0

            for v in re.findall(r"([RL]|\d+)", path):
                match v:
                    case 'R': f = (f+1)%4
                    case 'L': f = (f-1)%4
                    case _: pos, f = walk(pos, f, int(v), wrap_func)


            print(pos, f, 1000*(pos[1]+1) + 4*(pos[0]+1) + f)


        go(lambda p, f: wrap2d(p, f))
        go(lambda p, f: wrap3d[(p, f)])

