def play(nums, rounds):
    l = list(range(len(nums)))
    for _ in range(rounds):
        for n, m in enumerate(nums):
            i = l.index(n)
            del l[i]

            i = (i + m) % (len(l))
            l.insert(i, n)

    i = l.index(nums.index(0))
    return sum(nums[l[(i + n) % len(l)]] for n in [1000, 2000, 3000])


if __name__ == "__main__":
    with open("input/day20.txt") as file:
        nums = [int(s) for s in file]
        print(play(nums, 1))
        print(play([n*811589153 for n in nums], 10))
