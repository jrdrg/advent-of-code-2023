import util
import functools

example_input = """
Time:      7  15   30
Distance:  9  40  200
"""

input_str = """
Time:        46     80     78     66
Distance:   214   1177   1402   1024
"""

lines = util.get_lines(input_str)


def parse_input(lines: list[str]):
    time, distance = lines
    times = [int(s) for s in time.split(" ") if s.strip().isdigit()]
    distances = [int(s) for s in distance.split(" ") if s.strip().isdigit()]
    return list(map(lambda a, b: (a, b), times, distances))

def parse_part2_input(lines: list[str]):
    time, distance = lines
    times = [s for s in time.split(" ") if s.strip().isdigit()]
    distances = [s for s in distance.split(" ") if s.strip().isdigit()]
    return (int("".join(times)), int("".join(distances)))

def find_distance(button_time: int, time: int):
    remaining = time - button_time
    if (remaining <= 0):
        return 0
    return remaining * button_time

def find_winning_button_times(time: int, distance: int):
    midpoint = int(time / 2)
    timelist = [t for t in range(0, midpoint + 1) if find_distance(t, time) > distance]
    times = len(timelist)
    return (times * 2) - 1 if time % 2 == 0 else (times * 2)


print(find_distance(1, 7))
print(find_distance(2, 7))
print(find_distance(3, 7))
print(find_distance(4, 7))


def part1():
    races = parse_input(lines)
    distances = [find_winning_button_times(t, d) for (t, d) in races]
    print("t", races)
    print("d", distances)
    return functools.reduce(lambda a, b: a * b, distances)

def part2():
    (t, d) = parse_part2_input(lines)
    distances = find_winning_button_times(t, d)
    print("r", t, d)
    print("d", distances)
    return distances


print("Part 1", part1())
print("Part 2", part2())
