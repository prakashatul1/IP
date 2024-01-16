from no_of_times_sorted_array_is_rotated import find_no_of_times
from binary_serach_sorted_array import  binary_search

def find_element_in_sorted_rotated_array(array_1, ele):
    index = find_no_of_times(array_1)

    l: int = len(array_1)
    start = 0
    end = l - 1

    leftarray = binary_search(array_1[start:l+1])
    rightarray = binary_search(array_1[l+1,end])

    return max(leftarray, rightarray)

