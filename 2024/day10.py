from utils import read_input


def parse_input(content: str) -> list[list[int]]:
    return [list(map(int, row)) for row in content.splitlines()]


def count_trails(tmap: list[list[int]], i: int, j: int,
                 only_unique_endings: bool, already_visited_endings: set[tuple[int, int]]) -> int:
    num = tmap[i][j]

    if num == 9:
        ending_pos = (i, j)
        if only_unique_endings and ending_pos in already_visited_endings:
            return 0

        already_visited_endings.add(ending_pos)
        return 1

    # branch in all directions
    count = 0
    if i > 0 and tmap[i-1][j] - num == 1:
        count += count_trails(tmap, i-1, j, only_unique_endings, already_visited_endings)  # up
    if i < len(tmap)-1 and tmap[i+1][j] - num == 1:
        count += count_trails(tmap, i+1, j, only_unique_endings, already_visited_endings)  # down
    if j > 0 and tmap[i][j-1] - num == 1:
        count += count_trails(tmap, i, j-1, only_unique_endings, already_visited_endings)  # left
    if j < len(tmap[0])-1 and tmap[i][j+1] - num == 1:
        count += count_trails(tmap, i, j+1, only_unique_endings, already_visited_endings)  # right

    return count


def count_total_trails(tmap: list[list[int]], only_unique_endings: bool) -> int:
    total_trails = 0
    for i, row in enumerate(tmap):
        for j, tile in enumerate(row):
            if tile == 0:
                total_trails += count_trails(tmap, i, j, only_unique_endings, set())
    return total_trails


def part1(content: str) -> int:
    return count_total_trails(parse_input(content), True)


def part2(content: str) -> int:
    return count_total_trails(parse_input(content), False)


print(f"Part 1: {part1(read_input(__file__))}")  # 682
print(f"Part 2: {part2(read_input(__file__))}")  # 1511
