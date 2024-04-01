import os.path

DATA = os.path.join(os.path.dirname(__file__), 'day18.txt')


def __build_grid(data) -> dict:
    grid = {}
    for i in range(0, 100):
        for j in range(0, 100):
            grid[(i, j)] = '.'

    for i, line in enumerate(data.splitlines()):
        for j in range(0, len(line)):
            grid[(i, j)] = line[j]

    return grid


def __is_corner(pos) -> bool:
    return pos == (0, 0) or pos == (0, 99) or pos == (99, 0) or pos == (99, 99)


def __simulate_lights(data, fixed_corners) -> int:
    light_map = __build_grid(data)
    if fixed_corners:
        for p in [(0, 0), (0, 99), (99, 0), (99, 99)]:
            light_map[p] = '#'

    steps = 100

    while steps != 0:
        next_state = {}
        for k, v in light_map.items():

            if fixed_corners and __is_corner(k):
                next_state[k] = '#'
                continue

            i, j = k[0], k[1]
            neighbors = [(i, j - 1), (i - 1, j - 1), (i - 1, j), (i - 1, j + 1),
                         (i, j + 1), (i + 1, j + 1), (i + 1, j), (i + 1, j - 1)]
            neighbors = [(x, y) for (x, y) in neighbors if 0 <= x < 100 and 0 <= y < 100]

            count = 0
            for n in neighbors:
                if light_map[n] == '#':
                    count += 1

            next_state[k] = '.'
            if v == '#':
                if count == 2 or count == 3:
                    next_state[k] = '#'
            else:
                if count == 3:
                    next_state[k] = '#'

        light_map = next_state
        steps -= 1

    return len(list(filter(lambda state: state == '#', light_map.values())))


def lights_on_after_100_steps(data) -> int:
    return __simulate_lights(data, False)


def lights_on_after_100_steps_with_fixed_corners(data) -> int:
    return __simulate_lights(data, True)


def main() -> int:
    with open(DATA) as f:
        data = f.read()
        print("Part 1: " + str(lights_on_after_100_steps(data)))
        print("Part 2: " + str(lights_on_after_100_steps_with_fixed_corners(data)))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
