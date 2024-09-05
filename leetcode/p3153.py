from collections import defaultdict
from typing import List


# https://leetcode.cn/problems/sum-of-digit-differences-of-all-pairs/?envType=daily-question&envId=2024-08-30
class Solution:
    def sumDigitDifferences(self, nums: List[int]) -> int:
        N = len(nums)
        CNT = len(str(nums[0]))
        ans = 0
        pos_num_cnt = [[0 for _ in range(10)] for _ in range(CNT)]
        for n in nums:
            pos = 0
            while n > 0:
                pos_num_cnt[pos][n % 10] += 1
                n //= 10
                pos += 1

        for pos, dic in enumerate(pos_num_cnt):
            for n1, cnt1 in enumerate(dic):
                for n2 in range(n1 + 1, 10):
                    ans += cnt1 * dic[n2]
        return ans

        # for i in range(N):
        #     for j in range(i + 1, N):
        #         a, b = str(nums[i]), str(nums[j])
        #         for k in range(CNT):
        #             if a[k] != b[k]:
        #                 ans += 1
        # return ans