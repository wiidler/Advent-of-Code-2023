import re

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

total = 0

while True:
    line = input("Enter a string with numbers (or press Enter to exit): ")

    if line == "":
        break

    numbers = re.findall(r"(?=(one|two|three|four|five|six|seven|eight|nine|\d))", line)
    print(numbers)
    numbers = [number_names.get(num, num) for num in numbers]
    numbers = [int(num) for num in numbers]

    if len(numbers) > 0:
        numbers = [numbers[0], numbers[-1]]
        if len(numbers) == 1:
            numbers.append(numbers[0])
        num = int("".join(map(str, numbers)))
        print(num)
        total += num

print("The sum of all numbers is:", total)
