# https://leetcode.com/problems/construct-string-with-repeat-limit/description/?envType=daily-question&envId=2024-12-17
from collections import Counter

import utils


class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        N = len(s)
        counter = [0] * 26
        remain_letter_cnt = N
        for ch in s:
            counter[ord(ch) - ord('a')] += 1
        letters = [[chr(ord('a') + i), cnt] for i, cnt in enumerate(counter) if cnt > 0]
        LN = len(letters)
        ans = ''
        while len(ans) < N and remain_letter_cnt > 0:
            has_higher = False
            for i in range(LN - 1, -1, -1):
                ch, c = letters[i]
                if c == 0:
                    continue
                # if ans:
                #     print(f'ch={ch} c={c} ans={ans} ans[-1]={ans[-1]}cond={ans[-1] }')
                if (not ans) or (ans[-1] != ch):
                    if has_higher:
                        ans += ch
                        letters[i][1] = c - 1
                        remain_letter_cnt -= 1
                    elif c <= repeatLimit:
                        ans += ch * c
                        letters[i][1] = 0
                        remain_letter_cnt -= c
                    else:
                        ans += ch * repeatLimit
                        letters[i][1] = c - repeatLimit
                        remain_letter_cnt -= repeatLimit
                    has_higher = True
                else:
                    continue
                break
        return ans


class Solution2:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        N = len(s)
        counter = [0] * 26
        remain_letter_cnt = N
        for ch in s:
            counter[ord(ch) - ord('a')] += 1
        letters = [[chr(ord('a') + i), cnt] for i, cnt in enumerate(counter) if cnt > 0]
        LN = len(letters)
        ans = ''
        i = LN - 1
        while len(ans) < N and remain_letter_cnt > 0:
            ch, c = letters[i]
            if c != 0 and (not ans or (ans[-1] != c)):
                if c <= repeatLimit:
                    ans += ch * c
                    letters[i][1] = 0
                    remain_letter_cnt -= c
                else:
                    ans += ch * repeatLimit
                    letters[i][1] = c - repeatLimit
                    remain_letter_cnt -= repeatLimit
            i = (i - 1 + LN) % LN
        return ans


def check(s: str, repeatLimit: int, ans: str):
    output = Solution().repeatLimitedString(s, repeatLimit)
    utils.tst(f's={s} repeatLimit={repeatLimit}', output, ans)


if __name__ == '__main__':
    # check('cczazcc', 3, 'zzcccac')
    check('aababab', 2, 'bbabaa')
    # wd = 'aa'
    # print(wd[-1] == 'a')
