# https://leetcode.com/problems/count-partitions-with-max-min-difference-at-most-k/?envType=daily-question&envId=2025-12-06
from typing import List, Dict, Optional, Tuple
from collections import deque


class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        N = len(nums)
        MOD = pow(10, 9) + 7
        dp = [0] * (N + 1)
        dp[0] = 1
        min_stk = deque()
        max_stk = deque()
        window_sum = 0
        left = 0

        for i, x in enumerate(nums):
            window_sum += dp[i]
            while min_stk and nums[min_stk[-1]] >= x:
                min_stk.pop()
            min_stk.append(i)
            while max_stk and nums[max_stk[-1]] <= x:
                max_stk.pop()
            max_stk.append(i)

            while nums[max_stk[0]] - nums[min_stk[0]] > k:
                window_sum -= dp[left]
                left += 1
                if min_stk[0] < left:
                    min_stk.popleft()
                if max_stk[0] > left:
                    max_stk.popleft()
            dp[i + 1] = window_sum % MOD
        return dp[-1]


        # dp[i] =
        #   for j in range(i - 1, -1, -1):
        #     if max(nums[0...j]) - min(nums[0...j]) > k:
        #       break
        #     += dp[j]
        #   j + 1