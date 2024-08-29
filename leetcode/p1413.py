from typing import List


# https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum/
class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        min_sum = 0
        s = 0
        for n in nums:
            s += n
            min_sum = min(s, min_sum)
        if min_sum < 0:
            return -min_sum + 1
        else:
            return 1
