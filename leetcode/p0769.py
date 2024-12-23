# https://leetcode.com/problems/max-chunks-to-make-sorted/description/?envType=daily-question&envId=2024-12-19
from typing import List
from math import inf
from functools import cache

import utils


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        N = len(arr)
        min_arr = [inf] * N
        max_arr = [-inf] * N
        for i, x in enumerate(arr):
            if i > 0:
                min_arr[i] = min(min_arr[i - 1], x)
                max_arr[i] = max(max_arr[i - 1], x)
            else:
                min_arr[i] = max_arr[i] = x

        @cache
        def dfs(idx: int) -> int:
            min_val = arr[idx]
            max_val = arr[idx]
            ans = 1
            for i in range(idx, -1, -1):
                x = arr[i]
                min_val = min(min_val, x)
                max_val = max(max_val, x)
                if i > 0 and min_val >= max_arr[i - 1]:
                    ans = max(ans, 1 + dfs(i - 1))
                    break
            # print(f'idx={idx}, ans={ans}')
            return ans

        return dfs(N - 1)


def check(arr: List[int], expect: int):
    output = Solution().maxChunksToSorted(arr)
    utils.tst(f'{arr}', output, expect)


if __name__ == '__main__':
    check([1,0,2,3,4], 4)
    check([4,3,2,1,0], 1)
    check([0, 2, 1], 2)
