import os.path

DATA = os.path.join(os.path.dirname(__file__), 'day08.txt')


def find_difference(data) -> int:
    string_literals = []
    in_memory = []
    for line in data.splitlines():
        string_literals.append(len(line))
        in_memory.append(len(eval(line)))
    return sum(string_literals) - sum(in_memory)


def find_difference_new_rules(data) -> int:
    string_literals = []
    newly_encoded_string_literals = []
    for line in data.splitlines():
        string_literals.append(len(line))
        encoded = ""
        for i in range(0, len(line)):
            if line[i] == '"':
                encoded += "\\\""
            elif line[i] == "\\":
                encoded += "\\\\"
            else:
                encoded += line[i]
        encoded = '"' + encoded + '"'
        newly_encoded_string_literals.append(len(encoded))
    return sum(newly_encoded_string_literals) - sum(string_literals)


def main() -> int:
    with open(DATA) as f:
        data = f.read()
        print("Part 1: " + str(find_difference(data)))
        print("Part 2: " + str(find_difference_new_rules(data)))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
