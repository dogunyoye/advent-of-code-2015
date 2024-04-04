import os.path
import re

DATA = os.path.join(os.path.dirname(__file__), 'day19.txt')


def __build_replacements_list(data) -> list:
    replacements = []
    for line in data.splitlines():
        if len(line) == 0:
            break
        parts = re.findall(r'([A-Za-z]+) => ([A-Za-z]+)', line)[0]
        replacements.append((parts[0], parts[1]))
    return replacements


def __invert_replacements_list(replacements) -> list:
    inverted = []
    for replacement in replacements:
        inverted.append((replacement[1], replacement[0]))
    return inverted


def __replace(source, replace_string, idx, length) -> str:
    template_list = list(source)
    template_list.insert(idx + length, replace_string)
    for j in range(idx + length - 1, idx - 1, -1):
        del template_list[j]
    return str("".join(template_list))


def __find_and_replace(text, key, value) -> tuple:
    steps = 0
    indices = [m.start() for m in re.finditer('(?=' + key + ')', text)]
    while len(indices) != 0:
        text = __replace(text, value, indices[0], len(key))
        indices = [m.start() for m in re.finditer('(?=' + key + ')', text)]
        steps += 1
    return text, steps


def calculate_number_of_distinct_molecules(data) -> int:
    result = set()
    replacements = __build_replacements_list(data)
    medicine_molecule = data.splitlines()[-1]

    for replacement in replacements:
        template = medicine_molecule
        indices = [m.start() for m in re.finditer('(' + replacement[0] + ')', medicine_molecule)]
        length = len(replacement[0])

        for idx in indices:
            candidate = __replace(template, replacement[1], idx, length)
            result.add(candidate)

    return len(result)


def find_fewest_steps_to_generate_medicine_molecule(data) -> int:
    result = 0
    inverted_replacements = __invert_replacements_list(__build_replacements_list(data))
    medicine_molecule = data.splitlines()[-1]

    while True:
        for inv in inverted_replacements:
            medicine_molecule, steps = __find_and_replace(medicine_molecule, inv[0], inv[1])
            result += steps
            if medicine_molecule == "e":
                return result


def main() -> int:
    with open(DATA) as f:
        data = f.read()
        print("Part 1: " + str(calculate_number_of_distinct_molecules(data)))
        print("Part 2: " + str(find_fewest_steps_to_generate_medicine_molecule(data)))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
