# https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/?envType=daily-question&envId=2025-01-06
import bisect
from itertools import accumulate
from typing import List


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        N = len(boxes)
        indices = []
        for i, ch in enumerate(boxes):
            if ch == '1':
                indices.append(i)
        pre_sum = list(accumulate(indices, initial=0))
        ans = [0] * N
        for i in range(N):
            pos = bisect.bisect_left(indices, i)
            left = pos * i - (pre_sum[pos] - pre_sum[0])
            right = pre_sum[-1] - pre_sum[pos] - (len(indices) - pos) * i
            ans[i] = left + right
        return ans