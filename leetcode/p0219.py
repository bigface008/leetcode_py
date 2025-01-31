# https://leetcode.cn/problems/contains-duplicate-ii/?envType=daily-question&envId=2025-01-29
from collections import defaultdict
from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        N = len(nums)
        mp = defaultdict(int)
        for i, x in enumerate(nums):
            if x not in mp:
                mp[x] = i
            else:
                prev_i = mp[x]
                if abs(prev_i - i) <= k:
                    return True
                mp[x] = i
        return False