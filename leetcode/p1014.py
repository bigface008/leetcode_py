from typing import List


# https://leetcode.cn/problems/best-sightseeing-pair/description/?envType=daily-question&envId=2024-09-23
class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        N = len(values)
        ans = 0
        mxi = values[0]
        for i in range(1, N):
            tmp = mxi + values[i] - i
            ans = max(ans, tmp)
            mxi = max(mxi, i + values[i])
        return ans
        # for i in range(N):
        #     for j in range(i + 1, N):
        #         ans = max(ans, values[i] + values[j] + i - j)
        # return ans
