# https://leetcode.com/problems/combination-sum/description/
"""
Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
"""


def combinationSum(candidates, target):
    res = []

    def dfs(i, cur, total):

        if total == target:
            res.append(cur.copy())
            return

        if i >= len(candidates) or total > target:
            return

        cur.append(candidates[i])
        dfs(i, cur, total + candidates[i])

        cur.pop()
        dfs(i + 1, cur, total)

    dfs(0, [], 0)
    return res


print(combinationSum([2, 3, 6, 7], 7))
