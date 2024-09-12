import bisect
from typing import List


# https://leetcode.cn/problems/squares-of-a-sorted-array/description/
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        N = len(nums)
        i, j = 0, N - 1
        ans = []
        while i <= j:
            ni = nums[i] ** 2
            nj = nums[j] ** 2
            if ni > nj:
                ans.append(ni)
                i += 1
            else:
                ans.append(nj)
                j -= 1
        ans.reverse()
        return ans
