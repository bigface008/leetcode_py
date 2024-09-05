from typing import List


# dfs(i, select, cnt) =
# if i == N

# https://leetcode.cn/problems/happy-students/?envType=daily-question&envId=2024-09-04
class Solution:
    def countWays(self, nums: List[int]) -> int:
        N = len(nums)
        nums.sort()
        ans = 1 if nums[0] > 0 else 0
        for i in range(N - 1):
            if nums[i] < i + 1 < nums[i + 1]:
                ans += 1
        return ans + 1

