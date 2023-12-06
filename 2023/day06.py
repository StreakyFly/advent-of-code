from math import prod, ceil, sqrt

from utils import read_input


def parse_input(content: str) -> (list[int, ...], list[int, ...]):
    l_times, l_distances = content.splitlines()
    times = [int(i) for i in l_times.split()[1:]]
    distances = [int(i) for i in l_distances.split()[1:]]

    return times, distances


def calculate_num_of_ways_to_win_bruteforce(all_time: int, record_dist: int) -> int:
    num_ways_to_beat_record = 0
    for button_held in range(1, all_time + 1):
        this_dist = button_held * (all_time - button_held)
        if this_dist > record_dist:
            num_ways_to_beat_record += 1

    return num_ways_to_beat_record


def calculate_num_of_ways_to_win(t: int, d: int) -> int:
    lower_limit = ceil((t - sqrt((t ** 2 - 4 * d))) / 2)  # quadratic formula (a=1, b=-t, c=d)
    upper_limit = ceil((t + sqrt((t ** 2 - 4 * d))) / 2)  # (-b +- sqrt(b^2 - 4ac)) / 2a
    return min(t, upper_limit) - max(0, lower_limit)


def part1(content: str) -> int:
    return prod([calculate_num_of_ways_to_win(t, d) for t, d in zip(*parse_input(content))])


def part2(content: str) -> int:
    times, distances = parse_input(content)
    all_time = int(''.join(str(num) for num in times))
    record_dist = int(''.join(str(num) for num in distances))

    return calculate_num_of_ways_to_win(all_time, record_dist)


print(f"Part 1: {part1(read_input(__file__))}")  # 512295
print(f"Part 2: {part2(read_input(__file__))}")  # 36530883
