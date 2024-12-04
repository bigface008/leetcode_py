from math import inf
from functools import cache


def solution(s: str, t: str) -> str:

    @cache
    def dfs(i1: int, i2: int) -> int:
        if s[i1] != t[i2]:
            return inf
        if i2 == 0:
            return 1
        if i1 == 0:
            return inf
        prev2 = t[i2 - 1]
        res = inf
        for i in range(i1):
            ch = s[i]
            if ch == prev2:
                res = min(res, dfs(i, i2 - 1) + i1 - i)
        return res

    ans = inf
    ans_s = ''
    for i, ch in enumerate(s):
        if ch == t[-1]:
            size = dfs(i, len(t) - 1)
            print(f'i={i} size={size}')
            if size < ans:
                ans_s = s[i - size + 1:i + 1]
                ans = size
    return ans_s


def tst(s: str, t: str, expect: str):
    output = solution(s, t)
    print(f'output={output} expect={expect}')


if __name__ == '__main__':
    tst("abcdebdde", "bde", "bcde")
