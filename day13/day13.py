import os.path
import re

from itertools import permutations

DATA = os.path.join(os.path.dirname(__file__), 'day13.txt')


def __build_gain_loss_map(data) -> dict:
    gain_loss_map = {}
    for line in data.splitlines():
        parts = re.findall(r'([A-Za-z]+) would ([a-z]+) (\d+) happiness units by sitting next to ([A-Za-z]+).', line)[0]
        key, value = parts[0], parts[3]
        lose_or_gain = parts[1]
        happiness = int(parts[2])

        if key not in gain_loss_map:
            gain_loss_map[key] = {}

        relationship = gain_loss_map[key]
        if "lose" == lose_or_gain:
            relationship[value] = -happiness
        else:
            relationship[value] = happiness

    return gain_loss_map


def __calculate_gain_loss(order, gain_loss_map) -> int:
    result = 0
    for i in range(0, len(order)):
        left = i - 1
        right = i + 1

        if left == -1:
            left = len(order) - 1

        if right == len(order):
            right = 0

        relationship = gain_loss_map[order[i]]
        result += relationship[order[left]] + relationship[order[right]]

    return result


def find_best_total_change_in_happiness(data) -> int:
    gain_loss_map = __build_gain_loss_map(data)
    return max(__calculate_gain_loss(c, gain_loss_map) for c in list(permutations(gain_loss_map.keys())))


def find_best_total_change_in_happiness_involving_myself(data) -> int:
    gain_loss_map = __build_gain_loss_map(data)
    keys = gain_loss_map.keys()
    for k in keys:
        relationship = gain_loss_map[k]
        relationship["Myself"] = 0

    gain_loss_map["Myself"] = {}
    for k in keys:
        if k != "Myself":
            relationship = gain_loss_map["Myself"]
            relationship[k] = 0

    return max(__calculate_gain_loss(c, gain_loss_map) for c in list(permutations(gain_loss_map.keys())))


def main() -> int:
    with open(DATA) as f:
        data = f.read()
        print("Part 1: " + str(find_best_total_change_in_happiness(data)))
        print("Part 2: " + str(find_best_total_change_in_happiness_involving_myself(data)))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
