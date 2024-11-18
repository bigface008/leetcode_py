from collections import Counter
from typing import List


# https://leetcode.cn/problems/count-pairs-that-form-a-complete-day-ii/?envType=daily-question&envId=2024-10-23
class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        mp = [0] * 24
        ans = 0
        for i, h in enumerate(hours):
            mod = h % 24
            remain = 24 - mod
            if remain == 24:
                remain = 0
            ans += mp[remain]
            mp[mod] += 1
        return ans