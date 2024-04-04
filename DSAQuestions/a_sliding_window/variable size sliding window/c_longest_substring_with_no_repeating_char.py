def find_longest_substring(s: str) -> int:
    # i, j = 0, 0
    # length = len(string_alpha)
    # cal_dict = {}
    # calculation_unique = 0
    #
    # while j < length:
    #
    #     # calculation w.r.t j
    #     if string_alpha[j] not in cal_dict:
    #         cal_dict[string_alpha[j]] = 1
    #     else:
    #         cal_dict[string_alpha[j]] += 1
    #
    #     # getting one of many result
    #     # checking if last loop result is more close
    #     if cal_dict[string_alpha[j]] == 1:
    #         calculation_unique = max((j - i + 1), calculation_unique)
    #
    #     # adjustment for next window
    #
    #     while cal_dict[string_alpha[j]] > 1:
    #
    #         if cal_dict[string_alpha[i]] == 1:
    #             del cal_dict[string_alpha[i]]
    #         else:
    #             cal_dict[string_alpha[i]] -= 1
    #         i += 1
    #
    #     j += 1
    #
    # return calculation_unique
    if len(s) == 1:
        return 1
    elif len(s) == 0:
        return 0

    i, j = 0, 0
    a = ""
    max_len = 0

    while j < len(s):

        if not s[j] in a:
            a += s[j]
            max_len = max(max_len, len(a))
        else:
            while s[j] in a:
                i += 1
                a = a[1:]
            a += s[j]

        j += 1

    return max_len


string1 = "abbcde"
print(find_longest_substring(string1))
