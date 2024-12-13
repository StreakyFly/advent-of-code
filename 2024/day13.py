from utils import read_input


def parse_input(content: str) -> list[list[tuple[int, int]]]:
    machines = []

    for machine in content.split("\n\n"):
        button_a, button_b, prize = machine.splitlines()
        ax, ay = [int(e.split("+")[1]) for e in button_a.split(": ")[1].split(", ")]
        bx, by = [int(e.split("+")[1]) for e in button_b.split(": ")[1].split(", ")]
        px, py = [int(e.split("=")[1]) for e in prize.split(": ")[1].split(", ")]
        machines.append([(ax, ay), (bx, by), (px, py)])

    return machines


def calculate_min_presses(machine: list[tuple[int, int]]) -> tuple[int | None, int | None]:
    (ax, ay), (bx, by), (px, py) = machine
    denominator = ax * by - ay * bx

    A = (px * by - py * bx) / denominator
    B = (ax * py - ay * px) / denominator

    return (int(A), int(B)) if A.is_integer() and B.is_integer() else (None, None)


def part1(content: str) -> int:
    min_cost = 0

    for machine in parse_input(content):
        A, B = calculate_min_presses(machine)
        min_cost += (A * 3 + B) if A else 0

    return min_cost


def part2(content: str) -> int:
    CONVERSION_ERROR = 10000000000000
    min_cost = 0

    for machine in parse_input(content):
        (px, py) = machine[2]
        machine[2] = (px + CONVERSION_ERROR, py + CONVERSION_ERROR)
        A, B = calculate_min_presses(machine)
        min_cost += (A * 3 + B) if A else 0

    return min_cost


print(f"Part 1: {part1(read_input(__file__))}")  # 30413
print(f"Part 2: {part2(read_input(__file__))}")  # 92827349540204
