import os.path

DATA = os.path.join(os.path.dirname(__file__), 'day01.txt')


def which_floor(data) -> int:
    result = 0
    for c in data:
        if c == '(':
            result += 1
        elif c == ')':
            result -= 1

    return result


def which_floor_to_basement(data) -> int:
    result = 0
    for i, c in enumerate(data):
        if c == '(':
            result += 1
        elif c == ')':
            result -= 1

        if result == -1:
            return i + 1

    raise Exception("Could not find solution!")


def main() -> int:
    with open(DATA) as f:
        data = f.read()
        print("Part 1: " + str(which_floor(data)))
        print("Part 2: " + str(which_floor_to_basement(data)))

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
