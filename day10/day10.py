import os.path

DATA = os.path.join(os.path.dirname(__file__), 'day10.txt')


def __perform_look_say(data, times) -> int:
    runs = times
    number = data
    while runs != 0:
        count = 0
        look_say = []
        for i in range(0, len(number)):
            count += 1
            if (i == len(number) - 1) or (number[i + 1] != number[i]):
                look_say.append((number[i], count))
                count = 0

        number = ""
        for t in look_say:
            number += str(t[1]) + t[0]
        runs -= 1

    return len(number)


def perform_look_and_say_forty_times(data) -> int:
    return __perform_look_say(data, 40)


def perform_look_and_say_fifty_times(data) -> int:
    return __perform_look_say(data, 50)


def main() -> int:
    with open(DATA) as f:
        data = f.read()
        print("Part 1: " + str(perform_look_and_say_forty_times(data)))
        print("Part 2: " + str(perform_look_and_say_fifty_times(data)))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
