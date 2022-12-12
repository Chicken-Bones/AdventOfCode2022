from collections import *

dirs4 = [(1, 0), (-1, 0), (0, 1), (0, -1)]
def neighbours_4(x, y):
    return ((x + dx, y + dy) for dx, dy in dirs4)


if __name__ == "__main__":
    with open("input/day12.txt") as file:
        map = {(i, j): ord(c) for j, line in enumerate(file) for i, c in enumerate(line.strip())}

        start = next(k for k, v in map.items() if v == ord('S'))
        end = next(k for k, v in map.items() if v == ord('E'))
        map[start] = ord('a')
        map[end] = ord('z')

        def pathlen(start):
            q = deque()
            q.append((start, 0))

            visited = set()
            while len(q) > 0:
                p, i = q.popleft()
                if p == end:
                    return i

                if p in visited:
                    continue

                visited.add(p)

                h = map[p]
                for n in neighbours_4(*p):
                    if n in map and map[n] <= h + 1:
                        q.append((n, i + 1))

            return 100000000

        print(pathlen(start))
        print(min(pathlen(k) for k, v in map.items() if v == ord('a')))



