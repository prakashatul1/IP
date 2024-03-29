def find_longest_subarray(array_int: list[int], total_sum: int) -> int:
    i, j = 0, 0
    length = len(array_int)
    maxi = 0
    calculation_sum = 0

    while j < length:

        # calculation in cache
        # for calculation_sum < sum
        # add after i ++ to be able to reach to
        # if calculation_sum > sum: condition
        calculation_sum = calculation_sum + array_int[j]

        # getting the result
        if calculation_sum == total_sum:
            maxi = max(maxi, j - i + 1)

        # adjustment for next window
        elif calculation_sum > total_sum:
            calculation_sum = calculation_sum - array_int[i]
            i += 1

        j += 1

    return maxi


array1 = [4, 1, 1, 1, 1, 1, 2, 3, 5]
print(find_longest_subarray(array1, 9))
