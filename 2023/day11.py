from itertools import combinations

from utils import read_input


def parse_input(content: str) -> list[list[str]]:
    return [list(line) for line in content.splitlines()]


def coords_after_expansion(coords: tuple[int, int], multiplier: int,
                           empty_rows: list[int], empty_cols: list[int]) -> tuple[int, int]:
    empty_cols_before = sum([1 for col in empty_cols if col < coords[0]])
    empty_rows_before = sum([1 for row in empty_rows if row < coords[1]])
    x = coords[0] + empty_cols_before * (multiplier - 1)
    y = coords[1] + empty_rows_before * (multiplier - 1)
    return x, y


def calculate_manhattan_distance(galaxy1: tuple[int, int], galaxy2: tuple[int, int]) -> int:
    return abs(galaxy2[0] - galaxy1[0]) + abs(galaxy2[1] - galaxy1[1])


def get_galaxy_coords(matrix: list[list[str]], expansion_factor: int,
                      empty_rows: list[int], empty_cols: list[int]) -> list[tuple[int, int]]:
    galaxy_coords = []
    for y, row in enumerate(matrix):
        for x, item in enumerate(row):
            if item == '#':
                new_x, new_y = coords_after_expansion((x, y), expansion_factor, empty_rows, empty_cols)
                galaxy_coords.append((new_x, new_y))
    return galaxy_coords


def calculate_shortest_paths(matrix: list[list[str]], expansion_factor: int) -> list[int]:
    empty_rows = [y for y, row in enumerate(matrix) if all(i == '.' for i in row)]
    empty_cols = [x for x, col in enumerate(zip(*matrix)) if all(i == '.' for i in col)]

    pairs = combinations(get_galaxy_coords(matrix, expansion_factor, empty_rows, empty_cols), 2)
    return [calculate_manhattan_distance(g1, g2) for g1, g2 in pairs]


def part1(content: str) -> int:
    return sum(calculate_shortest_paths(matrix=parse_input(content), expansion_factor=2))


def part2(content: str) -> int:
    return sum(calculate_shortest_paths(matrix=parse_input(content), expansion_factor=1_000_000))


print(f"Part 1: {part1(read_input(__file__))}")  # 9.805.264
print(f"Part 2: {part2(read_input(__file__))}")  # 779.032.247.216
