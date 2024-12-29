# https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/?envType=daily-question&envId=2024-12-28
from itertools import accumulate
from typing import List
from math import inf

import utils


class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        N = len(nums)
        CNT = N - k + 1
        pre_sum = list(accumulate(nums, initial=0))
        left_arr = [[pre_sum[k] - pre_sum[0], 0] for _ in range(CNT)]
        for i in range(1, CNT):
            curr = pre_sum[i + k] - pre_sum[i]
            if left_arr[i - 1][0] < curr:
                left_arr[i] = [curr, i]
            else:
                left_arr[i] = left_arr[i - 1].copy()
        right_arr = [[pre_sum[CNT - 1 + k] - pre_sum[CNT - 1], CNT - 1] for _ in range(CNT)]
        for i in range(CNT - 2, -1, -1):
            curr = pre_sum[i + k] - pre_sum[i]
            if right_arr[i + 1][0] <= curr:
                right_arr[i] = [curr, i]
            else:
                right_arr[i] = right_arr[i + 1].copy()

        max_sum = -inf
        ans = (0, 0, 0)
        for i in range(k, CNT - k):
            curr = pre_sum[i + k] - pre_sum[i]
            prev_max = left_arr[i - k][0]
            next_max = right_arr[i + k][0]
            temp = curr + prev_max + next_max
            if temp > max_sum:
                max_sum = temp
                ans = (left_arr[i - k][1], i, right_arr[i + k][1])
        return ans


def check(nums: List[int], k: int, expect: List[int]) -> None:
    output = Solution().maxSumOfThreeSubarrays(nums, k)
    utils.tst(f'{nums}, {k}', output, expect)


if __name__ == '__main__':
    check([1,2,1,2,1,2,1,2,1], 2, [0, 2, 4])
