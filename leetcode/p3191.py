from typing import List


# https://leetcode.cn/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-i
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        N = len(nums)
        for i in range(N):
            d = nums[i]
            if d == 0:
                if i + 2 < N:
                    nums[i] = 1
                    nums[i + 1] = 1 - nums[i + 1]
                    nums[i + 2] = 1 - nums[i + 2]
                    ans += 1
                else:
                    return -1
        return ans


