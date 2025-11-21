# https://leetcode.cn/problems/most-beautiful-item-for-each-query/?envType=daily-question&envId=2025-03-09
from typing import List
import bisect

import utils


class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        N = len(items)
        Q = len(queries)
        ans = []
        items.sort(key=lambda x: x[0])
        max_beauty = [0] * N
        mx_b = 0
        for i, (price, beauty) in enumerate(items):
            max_beauty[i] = max(beauty, mx_b)
            mx_b = max_beauty[i]
        for i, query in enumerate(queries):
            j = bisect.bisect_left(range(N), True, key=lambda idx: items[idx][0] > query)
            if j > 0:
                ans.append(max_beauty[j - 1])
            else:
                ans.append(0)
        return ans


def check(items: List[List[int]], queries: List[int], expect: List[int]):
    actual = Solution().maximumBeauty(items, queries)
    utils.tst(f'items={items} queries={queries}', actual, expect)


if __name__ == '__main__':
    check([[1, 2], [3, 2], [2, 4], [5, 6], [3, 5]], [1, 2, 3, 4, 5, 6], [2, 4, 5, 5, 6, 6])
