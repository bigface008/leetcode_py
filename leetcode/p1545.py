# https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/?envType=daily-question&envId=2024-10-19
import utils


class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def dfs(i: int, k: int) -> int:
            cur_len = pow(2, i) - 1
            half = cur_len // 2
            ans = 0
            if k == half:
                ans = 1 if i != 1 else 0
            elif k < half:
                ans = dfs(i - 1, k)
            else:
                ans = 1 - dfs(i - 1, cur_len - k - 1)
            return ans
        return str(dfs(n, k - 1))


def tst(n: int, k: int, expect: str):
    output = Solution().findKthBit(n, k)
    utils.tst(f'find kth bit n={n} k={k}', output, expect)


if __name__ == '__main__':
    tst(4, 11, '1')