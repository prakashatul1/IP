def containsNearbyDuplicate(nums, k):
    i, j = 0, 0
    window = set()

    while j < len(nums):

        if j - i + 1 > k:
            window.remove(nums[i])
            i += 1

        if nums[j] in window:
            return True

        window.add(nums[j])

        j += 1

    return False


arr1, k1 = [1, 2, 3, 1], 3  # result True
arr2, k2 = [1, 0, 1, 1], 1  # result True
arr3, k3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 9], 3  # result True
arr4, k4 = [0, 1, 2, 3, 2, 5], 3  # result True

print(containsNearbyDuplicate(arr3, k3))