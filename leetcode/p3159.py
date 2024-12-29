# https://leetcode.cn/problems/find-occurrences-of-an-element-in-an-array/?envType=daily-question&envId=2024-12-27
from typing import List


class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        N, Q = len(nums), len(queries)
        ans = [-1] * Q
        pos = []
        for i, n in enumerate(nums):
            if n == x:
                pos.append(i)
        for i, q in enumerate(queries):
            if q > len(pos):
                continue
            ans[i] = pos[q - 1]
        return ans