from math import prod
from utils import read_input


def get_bounding_box(matrix: list[list], x1: int, y1: int, x2: int, y2: int) -> tuple[list[list], tuple[int, int]]:
    rows, cols = len(matrix), len(matrix[0])

    min_row, max_row = max(0, min(y1, y2) - 1), min(rows, max(y1, y2) + 2)
    min_col, max_col = max(0, min(x1, x2) - 1), min(cols, max(x1, x2) + 2)

    bounding_box = [row[min_col:max_col] for row in matrix[min_row:max_row]]
    top_left_coordinate = (min_col, min_row)

    return bounding_box, top_left_coordinate


def find_number_coordinates(matrix: list[list]) -> list[list[int, int], int]:
    digit_coords = []

    for row in range(len(matrix)):
        col = 0
        while col < len(matrix[row]):
            current_char = matrix[row][col]
            if current_char.isdigit():
                start_coordinates = [col, row]
                number_length = 1
                while col + number_length < len(matrix[row]) and (matrix[row][col + number_length]).isdigit():
                    number_length += 1
                digit_coords.append([start_coordinates, number_length])
                col += number_length
            else:
                col += 1

    return digit_coords


def contains_symbol(bounding_box: list[list]) -> bool:
    for row in bounding_box:
        for element in row:
            if not (element.isdigit() or element == '.'):
                return True
    return False


def create_string_matrix(content: str) -> list[list]:
    rows = content.strip().split('\n')
    return [list(row) for row in rows]


def get_string_from_matrix(matrix: list[list], x: int, y: int, string_length: int) -> str:
    return ''.join(matrix[y][x + i] for i in range(string_length) if 0 <= x + i < len(matrix[y]))


def part1(content: str) -> int:
    matrix = create_string_matrix(content)
    num_info = find_number_coordinates(matrix)

    valid_numbers = []
    for (x, y), length in num_info:
        bounding_box, _ = get_bounding_box(matrix, x, y, x + length - 1, y)
        if contains_symbol(bounding_box):
            number = int(''.join(matrix[y][x + i] for i in range(length)))
            valid_numbers.append(number)

    return sum(valid_numbers)


def part2(content: str) -> int:
    matrix = create_string_matrix(content)
    num_info = find_number_coordinates(matrix)

    gears = {}
    for (x, y), length in num_info:
        bounding_box, (bbx, bby) = get_bounding_box(matrix, x, y, x + length - 1, y)
        if any('*' in row for row in bounding_box):
            for row, row_data in enumerate(bounding_box):
                for col, element in enumerate(row_data):
                    if element == '*':
                        sx, sy = bbx+col, bby+row
                        number = int(get_string_from_matrix(matrix, x, y, length))
                        gears.setdefault((sx, sy), []).append(number)

    return sum(prod(v) for v in gears.values() if len(v) >= 2)


print(f"Part 1: {part1(read_input('day3.txt'))}")  # 540131
print(f"Part 2: {part2(read_input('day3.txt'))}")  # 86879020
