# https://leetcode.com/problems/house-robber/
"""
Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
"""


# memoization
def rob(nums):
    n = len(nums)
    calc = {}

    def dfs(index):

        if index >= n:
            return 0
        if index in calc:
            return calc[index]

        next_train = dfs(index + 1)

        this_train = nums[index] + (dfs(index + 2) if index + 2 <= n else 0)

        calc[index] = max(next_train, this_train)
        return calc[index]

    return dfs(0)


def rob_db(nums):
    rob1, rob2 = 0, 0

    for n in nums:
        temp = max(n + rob1, rob2)
        rob1 = rob2
        rob2 = temp
    return rob2


print(rob_db([2, 7, 9, 3, 1]))

print(rob([2, 7, 9, 3, 1]))
