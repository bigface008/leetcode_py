from typing import List


# https://leetcode.cn/problems/partition-to-k-equal-sum-subsets/?envType=daily-question&envId=2024-08-25
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        target = sum(nums)
        if target % k != 0:
            return False
        target /= k
        nums.sort(reverse=True)
        N = len(nums)
        group_sums = [0 for _ in range(k)]

        def dfs(idx: int) -> bool:
            if idx == N:
                return True
            for i in range(k):
                if i != 0 and group_sums[i] == group_sums[i - 1]:
                    continue
                if group_sums[i] + nums[idx] > target:
                    continue
                group_sums[i] += nums[idx]
                if dfs(idx + 1):
                    return True
                group_sums[i] -= nums[idx]
            return False

        return dfs(0)

