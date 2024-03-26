import os.path
import re

DATA = os.path.join(os.path.dirname(__file__), 'day02.txt')


def calculate_total_square_feet(data) -> int:
    result = 0
    for line in data.splitlines():
        dimensions = [eval(i) for i in re.findall(r'(\d+)x(\d+)x(\d+)', line)[0]]
        length = dimensions[0]
        width = dimensions[1]
        height = dimensions[2]

        result += ((2 * length * width) + (2 * width * height) + (2 * height * length)
                   + min(length * width, width * height, height * length))
    return result


def calculate_feet_of_ribbon(data) -> int:
    result = 0
    for line in data.splitlines():
        dimensions = [eval(i) for i in re.findall(r'(\d+)x(\d+)x(\d+)', line)[0]]
        length = dimensions[0]
        width = dimensions[1]
        height = dimensions[2]

        ribbon = min((2 * length + 2 * width), (2 * width + 2 * height), (2 * length + 2 * height))
        bow = length * width * height

        result += bow + ribbon
    return result


def main() -> int:
    with open(DATA) as f:
        data = f.read()
        print("Part 1: " + str(calculate_total_square_feet(data)))
        print("Part 2: " + str(calculate_feet_of_ribbon(data)))

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
