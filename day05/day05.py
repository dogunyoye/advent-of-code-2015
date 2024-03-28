import os.path
import re

DATA = os.path.join(os.path.dirname(__file__), 'day05.txt')


def __is_nice(data) -> bool:
    vowels = len(re.findall("[aeiou]", data))
    twice_in_a_row = False
    disallowed_pairs = {"ab", "cd", "pq", "xy"}
    for i in range(0, len(data) - 1):
        pair = str(data[i] + data[i + 1])
        if pair in disallowed_pairs:
            return False
        if pair[0] == pair[1]:
            twice_in_a_row = True

    return (vowels >= 3) & twice_in_a_row


def __is_nice_new_rules(data) -> bool:
    non_overlapping_pair = False
    repeating_start_and_end_letter = False

    for i in range(0, len(data) - 1):
        pair = str(data[i] + data[i + 1])
        indices = [m.start() for m in re.finditer('(?=' + pair + ')', data)]
        if len(indices) >= 2:
            non_overlapping_pair = True
            diff = indices[len(indices) - 1] - indices[0]
            if diff == 1:
                non_overlapping_pair = False
            break

    for i in range(0, len(data) - 2):
        if data[i] == data[i + 2]:
            repeating_start_and_end_letter = True
            break

    return non_overlapping_pair & repeating_start_and_end_letter


def __find(data, is_nice_fn) -> int:
    result = 0
    for line in data.splitlines():
        if is_nice_fn(line):
            result += 1

    return result


def find_number_of_nice_strings(data) -> int:
    return __find(data, __is_nice)


def find_number_of_nice_strings_with_new_rules(data) -> int:
    return __find(data, __is_nice_new_rules)


def main() -> int:
    with open(DATA) as f:
        data = f.read()
        print("Part 1: " + str(find_number_of_nice_strings(data)))
        print("Part 2: " + str(find_number_of_nice_strings_with_new_rules(data)))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
