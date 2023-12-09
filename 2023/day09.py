from utils import read_input


def parse_input(content: str) -> list[list[int]]:
    return [[int(value) for value in line.split()] for line in content.splitlines()]


def generate_difference_sequences(line: list[int]) -> list[list[int]]:
    difference_sequences = [line]

    while any(difference_sequences[-1]):  # create all difference_sequences
        current_sequence = difference_sequences[-1]
        ds = [next_i - curr_i for curr_i, next_i in zip(current_sequence, current_sequence[1:])]
        difference_sequences.append(ds)

    for num, diff_seq in enumerate(reversed(difference_sequences[:-1])):  # extrapolate using difference_sequences
        last_value = difference_sequences[-num - 1][-1]
        diff_seq.append(diff_seq[-1] + last_value)

    return difference_sequences


def calculate_predicted_values(lines: list[list[int]]) -> list[int]:
    return [generate_difference_sequences(line)[0][-1] for line in lines]


def part1(content: str) -> int:
    lines = parse_input(content)
    return sum(calculate_predicted_values(lines))


def part2(content: str) -> int:
    lines = parse_input(content)
    reversed_line_values = [line[::-1] for line in lines]
    return sum(calculate_predicted_values(reversed_line_values))


print(f"Part 1: {part1(read_input(__file__))}")  # 1861775706
print(f"Part 2: {part2(read_input(__file__))}")  # 1082
