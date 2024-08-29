import utils
from functools import cache

# i [down, up]
# if curr[i:n] == s[i:n] isPrevMax:
#   up = s[i]
# else:
#   up = 9
# if i == start of num: isStart
#   down = 1
# else:
#   down = 0

# https://leetcode.com/problems/count-special-integers/
class Solution:
    def countSpecialNumbers(self, n: int) -> int:
        s = str(n)

        @cache
        def dfs(i: int, mask: int, isLimit: bool, isNum: bool) -> int:
            if i == len(s):
                return int(isNum)
            res = 0
            if not isNum:
                res = dfs(i + 1, mask, False, False)
            up = int(s[i]) if isLimit else 9
            down = 0 if isNum else 1
            for d in range(down, up + 1):
                if mask >> d & 1 == 0:
                    res += dfs(i + 1, mask | (1 << d), isLimit and d == up, True)
            return res

        return dfs(0, 0, True, False)

        # @cache
        # def dfs(i: int, mask: int, isPrevMax: bool, isStart: bool) -> int:
        #     if i == len(s):
        #         return 0 if isStart else 1
        #     res = 0
        #     if isStart:
        #         res = dfs(i + 1, mask, False, True)
        #     up = int(s[i]) if isPrevMax else 9
        #     down = 1 if isStart else 0
        #     for d in range(down, up + 1):
        #         if (mask >> d) & i == 0:
        #             res += dfs(i + 1, mask | (1 << d), isPrevMax and d == up, False)
        #     return res
        #
        # return dfs(0, 0, True, True)


def tst(n: int, expect: int):
    output = Solution().countSpecialNumbers(n)
    utils.tst(f'count special numbers n={n}', output, expect)


if __name__ == '__main__':
    tst(20, 19)
    tst(5, 5)
    tst(135, 110)