input = open("./day5/input.txt", "r").readlines()

seeds = []
seed_to_soil_map = []
soil_to_fertilizer_map = []
fertilizer_to_water_map = []
water_to_light_map = []
light_to_temperature_map = []
temperature_to_humidity_map = []
humidity_to_location_map = []


def convert_number(number, map):
    for dest_start, source_start, length in map:
        if source_start <= number < source_start + length:
            return dest_start + (number - source_start)
    return number


def find_lowest_location(seeds):
    location_numbers = set()
    for seed in seeds:
        soil = convert_number(seed, seed_to_soil_map)
        fertilizer = convert_number(soil, soil_to_fertilizer_map)
        water = convert_number(fertilizer, fertilizer_to_water_map)
        light = convert_number(water, water_to_light_map)
        temperature = convert_number(light, light_to_temperature_map)
        humidity = convert_number(temperature, temperature_to_humidity_map)
        location = convert_number(humidity, humidity_to_location_map)
        location_numbers.add(location)
    return min(location_numbers)


def part1():
    for line in input:
        if line.startswith("seeds:"):
            seeds = list(map(int, line.split()[1:]))
        elif line.startswith("seed-to-soil map:"):
            current_map = seed_to_soil_map
        elif line.startswith("soil-to-fertilizer map:"):
            current_map = soil_to_fertilizer_map
        elif line.startswith("fertilizer-to-water map:"):
            current_map = fertilizer_to_water_map
        elif line.startswith("water-to-light map:"):
            current_map = water_to_light_map
        elif line.startswith("light-to-temperature map:"):
            current_map = light_to_temperature_map
        elif line.startswith("temperature-to-humidity map:"):
            current_map = temperature_to_humidity_map
        elif line.startswith("humidity-to-location map:"):
            current_map = humidity_to_location_map
        elif line.strip() and current_map is not None:
            current_map.append(list(map(int, line.split())))

    lowest_location = find_lowest_location(seeds)
    return lowest_location


def part2():
    seeds = []
    key = list(map(int, input[0].split()[1:]))
    for i in range(0, len(key), 2):
        for j in range(key[i + 1]):
            seeds.append(key[i] + j)
    lowest_location = find_lowest_location(seeds)
    return lowest_location


def main():
    print("Part 1:", part1())
    print("Part 2:", part2())


if __name__ == "__main__":
    main()
