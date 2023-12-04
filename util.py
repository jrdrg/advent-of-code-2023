def get_lines(inp: str) -> list[str]:
    lines = inp.split("\n")
    lines = filter(lambda l: len(l) > 0, lines)
    return list(lines)

def add(a: int, b: int):
    return a + b
