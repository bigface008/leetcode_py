from typing import List


# https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/?envType=daily-question&envId=2024-10-18
class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        N = len(nums)
        mask = 1 << N
        mx = 0
        ans = 0
        for state in range(mask):
            curr = 0
            for i in range(N):
                if (state >> i) & 1 == 1:
                    curr |= nums[i]
            if curr > mx:
                mx = curr
                ans = 1
            elif curr == mx:
                ans += 1
        return ans