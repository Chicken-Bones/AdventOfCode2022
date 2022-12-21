from recordclass import recordclass

Operation = recordclass('Operation', 'a op b')

def parseop(s: str):
    match s.split(' '):
        case [n]: return float(n)
        case [a, op, b]: return Operation(a, op, b)


def calc(v: str):
    match ops[v]:
        case Operation(a, op, b): return eval(f'{calc(a)}{op}{calc(b)}')
        case f: return f


if __name__ == "__main__":
    with open("input/day21.txt") as file:

        ops = {n: parseop(op) for n, op in (l.strip().split(": ") for l in file)}
        print(calc('root'))

        def solve_for(x):
            p, eq = next((k, op) for k, op in ops.items() if isinstance(op, Operation) and (op.a == x or op.b == x))

            if p == 'root':
                return calc(eq.a if eq.b == x else eq.b)

            y = solve_for(p)
            match eq: # y = ..., rearrange for x
                case Operation(o, '+', c) if o == x: return y-calc(c)
                case Operation(c, '+', o) if o == x: return y-calc(c)
                case Operation(o, '*', c) if o == x: return y/calc(c)
                case Operation(c, '*', o) if o == x: return y/calc(c)
                case Operation(o, '-', c) if o == x: return y+calc(c)
                case Operation(c, '-', o) if o == x: return -y+calc(c)
                case Operation(o, '/', c) if o == x: return y*calc(c)
                case Operation(c, '/', o) if o == x: return calc(c)/y

        print(solve_for('humn'))


