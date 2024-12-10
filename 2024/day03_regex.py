from utils import read_input
import re


def part1(content: str) -> int:
    return sum(int(a) * int(b) for a, b in re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", content))


def part2(content: str) -> int:
    # - ignore anything that starts with "don't()" and ends with "do()"
    # - store all remaining valid mul(x,y) instructions that don't get ignored because of being between don't() & do()
    # - add "do()" at the end of the content, in case there's a don't() instr near the end, then mul(x,y), but no do() after it;
    #    without adding do() at the end, the mul(x,y) instructions after last don't() wouldn't be ignored, even though they should be
    return sum(int(a) * int(b) for a, b in re.findall(r"don't\(\).*?do\(\)|mul\((\d{1,3}),(\d{1,3})\)", content+"do()", flags=re.DOTALL) if a and b)


print(f"Part 1: {part1(read_input(__file__))}")  # 174336360
print(f"Part 2: {part2(read_input(__file__))}")  # 88802350
