import hashlib
import os.path

DATA = os.path.join(os.path.dirname(__file__), 'day04.txt')


def __find_number(data, number_of_zeroes) -> int:
    result = 0
    while True:
        candidate = hashlib.md5((data + str(result)).encode()).hexdigest()
        if candidate.startswith("0" * number_of_zeroes):
            break
        result += 1
    return result


def find_number_for_hash_starting_with_five_zeroes(data) -> int:
    return __find_number(data, 5)


def find_number_for_hash_starting_with_six_zeroes(data) -> int:
    return __find_number(data, 6)


def main() -> int:
    with open(DATA) as f:
        data = f.read()
        print("Part 1: " + str(find_number_for_hash_starting_with_five_zeroes(data)))
        print("Part 2: " + str(find_number_for_hash_starting_with_six_zeroes(data)))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
