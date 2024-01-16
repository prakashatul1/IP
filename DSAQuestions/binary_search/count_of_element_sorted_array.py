from first_n_last_occurance import first_occurrence, last_occurrence


def find_count(arr, ele):
    first = first_occurrence(arr, ele)
    last = last_occurrence(arr, ele)

    return last - first + 1
