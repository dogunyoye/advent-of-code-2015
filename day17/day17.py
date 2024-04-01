import os.path
from itertools import permutations, combinations

DATA = os.path.join(os.path.dirname(__file__), 'day17.txt')


def find_number_of_different_combinations(data) -> int:
    result = 0
    containers = [eval(line) for line in data.splitlines()]
    for i in range(1, len(containers) + 1):
        result += len(list(filter(lambda combo: sum(combo) == 150, list(combinations(containers, i)))))
    return result


def find_number_of_different_combinations_to_fill_minimum_containers(data) -> int:
    containers = [eval(line) for line in data.splitlines()]
    result = {}
    for i in range(1, len(containers) + 1):
        value = len(list(filter(lambda combo: sum(combo) == 150, list(combinations(containers, i)))))
        if value > 0:
            result[i] = value
    return result[min(result.keys())]


def main() -> int:
    with open(DATA) as f:
        data = f.read()
        print("Part 1: " + str(find_number_of_different_combinations(data)))
        print("Part 2: " + str(find_number_of_different_combinations_to_fill_minimum_containers(data)))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
