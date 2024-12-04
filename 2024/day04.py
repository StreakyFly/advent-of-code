from utils import read_input


def parse_input(content: str) -> list[str]:
    return content.splitlines()


def part1(content: str) -> int:
    rows = parse_input(content)
    count = 0

    # go through the entire text char by char, and if there's an X, check all sides - left, right, up, down & diagonal
    for r, row in enumerate(rows):
        for c, char in enumerate(row):  # c as column
            if char != "X":
                continue

            words = [
                row[c:c+4],  # horizontal left to right
                row[max(0, c-3):c+1][::-1],  # horizontal right to left
                "".join([row[c] for row in rows[r:min(len(rows), r+4)]]),  # vertical down
                "".join([row[c] for row in rows[max(0, r-3):r+1]])[::-1],  # vertical up
                "", "", "", ""  # diagonal (in all directions)
            ]

            for i in range(4):
                words[4] += rows[r+i][c+i] if r+i < len(rows) and c+i < len(row) else ""  # diagonal down right
                words[5] += rows[r+i][c-i] if r+i < len(rows) and c-i >= 0 else ""  # diagonal down left
                words[6] += rows[r-i][c+i] if r-i >= 0 and c+i < len(row) else ""  # diagonal up right
                words[7] += rows[r-i][c-i] if r-i >= 0 and c-i >= 0 else ""  # diagonal up left

            count += sum([word == "XMAS" for word in words])

    return count


def part2(content: str) -> int:
    rows = parse_input(content)
    count = 0

    for r, row in enumerate(rows):
        for c, char in enumerate(row):  # c as column
            if char != "A":
                continue

            # if any of the needed adjacent indexes are out of range, continue
            if r-1 < 0 or c-1 < 0 or r+1 >= len(rows) or c+1 >= len(row):
                continue

            # check if upper left index and lower right index have "M" & "S" and same with upper right and lower left
            if (rows[r-1][c-1] in "MS" and rows[r+1][c+1] in "MS" and rows[r-1][c-1] != rows[r+1][c+1]) and \
               (rows[r-1][c+1] in "MS" and rows[r+1][c-1] in "MS" and rows[r-1][c+1] != rows[r+1][c-1]):
                count += 1

    return count


print(f"Part 1: {part1(read_input(__file__))}")  # 2562
print(f"Part 2: {part2(read_input(__file__))}")  # 1902
