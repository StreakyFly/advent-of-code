from utils import read_input
from collections import defaultdict


def parse_input(content: str) -> tuple[dict[int, list[int]], list[list[int]]]:
    order_rules_raw, update_numbers_raw = content.split("\n\n")

    order_rules = defaultdict(list)
    for rule in order_rules_raw.splitlines():
        num1, num2 = map(int, rule.split("|"))
        order_rules[num1].append(num2)

    update_numbers = [list(map(int, update.split(","))) for update in update_numbers_raw.splitlines()]
    return order_rules, update_numbers


def validate_updates(update_numbers: list[list[int]], order_rules: dict[int, list[int]]) -> dict[str, list[list[int]]]:
    validated_updates = {"correct": [], "incorrect": []}

    for update in update_numbers:
        is_invalid = False
        for num in update:
            if num not in order_rules:
                continue
            for num2 in order_rules[num]:
                if num2 in update and update.index(num2) < update.index(num):
                    is_invalid = True
                    break
            if is_invalid:
                break
        validated_updates["incorrect" if is_invalid else "correct"].append(update)

    return validated_updates


def part1(content: str) -> int:
    order_rules, update_numbers = parse_input(content)
    correctly_ordered_updates = validate_updates(update_numbers, order_rules)["correct"]
    return sum([update[len(update) // 2] for update in correctly_ordered_updates])


def part2(content: str) -> int:
    order_rules, update_numbers = parse_input(content)
    incorrectly_ordered_updates = validate_updates(update_numbers, order_rules)["incorrect"]
    middle_sum = 0

    for update in incorrectly_ordered_updates:
        swapped = True
        while swapped:
            swapped = False
            # Check and swap adjacent elements based on order rules
            for i0, (num0, num1) in enumerate(zip(update, update[1:])):
                if num0 in order_rules.get(num1, []):
                    update[i0], update[i0+1] = update[i0+1], update[i0]
                    swapped = True

        middle_sum += update[len(update) // 2]

    return middle_sum


print(f"Part 1: {part1(read_input(__file__))}")  # 5948
print(f"Part 2: {part2(read_input(__file__))}")  # 3062
