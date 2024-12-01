from utils import read_input


def parse_input(content: str) -> tuple[list[int], list[int]]:
    vals_l, vals_r = [], []

    for line in content.splitlines():
        vl, vr = map(int, line.split())
        vals_l.append(vl)
        vals_r.append(vr)

    return vals_l, vals_r


def part1(content: str) -> int:
    vals_l, vals_r = parse_input(content)
    delta_sum = sum(abs(vl - vr) for vl, vr in zip(sorted(vals_l), sorted(vals_r)))
    return delta_sum


def part2(content: str) -> int:
    vals_l, vals_r = parse_input(content)
    total_similarity_score = sum(vl * vals_r.count(vl) for vl in vals_l)
    return total_similarity_score


print(f"Part 1: {part1(read_input(__file__))}")  # 2066446
print(f"Part 2: {part2(read_input(__file__))}")  # 24931009
