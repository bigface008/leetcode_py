# https://leetcode.com/problems/minimum-pair-removal-to-sort-array-i/?envType=daily-question&envId=2026-01-22
from typing import List, Tuple
from math import inf


# min_sum=b+c
#       i
# a     b     c     d
# a+b   b+c   c+d   d+x


# a           b+c   d
# a+b+c       b+c+d d+x
class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        ans = 0
        N = len(nums)
        pair_sum = [0] * (N - 1)
        min_idx = -1
        min_sum = inf
        for i in range(N - 1):
            pair_sum[i] = nums[i] + nums[i + 1]
            if pair_sum[i] < min_sum:
                min_sum = pair_sum[i]
                min_idx = i

        def update_min():
            N = len(nums)
            nonlocal min_idx
            nonlocal min_sum
            min_idx = -1
            min_sum = inf
            for i in range(N - 1):
                if pair_sum[i] < min_sum:
                    min_sum = pair_sum[i]
                    min_idx = i

        def is_valid(arr: List[int]) -> bool:
            N = len(arr)
            for i in range(N - 1):
                if arr[i] > arr[i + 1]:
                    return False
            return True

        while not is_valid(nums):
            ans += 1
            N = len(nums)
            if min_idx - 1 >= 0:
                pair_sum[min_idx - 1] = nums[min_idx - 1] + min_sum
            if min_idx + 2 < N:
                pair_sum[min_idx + 1] = min_sum + nums[min_idx + 2]
            nums[min_idx + 1] = min_sum
            del pair_sum[min_idx]
            del nums[min_idx]
            update_min()

        return ans


if __name__ == '__main__':
    print(Solution().minimumPairRemoval([5, 2, 3, 1]))
