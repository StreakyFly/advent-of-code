from utils import read_input


def parse_input(content: str) -> (str, dict[str, tuple[str, str]]):
    instructions, _, *nodes_str = content.splitlines()

    nodes = {}
    for node_str in nodes_str:
        item, children = node_str.split(' = ')
        left, right = children[1:-1].split(', ')
        nodes[item] = (left, right)

    return instructions, nodes


def calculate_gcd(x: int, y: int) -> int:
    while y:
        x, y = y, x % y
    return x


def calculate_lcm(x: int, y: int) -> int:
    return x * y // calculate_gcd(x, y)


def calculate_multiple_num_lcm(numbers: list[int]) -> int:
    result = 1
    for num in numbers:
        result = calculate_lcm(num, result)

    return result


def find_first_nodes(nodes: dict[str, tuple[str, str]]) -> list[str]:
    return [node for node in nodes if node[-1] == 'A']


def count_steps(nodes: dict[str, tuple[str, str]], instructions: str, curr_node: str) -> int:
    steps = 0
    while curr_node[-1] != 'Z':
        instruction = instructions[steps % len(instructions)]
        left, right = nodes[curr_node]
        curr_node = left if instruction == 'L' else right
        steps += 1
    return steps


def part1(content: str) -> int:
    instructions, nodes = parse_input(content)
    return count_steps(nodes, instructions, curr_node='AAA')


def part2(content: str) -> int:
    instructions, nodes = parse_input(content)
    nodes_steps = [count_steps(nodes, instructions, curr_node) for curr_node in find_first_nodes(nodes)]
    return calculate_multiple_num_lcm(nodes_steps)


print(f"Part 1: {part1(read_input(__file__))}")  # 18673
print(f"Part 2: {part2(read_input(__file__))}")  # 17972669116327
