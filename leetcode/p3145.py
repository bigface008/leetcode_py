from typing import List
from functools import cache

from IPython.utils.tz import utcnow

import utils


# https://leetcode.cn/problems/find-products-of-elements-of-big-array/?envType=daily-question&envId=2024-08-23
class Solution:
    def findProductsOfElements(self, queries: List[List[int]]) -> List[int]:
        maxTo = 0
        for q in queries:
            if q[1] > maxTo:
                maxTo = q[1]

        bigNum = [1]
        num = 2
        while len(bigNum) < maxTo + 1:
            i = 0
            while (num >> i) > 0:
                tmp = (num >> i) & 1
                if tmp == 1:
                    bigNum.append(tmp << i)
                i += 1
            num += 1

        ans = []
        for q in queries:
            prod = 1
            l, r, mod = q
            for i in range(l, r + 1):
                prod *= bigNum[i]
                prod %= mod
            ans.append(prod)
        return ans


def tst(queries: List[List[int]], expect: List[int]):
    output = Solution().findProductsOfElements(queries)
    utils.tst(f'find products queries={queries}', output, expect)


if __name__ == '__main__':
    tst([[1, 3, 7]], [4])
    tst([[2, 5, 3], [7, 7, 4]], [2, 2])
