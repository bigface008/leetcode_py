# https://leetcode.com/problems/check-if-a-parentheses-string-can-be-valid/description/?envType=daily-question&envId=2025-01-12
import utils


class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        N = len(s)
        if N % 2 == 1:
            return False
        x = 0
        for i in range(N):
            if s[i] == '(' or locked[i] == '0':
                x += 1
            elif x > 0:
                x -= 1
            else:
                return False
        x = 0
        for i in range(N - 1, -1, -1):
            if s[i] == ')' or locked[i] == '0':
                x += 1
            elif x > 0:
                x -= 1
            else:
                return False
        return True



class Solution2:
    def canBeValid(self, s: str, locked: str) -> bool:
        N = len(s)
        if N // 2 == 1:
            return False
        stk = 0
        open_cnt = 0
        for i in range(N):
            ch = s[i]
            lock = locked[i] == 1
            if ch == '(':
                stk += 1
                open_cnt += 1
                if open_cnt > N // 2:
                    if lock:
                        return False
                    open_cnt -= 1
                    stk -= 2
            else:
                stk -= 1
                if stk < 0:
                    if lock:
                        return False
                    stk += 2
        return stk == 0

# ))()))
# 010100

# -1

# ( ) ( ) ( )
# 1 0 1 0 1 0

def check(s: str, locked: str, expect: bool):
    output = Solution().canBeValid(s, locked)
    utils.tst(f's={s} locked={locked}', output, expect)


if __name__ == '__main__':
    check(')', '0', False)
