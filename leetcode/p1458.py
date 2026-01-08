# https://leetcode.cn/problems/max-dot-product-of-two-subsequences/?envType=daily-question&envId=2026-01-08
from typing import List, Dict, Optional
from functools import cache
from math import inf


class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:

        @cache
        def dfs(i: int, j: int) -> int:
            ans = nums1[i] * nums2[j]
            if i - 1 >= 0:
                ans = max(ans, dfs(i - 1, j))
            if j - 1 >= 0:
                ans = max(ans, dfs(i, j - 1))
            if i - 1 >= 0 and j - 1 >= 0:
                ans = max(ans, max(dfs(i - 1, j - 1), 0) + nums1[i] * nums2[j])
            return ans

        return dfs(len(nums1) - 1, len(nums2) - 1)