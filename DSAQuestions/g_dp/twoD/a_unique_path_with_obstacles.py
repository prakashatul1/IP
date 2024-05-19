# https://leetcode.com/problems/unique-paths-ii/
from typing import List


def uniquePathsWithObstacles(obstacleGrid: List[List[int]]) -> int:
    M, N = len(obstacleGrid), len(obstacleGrid[0])
    dp = [0] * N
    dp[N - 1] = 1

    # Time: O(N*M), Space: O(N)
    for r in reversed(range(M)):
        for c in reversed(range(N)):
            if obstacleGrid[r][c]:
                dp[c] = 0
            elif c + 1 < N:
                dp[c] = dp[c] + dp[c + 1]
    return dp[0]


print(uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
