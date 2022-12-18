rocks = [
    [(0, 0), (1, 0), (2, 0), (3, 0)],
    [(1, 0), (0, 1), (1, 1), (2, 1), (1, 2)],
    [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)],
    [(0, 0), (0, 1), (0, 2), (0, 3)],
    [(0, 0), (0, 1), (1, 0), (1, 1)]
]

if __name__ == "__main__":
    with open("input/day17.txt") as file:
        tower = set()
        jets = file.read().strip()

        tops = [0] * 7

        def rock_at(x, y, rock):
            return ((x+rx, y+ry) for rx,ry in rock)

        def free(x, y, rock):
            return all(0 <= rx < 7 and (rx, ry) not in tower for rx, ry in rock_at(x, y, rock))

        i_rock = 0
        i_jet = 0

        states = [None]
        heights = [0]

        def drop():
            global i_rock, i_jet, period

            rock = rocks[i_rock]
            i_rock = (i_rock+1) % len(rocks)

            x = 2
            y = max(tops) + 4

            while True:
                jet = jets[i_jet]
                i_jet = (i_jet+1) % len(jets)

                dx = 1 if jet == '>' else -1
                if free(x+dx, y, rock):
                    x += dx

                if y == 1 or not free(x, y-1, rock):
                    break

                y -= 1

            for rx, ry in rock_at(x, y, rock):
                tower.add((rx, ry))
                tops[rx] = max(tops[rx], ry)

            heights.append(max(tops))

            c = tuple(y - e for e in tops)
            states.append((i_rock, i_jet, c))


        for i in range(0, 2022):
            drop()

        print(heights[-1])

        period = next(i for i, e in enumerate(reversed(states)) if i > 0 and e == states[-1])
        base = len(heights) - 1 - period
        h_per_period = heights[-1] - heights[base]

        def solve(i):
            i -= base
            return heights[(i % period) + base] + h_per_period * (i // period)

        print(solve(1000000000000))

