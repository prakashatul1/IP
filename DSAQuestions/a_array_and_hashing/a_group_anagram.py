from collections import defaultdict
from typing import List, Any


def groupAnagrams(strs: List[str]):
    res = defaultdict(list)

    for s in strs:

        count = [0] * 26

        for c in s:
            count[ord(c) - ord("a")] += 1

        res[tuple(count)].append(s)

    return res.values()
