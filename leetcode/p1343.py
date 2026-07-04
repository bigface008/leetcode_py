# https://leetcode.cn/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/
from typing import List, Dict, Tuple


class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        N = len(arr)
        T = threshold * k
        total = 0
        for i in range(k):
            if i < N:
                total += arr[i]
        ans = 0 if total < T else 1
        for i in range(k, N):
            total = total + arr[i] - arr[i-k]
            if total >= T:
                ans += 1
        return ans
