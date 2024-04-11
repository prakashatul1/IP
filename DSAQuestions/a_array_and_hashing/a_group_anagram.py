# https://leetcode.com/problems/group-anagrams/
"""
Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
"""

from collections import defaultdict


def groupAnagrams(strs):
    res = defaultdict(list)

    for s in strs:

        count = [0] * 26

        for c in s:
            count[ord(c) - ord("a")] += 1

        res[tuple(count)].append(s)

    return res.values()


print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
