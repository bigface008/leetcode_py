# https://leetcode.cn/problems/number-of-changing-keys/?envType=daily-question&envId=2025-01-07
import utils


class Solution:
    def countKeyChanges(self, s: str) -> int:
        N = len(s)
        ans = 0

        def calc(ch: str) -> int:
            # if ord(ch) >= ord('A'):
            #     return ord(ch) - ord('A')
            # return ord(ch) - ord('a')
            res = 0
            if ord('Z') >= ord(ch) >= ord('A'):
                res = ord(ch) - ord('A')
            else:
                res = ord(ch) - ord('a')
            # print(f'ch={ch} res={res}')
            return res

        for i in range(1, N):
            if calc(s[i]) != calc(s[i - 1]):
                ans += 1
        return ans


def check(s: str, expect: int):
    output = Solution().countKeyChanges(s)
    utils.tst(f's={s}', output ,expect)


if __name__ == '__main__':
    check("aAbBcC", 2)