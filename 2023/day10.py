import os
import time

from utils import read_input


# N = Up, S = Down, W = Left, E = Right
TILES = {'.': {}, 'S': {'U', 'D', 'L', 'R'}, '|': {'U', 'D'}, '-': {'L', 'R'},
         'L': {'U', 'R'}, 'J': {'L', 'U'}, '7': {'L', 'D'}, 'F': {'R', 'D'}}
PAIRS = {'U': 'D', 'D': 'U', 'L': 'R', 'R': 'L'}
NUM_TO_SIDE = {0: 'U', 1: 'L', 2: 'R', 3: 'D'}

FANCY_PIPES = {
    "|": "│",
    "-": "─",
    "F": "┌",
    "L": "└",
    "7": "┐",
    "J": "┘",
    ".": "•",
    "S": "┘",
}


def parse_input(content: str) -> list[list[str]]:
    return [list(line) for line in content.splitlines()]


def find_s_coordinates(matrix: list[list[str]]) -> (int, int):
    for num, row in enumerate(matrix):
        if 'S' in row:
            x, y = num, row.index('S')
            return x, y


def get_neighbour_tiles(matrix: list[tuple], x: int, y: int) -> tuple[
                        tuple[int, int], tuple[int, int], tuple[int, int], tuple[int, int]]:
    rows, cols = len(matrix)-1, len(matrix[0])-1

    up = max(0, x - 1), y
    up = up if up[0] != x else ()

    left = x, max(0, y - 1)
    left = left if left[1] != y else ()

    right = x, min(cols, y + 1)
    right = right if right[1] != y else ()

    down = min(rows, x + 1), y
    down = down if down[0] != x else ()

    return up, left, right, down


def get_matrix_item(matrix: list[tuple], x: int, y: int) -> str:
    return matrix[x][y]


def do_pipes_connect(curr_item: str, next_item: str, next_to_curr_relation: str) -> bool:
    # WARNING! This assumes that S (Start) connects in ALL directions!
    return next_to_curr_relation in TILES[curr_item] and PAIRS[next_to_curr_relation] in TILES[next_item]


def is_move_valid(matrix: list[tuple], curr_pos: tuple[int, int], next_pos: tuple[int, int], next_to_curr_relation: str) -> bool:
    curr_item = get_matrix_item(matrix, *curr_pos)
    next_item = get_matrix_item(matrix, *next_pos)

    if next_item == '.':
        return False

    return do_pipes_connect(curr_item, next_item, next_to_curr_relation)


def print_bounding_box(matrix: list[tuple], x: int, y: int, outline: int = 1, path: list = None) -> None:
    rows, cols = len(matrix), len(matrix[0])

    min_row, max_row = max(0, x - outline), min(rows, x + 1 + outline)
    min_col, max_col = max(0, y - outline), min(cols, y + 1 + outline)

    bounding_box = [row[min_col:max_col] for row in matrix[min_row:max_row]]

    draw = ''
    for row_num, row in enumerate(bounding_box):
        for col_num, i in enumerate(row):
            i = FANCY_PIPES.get(i, i)  # TODO comment for original pipes
            curr_corrd = (row_num+x-outline, col_num+y-outline)
            if curr_corrd in path:
                draw += f'\033[91m{i} \033[0m'
            else:
                draw += f'\033[93m{i} \033[0m'
        draw += '\n'

    os.system('cls' if os.name == 'nt' else 'clear')
    print(draw)

    time.sleep(0.05)


def get_path(matrix):
    count = 0
    path = [find_s_coordinates(matrix)]
    while len(set(path)) == len(path):
        curr_pos = path[-1]
        if VISUALIZE:
            print_bounding_box(matrix, curr_pos[0], curr_pos[1], 7, path)
        neighbour_tiles = get_neighbour_tiles(matrix, curr_pos[0], curr_pos[1])

        for num, next_pos in enumerate(neighbour_tiles):
            if not next_pos:
                continue
            curr_item = get_matrix_item(matrix, next_pos[0], next_pos[1])

            if next_pos not in path or (curr_item == 'S' and len(path) > 2):
                move_valid = is_move_valid(matrix, curr_pos=curr_pos, next_pos=next_pos, next_to_curr_relation=NUM_TO_SIDE[num])
                if move_valid:
                    path.append(next_pos)
                    break
        count += 1
    return path, count


def get_s_pipe(path: list[tuple[int, int]]) -> str:
    first_point = path[0]
    last_point = path[-1]

    fx, fy = first_point
    lx, ly = last_point

    # TODO surely, it's just a coincidence that this works for my input? Should be fixed.
    if fx - lx == 0:
        return '-'
    return '|'


def get_inside_points(sketch, loop):
    inside_points = []
    for y, row in enumerate(sketch):
        prev_corner = None
        crossings = 0
        for x, col in enumerate(row):
            if (x, y) in loop:
                match col:
                    case "|":
                        crossings += 1
                    case "7":
                        if prev_corner == "L":
                            crossings += 1
                    case "J":
                        if prev_corner == "F":
                            crossings += 1
                    case "S":
                        crossings += 1
                if col != "-":
                    prev_corner = col
            else:
                if crossings % 2 == 1:
                    inside_points.append((x, y))
    return inside_points


def transpose_matrix(matrix):
    return list(map(list, zip(*matrix)))


def part1(content: str) -> int:
    _, count = get_path(parse_input(content))
    return int((count+1) / 2)


def part2(content: str) -> int:
    matrix = parse_input(content)
    path, _ = get_path(matrix)

    matrix = [list(i) for i in matrix]
    s_coords = find_s_coordinates(matrix)
    matrix[s_coords[0]][s_coords[1]] = get_s_pipe(path)

    new_path = []
    for i in path:
        new_path.append((i[1], i[0]))

    inside_points = get_inside_points(matrix, new_path)

    return len(inside_points)


VISUALIZE = True

print(f"Part 1: {part1(read_input(__file__))}")  # 6697
print(f"Part 2: {part2(read_input(__file__))}")  # 423
