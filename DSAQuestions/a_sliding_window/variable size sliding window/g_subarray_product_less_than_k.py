# https://leetcode.com/problems/subarray-product-less-than-k/

def numSubarrayProductLessThanK(nums, k) -> int:
    i, j = 0, 0
    result = 0
    prod = 1

    if k <= 1:
        return 0

    while j < len(nums):

        prod *= nums[j]

        while prod >= k:
            prod = prod // nums[i]
            i += 1

        result += j - i + 1
        j += 1

    return result


# print(numSubarrayProductLessThanK([10, 5, 2, 6], 100))
print(numSubarrayProductLessThanK([1, 1, 1], 1))
