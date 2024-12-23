# https://leetcode.com/problems/maximum-number-of-integers-to-choose-from-a-range-i/description/?envType=daily-question&envId=2024-12-06
from typing import List

import utils


class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        ban_st = set(banned)
        valid_nums = []
        for x in range(1, n + 1):
            if x not in ban_st:
                valid_nums.append(x)
        cnt = 0
        ss = 0
        for x in valid_nums:
            cnt += 1
            ss += x
            if ss > maxSum:
                break
        return cnt - 1 if ss > maxSum else cnt


def check(banned: List[int], n: int, maxSum: int, expect: int):
    output = Solution().maxCount(banned, n, maxSum)
    utils.tst(f'banned={banned} n={n} maxSum={maxSum}', output, expect)


if __name__ == '__main__':
    check([1, 6, 5], 5, 6, 2)
