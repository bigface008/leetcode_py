# https://leetcode.com/problems/parsing-a-boolean-expression/?envType=daily-question&envId=2024-10-20
import utils


class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        N = len(expression)

        def parse(expr: str, left: int, right: int) -> bool:
            # print(f'left={left} right={right}')
            if left == right:
                return expr[left] == 't'
            if expr[left] == '!' and expr[right] == ')':
                return not parse(expr, left + 2, right - 1)
            stk_cnt = 0
            last_start = left + 2
            is_and = expr[left] == '&'
            res = is_and
            i = left + 2
            while i <= right:
                ch = expr[i]
                if (ch == ',' and stk_cnt == 0) or i == right:
                    if parse(expr, last_start, i - 1):
                        if not is_and:
                            res = True
                            break
                    else:
                        if is_and:
                            res = False
                            break
                    last_start = i + 1
                elif ch == '(':
                    stk_cnt += 1
                elif ch == ')':
                    stk_cnt -= 1
                i += 1
            return res

        return parse(expression, 0, N - 1)


def tst(expression: str, expect: bool):
    output = Solution().parseBoolExpr(expression)
    utils.tst(f'parse bool expr={expression}', output, expect)


if __name__ == '__main__':
    # tst("&(|(f))", False)
    tst("!(&(f,t))", True)
