# https://leetcode.cn/problems/maximum-score-of-a-good-subarray/
import bisect
from typing import List

import utils


class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        N = len(nums)
        N1, N2 = k + 1, N - k
        min_arr1 = [0] * N1
        min_arr1[-1] = nums[k]
        for i in range(k - 1, -1, -1):
            min_arr1[i] = min(min_arr1[i + 1], nums[i])
        min_arr2 = [0] * N2
        min_arr2[0] = nums[k]
        for i in range(k + 1, N):
            min_arr2[i - k] = min(min_arr2[i - k - 1], nums[i])

        ans = 0
        i, j = k, k
        # for i in range(k, -1, -1):
        while i >= 0:
            x = min_arr1[i]
            if i - 1 >= 0 and x == min_arr1[i - 1]:
                i -= 1
                continue
            j = bisect.bisect_left(range(k, N), True, key=lambda idx: min_arr2[idx - k] < x) + k - 1
            dist = j - i + 1
            score = x * dist
            ans = max(ans, score)
            i -= 1
        i, j = k, k
        while j < N:
            x = min_arr2[j - k]
            if j + 1 < N and x == min_arr2[j + 1 - k]:
                j += 1
                continue
            i = bisect.bisect_left(range(0, k + 1), True, key=lambda idx: min_arr1[idx] >= x)
            dist = j - i + 1
            score = x * dist
            ans = max(ans, score)
            j += 1
        return ans


def check(nums: List[int], k: int, expect: int):
    output = Solution().maximumScore(nums, k)
    utils.tst(f'nums={nums} k={k}', output, expect)


if __name__ == '__main__':
    # check([1, 4, 3, 7, 4, 5], 3, 15)
    # check([5, 5, 4, 5, 4, 1, 1, 1], 0, 20)
    check([8182, 1273, 9847, 6230, 52, 1467, 6062, 726, 4852, 4507, 2460, 2041, 500, 1025, 5524], 8, 9014)
