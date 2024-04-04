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


def __replace(source, replace_string, idx, length) -> str:
    template_list = list(source)
    template_list.insert(idx + length, replace_string)
    for j in range(idx + length - 1, idx - 1, -1):
        del template_list[j]
    return str("".join(template_list))


def __get_ingredient(ingredient, replacements) -> list:
    return list(filter(lambda i: i[0] == ingredient, replacements))


def __find_placeholders(text, replacements) -> list:
    result = []
    for r in replacements:
        indices = [m.start() for m in re.finditer('(?=' + r[0] + ')', text)]
        for idx in indices:
            result.append((r[0], r[1], idx))
    return result


def __build_medicine_molecule(medicine_molecule, replacements, curr, steps, result):
    if curr == medicine_molecule:
        result.append(steps)

    if len(curr) > len(medicine_molecule):
        return

    if len(result) > 0 and (steps >= min(result)):
        return

    placeholders = __find_placeholders(curr, replacements)
    for p in placeholders:
        k, v, idx = p[0], p[1], p[2]
        __build_medicine_molecule(medicine_molecule, replacements, __replace(curr, v, idx, len(k)), (steps + 1), result)


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


def __find_fewest_steps_to_generate_medicine_molecule(data) -> int:
    replacements = __build_replacements_list(data)
    medicine_molecule = data.splitlines()[-1]
    result = []

    start = __get_ingredient("e", replacements)
    for s in start:
        steps = 1
        __build_medicine_molecule(medicine_molecule, replacements, s[1], steps, result)

    return min(result)


def main() -> int:
    with open(DATA) as f:
        data = f.read()
        print("Part 1: " + str(calculate_number_of_distinct_molecules(data)))
        print("Part 2: " + str(__find_fewest_steps_to_generate_medicine_molecule(data)))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
