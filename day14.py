def sign(x: int):
    return 0 if x == 0 else 1 if x > 0 else -1


if __name__ == "__main__":
    with open("input/day14.txt") as file:
        map = set()
        for l in file:
            pts = [s.split(',') for s in l.split(" -> ")]
            pts = [(int(x), int(y)) for x, y in pts]
            for a, b in zip(pts, pts[1:]):
                x1, y1 = a
                x2, y2 = b

                map.add((x1, y1))
                while (x1, y1) != (x2, y2):
                    x1 += sign(x2 - x1)
                    y1 += sign(y2 - y1)
                    map.add((x1, y1))

        max_y = max(y for x, y in map)

        def play(part2=False):
            sand = set()

            def blocked(x, y):
                return (x, y) in sand or (x, y) in map or part2 and y == max_y+2

            def drop():
                x, y = (500, 0)
                if (x, y) in sand:
                    return False

                while y < max_y + 2:
                    n = next((p for p in [(x, y+1), (x-1, y+1), (x+1, y+1)] if not blocked(*p)), None)
                    if n is None:
                        sand.add((x, y))
                        return True

                    x, y = n

                return False

            while drop():
                pass

            return len(sand)

        print(play())
        print(play(part2=True))
