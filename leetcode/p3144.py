from collections import defaultdict
from functools import cache
from math import inf

import utils


# https://leetcode.cn/problems/minimum-substring-partition-of-equal-character-frequency/?envType=daily-question&envId=2024-08-28
class Solution:
    def minimumSubstringsInPartition(self, s: str) -> int:
        N = len(s)
        LC = 26
        f = [0] * (N + 1)
        f[0] = 0
        f[1] = 1
        for i in range(1, N):
            res = i + 1
            cnt = defaultdict(int)
            max_cnt = 0
            for j in range(i, -1, -1):
                cnt[s[j]] += 1
                max_cnt = max(max_cnt, cnt[s[j]])
                if max_cnt * len(cnt) == i - j + 1:
                    res = min(res, f[j] + 1)
            f[i + 1] = res
        return f[N]

        # pre_sum = [[0 for _ in range(LC)] for _ in range(N + 1)]
        # each_sum = [0] * LC
        # for i, ch in enumerate(s):
        #     each_sum[ord(ch) - ord('a')] += 1
        #     for j in range(LC):
        #         pre_sum[i + 1][j] = each_sum[j]
        #
        # f = [0] * (N + 1)
        # f[1] = 1
        # for i in range(1, N):
        #     ans = i + 1
        #     for j in range(i, -1, -1):
        #         each_cnt = [0] * LC
        #         cnt = -1
        #         valid = True
        #         for k in range(LC):
        #             v = pre_sum[i + 1][k] - pre_sum[j][k]
        #             each_cnt[k] = v
        #             if v != 0:
        #                 if cnt == -1:
        #                     cnt = v
        #                 elif cnt != v:
        #                     valid = False
        #                     break
        #         if valid:
        #             ans = min(ans, f[j])
        #     f[i + 1] = ans + 1
        # return f[N]

        # @cache
        # def dfs(i: int) -> int:
        #     if i < 0:
        #         return 0
        #     if i == 0:
        #         return 1
        #     ans = i + 1
        #     for j in range(i, -1, -1):
        #         each_cnt = [0] * LC
        #         cnt = -1
        #         valid = True
        #         for k in range(LC):
        #             v = pre_sum[i + 1][k] - pre_sum[j][k]
        #             each_cnt[k] = v
        #             if v != 0:
        #                 if cnt == -1:
        #                     cnt = v
        #                 elif cnt != v:
        #                     valid = False
        #                     break
        #         if valid:
        #             ans = min(ans, dfs(j - 1))
        #     return ans + 1
        #
        # return dfs(N - 1)


class RedBlackTree:
    def __init_(self):
        pass


def tst(s: str, expect: int):
    output = Solution().minimumSubstringsInPartition(s)
    utils.tst(f'min sub s={s}', output, expect)


if __name__ == '__main__':
    tst("fabccddg", 3)
    tst("bb", 3)
