# https://leetcode.com/problems/minimum-length-of-string-after-operations/?envType=daily-question&envId=2025-01-13
from collections import Counter


class Solution:
    def minimumLength(self, s: str) -> int:
        cnt = Counter(s)
        ans = 0
        for k, v in cnt.items():
            if v <= 2:
                ans += v
            else:
                ans += 1 if v % 2 == 1 else 2
        return ans

# 3 -> 1
# 4 -> 2
# 5 -> 3 -> 1
# 6 -> 4 -> 2
# 7 -> 5 -> 3 -> 1