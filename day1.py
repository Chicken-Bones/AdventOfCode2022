if __name__ == "__main__":
    with open("input/day1.txt") as file:
        food = [sum(int(s) for s in elf.splitlines()) for elf in file.read().split("\n\n")]
        print(max(food))
        print(sum(sorted(food, reverse=True)[:3]))
