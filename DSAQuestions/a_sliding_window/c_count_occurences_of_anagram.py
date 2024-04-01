# Input:
# txt = forxxorfxdofr
# pat = for
# Output: 3
# Explanation: for, orf and ofr appears
# in the txt, hence answer is 3.

def count_occurrence(string1: str, string2: str) -> int:
    if len(string2) > len(string1):
        return 0

    pattern_dict = {}
    for char in string2:
        if char in pattern_dict:
            pattern_dict[char] += 1
        else:
            pattern_dict[char] = 1

    start, matched = 0, 0
    result = 0
    window_dict = {}

    # Start sliding the window
    for end in range(len(string1)):
        char_end = string1[end]

        if char_end in pattern_dict:
            if char_end in window_dict:
                window_dict[char_end] += 1
            else:
                window_dict[char_end] = 1

            if window_dict[char_end] == pattern_dict[char_end]:
                matched += 1

        # Shrink the window if it's size exceeds string2's length
        if end >= len(string2):
            char_start = string1[start]
            start += 1
            if char_start in window_dict:
                if window_dict[char_start] == pattern_dict[char_start]:
                    matched -= 1
                window_dict[char_start] -= 1

        # Check if we have all matches
        if matched == len(pattern_dict):
            result += 1

    return result



# string1 = "forxxorfxdofr"
# string2 = "for"

string1 = "aabaabaa"
string2 = "abaa"
print(count_occurrence(string1, string2)) 
