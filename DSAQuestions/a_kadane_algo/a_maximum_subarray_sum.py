def maxSubArray(nums) -> int:
    res = nums[0]

    total = 0
    for n in nums:
        total += n
        res = max(res, total)
        if total < 0:
            total = 0
    return res


print(maxSubArray([5, -3, 5]))
# result = 7
