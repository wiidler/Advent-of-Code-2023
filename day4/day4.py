input = open("./day4/input.txt", "r").readlines()


def part1():
    total = 0
    for line in input:
        left_nums, right_nums = map(str.split, line.split("|"))
        matches = set(left_nums) & set(right_nums)

        if matches:
            total += 2 ** (len(matches) - 1)
    return total


def part2():
    cards = [1] * len(input)
    for i, line in enumerate(input):
        left_nums, right_nums = map(str.split, line.split("|"))
        matches = len(set(left_nums) & set(right_nums))
        for j in range(i + 1, min(i + 1 + matches, len(input))):
            cards[j] += cards[i]
    return sum(cards)


def main():
    print("Part 1:", part1())
    print("Part 2:", part2())


if __name__ == "__main__":
    main()
