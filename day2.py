def score(a, b):
    i = ord(a) - ord('A')
    j = ord(b) - ord('X')
    score = (j - i + 1) % 3 * 3
    return j + 1 + score


def score2(a, b):
    i = ord(a) - ord('A')
    j = ord(b) - ord('X')
    j = (i + j - 1) % 3
    score = (j - i + 1) % 3 * 3
    return j + 1 + score


if __name__ == "__main__":
    with open("input/day2.txt") as file:
        actions = [s.strip().split(' ') for s in file]
        print(sum(score(a, b) for a, b in actions))
        print(sum(score2(a, b) for a, b in actions))
