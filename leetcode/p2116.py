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
        if N % 2 == 1:
            return False
        lock_stk = []
        free_stk = []
        for i, ch in enumerate(s):
            if locked[i] == '0':
                free_stk.append(i)
            else:
                if ch == '(':
                    lock_stk.append(i)
                else:
                    if lock_stk:
                        lock_stk.pop()
                    elif free_stk:
                        free_stk.pop()
                    else:
                        return False
        while lock_stk and free_stk:
            if lock_stk[-1] > free_stk[-1]:
                return False
            lock_stk.pop()
            free_stk.pop()
        return not lock_stk

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
