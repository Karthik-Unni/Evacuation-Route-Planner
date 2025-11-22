import heapq
from .utils import DIRS, heuristic

def astar(grid, fire, start, goal):
    rows, cols = grid.shape

    pq = []
    heapq.heappush(pq, (0, start))
    came_from = {start: None}
    g = {start: 0}

    while pq:
        _, current = heapq.heappop(pq)

        if current == goal:
            break

        cr, cc = current

        for dr, dc in DIRS:
            nr, nc = cr + dr, cc + dc
            nxt = (nr, nc)

            if not (0 <= nr < rows and 0 <= nc < cols):
                continue
            if grid[nr][nc] == 1:
                continue
            if fire[nr][nc] == 1:
                continue

            new_g = g[current] + 1

            if nxt not in g or new_g < g[nxt]:
                g[nxt] = new_g
                f = new_g + heuristic(nxt, goal)
                heapq.heappush(pq, (f, nxt))
                came_from[nxt] = current

    if goal not in came_from:
        return None

    # Reconstruct path
    path = []
    node = goal
    while node is not None:
        path.append(node)
        node = came_from[node]
    return list(reversed(path))
