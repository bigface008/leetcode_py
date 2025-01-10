# https://leetcode.com/problems/word-subsets/?envType=daily-question&envId=2025-01-10
from collections import defaultdict
from typing import List


class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        cnt2 = defaultdict(int)
        for wd2 in words2:
            temp = defaultdict(int)
            for ch in wd2:
                temp[ch] += 1
            for k, v in temp.items():
                cnt2[k] = max(cnt2[k], v)
        ans = []
        for wd1 in words1:
            temp = defaultdict(int)
            for ch in wd1:
                temp[ch] += 1
            valid = True
            for k, v in cnt2.items():
                if v > temp[k]:
                    valid = False
                    break
            if valid:
                ans.append(wd1)
        return ans
