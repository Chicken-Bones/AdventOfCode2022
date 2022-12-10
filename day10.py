if __name__ == "__main__":
    with open("input/day10.txt") as file:
        v = [0, 1]
        for l in file:
            v.append(v[-1])
            if l.startswith("addx"):
                v.append(v[-1] + int(l.split(' ')[1]))

        print(sum(i*v[i] for i in [20, 60, 100, 140, 180, 220]))

        s = ['#' if e-1 <= i%40 < e+2 else ' ' for i, e in enumerate(v[1:])]
        for r in range(0, len(s), 40):
            print(''.join(s[r:r+40]))
