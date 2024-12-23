# https://leetcode.com/problems/make-string-a-subsequence-using-cyclic-increments/?envType=daily-question&envId=2024-12-04
from functools import cache

import utils


class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        N1, N2 = len(str1), len(str2)
        if N1 < N2:
            return False

        i2 = 0
        for i1, ch1 in enumerate(str1):
            ch2 = str2[i2]
            if ch2 == ch1 or (ord(ch1) - ord('a') + 1) % 26 == ord(ch2) - ord('a'):
                i2 += 1
                if i2 == N2:
                    return True
        return False
        # @cache
        # def dfs(i1: int, i2: int) -> bool:
        #     if i2 == 0 and i1 >= 0:
        #         return True
        #     if i2 != 0 and i1 == 0:
        #         return False
        #     ch1 = str1[i1 - 1]
        #     ch2 = str2[i2 - 1]
        #     if ch1 == ch2:
        #         return dfs(i1 - 1, i2 - 1)
        #     elif (ord(ch1) - ord('a') + 1) % 26 == ord(ch2) - ord('a'):
        #         return dfs(i1 - 1, i2 - 1) or dfs(i1 - 1, i2)
        #     else:
        #         return dfs(i1 - 1, i2)
        #
        # return dfs(N1, N2)

        # dp = [False] * (N2 + 1)
        # dp[0] = True
        # for i1 in range(1, N1 + 1):
        #     dp[0] = True
        #     for i2 in range(1, N2 + 1):
        #         ch1 = str1[i1 - 1]
        #         ch2 = str2[i2 - 1]
        #         res = False
        #         if ch1 == ch2:
        #             res = dp[i2 - 1]
        #         elif (ord(ch1) - ord('a') + 1) % 26 == ord(ch2) - ord('a'):
        #             res = dp[i2 - 1] or dp[i2]
        #         else:
        #             res = dp[i2]
        #         dp[i2] = res
        # return dp[N2]


def tst(str1: str, str2: str, expect: bool):
    output = Solution().canMakeSubsequence(str1, str2)
    utils.tst(f'str1={str1} str2={str2}', output, expect)


if __name__ == '__main__':
    tst('om', 'nm', False)
