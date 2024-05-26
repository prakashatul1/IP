# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

def removeDuplicates(nums):
    i, j = 1, 1

    while j < len(nums):

        if nums[j] != nums[j - 1]:
            nums[i] = nums[j]
            i += 1

        j += 1

    return i, nums[:i]


print(removeDuplicates(nums=[0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
