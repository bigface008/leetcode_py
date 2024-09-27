from functools import cmp_to_key
from typing import List
import bisect

import utils


# https://leetcode.com/problems/largest-number
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        ss = [str(n) for n in nums]

        def f(a: str, b: str) -> int:
            v1 = a + b
            v2 = b + a
            if v1 == v2:
                return 0
            elif v1 < v2:
                return 1
            else:
                return -1

        ss.sort(key=cmp_to_key(f))
        ans = ''.join(ss)
        zero_idx = -1
        for i, ch in enumerate(ans):
            if ch == '0':
                if i == len(ans) - 1:
                    break
                zero_idx = i
            else:
                break
        return ans[zero_idx + 1:]
        # size = sum(len(s) for s in ss)
        # print(ss, size)
        # ans = []
        # ss.sort(key=lambda s:10 - int(s[0]))
        # same_1st_digit_i = -1
        # for i, s in enumerate(ss):
        #     if i + 1 < len(ss) and ss[i + 1][0] == s[0]:
        #         same_1st_digit_i = i
        #         break
        #     else:
        #         ans.append(s)
        #
        # while i < len(ss):
        #     pass
        # while ss:
        #     i = 0
        #     while i < len(ss):
        #         if i + 1 < len(ss) and ss[i][0] == ss[i + 1][0]:
        # for i, s in enumerate(ss):
        #     l, r = 0, len(ans)
        #     while l <= r:
        #         mid = (l + r) // 2
        #         val = ss[mid]
        #         if val[0] == s[0]:
        #
            # bisect.insort_left(ans, s, key=)


# 53 5 4
# 5534

# 4 40 41 53 51 5 6 8 9
# 986

# 9 81 71 6 59

# 32 3 38 -> 38,3,32
# 32 3 31 -> 3,31,32

# 31, 3
# 310, 30
# 3, 31

# 38, 3
# 380 30
# 38, 3


# 337, 32, 3, 38, 309
# 3, 38, 32, 337, 309
    # if a[0] > b[0]:
    #     return 1
    # if a[0] < b[0]:
    #     return -1
    # i, j = 0, 0
    # na, nb = len(a), len(b)
    # while i < na and j < nb:
    #     if a[i] > b[j]:
    #         return 1
    #     elif a[i] < b[j]:
    #         return -1
    #     else:
    #         i += 1
    #         j += 1



def tst(nums: List[int], expect: str):
    output = Solution().largestNumber(nums)
    utils.tst(f'nums={nums}', output, expect)


if __name__ == '__main__':
    # tst([10, 2], '210')
    # tst([3, 30, 34, 5, 9], '9534330')
    print('30' > '3')
    print('30' * 10 > '3' * 10)
    print('31' > '3')
    print('31' * 10 > '3' * 10)
    print('38' > '3')
    print('38' * 10 > '3' * 10)
