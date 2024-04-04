# description : https://leetcode.com/problems/longest-repeating-character-replacement/description/

def characterReplacement(s: str, k: int) -> int:

    countl = dict()
    res = 0
    maxf = 0

    i, j = 0, 0

    while j < len(s):

        countl[s[j]] = 1 + countl.get(s[j], 0)
        maxf = max(maxf, countl[s[j]])

        while (j - i + 1) - maxf > k:
            countl[s[i]] -= 1
            i += 1

        res = max(res, j - i + 1)
        j += 1

    return res
