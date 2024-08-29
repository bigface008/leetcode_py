# https://leetcode.com/problems/fraction-addition-and-subtraction/?envType=daily-question&envId=2024-08-23
import utils


class Solution:
    def fractionAddition(self, expression: str) -> str:
        frac = [] # (num, deno)
        op = [] # +, -
        start = 0
        N = len(expression)
        if expression[0] == '-':
            op.append('-')
            start = 1
        else:
            op.append('+')
        i = start
        while i < N:
            ch = expression[i]
            if ch.isdigit():
                d = int(ch)
                if i + 1 < N and expression[i + 1].isdigit():
                    d = int(expression[i: i + 2])
                    i += 1
                if not frac:
                    frac.append([d])
                else:
                    if len(frac[-1]) == 1:
                        frac[-1].append(d)
                    else:
                        frac.append([d])
            elif ch == '/':
                pass
            elif ch == '+' or ch == '-':
                op.append(ch)
            i += 1
        prod = 1
        for f in frac:
            prod *= f[1]
        num = 0
        for i, f in enumerate(frac):
            tmp = f[0] * prod / f[1]
            if op[i] == '+':
                num += tmp
            else:
                num -= tmp

        def gcd(a: int, b: int) -> int:
            while b != 0:
                a, b = b, a % b
            return a

        g = gcd(abs(num), prod)
        return f'{int(num / g)}/{int(prod / g)}'


def tst(expression: str, expect: str) -> bool:
    output = Solution().fractionAddition(expression)
    utils.tst(f'frac add sub expr={expression}', output, expect)


if __name__ == '__main__':
    # tst("-1/2+1/2+1/3", "1/3")
    # tst("1/3-1/2", "-1/6")
    pass