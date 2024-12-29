# https://leetcode.cn/problems/flip-columns-for-maximum-number-of-equal-rows/description/
from typing import List
from collections import Counter

import utils


class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        cnt = Counter()
        for row in matrix:
            if row[0]:
                for j in range(len(row)):
                    row[j] ^= 1
            cnt[tuple(row)] += 1
        return max(cnt.values())


def check(matrix: List[List[int]], expect: int):
    output = Solution().maxEqualRowsAfterFlips(matrix)
    utils.tst(f'matrix={matrix}', output, expect)


if __name__ == '__main__':
    check([[0, 0, 0], [0, 0, 1], [1, 1, 0]], 2)
