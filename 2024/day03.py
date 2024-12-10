from utils import read_input


MUL_INSTR_START = "mul("
DO_INSTR = "do()"
DONT_INSTR = "don't()"


def run_instr(instr: str) -> int:
    x, y = map(int, instr[4:-1].split(","))
    return x * y


def parse_mul_instruction(content: str, start_index: int) -> tuple[str, int]:
    end_index = content.find(")", start_index, start_index + 12)  # 12 is max length of instruction: "mul(123,123)"
    if end_index == -1 or \
            content[start_index+4:end_index].count(",") != 1 or \
            not content[start_index+4:end_index].replace(",", "").isdigit():
        return "", start_index + 4  # skip invalid instruction

    return content[start_index:end_index+1], end_index + 1


def parse_instructions(content: str, include_do_dont: bool = False) -> list[str]:
    instructions = []
    i = 0

    while i < len(content):
        if content[i:i+4] == MUL_INSTR_START:
            instr, i = parse_mul_instruction(content, i)
            if instr:
                instructions.append(instr)
        elif include_do_dont:
            if content[i:i+4] == DO_INSTR:
                instructions.append(DO_INSTR)
                i += 4
            elif content[i:i+7] == DONT_INSTR:
                instructions.append(DONT_INSTR)
                i += 7
            else:
                i += 1
        else:
            i += 1

    return instructions


def part1(content: str) -> int:
    return sum(run_instr(instr) for instr in parse_instructions(content))


def part2(content: str) -> int:
    instructions = parse_instructions(content, include_do_dont=True)
    enabled_instructions = []
    enabled = True

    for instr in instructions:
        if instr == DO_INSTR:
            enabled = True
        elif instr == DONT_INSTR:
            enabled = False
        elif enabled:
            enabled_instructions.append(instr)

    return sum(run_instr(instr) for instr in enabled_instructions)


print(f"Part 1: {part1(read_input(__file__))}")  # 174336360
print(f"Part 2: {part2(read_input(__file__))}")  # 88802350
