def minSubArrayLen(target: int, nums: list[int]) -> int:
    i, j = 0, 0
    length = len(nums)
    summ = 0
    mini = None

    while j < length:

        summ = summ + nums[j]
        if summ >= target:
            if not mini or mini > j - i + 1:
                mini = j - i + 1

        if mini:
            while j - i + 1 > mini or summ > target:
                summ = summ - nums[i]
                i += 1

                if summ >= target:
                    if mini > j - i + 1:
                        mini = j - i + 1
        j += 1

    return mini if mini else 0


print(minSubArrayLen(9, [4, 1, 1, 1, 1, 1, 2, 3, 5]))
