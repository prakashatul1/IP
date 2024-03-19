def longestConsecutive(nums):
    # j = 0
    # max_count = 1
    # prev = None
    # nums = sorted(nums)
    #
    # print(nums)
    # count = 1
    # while j < len(nums):
    #     if prev is None:
    #         prev = nums[j]
    #     else:
    #         if prev + 1 == nums[j]:
    #             count += 1
    #         else:
    #             max_count = max(count, max_count)
    #             count = 1
    #
    #         prev = nums[j]
    #     j += 1
    #
    # return max(count, max_count)


    numSet = set(nums)
    longest = 0

    for n in nums:

        if n-1 not in numSet:
            length = 0
            while (n + length) in numSet:
                length += 1
            longest = max(length, longest)

    return longest




arr1 = [100, 4, 200, 1, 3, 2]
arr2 = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
arr3 = [9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6]

print(longestConsecutive(arr1))
