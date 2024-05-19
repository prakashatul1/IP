# https://leetcode.com/problems/unique-paths/
# you can go only right and down. no obstacles
# time - n
# space - n


from collections import deque


# bfs
def uniquePaths(m, n):
    queue = deque()
    queue.append((0, 0))
    calc = [[0] * n for _ in range(m)]
    calc[0][0] = 1

    directions = [[0, 1], [1, 0]]

    while queue:
        row, col = queue.popleft()
        for r, c in directions:
            dr, dc = row + r, c + col
            if 0 <= dr < m and 0 <= dc < n:
                if calc[dr][dc] == 0:
                    queue.append((dr, dc))
                calc[dr][dc] += calc[row][col]

    return calc[m - 1][n - 1]


# top down memo
def uniquePathsMemo(m, n):
    def memoization(r, c, rows, cols, cache):

        if r == rows or c == cols:
            return 0
        if cache[r][c] > 0:
            return cache[r][c]
        if r == rows - 1 and c == cols - 1:
            return 1

        cache[r][c] = (memoization(r + 1, c, rows, cols, cache) +
                       memoization(r, c + 1, rows, cols, cache))

        return cache[r][c]

    return memoization(0, 0, m, n, [[0] * n for _ in range(m)])


# bottom up dp
# time = m*n
# space = n
def uniquePathsDp(m: int, n: int) -> int:
    dp = [0] * n
    dp[n - 1] = 1

    for r in reversed(range(m)):
        for c in reversed(range(n)):
            if c + 1 < n:
                dp[c] = dp[c + 1] + dp[c]

    return dp[0]


print(uniquePaths(3, 7))  # result = 28
print(uniquePathsMemo(3, 7))  # result = 28
print(uniquePathsDp(3, 7))  # result = 28
