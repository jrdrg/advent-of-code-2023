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
