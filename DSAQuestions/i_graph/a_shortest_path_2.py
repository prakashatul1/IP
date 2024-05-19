# https://leetcode.com/problems/shortest-path-in-binary-matrix/description/
"""
Example 1:
Input: grid = [[0,1],[1,0]]
Output: 2

Example 2:
Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
Output: 4

Example 3:
Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
Output: -1

"""

from collections import deque

def shortestPathBinaryMatrix(grid):
    if not grid or not grid[0]:
        return 0

    visit = set()
    rows, cols = len(grid), len(grid[0])

    def bfs(r, c):
        q = deque()
        visit.add((r, c))
        q.append((r, c, 1))

        while q:
            row, col, length = q.popleft()
            if grid[row][col] == 1:
                return -1
            if row == rows - 1 and col == cols - 1:
                return length

            directions = [[-1, -1], [-1, 1], [1, -1], [1, 1], [1, 0], [-1, 0], [0, 1], [0, -1]]

            for dr, dc in directions:
                r, c = row + dr, col + dc
                if r in range(rows) and c in range(cols) and grid[r][c] == 0 and (r, c) not in visit:
                    q.append((r, c, length + 1))
                    visit.add((r, c))

        return -1

    return bfs(0, 0)


grid = [[0, 1], [1, 0]]
grid2 = [[0, 0, 0],
         [1, 1, 0],
         [1, 1, 0]]

grid3 = [[0, 0, 0, 0],
        [1, 1, 0, 0],
        [0, 0, 0, 1],
        [0, 1, 0, 0]]
print(shortestPathBinaryMatrix(grid3))
