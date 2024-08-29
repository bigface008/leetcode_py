from functools import cache
import utils


# dfs(i, s1 & s2) = dfs(i - 1, n1 & n2)
# dfs(i, s1 & n2) = dfs(i - 1, n1 & n2) + dfs(i - 1, n1 & s2)
# dfs(i, n1 & s2) = dfs(i - 1, n1 & n2) + dfs(i - 1, s1 & n2)
# dfs(i, n1 & n2) = dfs(i - 1, n1 & n2) + dfs(i - 1, s1 & s2) + dfs(, s1 & n2) + dfs(, n1 & s2)

# https://leetcode.com/problems/count-number-of-ways-to-place-houses/
class Solution:
    def countHousePlacements(self, n: int) -> int:
        MOD = pow(10, 9) + 7
        f = [0 for _ in range(n + 1)]
        f[0] = 1
        f[1] = 2
        for i in range(2, n + 1):
            f[i] = (f[i - 1] + f[i - 2]) % MOD
        return pow(f[-1], 2) % MOD

        # f = [[0, 0] for _ in range(n)]
        # f[0] = [1, 1]
        # for i in range(1, n):
        #     f[i][0] = (f[i - 1][0] + f[i - 1][1]) % MOD
        #     f[i][1] = f[i - 1][0]
        # return sum(f[-1]) ** 2 % MOD

        # f = [[[0, 0], [0, 0]] for _ in range(n)]
        # f[0] = [[1, 1], [1, 1]]
        # for i in range(1, n):
        #     f[i][1][1] = f[i - 1][0][0]
        #     f[i][1][0] = (f[i - 1][0][1] + f[i - 1][0][0]) % MOD
        #     f[i][0][1] = (f[i - 1][0][0] + f[i - 1][1][0]) % MOD
        #     f[i][0][0] = (f[i - 1][0][0] + f[i - 1][1][1] + f[i - 1][1][0] + f[i - 1][0][1]) % MOD
        # return (sum(f[-1][0]) + sum(f[-1][1])) % MOD

        # @cache
        # def dfs(i: int, select_up: bool, select_down: bool) -> int:
        #     if i < 0:
        #         return 0
        #     if i == 0:
        #         return 1
        #     res = 0
        #     if select_up:
        #         if select_down:
        #             res = dfs(i - 1, False, False)
        #         else:
        #             res = dfs(i - 1, False, True) + dfs(i - 1, False, False)
        #     else:
        #         if select_down:
        #             res = dfs(i - 1, False, False) + dfs(i - 1, True, False)
        #         else:
        #             res = dfs(i - 1, False, False) + dfs(i - 1, True, True) + dfs(i - 1, True, False) + dfs(i - 1, False, True)
        #     return res % MOD
        #
        # ans = dfs(n - 1, True, True) + dfs(n - 1, True, False) + dfs(n - 1, False, True) + dfs(n - 1, False, False)
        # return ans % MOD


def tst(n: int, expect: int):
    output = Solution().countHousePlacements(n)
    utils.tst(f'count house n={n}', output, expect)


if __name__ == '__main__':
    tst(1, 4)
    tst(2, 9)
    tst(3, 25)