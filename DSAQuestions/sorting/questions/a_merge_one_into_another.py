def merge_one_into_another(first, second):
    """
    Args:
     first(list_int32)
     second(list_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    i = len(first) - 1
    j = len(first) - 1
    k = len(second) - 1

    while i >= 0 and j >= 0 and k >= 0:

        if first[i] >= second[j]:
            second[k] = first[i]
            i -= 1
        else:
            second[k] = second[j]
            j -= 1
        k -= 1

    while i >= 0:
        second[i] = first[i]
        i -= 1

    return second


print(merge_one_into_another( [1, 2, 3],  [4, 5, 6, 0, 0, 0]))
