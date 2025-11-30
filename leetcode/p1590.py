# https://leetcode.cn/problems/make-sum-divisible-by-p/?envType=daily-question&envId=2025-11-30
from itertools import accumulate
from typing import List, Optional, Dict, Tuple
from math import inf
from collections import defaultdict


# NEED_SUM + T * p = R + T2 * p + x
# NEED_SUM - x + (T - T2) * p = R
# (NEED_SUM - x) % p = R

# (curr - target) % p = NEED_REMAIN


class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        N = len(nums)
        pre_sum = 0
        NEED_REMAIN = sum(nums) % p
        remain_to_last_pos: Dict[int] = {0: -1}
        ans = inf
        for i, v in enumerate(nums):
            pre_sum = (pre_sum + v) % p
            target_remain = (pre_sum - NEED_REMAIN) % p
            if target_remain in remain_to_last_pos:
                pos = remain_to_last_pos[target_remain]
                ans = min(ans, i - pos)
            remain_to_last_pos[pre_sum % p] = i
        return ans



        # N = len(nums)
        # pre_sum = list(accumulate(nums, initial=0))
        # NEED_REMAIN = pre_sum[-1] % p
        # if NEED_REMAIN == 0:
        #     return 0
        # remain_to_last_pos: Dict[int] = defaultdict(int)
        # ans = inf
        # for i in range(N + 1):
        #     x = pre_sum[i]
        #     target_remain = (p + x % p - NEED_REMAIN) % p
        #     if target_remain in remain_to_last_pos:
        #         pos = remain_to_last_pos[target_remain]
        #         ans = min(ans, i - pos)
        #     remain_to_last_pos[x % p] = i
        # if ans == inf or ans == N:
        #     return -1
        # return ans



        # N = len(nums)
        # NEED_SUM = sum(nums) % p
        # if NEED_SUM == 0:
        #     return 0
        #
        # def dfs(i: int, remain: int) -> int:
        #     x = nums[i]
        #     key = f'{i}.{remain}'
        #     if i == 0 and remain != x % p:
        #         return inf
        #     if remain == x % p:
        #         return 1
        #     prev_remain = (remain - x) % p
        #     prev_res = dfs(i - 1, prev_remain)
        #     res = prev_res + 1 if prev_res != inf else inf
        #     return res
        #
        # ans = inf
        # for i in range(N - 1, -1, -1):
        #     ans = min(ans, dfs(i, NEED_SUM))
        # if ans == inf or ans == N:
        #     return -1
        # return ans

        # N = len(nums)
        # NEED_SUM = sum(nums) % p
        # if NEED_SUM == 0:
        #     return 0
        # dp: List[int] = [inf] * p
        # ans = inf
        # for i, x in enumerate(nums):
        #     new_dp = [inf] * p
        #     new_dp[x % p] = 1
        #     for remain_prev in range(p):
        #         remain_i = (remain_prev + x) % p
        #         new_dp[remain_i] = min(new_dp[remain_i], dp[remain_prev] + 1)
        #     dp = new_dp
        #     ans = min(ans, dp[NEED_SUM])
        # if ans == inf or ans == N:
        #     return -1
        # return ans

        # N = len(nums)
        # NEED_SUM = sum(nums) % p
        # if NEED_SUM == 0:
        #     return 0
        # dp: List[int] = [inf] * p
        # ans = inf
        # for i, x in enumerate(nums):
        #     new_dp = [inf] * p
        #     new_dp[x % p] = 1
        #     for remain_prev in range(p):
        #         remain_i = (remain_prev + x) % p
        #         new_dp[remain_i] = min(new_dp[remain_i], dp[remain_prev] + 1)
        #     dp = new_dp
        #     ans = min(ans, dp[NEED_SUM])
        # if ans == inf or ans == N:
        #     return -1
        # return ans

        # N = len(nums)
        # NEED_SUM = sum(nums) % p
        # if NEED_SUM == 0:
        #     return 0
        # # dp[i][remain] =
        # dp: List[List[int]] = [[inf] * p for _ in range(N)]
        # ans = inf
        # for i, x in enumerate(nums):
        #     dp[i][x % p] = 1
        #     for remain_prev in range(p):
        #         remain_i = (remain_prev + x) % p
        #         dp[i][remain_i] = min(dp[i][remain_i], dp[i - 1][remain_prev] + 1)
        #     ans = min(ans, dp[i][NEED_SUM])
        # if ans == inf or ans == N:
        #     return -1
        # return ans


if __name__ == '__main__':
    print(Solution().minSubarray([1, 2, 3], 3))
    # print(Solution().minSubarray([6, 3, 5, 2], 9))
    # print(Solution().minSubarray([3, 1, 4, 2], 6))
