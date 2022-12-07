if __name__ == "__main__":
    with open("input/day7.txt") as file:
        fs = {}
        cwd = fs

        for l in file:
            l = l.strip()
            if l.startswith("$ cd "):
                d = l[5:]
                if d == '/':
                    cwd = fs
                    continue

                if d not in cwd:
                    cwd[d] = {"..": cwd}

                cwd = cwd[d]
            elif l.startswith("$ ls") or l.startswith("dir"):
                pass
            else:
                size, name = l.split(' ')
                cwd[name] = int(size)

        sizes = []
        def stat(f):
            global sizes
            if isinstance(f, int):
                return f

            s = sum(stat(d) for k, d in f.items() if k != '..')
            sizes.append(s)
            return s

        total = stat(fs)
        print(sum(s for s in sizes if s <= 100000))

        rem = 70000000 - total
        needed = 30000000 - rem
        print(min(s for s in sizes if s >= needed))

