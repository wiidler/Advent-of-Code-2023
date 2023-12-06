input = open("./day6/input.txt", "r").readlines()


def part1():
    time_list = list(map(int, input[0].split()[1:]))
    distance_list = list(map(int, input[1].split()[1:]))
    pairs = list(zip(time_list, distance_list))
    result = 1
    for pair in pairs:
        ways = 0
        for hold_time in range(pair[0]):
            remaining_time = pair[0] - hold_time - 1
            distance = (hold_time + 1) * remaining_time
            if distance > pair[1]:
                ways += 1
        result *= ways
    return result


def part2():
    time_list = list(map(int, input[0].split()[1:]))
    distance_list = list(map(int, input[1].split()[1:]))
    combined_time = int("".join(map(str, time_list)))
    combined_distance = int("".join(map(str, distance_list)))
    ways = 0
    result = 1
    for hold_time in range(combined_time):
        remaining_time = combined_time - hold_time - 1
        distance = (hold_time + 1) * remaining_time
        if distance > combined_distance:
            ways += 1
    result *= ways
    return result


def main():
    print("Part 1:", part1())
    print("Part 2:", part2())


if __name__ == "__main__":
    main()
