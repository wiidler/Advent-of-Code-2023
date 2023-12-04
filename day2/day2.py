import re

string = open("./day2/input.txt", "r").readlines()


def part1():
    total = 0
    for line in string:
        add = True
        # Extract game number
        game_number = re.search(r"Game (\d+):", line).group(1)
        numbers_with_colors = re.findall(r"(\d+) (\w+)", line)
        for number, color in numbers_with_colors:
            if (
                (color == "red" and int(number) > 12)
                or (color == "green" and int(number) > 13)
                or (color == "blue" and int(number) > 14)
            ):
                add = False
        if add:
            total += int(game_number)

    return total


def part2():
    total = 0
    for line in string:
        largest_numbers = {
            "red": 0,
            "green": 0,
            "blue": 0,
        }
        numbers_with_colors = re.findall(r"(\d+) (\w+)", line)
        for number, color in numbers_with_colors:
            largest_numbers[color] = max(largest_numbers[color], int(number))

        # Multiply all the largest numbers into total
        mult = 1
        for color, number in largest_numbers.items():
            mult *= number
        total += mult

    return total


def main():
    print("Part 1:", part1())
    print("Part 2:", part2())


if __name__ == "__main__":
    main()
