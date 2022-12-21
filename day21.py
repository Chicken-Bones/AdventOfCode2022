import re

if __name__ == "__main__":
    with open("input/day21.txt") as file:
        ops = {n: op for n, op in (l.strip().split(": ") for l in file)}

        def g(n):
            return eval(re.sub(r"([a-z]+)", r"g('\1')", ops[n]))

        print(g('root'))

        ops['root'] = re.sub("[+*/]", "-", ops['root'])

        ops['humn'] = '0'; a = g('root')
        ops['humn'] = '1000'; b = g('root')
        print(a*1000/(a-b))

