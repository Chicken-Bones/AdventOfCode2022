from recordclass import recordclass

Operation = recordclass('Operation', 'a op b')
LinearEq = recordclass('LinearEq', 'm c')

def parseop(s: str):
    match s.split(' '):
        case [n]: return float(n)
        case [a, op, b]:
            return Operation(a, op, b)


def apply(a, op, b):
    match (a, op, b):
        case (float(v1), _, float(v2)):
            return eval(f'{v1}{op}{v2}')

        case (LinearEq(m, c), '+'|'-', float(v)):
            return LinearEq(m, apply(c, op, v))

        case (LinearEq(m, c), '*'|'/', float(v)):
            return LinearEq(apply(m, op, v), apply(c, op, v))

        case (float(v), '+', LinearEq(m, c)):
            return LinearEq(m, v+c)

        case (float(v), '*', LinearEq(m, c)):
            return LinearEq(v*m, v*c)

        case (float(v), '-', LinearEq(m, c)):
            return LinearEq(-m, v-c)

        case (_, '/', LinearEq()):
            raise Exception('Cannot handle divide on denominator')

        case _:
            raise Exception('What did I forget?')


def simplify(v):
    match v:
        case Operation(a, op, b):
            return apply(simplify(ops[a]), op, simplify(ops[b]))
        case _:
            return v


if __name__ == "__main__":
    with open("input/day21.txt") as file:

        ops = {n: parseop(op) for n, op in (l.strip().split(": ") for l in file)}
        root_op = ops['root']
        print(simplify(root_op))

        ops['humn'] = LinearEq(1.0, 0.0)
        eq = Operation(root_op.a, '-', root_op.b)
        sln = simplify(eq)
        print(sln)
        print(-sln.c/sln.m) # 0 = mx+c


