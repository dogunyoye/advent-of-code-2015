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


def calculate_number_of_distinct_molecules(data) -> int:
    result = set()
    replacements = __build_replacements_list(data)
    medicine_molecule = data.splitlines()[-1]

    for replacement in replacements:
        template = medicine_molecule
        indices = [m.start() for m in re.finditer('(' + replacement[0] + ')', medicine_molecule)]

        length = len(replacement[0])

        for idx in indices:
            template_list = list(template)
            template_list.insert(idx + length, replacement[1])
            for j in range(idx + length - 1, idx - 1, -1):
                del template_list[j]

            candidate = str("".join(template_list))
            result.add(candidate)

    return len(result)


def main() -> int:
    with open(DATA) as f:
        data = f.read()
        print("Part 1: " + str(calculate_number_of_distinct_molecules(data)))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
