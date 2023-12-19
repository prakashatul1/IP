def find_longest_substring(string_alpha: str, unique: int) -> int:

    i, j = 0, 0
    length = len(string_alpha)
    cal_dict = {}
    calculation_unique = 0

    while j < length:

        # calculation w.r.t j
        if string_alpha[j] not in cal_dict:
            cal_dict[string_alpha[j]] = 1
        else:
            cal_dict[string_alpha[j]] += 1

        # getting one of many result
        # checking if last loop result is more close
        if len(cal_dict) == unique:
            calculation_unique = max((j - i + 1), calculation_unique)

        # adjustment for next window
        while len(cal_dict) > unique:
            if cal_dict[string_alpha[i]] == 1:
                del cal_dict[string_alpha[i]]
            else:
                cal_dict[string_alpha[i]] -= 1
            i += 1

        j += 1

    return calculation_unique

string1 = "aabacbebebe"
print(find_longest_substring(string1, 3))
