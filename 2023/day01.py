from utils import read_input


def remove_non_digits(s: str) -> str:
    return ''.join([i for i in s if i.isdigit()])


def digitify(s: str) -> str:
    NUM_WORDS = {'one': 'o1e', 'two': 't2o', 'three': 't3e',
                 'four': 'f4r', 'five': 'f5e', 'six': 's6x',
                 'seven': 's7n', 'eight': 'e8t', 'nine': 'n9e'}

    for k, v in NUM_WORDS.items():
        s = s.replace(k, v)
    return s


def part1(content: str) -> int:
    nums = []
    for s in content.split('\n'):
        s = remove_non_digits(s)
        nums.append(int(f"{s[0]}{s[-1]}"))

    return sum(nums)


def part2(content: str) -> int:
    nums = []
    for s in content.split('\n'):
        s = remove_non_digits(digitify(s))
        nums.append(int(f"{s[0]}{s[-1]}"))

    return sum(nums)


print(f"Part 1: {part1(read_input(__file__, 1))}")  # 55172
print(f"Part 2: {part2(read_input(__file__, 2))}")  # 54925
