# https://leetcode.cn/problems/sort-integers-by-the-power-value/description/?envType=daily-question&envId=2024-12-22
from heapq import nlargest, nsmallest


class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:

        def weight(x: int) -> int:
            res = 0
            while x != 1:
                if x % 2 == 0:
                    x //= 2
                else:
                    x = 3 * x + 1
                res += 1
            return res


        return nsmallest(k, range(lo, hi + 1), key=lambda num: weight(num))[-1]