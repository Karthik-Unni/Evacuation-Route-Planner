import numpy as np
from .utils import DIRS

def spread_fire(fire_grid):
    rows, cols = fire_grid.shape
    new_fire = fire_grid.copy()

    for r in range(rows):
        for c in range(cols):
            if fire_grid[r][c] == 1:
                for dr, dc in DIRS:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols:
                        new_fire[nr, nc] = 1

    return new_fire
