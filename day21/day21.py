import os.path
from itertools import combinations, product

DATA = os.path.join(os.path.dirname(__file__), 'day21.txt')


def __create_weapons() -> list:
    return \
        [
            ("Dagger", 8, 4, 0),
            ("Shortsword", 10, 5, 0),
            ("Warhammer", 25, 6, 0),
            ("Longsword", 40, 7, 0),
            ("Greataxe", 74, 8, 0)
        ]


def __create_armor() -> list:
    return \
        [
            ("Leather", 13, 0, 1),
            ("Chainmail", 31, 0, 2),
            ("Splintmail", 53, 0, 3),
            ("Bandedmail", 75, 0, 4),
            ("Platemail", 102, 0, 5)
        ]


def __create_rings() -> list:
    return \
        [
            ("Damage +1", 25, 1, 0),
            ("Damage +2", 50, 2, 0),
            ("Damage +3", 100, 3, 0),
            ("Defense +1", 20, 0, 1),
            ("Defense +2", 40, 0, 2),
            ("Defense +3", 80, 0, 3)
        ]


def __create_boss_player(data) -> tuple:
    stats = []
    for line in data.splitlines():
        stats.append(eval(line.split(": ")[1]))
    return "Boss", stats[0], stats[1], stats[2]


def __fight_boss(player, boss) -> bool:
    rounds = 0
    hp = {player[0]: player[1], boss[0]: boss[1]}
    while True:
        if rounds % 2 == 0:
            attacker = player
            defender = boss
        else:
            attacker = boss
            defender = player

        dmg = attacker[2] - defender[3]
        if dmg <= 0:
            dmg = 1
        hp[defender[0]] -= dmg

        if hp[defender[0]] <= 0:
            return defender[0] == "Boss"
        rounds += 1


def __simulate_boss_fight(combos, boss, winning) -> list:
    result = []
    for items in combos:
        items_cost, damage, armor = 0, 0, 0
        for item in items:
            # 2 rings
            if isinstance(item[0], tuple):
                items_cost += item[0][1] + item[1][1]
                damage += item[0][2] + item[1][2]
                armor += item[0][3] + item[1][3]
            else:
                items_cost += item[1]
                damage += item[2]
                armor += item[3]

        player = ("Player", 100, damage, armor)
        if (winning and __fight_boss(player, boss)) or (not winning and not __fight_boss(player, boss)):
            result.append(items_cost)
    return result


def __generate_item_configurations() -> list:
    weapons, armor, rings = __create_weapons(), __create_armor(), __create_rings()

    weapon_one_ring = list(product(weapons, rings))
    weapon_two_rings = list(product(weapons, list(combinations(rings, 2))))
    weapon_armor = list(product(weapons, armor))
    weapon_armor_one_ring = list(product(weapons, armor, rings))
    weapon_armor_two_rings = list(product(weapons, armor, list(combinations(rings, 2))))

    return [weapon_one_ring, weapon_two_rings, weapon_armor, weapon_armor_one_ring, weapon_armor_two_rings]


def __calculate_total_item_cost_for_boss_fight(data, winning) -> list:
    result = []
    boss = __create_boss_player(data)

    for c in __generate_item_configurations():
        [result.append(r) for r in __simulate_boss_fight(c, boss, winning)]

    return result


def calculate_least_amount_of_gold_needed_to_win(data) -> int:
    return min(__calculate_total_item_cost_for_boss_fight(data, True))


def calculate_most_amount_gold_to_lose(data) -> int:
    return max(__calculate_total_item_cost_for_boss_fight(data, False))


def main() -> int:
    with open(DATA) as f:
        data = f.read()
        print("Part 1: " + str(calculate_least_amount_of_gold_needed_to_win(data)))
        print("Part 2: " + str(calculate_most_amount_gold_to_lose(data)))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
