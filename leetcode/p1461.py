# https://leetcode.cn/problems/check-if-a-string-contains-all-binary-codes-of-size-k/description/
import utils

class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        N = len(s)
        target = pow(2, k)
        if N < target:
            return False

        found = set()
        for i in range(k - 1, N):
            found.add(s[i - k + 1:i + 1])
        return len(found) == target


class Solution2:
    def hasAllCodes(self, s: str, k: int) -> bool:
        N = len(s)
        found = 0
        target = pow(2, k) - 1

        win_val = int(s[:k], 2)
        print(f'win_val={win_val}')
        found |= win_val
        for i in range(k, N):
            curr = int(s[i])
            prev = int(s[i - k])
            win_val = ((win_val - (prev << (k - 1))) << 1) + curr
            found |= win_val
            print(f'i={i} win_val={win_val} found={found}')
        return found == target


def tst(s: str, k: int, expect: bool):
    output = Solution().hasAllCodes(s, k)
    utils.tst(f's={s} k={k}', output, expect)


if __name__ == '__main__':
    # tst('00110110', 2, True)
    tst('0110', 2, False)
