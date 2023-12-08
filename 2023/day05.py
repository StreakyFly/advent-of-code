from utils import read_input


def parse_input(content: str) -> (list, dict[tuple, list[tuple[int, int, int]]]):
    seeds, *mapping = content.split('\n\n')

    seeds = [int(i) for i in seeds.split()[1:]]
    maps = {}

    for m in mapping:
        key, *nums = m.splitlines()
        map_from, map_to = key.split()[0].split('-to-')
        maps[map_from, map_to] = [tuple(map(int, n.split())) for n in nums]

    return seeds, maps


def create_ranges(numbers: list[int]) -> list[tuple[int, int]]:
    return [(start, start + length) for start, length in zip(numbers[::2], numbers[1::2])]


def update_ranges(current_ranges: list[tuple[int, int]], mappings: list[tuple[int, int, int]]) -> list[tuple[int, int]]:
    next_ranges = []

    for start, end in current_ranges:
        for dest, src, l in mappings:
            if src <= start < src + l:
                if end - start < l:
                    next_ranges.append((start + (dest - src), end + (dest - src)))
                else:
                    next_ranges.append((start + (dest - src), start + (dest - src) + l - 1))
                    current_ranges.append((start + l, end))
                break
            elif src <= end < src + l:
                next_ranges.append((dest, end + (dest - src - 1)))
                current_ranges.append((start, src - 1))
                break
            elif start < src and src + l < end:
                next_ranges.append((dest, dest + l - 1))
                current_ranges.extend([(start, src - 1), (src + l, end)])
                break
        else:  # if mappings for these numbers aren't defined keep ranges same
            next_ranges.append((start, end))

    return next_ranges


def part1(content: str) -> int:
    seeds, maps = parse_input(content)

    values = []
    for num in seeds:
        for _, mappings in maps.items():
            # mappings are in order - if they weren't you would need to find the right mappings each time
            for dest, src, l in mappings:
                if src <= num <= src+l:
                    num += dest - src
                    break

        values.append(num)

    return min(values)


def part2(content: str) -> int:
    seed_nums, maps = parse_input(content)
    minimums = []

    for seed_min, seed_max in create_ranges(seed_nums):
        current_ranges = [(seed_min, seed_max)]

        for _, mappings in maps.items():
            current_ranges = update_ranges(current_ranges, mappings)

        minimums.append(min(i[0] for i in current_ranges))

    return min(minimums)


print(f"Part 1: {part1(read_input(__file__))}")  # 173706076
print(f"Part 2: {part2(read_input(__file__))}")  # 11611182
