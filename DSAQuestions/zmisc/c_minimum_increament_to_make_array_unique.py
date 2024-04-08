# https://leetcode.com/problems/minimum-increment-to-make-array-unique/


"""
Example:

Input: nums = [3,2,1,2,1,7]
Output: 6
Explanation: After 6 moves, the array could be [3, 4, 1, 2, 5, 7].
It can be shown with 5 or less moves that it is impossible for the array to have all unique values.
"""


def minIncrementForUnique(nums) -> int:
    nums.sort()
    count = 0

    for i, each in enumerate(nums):

        if i > 0 and not each > nums[i - 1]:
            new = nums[i - 1] + 1
            count += (new - each)
            nums[i] = new

    return count


print(minIncrementForUnique([3, 2, 1, 2, 1, 7]))
