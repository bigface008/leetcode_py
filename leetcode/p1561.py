# https://leetcode.cn/problems/maximum-number-of-coins-you-can-get/description/?envType=daily-question&envId=2025-01-22
from typing import List


class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        ans = 0
        N = len(piles) // 3
        for i in range(N):
            ans += piles[2 * i + 1]
        return ans