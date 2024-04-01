import os.path
import re

DATA = os.path.join(os.path.dirname(__file__), 'day16.txt')


def __build_sue_map(data) -> dict:
    sue_list = []
    sue_map = {}
    for line in data.splitlines():
        parts = re.split(r'\d+:', line)
        sue_list.append(list(parts[1].strip().split(', ')))

    for i, s_list in enumerate(sue_list):
        sue_map[str(i + 1)] = {}
        for v in s_list:
            parts = re.findall(r'([a-z]+): (\d+)', v)[0]
            sue_map[str(i + 1)][parts[0]] = int(parts[1])

    return sue_map


def __build_ticker_tape_message() -> dict:
    return eval('''{"children": 3, "cats": 7, "samoyeds": 2, "pomeranians": 3, "akitas": 0, "vizslas": 0, "goldfish": 
    5, "trees": 3, "cars": 2, "perfumes": 1 }''')


def __parse_sue(sue, ticker_tape_message) -> bool:
    for k, v in ticker_tape_message.items():
        if (k in sue and sue[k] == v) or k not in sue:
            continue
        return False
    return True


def __parse_real_sue(sue, ticker_tape_message) -> bool:
    for k, v in ticker_tape_message.items():
        if k not in sue:
            continue

        if (k in sue) and (k == "cats" or k == "trees"):
            if sue[k] > v:
                continue

        if (k in sue) and (k == "pomeranians" or k == "goldfish"):
            if sue[k] < v:
                continue

        if (k in sue) and sue[k] == v:
            continue

        return False
    return True


def __find(data, parse_fn) -> int:
    sue_map = __build_sue_map(data)
    spec = __build_ticker_tape_message()

    for k, v in sue_map.items():
        if parse_fn(v, spec):
            return k

    raise Exception("Could not find Sue!")


def find_sue(data) -> int:
    return __find(data, __parse_sue)


def find_real_sue(data) -> int:
    return __find(data, __parse_real_sue)


def main() -> int:
    with open(DATA) as f:
        data = f.read()
        print("Part 1: " + str(find_sue(data)))
        print("Part 2: " + str(find_real_sue(data)))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
