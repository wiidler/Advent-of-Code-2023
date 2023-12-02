import re

string = "Game 1: 20 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"

# Extract game number
game_number = re.search(r"Game (\d+):", string).group(1)

total = 0

# Store the largest number for each color
largest_numbers = {"red": float("-inf"), "green": float("-inf"), "blue": float("-inf")}


def part1():
    while True:
        add = True
        string = input("Enter a string with numbers (or press Enter to exit): ")

        if string == "":
            break

        # Extract game number
        game_number = re.search(r"Game (\d+):", string).group(1)
        numbers_with_colors = re.findall(r"(\d+) (\w+)", string)

        print("Game Number:", game_number)
        print("Numbers with Colors:")
        for number, color in numbers_with_colors:
            if (
                (color == "red" and int(number) > 12)
                or (color == "green" and int(number) > 13)
                or (color == "blue" and int(number) > 14)
            ):
                print("Invalid pull:", number, color)
                add = False
            else:
                print(number, color)
        if add:
            total += int(game_number)

    print("The sum of all numbers is:", total)


def part2():
    total = 0
    while True:
        string = input("Enter a string with numbers (or press Enter to exit): ")

        if string == "":
            break
        largest_numbers = {
            "red": 0,
            "green": 0,
            "blue": 0,
        }
        numbers_with_colors = re.findall(r"(\d+) (\w+)", string)
        for number, color in numbers_with_colors:
            largest_numbers[color] = max(largest_numbers[color], int(number))
        print(largest_numbers)

        # Multiply all the largest numbers into total
        mult = 1
        for color, number in largest_numbers.items():
            mult *= number
        total += mult

    print("Sum of the power of the sets:", total)


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
