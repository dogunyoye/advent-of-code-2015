import os.path
from math import prod

DATA = os.path.join(os.path.dirname(__file__), 'day24.txt')


# Takes 32 seconds
# https://stackoverflow.com/a/34519260
def subset_sum(numbers, target, partial=None, partial_sum=0):
    if partial is None:
        partial = []
    if partial_sum == target:
        yield partial
    if partial_sum >= target:
        return
    for i, n in enumerate(numbers):
        remaining = numbers[i + 1:]
        yield from subset_sum(remaining, target, partial + [n], partial_sum + n)


# This problem is the subset sum problem - https://en.wikipedia.org/wiki/Subset_sum_problem
def __find_quantum_entanglement(data, groups) -> int:
    numbers = [eval(line) for line in data.splitlines()]
    group_size = sum(numbers) // groups

    # Brute force solution, fairly slow... takes 140s for both parts
    # result = [seq for i in range(len(numbers), 0, -1)
    #           for seq in combinations(numbers, i)
    #           if sum(seq) == group_size]

    result = list(subset_sum(numbers, group_size))

    result.sort(key=lambda c: len(c))
    smallest_size = len(result[0])
    result = list(filter(lambda c: len(c) == smallest_size, result))

    return min([prod(c) for c in result])


def find_quantum_entanglement_with_three_groups(data) -> int:
    return __find_quantum_entanglement(data, 3)


def find_quantum_entanglement_with_four_groups(data) -> int:
    return __find_quantum_entanglement(data, 4)


def main() -> int:
    with open(DATA) as f:
        data = f.read()
        print("Part 1: " + str(find_quantum_entanglement_with_three_groups(data)))
        print("Part 2: " + str(find_quantum_entanglement_with_four_groups(data)))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
