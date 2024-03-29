import os.path

import json

DATA = os.path.join(os.path.dirname(__file__), 'day12.txt')


def __recurse_json(json_object) -> int:
    if isinstance(json_object, int):
        return json_object

    if isinstance(json_object, str):
        return 0

    result = 0
    if isinstance(json_object, list):
        for item in json_object:
            result += __recurse_json(item)

    if isinstance(json_object, dict):
        for item in json_object.values():
            result += __recurse_json(item)

    return result


def __recurse_json_discounting_red(json_object) -> int:
    if isinstance(json_object, int):
        return json_object

    if isinstance(json_object, str):
        return 0

    result = 0
    if isinstance(json_object, list):
        for item in json_object:
            result += __recurse_json_discounting_red(item)

    if isinstance(json_object, dict):
        values = json_object.values()
        if "red" not in values:
            for v in values:
                result += __recurse_json_discounting_red(v)

    return result


def calculate_total_of_all_numbers(data) -> int:
    json_object = json.loads(data)
    return __recurse_json(json_object)


def calculate_total_of_all_numbers_discounting_red(data) -> int:
    json_object = json.loads(data)
    return __recurse_json_discounting_red(json_object)


def main() -> int:
    with open(DATA) as f:
        data = f.read()
        print("Part 1: " + str(calculate_total_of_all_numbers(data)))
        print("Part 2: " + str(calculate_total_of_all_numbers_discounting_red(data)))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
