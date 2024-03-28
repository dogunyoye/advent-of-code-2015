import os.path
import re

DATA = os.path.join(os.path.dirname(__file__), 'day06.txt')


class Position(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '<' + str(self.x) + ',' + str(self.y) + '>'

    def __eq__(self, other):
        return self.y == other.y and self.x == other.x

    def __hash__(self):
        return hash((self.x, self.y))

    def __repr__(self):
        return "Position(%d, %d)" % (self.x, self.y)


def find_how_many_lights_on(data) -> int:
    on = set()
    for line in data.splitlines():
        if "toggle" in line:
            parts = re.findall(r'([a-z]+) (\d+),(\d+) through (\d+),(\d+)', line)[0]
            start_x, end_x, start_y, end_y = int(parts[1]), int(parts[3]), int(parts[2]), int(parts[4])
        else:
            parts = re.findall(r'([a-z]+) ([a-z]+) (\d+),(\d+) through (\d+),(\d+)', line)[0]
            start_x, end_x, start_y, end_y = int(parts[2]), int(parts[4]), int(parts[3]), int(parts[5])

        for x in range(start_x, end_x + 1):
            for y in range(start_y, end_y + 1):
                if "toggle" in line:
                    if Position(x, y) in on:
                        on.remove(Position(x, y))
                    else:
                        on.add(Position(x, y))
                else:
                    if parts[1] == "on":
                        on.add(Position(x, y))
                    else:
                        if Position(x, y) in on:
                            on.remove(Position(x, y))

    return len(on)


def find_total_brightness_of_all_lights(data) -> int:
    lights = {}
    for line in data.splitlines():
        if "toggle" in line:
            parts = re.findall(r'([a-z]+) (\d+),(\d+) through (\d+),(\d+)', line)[0]
            start_x, end_x, start_y, end_y = int(parts[1]), int(parts[3]), int(parts[2]), int(parts[4])
        else:
            parts = re.findall(r'([a-z]+) ([a-z]+) (\d+),(\d+) through (\d+),(\d+)', line)[0]
            start_x, end_x, start_y, end_y = int(parts[2]), int(parts[4]), int(parts[3]), int(parts[5])

        for x in range(start_x, end_x + 1):
            for y in range(start_y, end_y + 1):
                if "toggle" in line:
                    if Position(x, y) in lights:
                        lights[Position(x, y)] += 2
                    else:
                        lights[Position(x, y)] = 2
                else:
                    if parts[1] == "on":
                        if Position(x, y) in lights:
                            lights[Position(x, y)] += 1
                        else:
                            lights[Position(x, y)] = 1
                    else:
                        if Position(x, y) in lights:
                            if lights[Position(x, y)] != 0:
                                lights[Position(x, y)] -= 1

    return sum(lights.values())


def main() -> int:
    with open(DATA) as f:
        data = f.read()
        print("Part 1: " + str(find_how_many_lights_on(data)))
        print("Part 2: " + str(find_total_brightness_of_all_lights(data)))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
