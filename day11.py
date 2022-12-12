from math import *
from recordclass import recordclass

Monkey = recordclass('Monkey', 'items op test m1 m2 inspected')


def play(rounds, div3):
    monkeys = [
        Monkey([78, 53, 89, 51, 52, 59, 58, 85], lambda i: i*3, 5, 2, 7, 0),
        Monkey([64], lambda i: i+7, 2, 3, 6, 0),
        Monkey([71, 93, 65, 82], lambda i: i+5, 13, 5, 4, 0),
        Monkey([67, 73, 95, 75, 56, 74], lambda i: i+8, 19, 6, 0, 0),
        Monkey([85, 91, 90], lambda i: i+4, 11, 3, 1, 0),
        Monkey([67, 96, 69, 55, 70, 83, 62], lambda i: i*2, 3, 4, 1, 0),
        Monkey([53, 86, 98, 70, 64], lambda i: i+6, 7, 7, 0, 0),
        Monkey([88, 64], lambda i: i*i, 17, 2, 5, 0)
    ]

    lcd = prod([m.test for m in monkeys])

    for _ in range(rounds):
        for m in monkeys:
            for i in m.items:
                i = m.op(i)
                i %= lcd
                if div3: i //= 3
                n = m.m1 if i % m.test == 0 else m.m2
                monkeys[n].items.append(i)
                m.inspected += 1

            m.items = []

    inspected = [m.inspected for m in monkeys]
    inspected.sort(reverse=True)
    return inspected[0] * inspected[1]


if __name__ == "__main__":
    print(play(20, div3=True))
    print(play(10000, div3=False))


