def pair_sum_sorted_array(numbers, target):
    """
    Args:
     numbers(list_int32)
     target(int32)
    Returns:
     list_int32
    """
    # Write your code here.
    i = 0
    j = len(numbers) - 1

    while i < j:

        if numbers[j] + numbers[i] == target:
            return [i, j]
        elif numbers[j] + numbers[i] < target:
            i += 1
        else:
            j -= 1

    return [-1, -1]


print(pair_sum_sorted_array([1, 2, 3, 5, 10], 7))
