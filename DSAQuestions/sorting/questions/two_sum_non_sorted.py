"""
* Asymptotic complexity in terms of the size of `numbers` = `n`:
* Time: O(n).
* Auxiliary space: O(n).
* Total space: O(n).
"""


def two_sum(numbers, target):
    n = len(numbers)
    array_index = {}
    for i in range(n):
        current = numbers[i]
        required = target - current  # complementary target pair

        if required in array_index:
            return [i, array_index[required]]

        # Add every element to map after checking for required.
        # This ensures that element does not match itself (indices to be unique).
        array_index[current] = i

    return [-1, -1]


print(two_sum([1, 2, 3, 5, 10], 7))
