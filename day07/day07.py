import os.path

DATA = os.path.join(os.path.dirname(__file__), 'day07.txt')


def __traverse_wires(connected, operations, signals, wire) -> int:
    if wire in signals:
        return signals[wire]

    parents = connected[wire]

    if parents[0].isnumeric():
        left = int(parents[0])
    else:
        left = __traverse_wires(connected, operations, signals, parents[0])

    if wire not in operations:
        return left

    if len(parents) == 2:

        if (operations[wire] == "AND") | (operations[wire] == "OR"):
            if parents[1].isnumeric():
                right = int(parents[1])
            else:
                right = __traverse_wires(connected, operations, signals, parents[1])

            if operations[wire] == "AND":
                signals[wire] = left & right
            else:
                signals[wire] = left | right
        else:
            shift = int(parents[1])
            if operations[wire] == "LSHIFT":
                signals[wire] = left << shift
            else:
                signals[wire] = left >> shift
    else:
        signals[wire] = pow(2, 16) + ~left

    return signals[wire]


def __build_wires_map(data) -> tuple:
    signals, connected, operations = {}, {}, {}

    for line in data.splitlines():
        parts = line.split(" -> ")
        wire = parts[1]

        if parts[0].isnumeric():
            signals[wire] = int(parts[0])
        else:
            input_parts = parts[0].split(" ")
            if len(input_parts) == 3:  # AND, OR, LSHIFT, RSHIFT
                connected[wire] = [input_parts[0], input_parts[2]]
                operations[wire] = input_parts[1]
            elif len(input_parts) == 2:  # NOT
                connected[wire] = [input_parts[1]]
                operations[wire] = "NOT"
            else:
                connected[wire] = [parts[0]]

    return signals, connected, operations


def find_signal_provided_to_wire_a(data) -> int:
    signals, connected, operations = __build_wires_map(data)
    return __traverse_wires(connected, operations, signals, "a")


def find_signal_provided_to_wire_a_after_rewire(data) -> int:
    original_a = find_signal_provided_to_wire_a(data)
    signals, connected, operations = __build_wires_map(data)
    signals["b"] = original_a
    return __traverse_wires(connected, operations, signals, "a")


def main() -> int:
    with open(DATA) as f:
        data = f.read()
        print("Part 1: " + str(find_signal_provided_to_wire_a(data)))
        print("Part 2: " + str(find_signal_provided_to_wire_a_after_rewire(data)))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
