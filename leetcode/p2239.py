# https://leetcode.cn/problems/find-closest-number-to-zero/?envType=daily-question&envId=2025-01-20
from typing import List
from math import inf


class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        N = len(nums)
        dist = inf
        cnt = 0
        ans = inf
        for x in nums:
            temp = abs(x)
            if temp < dist:
                dist = temp
                cnt = 1
                ans = x
            elif temp == dist:
                cnt += 1
                ans = max(ans, x)
        return ans