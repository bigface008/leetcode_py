# https://leetcode.com/problems/valid-number/
import utils


class Solution:
    def isNumber(self, s: str) -> bool:
        N = len(s)

        def isInt(s: str) -> bool:
            for ch in s:
                if not ch.isnumeric():
                    return False
            return True

        def isIntWithOp(s: str) -> bool:
            if s == '':
                return True
            ch0 = s[0]
            if ch0 == '+' or ch0 == '-':
                return isInt(s[1:]) and len(s) != 1
            else:
                return isInt(s)

        ei = s.rfind('e')
        Ei = s.rfind('E')
        if ei == -1 and Ei != -1:
            ei = Ei
        e_follow = ''
        if ei != -1:
            if ei + 1 >= N:
                return False
            e_follow = s[(ei + 1):]
            if not isIntWithOp(e_follow):
                return False
            if ei == 0:
                return False

        if ei == -1:
            ei = len(s)

        doti = s.rfind('.', 0, ei)
        dot_follow = ''
        if doti != -1:
            dot_follow = s[doti + 1:ei]
            if not isInt(dot_follow):
                return False
            if doti == 0:
                if dot_follow == '':
                    return False
                return True

        if doti == -1:
            start = s[:ei]
        else:
            start = s[:doti]
            if start == '' and doti == N - 1:
                return False
        ch0 = start[0]
        if ch0.isnumeric():
            pass
        elif ch0 == '+' or ch0 == '-':
            start = start[1:]
        else:
            return False

        if start == '' and dot_follow == '':
            return False
        return isInt(start)


def check(s: str, expect: bool):
    output = Solution().isNumber(s)
    utils.tst(s, output, expect)


if __name__ == '__main__':
    # check('0', True)
    # check('e', False)
    # check('.9', True)
    # check('e9', False)
    # check('9.', True)
    # check('.', False)
    # check('+.', False)
    # check('+.8', True)
    # check('005047e+6', True)
    # check('4e+', False)
    check('1E9', True)