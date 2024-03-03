def insertion_sort(arr):
    """
    Args:
     arr(list_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    for i in range(len(arr)):
        temp = arr[i]
        red = i - 1
        while red >= 0 and arr[red] > temp:
            arr[red + 1] = arr[red]
            red -= 1
        arr[red + 1] = temp

    return arr


print(insertion_sort([5, 8, 3, 9, 4, 1, 7]))
