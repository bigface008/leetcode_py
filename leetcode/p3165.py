# https://leetcode.com/problems/maximum-sum-of-subsequence-with-non-adjacent-elements/
from typing import List


class Solution:
    def maximumSumSubsequence(self, nums: List[int], queries: List[List[int]]) -> int:
        N = len(nums)
        MOD = pow(10, 9) + 7
        t = [[0] * 4 for _ in range(2 << N.bit_length())]
        ans = 0

        def build(o: int, l: int, r: int):
            if l == r:
                t[o][3] = max(nums[l], 0)
                return
            m = (l + r) // 2
            build(o * 2, l, m)
            build(o * 2 + 1, m + 1, r)
            maintain(o)

        def update(o: int, l: int, r: int, idx: int, val: int):
            if l == r:
                t[o][3] = max(val, 0)
                return
            m = (l + r) // 2
            if idx <= m:
                update(o * 2, l, m, idx, val)
            else:
                update(o * 2 + 1, m + 1, r, idx, val)
            maintain(o)

        def maintain(o: int):
            a = t[o * 2]
            b = t[o * 2 + 1]
            t[o][0] = max(a[1] + b[0], a[0] + b[2])
            t[o][1] = max(a[1] + b[1], a[0] + b[3])
            t[o][2] = max(a[3] + b[0], a[2] + b[2])
            t[o][3] = max(a[2] + b[3], a[3] + b[1])

        build(1, 0, N - 1)
        for q in queries:
            update(1, 0, N - 1, q[0], q[1])
            ans = (ans + t[1][3]) % MOD
        return ans
