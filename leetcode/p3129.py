import utils


# https://leetcode.cn/problems/find-all-possible-stable-binary-arrays-i/description/
class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        return 0


def tst(zero, one, limit, expect):
    sol = Solution()
    output = sol.numberOfStableArrays(zero, one, limit)
    utils.tst(f'number of stable arrays zero={zero} one={one} limit={limit}', output, expect)


if __name__ == '__main__':
    tst(1, 1, 2, 2)
    tst(1, 2, 1, 1)
    tst(3, 3, 2, 14)
