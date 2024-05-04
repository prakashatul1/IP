from collections import deque


def maxAreaOfIsland(grid):
    if not grid or not grid[0]:
        return 0

    max_area = 0
    visit = set()
    rows, cols = len(grid), len(grid[0])

    def bfs(r, c):
        q = deque()
        visit.add((r, c))
        q.append((r, c))
        area = 1

        while q:
            row, col = q.popleft()
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

            for dr, dc in directions:
                r, c = row + dr, col + dc
                if r in range(rows) and c in range(cols) and grid[r][c] == 1 and (r, c) not in visit:
                    q.append((r, c))
                    visit.add((r, c))
                    area += 1

        return area

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1 and (r, c) not in visit:
                area = bfs(r, c)
                max_area = max(max_area, area)

    return max_area


grid = [
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]
]


print(maxAreaOfIsland(grid))