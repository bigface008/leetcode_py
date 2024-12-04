from typing import List


# https://leetcode.cn/problems/find-if-digit-game-can-be-won/description/?envType=daily-question&envId=2024-11-30
class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        all_sum = 0
        single_sum = 0
        for x in nums:
            if x < 10:
                single_sum += x
            all_sum += x
        return all_sum - single_sum != single_sum