from utils import read_input


def parse_input(content: str) -> list[list[int]]:
    return [[*map(int, line.split())] for line in content.splitlines()]


def is_safe(report: list[int]) -> bool:
    if len(report) != len(set(report)):
        return False

    sorted_report = sorted(report)
    if not (report == sorted_report or report == sorted_report[::-1]):
        return False

    for (l1, l2) in zip(report, report[1:]):
        if abs(l1 - l2) > 3:  # or abs(l1 - l2) < 1:  # Not necessary, as we return early if there are any duplicates.
            return False

    return True


def part1(content: str) -> int:
    return sum([is_safe(report) for report in parse_input(content)])


def part2(content: str) -> int:
    reports = parse_input(content)
    count = 0

    for report in reports:
        if is_safe(report):
            count += 1
        else:
            for i in range(len(report)):
                if is_safe(report[:i] + report[i + 1:]):
                    count += 1
                    break

    return count


print(f"Part 1: {part1(read_input(__file__))}")  # 411
print(f"Part 2: {part2(read_input(__file__))}")  # 465
