from enum import Enum

def get_lines(inp: str, remove_blanks: bool = True) -> list[str]:
    lines = inp.split("\n")
    if remove_blanks:
        lines = filter(lambda l: len(l) > 0, lines)
    return list(lines)

def add(a: int, b: int):
    return a + b


Grid = dict[tuple[int, int], str]

def lines_to_grid(lines: list[str]) -> Grid:
    grid = {}
    for y, line in enumerate(lines):
        for x, cell in enumerate(line):
            grid[(y, x)] = cell
    return grid

class Direction(Enum):
    NORTH = (-1, 0)
    SOUTH = (1, 0)
    EAST = (0, 1)
    WEST = (0, -1)

def intersect_range(x: range, y: range):
    return range(max(x[0], y[0]), min(x[-1], y[-1])+1)
