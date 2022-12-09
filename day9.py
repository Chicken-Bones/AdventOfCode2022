from recordclass import recordclass

Point = recordclass('Point', 'x y')

def follow(rope):
    for h, t in zip(rope, rope[1:]):
        dx = h.x - t.x
        dy = h.y - t.y

        if abs(dx) >= 2 or abs(dy) >= 2:
            t.x += 0 if dx == 0 else 1 if dx > 0 else -1
            t.y += 0 if dy == 0 else 1 if dy > 0 else -1


def ropesim(input, ropelen):
    rope = [Point(0, 0) for _ in range(ropelen)]
    seen = set()
    h = rope[0]
    t = rope[-1]
    for l in input:
        d, n = l.split(' ')
        n = int(n)

        for i in range(n):
            if d == 'U': h.y += 1
            elif d == 'D': h.y -= 1
            elif d == 'L': h.x -= 1
            elif d == 'R': h.x += 1

            follow(rope)
            seen.add((t.x, t.y))

    return len(seen)


if __name__ == "__main__":
    with open("input/day9.txt") as file:
        input = list(file)
        print(ropesim(input, 2))
        print(ropesim(input, 10))
