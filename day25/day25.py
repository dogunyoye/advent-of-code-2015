import os.path
import re

DATA = os.path.join(os.path.dirname(__file__), 'day25.txt')


def __get_code_location(data) -> tuple:
    parts = []
    for line in data.splitlines():
        parts = re.findall(
            r'To continue, please consult the code grid in the manual. '
            r'Enter the code at row (\d+), column (\d+).', line)[0]
    return eval(parts[0]), eval(parts[1])


def __traverse_sheet_of_paper(code_location):
    destination = code_location[0]-1, code_location[1]-1
    current_code = 20151125
    count = 1

    while True:
        current_pos = (count, 0)
        for _ in range(0, count + 1):
            current_code *= 252533
            current_code %= 33554393
            if current_pos == destination:
                return current_code
            current_pos = (current_pos[0] - 1, current_pos[1] + 1)
        count += 1


def calculate_code(data) -> int:
    code_location = __get_code_location(data)
    return __traverse_sheet_of_paper(code_location)


def main() -> int:
    with open(DATA) as f:
        data = f.read()
        print("Part 1: " + str(calculate_code(data)))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
