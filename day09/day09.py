import os.path
import re

from itertools import permutations

DATA = os.path.join(os.path.dirname(__file__), 'day09.txt')


def __calculate_journey(journey, distance_map) -> int:
    total_distance = 0
    for i in range(0, len(journey) - 1):
        start, end = journey[i], journey[i + 1]
        total_distance += distance_map[start + "-" + end]
    return total_distance


def __build_map_data(data) -> tuple:
    cities = set()
    distance_map = {}
    for line in data.splitlines():
        parts = re.findall(r'([A-Za-z]+) to ([A-Za-z]+) = (\d+)', line)[0]
        start, end, distance = parts[0], parts[1], int(parts[2])
        cities.add(start)
        cities.add(end)
        distance_map[start + "-" + end] = distance
        distance_map[end + "-" + start] = distance

    return cities, distance_map


def find_distance_of_shortest_route(data) -> int:
    cities, distance_map = __build_map_data(data)
    return min(__calculate_journey(journey, distance_map) for journey in list(permutations(cities)))


def find_distance_of_longest_route(data) -> int:
    cities, distance_map = __build_map_data(data)
    return max(__calculate_journey(journey, distance_map) for journey in list(permutations(cities)))


def main() -> int:
    with open(DATA) as f:
        data = f.read()
        print("Part 1: " + str(find_distance_of_shortest_route(data)))
        print("Part 2: " + str(find_distance_of_longest_route(data)))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
