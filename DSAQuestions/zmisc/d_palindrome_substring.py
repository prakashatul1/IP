# https://leetcode.com/problems/palindromic-substrings/
"""
Example 1:

Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
Example 2:

Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
"""


def countSubstrings(s: str) -> int:
    count = 0
    for i in range(len(s)):
        count += countPalindrome(s, i, i)  # odd
        count += countPalindrome(s, i, i + 1)  # even

    return count


def countPalindrome(s, i, j):
    count = 0

    while i >= 0 and j < len(s) and s[i] == s[j]:
        count += 1
        i -= 1
        j += 1

    return count


print(countSubstrings(s="abc"))  # result 3
print(countSubstrings(s="aaa"))  # result 6
print(countSubstrings(s="aba"))  # result 4
