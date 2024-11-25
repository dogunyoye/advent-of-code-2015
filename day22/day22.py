import copy
import os.path

DATA = os.path.join(os.path.dirname(__file__), 'day22.txt')

# Spells
MAGIC_MISSILE = "Magic Missile"
DRAIN = "Drain"
SHIELD = "Shield"
POISON = "Poison"
RECHARGE = "Recharge"


class Player(object):
    def __init__(self, hp, mana, armor, effects):
        self.hp = hp
        self.mana = mana
        self.armor = armor
        self.effects = effects

    def can_cast(self) -> list:
        spells = create_spells()
        spells = list(filter(lambda s: s[0] not in self.effects.keys() and s[1] <= self.mana, spells))
        return spells


class Boss(object):
    def __init__(self, hp, damage):
        self.hp = hp
        self.damage = damage


def __create_boss(data) -> Boss:
    stats = []
    for line in data.splitlines():
        stats.append(eval(line.split(": ")[1]))
    return Boss(stats[0], stats[1])


def __create_player() -> Player:
    return Player(50, 500, 0, {})


def create_spells() -> list:
    return [
        (MAGIC_MISSILE, 53),
        (DRAIN, 73),
        (SHIELD, 113),
        (POISON, 173),
        (RECHARGE, 229)
    ]


def __fight(hard_mode, boss, player, turn, spent, result):
    if hard_mode and turn == "Player":
        player.hp -= 1

    if player.hp <= 0:
        # player has lost
        return

    if len(result) > 0 and spent > min(result):
        # this current branch won't lead us to better result
        return

    for k in player.effects.keys():
        if k == "Shield":
            if player.armor != 7:
                player.armor = 7
        elif k == "Poison":
            boss.hp -= 3
            if boss.hp <= 0:
                result.append(spent)
                return
        else:
            player.mana += 101
        player.effects[k] -= 1

    finished_effects = list(filter(lambda kv: kv[1] == 0, player.effects.items()))
    for e in finished_effects:
        spell_name = e[0]
        if spell_name == SHIELD:
            player.armor = 0
        del player.effects[e[0]]

    spells = player.can_cast()
    if len(spells) == 0:
        # player has lost
        return

    if turn == "Boss":
        player.hp -= (boss.damage - player.armor)
        if player.hp <= 0:
            return
        __fight(hard_mode, boss, player, "Player", spent, result)
    else:
        for s in spells:
            spell_name = s[0]
            spell_cost = s[1]

            new_player = Player(player.hp, player.mana, player.armor, copy.deepcopy(player.effects))
            new_boss = Boss(boss.hp, boss.damage)
            new_spent = spent

            if spell_name == MAGIC_MISSILE:
                new_boss.hp -= 4
            elif spell_name == DRAIN:
                new_boss.hp -= 2
                new_player.hp += 2
            elif spell_name == SHIELD or spell_name == POISON:
                new_player.effects[spell_name] = 6
            elif spell_name == RECHARGE:
                new_player.effects[RECHARGE] = 5

            new_player.mana -= spell_cost
            new_spent += spell_cost

            if new_boss.hp <= 0:
                result.append(new_spent)
            else:
                __fight(hard_mode, new_boss, new_player, "Boss", new_spent, result)


def __play_game(hard_mode, data) -> int:
    result = []
    boss = __create_boss(data)
    player = __create_player()

    __fight(hard_mode, boss, player, "Player", 0, result)
    return min(result)


def find_least_amount_of_mana_to_win(data) -> int:
    return __play_game(False, data)


def find_least_amount_of_mana_to_win_on_hard_mode(data) -> int:
    return __play_game(True, data)


def main() -> int:
    with open(DATA) as f:
        data = f.read()
        print("Part 1: " + str(find_least_amount_of_mana_to_win(data)))
        print("Part 2: " + str(find_least_amount_of_mana_to_win_on_hard_mode(data)))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
