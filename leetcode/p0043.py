# https://leetcode.com/problems/multiply-strings/
from collections import defaultdict

import utils


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1[0] == '0' or num2[0] == '0':
            return '0'
        N1, N2 = len(num1), len(num2)
        i, j = 0, 0
        mp = defaultdict(int)  # pos -> digit
        for i, x in enumerate(num1):
            for j, y in enumerate(num2):
                prod = int(x) * int(y)
                zero_cnt = (N1 - i - 1) + (N2 - j - 1)
                d = prod
                k = zero_cnt
                while d > 0:
                    d = mp[k] + d
                    mp[k] = d % 10
                    k += 1
                    d //= 10
        keys = sorted(mp)
        max_pos = max(keys) + 1
        ans = ['0'] * max_pos
        for k in keys:
            ans[max_pos - k - 1] = str(mp[k])
        return ''.join(ans)


def tst(num1: str, num2: str, expect: str):
    output = Solution().multiply(num1, num2)
    utils.tst(f'multiply num1={num1} num2={num2}', output, expect)


if __name__ == '__main__':
    tst('2', '3', '6')
    tst('123', '456', '56088')
