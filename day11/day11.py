import os.path

DATA = os.path.join(os.path.dirname(__file__), 'day11.txt')


def __increment_password(password) -> str:
    new_password = []
    wrapped_around = False

    while True:
        for i in range(len(password) - 1, -1, -1):
            next_char = (ord(password[i]) + 1) % 123
            if next_char == 0:
                wrapped_around = True
                next_char = 97
            new_password.append(chr(next_char))
            if not wrapped_around:
                for j in range(i - 1, -1, -1):
                    new_password.append(password[j])
                break
            wrapped_around = False
        new_password.reverse()
        return "".join(new_password)


def find_next_password(data) -> str:
    new_password = data
    disallowed_chars = {'i', 'o', 'l'}
    while True:
        new_password = __increment_password(new_password)
        contains_disallowed_chars = False
        three_consecutive_letters = False
        two_non_overlapping_pairs = False

        for i in range(0, len(new_password)):
            if new_password[i] in disallowed_chars:
                contains_disallowed_chars = True
                break

        if contains_disallowed_chars:
            continue

        for i in range(0, len(new_password) - 2):
            first, second, third = ord(new_password[i]), ord(new_password[i + 1]), ord(new_password[i + 2])
            if first + 1 == second and second + 1 == third:
                three_consecutive_letters = True
                break

        if not three_consecutive_letters:
            continue

        pair_indices = set()
        for i in range(0, len(new_password) - 1):
            first, second = ord(new_password[i]), ord(new_password[i + 1])
            if first == second:
                pair_indices.add(i)
                pair_indices.add(i + 1)

        if len(pair_indices) >= 4:
            two_non_overlapping_pairs = True

        if two_non_overlapping_pairs:
            return new_password


def find_next_password_again(data) -> str:
    return find_next_password(find_next_password(data))


def main() -> int:
    with open(DATA) as f:
        data = f.read()
        print("Part 1: " + find_next_password(data))
        print("Part 2: " + find_next_password_again(data))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
