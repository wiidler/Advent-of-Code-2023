import re

input = open("./day3/input.txt", "r").readlines()


def part1():
    total = 0
    symbols = {}
    gears = {}

    for row in range(len(input[0]) - 1):
        for col in range(len(input)):
            if input[row][col] not in "0123456789.":
                symbols[(row, col)] = input[row][col]
    for row_num, row in enumerate(input):
        for p in re.finditer(r"\d+", row):
            temp = []
            for i in range(p.start() - 1, p.end() + 1):
                temp.append((row_num - 1, i))
                temp.append((row_num, i))
                temp.append((row_num + 1, i))
            valid = False
            for q in temp:
                if q in symbols:
                    valid = True
            if valid:
                total += int(p.group())
    return total


def part2():
    total = 0
    symbols = {}
    gears = {}

    for row in range(len(input[0]) - 1):
        for col in range(len(input)):
            if input[row][col] == "*":
                gears[(row, col)] = []
    for row_num, row in enumerate(input):
        for p in re.finditer(r"\d+", row):
            temp = []
            for i in range(p.start() - 1, p.end() + 1):
                temp.append((row_num - 1, i))
                temp.append((row_num, i))
                temp.append((row_num + 1, i))
            valid = False
            for q in temp:
                if q in gears:
                    gears[q].append(int(p.group()))
    for g in gears:
        if len(gears[g]) == 2:
            total += gears[g][0] * gears[g][1]
    return total


def main():
    print("Part 1:", part1())
    print("Part 2:", part2())


if __name__ == "__main__":
    main()
