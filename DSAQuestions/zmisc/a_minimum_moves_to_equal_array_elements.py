# https://leetcode.com/problems/minimum-moves-to-equal-array-elements/

"""
Example 1:

Input: nums = [1,2,3]
Output: 3
Explanation: Only three moves are needed (remember each move increments two elements):
[1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]

"""


def minMoves(nums) -> int:
    mini = min(nums)
    result = 0

    for each in nums:
        result += each - mini

    return result


print(minMoves([1, 2, 3]))
