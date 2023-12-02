from utils import read_input


def parse_games(content: str) -> list[str]:
    return [i.split(':')[1] for i in content.split('\n')]


def part1(content: str) -> int:
    BAG = {'red': 12, 'green': 13, 'blue': 14}
    total = 0

    for game_num, game in enumerate(parse_games(content), start=1):
        game_valid = True
        for bag_set in game.split(';'):
            for item in bag_set.split(','):
                amount, color = item.split()
                if int(amount) > BAG[color]:
                    game_valid = False
                    break
        if game_valid:
            total += game_num

    return total


def part2(content: str) -> int:
    total = 0

    for game_num, game in enumerate(parse_games(content), start=1):
        curr_bag = {'red': 0, 'green': 0, 'blue': 0}
        for bag_set in game.split(';'):
            for item in bag_set.split(','):
                amount, color = item.split()
                if int(amount) > curr_bag[color]:
                    curr_bag[color] = int(amount)
        multiplied = 1
        for i in curr_bag.values():
            multiplied *= i
        total += multiplied

    return total


print(f"Part 1: {part1(read_input('day2.txt'))}")  # 2006
print(f"Part 2: {part2(read_input('day2.txt'))}")  # 84911
