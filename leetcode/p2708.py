from typing import List


# https://leetcode.cn/problems/maximum-strength-of-a-group/?envType=daily-question&envId=2024-09-03
class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        ans = 1
        negatives = []
        positive_cnt = 0
        has_zero = False
        for n in nums:
            if n > 0:
                ans *= n
                positive_cnt += 1
            elif n < 0:
                negatives.append(n)
            else:
                has_zero = True
        if positive_cnt == 0:
            if has_zero and len(negatives) <= 1:
                return 0
            elif len(negatives) == 1:
                return negatives[0]
        for n in negatives:
            ans *= -n
        if len(negatives) % 2 != 0:
            min_abs = -max(negatives)
            ans //= min_abs
        return ans