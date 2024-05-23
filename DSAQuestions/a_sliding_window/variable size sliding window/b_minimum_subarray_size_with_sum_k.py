# https://leetcode.com/problems/minimum-size-subarray-sum/description/

from typing import List


def minSubArrayLen(target: int, nums: List[int]) -> int:
    i, j = 0, 0
    total = 0
    minl = len(nums) + 1

    while j < len(nums):

        total += nums[j]

        if total >= target:
            minl = min(minl, j - i + 1)

        while j - i + 1 > minl or total > target:
            total -= nums[i]
            i += 1

            if total >= target:
                minl = min(minl, j - i + 1)

        j += 1

    return minl if minl != len(nums) + 1 else 0


print(minSubArrayLen(9, [4, 1, 1, 1, 1, 1, 2, 3, 5]))
