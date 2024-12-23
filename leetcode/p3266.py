# https://leetcode.cn/problems/final-array-state-after-k-multiplication-operations-ii/?envType=daily-question&envId=2024-12-14
import heapq
from typing import List

import utils

class Solution2:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        pass


class Solution2:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        if multiplier == 1:  # 数组不变
            return nums

        MOD = 1_000_000_007
        n = len(nums)
        mx = max(nums)
        h = [(x, i) for i, x in enumerate(nums)]
        heapq.heapify(h)

        # 模拟，直到堆顶是 mx
        while k and h[0][0] < mx:
            x, i = h[0]
            heapq.heapreplace(h, (x * multiplier, i))
            k -= 1

        # 剩余的操作可以直接用公式计算
        h.sort()
        for i, (x, j) in enumerate(h):
            nums[j] = x * pow(multiplier, k // n + (i < k % n), MOD) % MOD
        return nums


def check(nums: List[int], k: int, multiplier: int, expect: List[int]):
    output = Solution().getFinalState(nums, k, multiplier)
    utils.tst(f'getFinalState({nums}, {k}, {multiplier})', output, expect)


if __name__ == '__main__':
    # check([161209470], 56851412, 39846, [0])
    i = 10
    k = 11
    n = 2
    print(i < k % n)