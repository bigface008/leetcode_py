from collections import defaultdict
from typing import List

import utils


# https://leetcode.com/problems/xor-queries-of-a-subarray/?envType=daily-question&envId=2024-09-13
class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        LQ = len(queries)
        N = len(arr)
        ans = [0] * LQ
        pre_xor = [0] * (N + 1)
        xor = 0
        for i, x in enumerate(arr):
            xor ^= x
            pre_xor[i + 1] = xor
        for i, q in enumerate(queries):
            l, r = q
            ans[i] = pre_xor[r + 1] ^ pre_xor[l]
        return ans


def tst(arr: List[int], queries: List[List[int]], expect: List[int]):
    output = Solution().xorQueries(arr, queries)
    utils.tst(f'xorQueries arr={arr} queries={queries}', output, expect)


if __name__ == '__main__':
    tst([1, 3, 4, 8], [[0, 1], [1, 2], [0, 3], [3, 3]], [2, 7, 14, 8])
