# https://leetcode.com/problems/search-in-rotated-sorted-array/
def search(nums, target: int) -> int:
    i, j = 0, len(nums) - 1
    n = get_rotated_count(nums)

    if target == nums[n]:
        return n
    elif target > nums[j]:
        return binarySearch(nums, i, n - 1, target)
    else:
        return binarySearch(nums, n + 1, j, target)


def binarySearch(nums, i, j, target):
    while i <= j:

        mid = (i + j) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            j = mid - 1
        elif nums[mid] < target:
            i = mid + 1

    return -1


def get_rotated_count(nums):
    i, j = 0, len(nums) - 1
    while i <= j:

        mid = (i + j) // 2
        nexte = (mid + 1) % len(nums)
        previous = (mid - 1 + len(nums) % len(nums))

        if nums[mid] <= nums[previous] and nums[mid] <= nums[nexte]:
            return mid
        elif nums[i] < nums[j]:
            return i
        elif nums[i] <= nums[mid]:
            i = nexte
        else:
            j = previous

    return 0


print(search([4, 5, 6, 7, 0, 1, 2], 0))
print(search([4, 5, 6, 7, 0, 1, 3], 3))
print(search([1, 3], 2))
