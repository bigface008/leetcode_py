# https://leetcode.cn/problems/count-odd-numbers-in-an-interval-range/description/?envType=daily-question&envId=2025-12-07
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if low % 2 == high % 2:
            if low % 2 == 0:
                return (high - low) // 2
            else:
                return (high - low) // 2 + 1
        else:
            return (high - low + 1) // 2