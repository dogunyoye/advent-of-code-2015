import os.path
import re

DATA = os.path.join(os.path.dirname(__file__), 'day02.txt')


def calculate_total_square_feet(data) -> int:
    result = 0
    for line in data.splitlines():
        dimensions = [eval(i) for i in re.findall(r'(\d+)x(\d+)x(\d+)', line)[0]]
        length, width, height = dimensions[0], dimensions[1], dimensions[2]
        lw, wh, hl = length * width, width * height, height * length
        result += ((2 * lw) + (2 * wh) + (2 * hl) + min(lw, wh, hl))
    return result


def calculate_feet_of_ribbon(data) -> int:
    result = 0
    for line in data.splitlines():
        dimensions = [eval(i) for i in re.findall(r'(\d+)x(\d+)x(\d+)', line)[0]]
        length, width, height = dimensions[0], dimensions[1], dimensions[2]

        present = min((2 * length + 2 * width), (2 * width + 2 * height), (2 * length + 2 * height))
        bow = length * width * height
        result += bow + present
    return result


def main() -> int:
    with open(DATA) as f:
        data = f.read()
        print("Part 1: " + str(calculate_total_square_feet(data)))
        print("Part 2: " + str(calculate_feet_of_ribbon(data)))

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
