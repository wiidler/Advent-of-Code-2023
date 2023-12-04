import re

lines = open("day1\input.txt", "r").readlines()

number_names = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def part1():
    total = 0
    for line in lines:
        numbers = re.findall(r"(?=(\d))", line)
        numbers = [number_names.get(num, num) for num in numbers]
        numbers = [int(num) for num in numbers]

        if len(numbers) > 0:
            numbers = [numbers[0], numbers[-1]]
            if len(numbers) == 1:
                numbers.append(numbers[0])
            num = int("".join(map(str, numbers)))
            total += num
    return total


def part2():
    total = 0
    for line in lines:
        numbers = re.findall(
            r"(?=(one|two|three|four|five|six|seven|eight|nine|\d))", line
        )
        numbers = [number_names.get(num, num) for num in numbers]
        numbers = [int(num) for num in numbers]

        if len(numbers) > 0:
            numbers = [numbers[0], numbers[-1]]
            if len(numbers) == 1:
                numbers.append(numbers[0])
            num = int("".join(map(str, numbers)))
            total += num
    return total


def main():
    print("Part 1:", part1())
    print("Part 2:", part2())


if __name__ == "__main__":
    main()
