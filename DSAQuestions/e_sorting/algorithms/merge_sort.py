# stable = yes
# 

def merge_sort(arr):
    helper(arr, 0, len(arr) - 1)
    return arr


def helper(arr, start, end):
    """
    Args:
     arr(list_int32)
    Returns:
     list_int32
     :param arr:
     :param end:
     :param start:
    """
    # Write your code here.

    # leaf worker
    if start == end:
        return

    # internal worker
    mid = (start + end) // 2
    helper(arr, start, mid)
    helper(arr, mid + 1, end)

    aux = []
    i, j = start, mid + 1

    while i <= mid and j <= end:
        if arr[i] <= arr[j]:
            aux.append(arr[i])
            i += 1
        else:
            aux.append(arr[j])
            j += 1

    # gather phase
    while i <= mid:
        aux.append(arr[i])
        i += 1
    while j <= end:
        aux.append(arr[j])
        j += 1

    arr[start:end+1] = aux
    return arr


print(merge_sort([5, 8, 3, 9, 4, 1, 7]))
