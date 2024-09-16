from typing import List


# https://leetcode.com/problems/first-missing-positive/
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        N = len(nums)
        for i in range(N):
            if nums[i] <= 0:
                nums[i] = N + 1

        for i in range(N):
            x = abs(nums[i])
            if x <= N:
                nums[x - 1] = -abs(nums[x - 1])

        for i in range(N):
            if nums[i] > 0:
                return i + 1

        return N + 1
