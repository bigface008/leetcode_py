import utils
from functools import cache


# https://leetcode.cn/problems/find-all-possible-stable-binary-arrays-i/description/
class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 10 ** 9 + 7

        @cache
        def dfs(zero_cnt: int, one_cnt: int, last: int) -> int:
            if zero_cnt == 0 and one_cnt == 0:
                return 0
            if zero_cnt < 0 or one_cnt < 0:
                return 0
            if zero_cnt == 0:
                if last == 1 and one_cnt <= limit:
                    return 1
                else:
                    return 0
            if one_cnt == 0:
                if last == 0 and zero_cnt <= limit:
                    return 1
                else:
                    return 0
            ans = 0
            if last == 0:
                ans = dfs(zero_cnt - 1, one_cnt, 0) + dfs(zero_cnt - 1, one_cnt, 1) - (dfs(zero_cnt - limit - 1, one_cnt, 1) if zero_cnt > limit else 0)
            else:
                ans = dfs(zero_cnt, one_cnt - 1, 0) + dfs(zero_cnt, one_cnt - 1, 1) - (dfs(zero_cnt, one_cnt - limit - 1, 0) if one_cnt > limit else 0)
            return ans % MOD

        ans = (dfs(zero, one, 1) + dfs(zero, one, 0)) % MOD
        dfs.cache_clear()
        return ans


def tst(zero, one, limit, expect):
    sol = Solution()
    output = sol.numberOfStableArrays(zero, one, limit)
    utils.tst(f'number of stable arrays zero={zero} one={one} limit={limit}', output, expect)


if __name__ == '__main__':
    tst(1, 1, 2, 2)
    tst(1, 2, 1, 1)
    tst(3, 3, 2, 14)
