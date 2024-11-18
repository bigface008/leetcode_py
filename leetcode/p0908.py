from typing import List


# https://leetcode.cn/problems/smallest-range-i/?envType=daily-question&envId=2024-10-20
class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        mn = min(nums)
        mx = max(nums)
        diff = mx - mn
        if diff <= 2 * k:
            return 0
        return diff - 2 * k
