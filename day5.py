import re

crate_s = """
        [M]     [B]             [N]
[T]     [H]     [V] [Q]         [H]
[Q]     [N]     [H] [W] [T]     [Q]
[V]     [P] [F] [Q] [P] [C]     [R]
[C]     [D] [T] [N] [N] [L] [S] [J]
[D] [V] [W] [R] [M] [G] [R] [N] [D]
[S] [F] [Q] [Q] [F] [F] [F] [Z] [S]
[N] [M] [F] [D] [R] [C] [W] [T] [M]
"""

if __name__ == "__main__":
    with open("input/day5.txt") as file:
        T = list(zip(*crate_s.strip("\n").splitlines()))
        stacks = [list(''.join(t).strip())[::-1] for t in T[1::4]]

        moves = [(int(n), int(a)-1, int(b)-1) for n, a, b in re.findall(r"move (\d+) from (\d+) to (\d+)", file.read())]

        for n, a, b in moves:
            s_a = stacks[a]
            s_b = stacks[b]
            for i in range(n):
                s_b.append(s_a.pop())

        print(''.join(s[-1] for s in stacks))

        stacks = [list(''.join(t).strip())[::-1] for t in T[1::4]]
        for n, a, b in moves:
            s_a = stacks[a]
            s_b = stacks[b]
            stacks[a] = s_a[:-n]
            stacks[b] = s_b + s_a[-n:]

        print(''.join(s[-1] for s in stacks))
