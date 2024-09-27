from collections import Counter
from typing import List


# https://leetcode.com/problems/uncommon-words-from-two-sentences
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        dic1 = Counter()
        dic2 = Counter()
        for wd in s1.split(' '):
            dic1[wd] += 1
        for wd in s2.split(' '):
            dic2[wd] += 1
        ans = []
        for wd, cnt in dic1.items():
            if cnt == 1 and wd not in dic2:
                ans.append(wd)
        for wd, cnt in dic2.items():
            if cnt == 1 and wd not in dic1:
                ans.append(wd)
        return ans
