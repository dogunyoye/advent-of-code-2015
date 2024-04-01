import os.path
import re

from math import prod

DATA = os.path.join(os.path.dirname(__file__), 'day15.txt')


def __build_ingredient(line) -> tuple:
    parts = re.findall(r'([A-Za-z]+): capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), '
                       r'calories (-?\d+)', line)[0]
    return parts[0], int(parts[1]), int(parts[2]), int(parts[3]), int(parts[4]), int(parts[5])


def calculate_total_score(data, has_calorie_limit) -> int:
    scores = []
    combos = []
    ingredients = [__build_ingredient(line) for line in data.splitlines()]

    # below runs out of memory!
    # combos = list(filter(lambda combo: combo[0] + combo[1] == 100, list(permutations(range(1, 101), 2))))

    for a in range(1, 98):
        for b in range(1, 98):
            if a + b > 98:
                continue
            for c in range(1, 98):
                if a + b + c > 99:
                    continue
                for d in range(1, 98):
                    if a + b + c + d == 100:
                        combos.append((a, b, c, d))

    for pair in combos:
        results = []
        overall = []

        for i, quantity in enumerate(pair):
            score = []
            ingredient = ingredients[i]
            for j in range(1, len(ingredient)):
                score.append(quantity * ingredient[j])
            results.append(score)

        for a in range(0, 4):
            total = 0
            for r in results:
                total += r[a]
            if total > 0:
                overall.append(total)

        if has_calorie_limit:
            calorie_count = 0
            for r in results:
                calorie_count += r[4]
            if calorie_count == 500:
                scores.append(prod(overall))
        else:
            scores.append(prod(overall))

    return max(scores)


def calculate_total_score_of_highest_scoring_cookie(data) -> int:
    return calculate_total_score(data, False)


def calculate_total_score_of_highest_scoring_cookie_with_500_calorie_limit(data) -> int:
    return calculate_total_score(data, True)


def main() -> int:
    with open(DATA) as f:
        data = f.read()
        print("Part 1: " + str(calculate_total_score_of_highest_scoring_cookie(data)))
        print("Part 2: " + str(calculate_total_score_of_highest_scoring_cookie_with_500_calorie_limit(data)))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
