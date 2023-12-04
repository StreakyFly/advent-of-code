from utils import read_input


def calculate_wins_and_points(winning: list, yours: list) -> tuple[int, int]:
    num_wins = sum(1 for card in winning if card in yours)
    card_points = 2 ** (num_wins - 1) if num_wins else 0
    return num_wins, card_points


def part1(content: str) -> int:
    total_points = 0

    for card in content.split('\n'):
        winning, yours = card.split(': ')[1].split(' | ')
        total_points += calculate_wins_and_points(winning.split(), yours.split())[1]

    return total_points


def part2(content: str) -> int:
    total_cards = 0
    extra_cards = {}

    for card_num, card in enumerate(content.split('\n'), start=1):
        extra_cards.setdefault(card_num, 0)

        winning, yours = card.split(': ')[1].split(' | ')
        wins, _ = calculate_wins_and_points(winning.split(), yours.split())

        while extra_cards[card_num] >= 0:
            for i in range(wins):
                curr_key = card_num + i + 1
                extra_cards[curr_key] = extra_cards.get(curr_key, 0) + 1
            total_cards += 1
            extra_cards[card_num] -= 1
        del extra_cards[card_num]

    return total_cards


print(f"Part 1: {part1(read_input('day4.txt'))}")  # 20667
print(f"Part 2: {part2(read_input('day4.txt'))}")  # 5833065
