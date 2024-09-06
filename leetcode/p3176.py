from typing import List
from functools import cache

import utils


# https://leetcode.cn/problems/find-the-maximum-length-of-a-good-subsequence-i/description/?envType=daily-question&envId=2024-09-06
class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        N = len(nums)
        ret = 0

        @cache
        def dfs(i: int, diff_cnt: int) -> int:
            nonlocal ret
            if i == 0:
                return 1
            ans = 1
            # ans = max(1, dfs(i - 1, diff_cnt))
            for pos in range(i):
                if nums[pos] == nums[i]:
                    ans = max(ans, dfs(pos, diff_cnt) + 1)
                else:
                    if diff_cnt >= 1:
                        ans = max(ans, dfs(pos, diff_cnt - 1) + 1)
            return ans

        # dfs(N - 1, k)
        for i in range(N):
            ret = max(ret, dfs(i, k))
        return ret


class Solution2:
    def maximumLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        f = [[1] * (k + 1) for _ in range(n)]
        ans = 0
        for i, x in enumerate(nums):
            for h in range(k + 1):
                for j, y in enumerate(nums[:i]):
                    if x == y:
                        f[i][h] = max(f[i][h], f[j][h] + 1)
                    elif h:
                        f[i][h] = max(f[i][h], f[j][h - 1] + 1)
            ans = max(ans, f[i][k])
        for i in range(n):
            for mk in range(k + 1):
                print(f'i={i} k={mk} f={f[i][mk]}')
        return ans

# right
# i=0 k=0 f=1
# i=1 k=0 f=2
# i=2 k=0 f=1
# i=3 k=0 f=2

# wrong1
# i=1, diff_cnt=0, ans=2
# i=2, diff_cnt=0, ans=2
# i=3, diff_cnt=0, ans=3


# class Solution:
#     def maximumLength(self, nums: List[int], k: int) -> int:
#         N = len(nums)
#         ans = 0
#
#         @cache
#         def dfs(i: int, diff_cnt: int) -> int:
#             if i == 0:
#                 return 1
#             ans = max(1, dfs(i - 1, diff_cnt))
#             for pos in range(i):
#                 if nums[pos] == nums[i]:
#                     ans = max(ans, dfs(pos, diff_cnt) + 1)
#                 else:
#                     if diff_cnt >= 1:
#                         ans = max(ans, dfs(pos, diff_cnt - 1) + 1)
#             print(f'i={i}, diff_cnt={diff_cnt}, ans={ans}')
#             return ans
#
#         return dfs(N - 1, k)


def tst(nums: List[int], k: int, expect: int):
    output = Solution().maximumLength(nums, k)
    utils.tst(nums, output, expect)


if __name__ == '__main__':
    # tst([1, 2, 1, 1, 3], 2, 4)
    # tst([1, 17], 0, 1)

    # right
    # i = 0; k = 0; f = 1
    # i = 1; k = 0; f = 2
    # i = 2; k = 0; f = 1
    # wrong
    # i=2, diff_cnt=0, ans=1
    tst([30, 30, 29], 0, 2)


    tst([39, 39, 38, 38], 0, 2)
    # tst([39, 39, 38, 38], 0, 2)
    # tst([1, 2, 3, 4, 5, 1], 0, 2)
