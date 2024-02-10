from utils import read_input


def parse_input(content: str) -> list:
    blocks = content.split('\n\n')
    for i, block in enumerate(blocks):
        blocks[i] = [list(line) for line in block.splitlines()]
    return blocks


def transpose_matrix(matrix: list) -> list:
    return list(map(list, zip(*matrix)))


def find_pattern1(block) -> int:
    reflections = list(range(len(block) - 1))

    for num, (l1, l2) in enumerate(zip(block, block[1:])):
        if num in reflections and l1 != l2:
            reflections.remove(num)

    for reflection in reflections.copy():
        for i in range(len(block) // 2):
            l1, l2 = get_farther_lines(block, reflection, i)
            if l1 != -1 and l1 != l2:
                reflections.remove(reflection)
                break

    if reflections:
        return reflections[0] + 1
    return -1


def valid_line_smudge(l1: list, l2: list):
    # first bool tells us if it's valid, second bool tells us if it's valid but has a smudge
    valid = True
    for i1, i2 in zip(l1, l2):
        if i1 != i2:
            if not valid:
                return False, False
            valid = False
    return True, not valid


def get_farther_lines(block: list, middle_left: int, distance: int) -> tuple[list, list]:
    if middle_left - distance < 0 or middle_left + distance + 1 >= len(block):
        return [-1], [-1]

    return block[middle_left - distance], block[middle_left + distance + 1]


def find_pattern2(block) -> int:
    reflections = list(range(len(block)-1))

    for num, (l1, l2) in enumerate(zip(block, block[1:])):
        if num in reflections and not valid_line_smudge(l1, l2)[0]:
            reflections.remove(num)

    for reflection in reflections.copy():
        actually_valid = False
        for i in range(len(block) // 2):
            l1, l2 = get_farther_lines(block, reflection, i)
            if l1 == [-1]:
                continue
            valid, has_smudge = valid_line_smudge(l1, l2)
            if valid:
                if has_smudge:
                    actually_valid = True
            else:
                reflections.remove(reflection)
                break

        if not actually_valid and reflection in reflections:
            reflections.remove(reflection)

    if reflections:
        return reflections[0] + 1
    return -1


def calculate_patterns(blocks: list, find_pattern_func: callable) -> list[int]:
    patterns = []
    for block in blocks:
        pattern = find_pattern_func(block) * 100
        if pattern == -100:
            pattern = find_pattern_func(transpose_matrix(block))
        patterns.append(pattern)
    return patterns


def part1(content: str) -> int:
    return sum(calculate_patterns(parse_input(content), find_pattern1))


def part2(content: str) -> int:
    return sum(calculate_patterns(parse_input(content), find_pattern2))


print(f"Part 1: {part1(read_input(__file__))}")  # 27742
print(f"Part 2: {part2(read_input(__file__))}")  # 32728
