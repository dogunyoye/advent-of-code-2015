import os.path
import re

DATA = os.path.join(os.path.dirname(__file__), 'day14.txt')


def __build_reindeer(line) -> tuple:
    parts = \
        re.findall(r'([A-Za-z]+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.', line)[0]
    return parts[0], int(parts[1]), int(parts[2]), int(parts[3])


def __race_reindeer(r, time) -> int:
    speed, active, resting = r[1], r[2], r[3]
    covered = speed * active
    div = time // (active + resting)
    rem = time % (active + resting)

    result = covered * div

    if rem < active:
        result += rem * speed
        return result

    while rem != 0:
        rem //= (active + resting)
        result += covered

    return result


def __race_reindeer_for_points(data, limit) -> int:
    table = {}
    distance = {}
    current_time = 0
    reindeer = list(map(__build_reindeer, data.splitlines()))
    for r in reindeer:
        distance[r[0]] = 0
        table[r[0]] = 0

    while current_time != limit:
        current_time += 1
        for r in reindeer:
            name, speed, active, resting = r[0], r[1], r[2], r[3]
            cycle = active + resting
            if 0 < (current_time % cycle) <= active:
                distance[name] += speed
        leaders = [key for m in [max(distance.values())] for key, val in distance.items() if val == m]
        for leader in leaders:
            table[leader] += 1

    return max(table.values())


def calculate_distance_of_winning_reindeer(data) -> int:
    return max(__race_reindeer(__build_reindeer(line), 2503) for line in data.splitlines())


def calculate_winning_reindeer_points(data) -> int:
    return __race_reindeer_for_points(data, 2503)


def main() -> int:
    with open(DATA) as f:
        data = f.read()
        print("Part 1: " + str(calculate_distance_of_winning_reindeer(data)))
        print("Part 2: " + str(calculate_winning_reindeer_points(data)))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
