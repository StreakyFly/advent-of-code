from utils import read_input


def parse_input(content: str) -> list[int]:
    return [int(num) for num in content.split()]


def blink(n: int) -> list[int]:
    if n == 0:
        return [1]
    elif len(str(n)) % 2 == 0:
        str_n = str(n)
        half = len(str_n) // 2
        return [int(str_n[:half]), int(str_n[half:])]
    else:
        return [n * 2024]


def solve(stones: list[int], num_iterations: int) -> int:
    curr_step = {n: 1 for n in stones}

    for _ in range(num_iterations):
        next_step = {}
        for num in curr_step:
            for n in blink(num):
                next_step[n] = next_step.get(n, 0) + curr_step[num]
        curr_step = next_step

    return sum(curr_step.values())


def part1(content: str) -> int:
    stones = parse_input(content)

    for _ in range(25):
        i = 0
        while i < len(stones):
            stone = stones[i]
            if stone == 0:
                stones[i] = 1
            elif len(str(stone)) % 2 == 0:
                stone_str = str(stone)
                half = len(stone_str) // 2
                s1 = int(stone_str[:half])
                s2 = int(stone_str[half:])
                stones[i] = s1
                i += 1  # increment i to skip the newly inserted stone
                stones.insert(i, s2)
            else:
                stones[i] = stone * 2024
            i += 1

    return len(stones)


def part2(content: str) -> int:
    return solve(parse_input(content), 75)


print(f"Part 1: {part1(read_input(__file__))}")  # 231278
print(f"Part 2: {part2(read_input(__file__))}")  # 274229228071551
