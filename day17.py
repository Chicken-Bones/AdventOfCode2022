rocks = [
    [(0, 0), (1, 0), (2, 0), (3, 0)],
    [(1, 0), (0, 1), (1, 1), (2, 1), (1, 2)],
    [(2, 0), (2, 1), (0, 2), (1, 2), (2, 2)],
    [(0, 0), (0, 1), (0, 2), (0, 3)],
    [(0, 0), (0, 1), (1, 0), (1, 1)]
]

if __name__ == "__main__":
    with open("input/day17.txt") as file:
        tower = set()
        jets = file.read().strip()

        h = [0] * 7

        def rock_at(x, y, rock):
            return ((x+rx, y-ry) for rx,ry in rock)

        def free(x, y, rock):
            for rx, ry in rock_at(x, y, rock):
                if rx < 0 or rx >= 7 or ry < 1 or (rx, ry) in tower:
                    return False

            return True

        i_rock = 0
        i_jet = 0

        states = []
        heights = []

        def drop():
            global i_rock, i_jet, period

            rock = rocks[i_rock]
            i_rock = (i_rock+1) % len(rocks)

            x = 2
            y = max(h) + 4 + max(y for _,y in rock)

            while True:
                jet = jets[i_jet]
                i_jet = (i_jet+1) % len(jets)

                dx = 1 if jet == '>' else -1
                if free(x+dx, y, rock):
                    x += dx

                if not free(x, y-1, rock):
                    break

                y -= 1

            for rx, ry in rock_at(x, y, rock):
                tower.add((rx, ry))
                h[rx] = max(h[rx], ry)

            heights.append(max(h))

            c = tuple(y - e for e in h)
            states.append((i_rock, i_jet, c))


        for i in range(0, 2022):
            drop()

        print(heights[-1])

        period = next(i for i, e in enumerate(reversed(states)) if i > 0 and e == states[-1])
        base = len(heights) - period - 1
        h_per_period = heights[-1] - heights[base]

        def solve(i):
            i -= base
            return heights[(i % period) + base] + h_per_period * (i // period)

        print(solve(1000000000000 - 1))

