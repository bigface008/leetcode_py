# https://leetcode.com/problems/minimize-xor/?envType=daily-question&envId=2025-01-15
import utils


class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        N1 = int(num1).bit_count()
        N2 = int(num2).bit_count()
        cnt = 0
        ans = 0
        for b in range(31, -1, -1):
            if num1 & (1 << b) != 0:
                cnt += 1
                ans += 1 << b
            if cnt >= N2:
                break
        if cnt < N2:
            for b in range(32):
                if num1 & (1 << b) == 0:
                    cnt += 1
                    ans += 1 << b
                if cnt >= N2:
                    break
        return ans


def check(num1: int, num2: int, expect: int):
    output = Solution().minimizeXor(num1, num2)
    utils.tst(f'num1={num1} num2={num2}', output, expect)


if __name__ == '__main__':
    check(3, 5, 3)
