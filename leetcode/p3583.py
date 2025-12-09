# https://leetcode.com/problems/count-special-triplets/?envType=daily-question&envId=2025-12-09
from typing import List, Dict, Optional, Tuple
from collections import defaultdict


class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        N = len(nums)
        MOD = pow(10, 9) + 7
        num_to_count = defaultdict(int)
        j_to_i_cnt = [0] * N
        j_to_k_cnt = [0] * N
        ans = 0
        for pos, x in enumerate(nums):
            double = 2 * x
            if double in num_to_count:
                j_to_i_cnt[pos] += num_to_count[double]
            num_to_count[x] += 1
        num_to_count = defaultdict(int)
        for pos in range(N - 1, -1, -1):
            x = nums[pos]
            double = 2 * x
            if double in num_to_count:
                j_to_k_cnt[pos] += num_to_count[double]
            num_to_count[x] += 1
        for i in range(N):
            ans += j_to_k_cnt[i] * j_to_i_cnt[i]
            ans %= MOD
        return ans

        # num_to_pos = defaultdict(list)
        # j_to_i_cnt = defaultdict(int)
        # j_to_k_cnt = defaultdict(int)
        # ans = 0
        # for pos, x in enumerate(nums):
        #     double = 2 * x
        #     if double in num_to_pos:
        #         j_to_i_cnt[pos] += len(num_to_pos[double])
        #     if x % 2 == 0:
        #         half = x // 2
        #         if half in num_to_pos:
        #             for pos_j in num_to_pos[half]:
        #                 j_to_k_cnt[pos_j] += 1
        #     num_to_pos[x].append(pos)
        # for val_j, cnt_i in j_to_i_cnt.items():
        #     if val_j in j_to_k_cnt:
        #         ans += j_to_k_cnt[val_j] * cnt_i
        # return ans
