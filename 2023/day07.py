from utils import read_input


CARD_STRENGTH = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10}


def parse_input(content: str) -> list[tuple[str, int]]:
    data = []
    for line in content.splitlines():
        hand, bid = line.split()
        data.append((hand, int(bid)))
    return data


def get_card_counts(hand: str) -> dict[str, int]:
    return {card: hand.count(card) for card in set(hand)}


def get_cards_strength(hand: str) -> list[int]:
    return [CARD_STRENGTH.get(card) or int(card) for card in hand]


def sort_hands(hands: list[tuple[str, int]]) -> list[tuple[str, int]]:
    return sorted(hands, key=lambda hand_info: get_cards_strength(hand_info[0]))


def order_hands_by_card_strength(hands_type_ordered: list[list[tuple[str, int]]]) -> list[tuple[str, int]]:
    hands_ordered = []  # from least to most
    for hands in hands_type_ordered:
        hands_ordered.extend(sort_hands(hands))

    return hands_ordered


def get_hand_type(card_counts: dict[str, int]) -> int:
    values = list(card_counts.values())
    num_unique_values = len(values)

    if num_unique_values == 1 and max(values) == 5:
        return 7  # Five of a kind
    elif num_unique_values == 2:
        if 4 in values:
            return 6  # Four of a kind
        elif 3 in values and 2 in values:
            return 5  # Full house
    elif num_unique_values == 3:
        if 3 in values:
            return 4  # Three of a kind
        elif 2 in values:
            return 3  # Two pair
    elif num_unique_values == 4:
        return 2  # One pair

    return 1  # High card (all 5 cards are different)


def get_hand_type_joker_edition(card_counts: dict[str, int]) -> int:
    max_card = None
    max_count = 0
    for card, count in card_counts.items():
        if count > max_count and not (card == 'J' and card_counts['J'] != 5):
            max_count = count
            max_card = card

    if 'J' in card_counts and card_counts['J'] != 5:
        card_counts[max_card] += card_counts['J']
        del card_counts['J']

    return get_hand_type(card_counts)


def calculate_winnings(data: list[tuple[str, int]], get_hand_type_fn: callable) -> int:
    hand_types = {}
    for hand, bid in data:
        hand_type = get_hand_type_fn(get_card_counts(hand))
        hand_types.setdefault(hand_type, []).append((hand, bid))

    hands_type_ordered = [hand_types[key] for key in sorted(hand_types.keys())]

    winnings = (bid * num for num, (_, bid) in enumerate(order_hands_by_card_strength(hands_type_ordered), start=1))
    return sum(winnings)


def part1(content: str) -> int:
    return calculate_winnings(parse_input(content), get_hand_type)


def part2(content: str) -> int:
    CARD_STRENGTH['J'] = 1  # J cards are the weakest in part2
    return calculate_winnings(parse_input(content), get_hand_type_joker_edition)


print(f"Part 1: {part1(read_input(__file__))}")  # 250946742
print(f"Part 2: {part2(read_input(__file__))}")  # 251824095
