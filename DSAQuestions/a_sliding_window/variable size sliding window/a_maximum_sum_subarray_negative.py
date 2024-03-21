def maxSubArray(nums) -> int:
    i, j = 0, 0
    curs = 0
    maxs = nums[0]

    while j < len(nums):

        if curs < 0:
            curs = 0
            i = j

        curs += nums[j]

        if curs > maxs:
            maxs = curs
            # can store i and j and return value here

        j += 1

    return maxs


print(maxSubArray([5, -3, 5]))
# result 7
