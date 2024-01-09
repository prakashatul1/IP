# find minimum window substring which has all letters of child string in minimum quantity as in child string
def minimum_window_substring(parent_string: str, child_string: str):
    i, j = 0, 0
    parent_string_length = len(parent_string)
    cal_dict = {}

    # help to find minimum when initialized with this number
    result = 99999

    # to calculated match
    count = 0

    # create an array from smaller string for calculation
    # specially when increasing i
    for each in child_string:
        if each not in cal_dict:
            cal_dict[each] = 1
        else:
            cal_dict[each] += 1
        count += 1

    # loop till end of bigger string
    while j < parent_string_length:

        # different condition if value is negative
        if parent_string[j] in cal_dict:
            if cal_dict[parent_string[j]] > 0:
                count -= 1

            cal_dict[parent_string[j]] -= 1

        # when one of the match is found
        while count == 0:
            result = min(result, j-i+1)

            # sliding the window
            if parent_string[i] in cal_dict:

                # taking care of negatives also
                # it can come when there is extra count is more than required
                if cal_dict[parent_string[i]] >= 0:
                    count += 1

                cal_dict[parent_string[i]] += 1

            i += 1

        j += 1

    return result


print(minimum_window_substring("timetoacode", "toc"))
