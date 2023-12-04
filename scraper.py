import os
import requests
from datetime import datetime
import pytz

# Set the initial date
time = datetime.now(pytz.timezone("US/Eastern")).strftime("%d")
date = int(time)

# Create a folder with the name "daydate"
folder_name = f"day{date}"
os.makedirs(folder_name, exist_ok=True)

# Create daydate.py and input.txt files
with open(os.path.join(folder_name, f"day{date}.py"), "w") as day_file:
    day_file.write(
        """\
input = open("./{}/input.txt", "r").readlines()

def part1():
    # TODO: Implement Part 1 logic

# def part2():
#     # TODO: Implement Part 2 logic

def main():
    print("Part 1:", part1())
    # print("Part 2:", part2())

if __name__ == "__main__":
    main()
""".format(
            folder_name
        )
    )

# Fetch the input data from the website
url = f"https://adventofcode.com/2023/day/{date}/input"
response = requests.get(
    url,
    cookies={
        "session": "53616c7465645f5f0398db9953dd4313f592153eaf598e6f69bd2bd869801ee06faea5029959c44fe431cfdf783de14d9e6007fc8f67cefda94d55823781939c"
    },
)
input_text = response.text

# Write the input data to input.txt
with open(os.path.join(folder_name, "input.txt"), "w") as input_file:
    input_file.write(input_text)

print(f"Files created in the folder: {folder_name}")
