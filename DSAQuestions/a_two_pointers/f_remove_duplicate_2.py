# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
from typing import List, Tuple


def removeDuplicates(nums: List[int]) -> tuple[int, list[int]]:
    r, l = 0, 0

    while r < len(nums):

        count = 1
        while r + 1 in range(len(nums)) and nums[r] == nums[r + 1]:
            r += 1
            count += 1

        for i in range(min(2, count)):
            nums[l] = nums[r]
            l += 1

        r += 1

        print(r, count)

    return l, nums[:l]


print(removeDuplicates([1, 1, 1, 2, 2, 3]))
