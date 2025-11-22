DIRS = [
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1),
]

def heuristic(a, b):
    """Manhattan distance"""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])
