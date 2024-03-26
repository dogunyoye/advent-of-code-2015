import os.path

DATA = os.path.join(os.path.dirname(__file__), 'day03.txt')


class Position(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '<' + str(self.x) + ',' + str(self.y) + '>'

    def __eq__(self, other):
        return self.y == other.y and self.x == other.x

    def __hash__(self):
        return hash(self.x) + hash(self.y)

    def __repr__(self):
        return "Coordinate(%d, %d)" % (self.x, self.y)


def move(direction: str, current_pos: Position, result: set):
    if direction == '^':
        result.add(Position(current_pos.x - 1, current_pos.y))
        current_pos.x -= 1
    elif direction == '>':
        result.add(Position(current_pos.x, current_pos.y + 1))
        current_pos.y += 1
    elif direction == 'v':
        result.add(Position(current_pos.x + 1, current_pos.y))
        current_pos.x += 1
    else:
        result.add(Position(current_pos.x, current_pos.y - 1))
        current_pos.y -= 1


def calculate_houses_visited(data) -> int:
    santa_pos = Position(0, 0)
    result = {Position(0, 0)}

    [move(c, santa_pos, result) for c in data]
    return len(result)


def calculate_houses_visited_with_robo_santa(data) -> int:
    santa_pos = Position(0, 0)
    robo_santa_pos = Position(0, 0)

    result = {Position(0, 0)}
    for i, c in enumerate(data):

        if i % 2 == 0:
            current_pos = santa_pos
        else:
            current_pos = robo_santa_pos

        move(c, current_pos, result)
    return len(result)


def main() -> int:
    with open(DATA) as f:
        data = f.read()
        print("Part 1: " + str(calculate_houses_visited(data)))
        print("Part 2: " + str(calculate_houses_visited_with_robo_santa(data)))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
