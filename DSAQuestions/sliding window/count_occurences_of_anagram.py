def count_occurrence(string1: str, string2: str) -> int:
    i, j = 0, 0
    length = len(string1)
    k = len(string2)
    result = 0
    calculation = k

    pattern_dict = {}
    for each in range(k):
        if not string2[each] in pattern_dict:
            pattern_dict[string2[each]] = 1
        else:
            pattern_dict[string2[each]] += 1

    while j < length:

        # calculation in cache
        if string1[j] in pattern_dict:
            calculation -= 1

        # increasing window till size k
        if j - i + 1 < k:
            j += 1

        # when window is of size k
        elif j - i + 1 == k:

            # result for the window
            if calculation == 0:
                result += 1

            # adjust the calculation cache to work with next
            # window before increasing i
            if string1[i] in pattern_dict:
                calculation += 1

            j += 1
            i += 1

    return result


# string1 = "forxxorfxdofr"
# string2 = "for"

string1 = "aabaabaa"
string2 = "abaa"
print(count_occurrence(string1, string2))
