from typing import List


# https://leetcode.com/problems/count-the-number-of-consistent-strings/?envType=daily-question&envId=2024-09-12
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        st = set(allowed)
        ans = 0
        for word in words:
            consistent = True
            for ch in word:
                if ch not in st:
                    consistent = False
                    break
            if consistent:
                ans += 1
        return ans
