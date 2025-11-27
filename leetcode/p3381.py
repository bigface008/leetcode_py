# https://leetcode.com/problems/maximum-subarray-sum-with-length-divisible-by-k
from typing import List, Dict, Tuple, Optional
from math import inf


# dp[i] = dp[i - 1] + x if x > 0 else x
# res = max(res, dp[i])

# nums[a] ... nums[b] = pre_sum[b] - pre_sum[a - 1]

# nums[i * k + j] ... nums[(i + 1) * k - 1 + j]
# dp[i][j] = dp[i - 1][j] + pre_sum[(i + 1) * k - 1 + j] - (pre_sum[i * k + j - 1] if i * k + j - 1 >= 0 else 0)
# res[j] = max(res[j], dp[i][j])
# ans = max(ans, res[j])

# 0 <= j <= k-1

class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        N = len(nums)
        ans = -inf
        div = N // k
        pre_sum = [0] * (div + 1) * k
        for i, x in enumerate(nums):
            pre_sum[i] = (pre_sum[i - 1] + x) if i != 0 else x
        for i in range(N, (div + 1) * k):
            pre_sum[i] = pre_sum[i - 1]

        dp = [[0] * k for _ in range(div)]
        for j in range(k):
            div = (N - j) // k
            for i in range(div):
                x = pre_sum[(i + 1) * k - 1 + j] - (pre_sum[i * k + j - 1] if (i * k + j - 1 >= 0) else 0)
                dp[i][j] = dp[i - 1][j] + x if dp[i - 1][j] >= 0 else x
                ans = max(ans, dp[i][j])
        return ans


# class Solution:
#     def maxSubarraySum(self, nums: List[int], k: int) -> int:
#         N = len(nums)
#         ans = -inf
#         if k == 1:
#             dp = [0] * N
#             dp[0] = nums[0]
#             ans = dp[0]
#             for i in range(1, N):
#                 x = nums[i]
#                 dp[i] = (dp[i - 1] + x) if x >= 0 else x
#                 ans = max(ans, dp[i])
#             return ans
#         div = N // k
#         pre_sum = [0] * (div + 1) * k
#         for i, x in enumerate(nums):
#             pre_sum[i] = (pre_sum[i - 1] + x) if i != 0 else x
#         for i in range(N, (div + 1) * k):
#             pre_sum[i] = pre_sum[i - 1]
#
#         dp = [[0] * k for _ in range(div)]
#         for j in range(k):
#             div = (N - j) // k
#             for i in range(div):
#                 x = pre_sum[(i + 1) * k - 1 + j] - (pre_sum[i * k + j - 1] if (i * k + j - 1 >= 0) else 0)
#                 dp[i][j] = dp[i - 1][j] + x if x >= 0 else x
#                 ans = max(ans, dp[i][j])
#         # for row in dp:
#         #     row
#         return ans


if __name__ == '__main__':
    Solution().maxSubarraySum([-10, 4], 1)
    # Solution().maxSubarraySum([-1, -2, -3, -4, -5], 4)
