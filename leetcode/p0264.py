import bisect
import heapq
from typing import List

import utils


# https://leetcode.com/problems/ugly-number-ii/description/?envType=daily-question&envId=2024-08-18
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        minHeap = [1]
        seen = {1}
        factors = (2, 3, 5)
        curr = 1
        for i in range(n):
            curr = heapq.heappop(minHeap)
            for f in factors:
                tmp = curr * f
                if tmp not in seen:
                    heapq.heappush(minHeap, tmp)
                    seen.add(tmp)
        return curr



def tst(n: int, expect: int):
    output = Solution().nthUglyNumber(n)
    utils.tst(f'nth ugly num n={n}', output, expect)


if __name__ == '__main__':
    tst(10, 12)
    tst(1, 1)
    tst(4, 4)
    tst(8, 9)