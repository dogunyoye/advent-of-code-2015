import os.path

DATA = os.path.join(os.path.dirname(__file__), 'day20.txt')


def find_lowest_house_number_to_receive_36000000_presents(data) -> int:
    house_number = 1
    total_presents = eval(data)

    while True:
        factors = {1}
        dividend, div = house_number, 1
        quotient = dividend // div

        while quotient > div:
            if dividend % div == 0:
                factors.add(quotient)
                factors.add(div)
            div += 1
            quotient = dividend // div

        if sum(list(map(lambda f: f * 10, factors))) >= total_presents:
            return house_number
        house_number += 1


def find_lowest_house_number_to_receive_36000000_presents_with_constraints(data) -> int:
    house_number = 1
    total_presents = eval(data)

    while True:
        factors = {1}
        dividend, div = house_number, 1
        quotient = dividend // div

        while quotient > div:
            if dividend % div == 0:
                factors.add(quotient)
                factors.add(div)
            div += 1
            quotient = dividend // div

        factors = list(filter(lambda f: (house_number // f) <= 50, factors))
        if sum(list(map(lambda f: f * 11, factors))) >= total_presents:
            return house_number
        house_number += 1


# TODO slow solution, optimisation needed
def main() -> int:
    with open(DATA) as f:
        data = f.read()
        print("Part 1: " + str(find_lowest_house_number_to_receive_36000000_presents(data)))
        print("Part 2: " + str(find_lowest_house_number_to_receive_36000000_presents_with_constraints(data)))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
