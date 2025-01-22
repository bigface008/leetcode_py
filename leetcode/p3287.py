# https://leetcode.cn/problems/find-the-maximum-sequence-value-of-array/?envType=daily-question&envId=2025-01-18
from functools import reduce
from typing import List


class Solution:
    def maxValue(self, nums: List[int], k: int) -> int:
        N = len(nums)
        suf = [set() for _ in range(N - k + 1)]
        f = [set() for _ in range(k + 1)]
        f[0].add(0)
        for i in range(N - 1, k - 1, -1):
            v = nums[i]
            for l in range(min(k, N - i), 0, -1):
                f[l].update(v | x for x in f[l - 1])
            if i <= N - k:
                suf[i] = f[k].copy()

        g = [set() for _ in range(k + 1)]
        g[0].add(0)
        ans = 0
        for i in range(N - k):
            v = nums[i]
            for l in range(min(k, N - i), 0, -1):
                g[l].update(v | x for x in g[l - 1])
            if i >= k - 1:
                for x in g[k]:
                    for y in suf[i + 1]:
                        ans = max(ans, x ^ y)
        return ans



class Solution2:
    def maxValue(self, nums: List[int], k: int) -> int:
        N = len(nums)
        mx = reduce(lambda x, y: x | y, nums)
        suf = [None] * (N - k + 1)
        f = [[False] * (mx + 1) for _ in range(k + 1)]
        f[0][0] = True
        for i in range(N - 1, k - 1, -1):
            v = nums[i]
            for j in range(min(k - 1, N - 1 - i), -1, -1):
                for x, has_x in enumerate(f[j]):
                    if has_x:
                        f[j + 1][x | v] = True
            if i <= N - k:
                suf[i] = f[k].copy()

        ans = 0
        pre = [[False] * (mx + 1) for _ in range(k + 1)]
        pre[0][0] = True
        for i, v in enumerate(nums[:-k]):
            for j in range(min(k - 1, i), -1, -1):
                for x, has_x in enumerate(pre[j]):
                    if has_x:
                        pre[j + 1][x | v] = True
                if i < k - 1:
                    continue
                for x, has_x in enumerate(pre[k]):
                    if has_x:
                        for y, has_y in enumerate(suf[i + 1]):
                            if has_y and x ^ y > ans:
                                ans = x ^ y
            if ans == mx:
                return ans
        return ans


        # N = len(nums)
        # B = max(nums).bit_length()
        # f = [[0] * B for _ in range(N + 1)]
        # for i, x in enumerate(nums):
        #     for b in range(B):
        #         f[i + 1][b] = f[i][b] + (0 if (x & (1 << b) == 0) else 1)
        # start, end = 0, 2 * k - 1
        # ans = 0
        # while end < N:
        #     p1, p2 = 0, 0
        #     for b in range(B):
        #         if f[start + k][b] - f[start][b] != 0:
        #             p1 |= 1 << b
        #         if f[end + 1][b] - f[start + k][b] != 0:
        #             p2 |= 1 << b
        #     ans = max(ans, p1 ^ p2)
        #     start += 1
        #     end += 1
        # return ans