# https://leetcode.cn/problems/maximum-length-substring-with-two-occurrences/description/
from typing import List
from collections import defaultdict


class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        freq_mp = defaultdict(int)

        def check_valid() -> bool:
            for v in freq_mp.values():
                if v > 2:
                    return False
            return True

        left = 0
        ans = 0
        for right, ch in enumerate(s):
            freq_mp[ch] += 1
            while left <= right and not check_valid():
                lch = s[left]
                freq_mp[lch] -= 1
                if freq_mp[lch] == 0:
                    del freq_mp[lch]
                left += 1
            ans = max(ans, right - left + 1)
        return ans

