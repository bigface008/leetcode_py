# 给定一个数组（怪兽），和一个初始值
# 从左到右，每遇到一个怪兽，如果大于当前值，则把当前值减一
# 如果等于当前值，不动，继续遍历
# 如果小于当前值，把当前值加一
# 求，要求最后的值大于初始值，最小的初始值是多少？
# [1, 2, 3, 4, 5] -> 2

from typing import List
from functools import cache

import utils


def valid(x: int, nums: List[int]) -> bool:
    tmp = x
    for n in nums:
        if x > n:
            x += 1
        elif x < n:
            x -= 1
    return x > tmp


def solution1(nums: List[int]) -> int:
    l, r = min(nums), max(nums)
    ans = 0
    while l <= r:
        mid = (l + r) // 2
        if valid(mid, nums):
            r = mid - 1
            ans = mid
        else:
            l = mid + 1
    return ans


def solution2(nums: List[int]) -> int:
    n = len(nums)
    dp = [0] * n
    dp[0] = nums[0]

    for i in range(1, n):
        if dp[i - 1] < nums[i]:
            dp[i] = dp[i - 1] + 1
        else:
            dp[i] = nums[i]

    return dp[-1]


# dfs(i)表示考虑从i开始到结尾的所有值时对应的最小初始值
# 对于所有的dfs(i)和dfs(i+1)对，dfs(i)越小，dfs(i+1)一定不会变大，即有单调性，所以得到了dfs(i+1)，就一定对应了dfs(i)
# 那么分类讨论，
# - 当dfs(i + 1) == nums[i]，dfs(i)必定是等于nums[i]的，
# - 当小于，dfs(i)必定也是小于的，所以dfs(i) = dfs(i+1) + 1；
# - 大于同理，得到dfs(i) = dfs(i + 1) - 1。
# 对应边界情况，即i==N-1，肯定就是最后一个数加一
def solution(nums: List[int]) -> int:
    N = len(nums)
    f = [0] * N
    f[N - 1] = nums[-1] + 1
    for i in range(N - 2, -1, -1):
        next = f[i + 1]
        x = nums[i]
        tmp = 0
        if next == x:
            tmp = next
        elif next == x + 1:
            tmp = next
        elif next > x + 1:
            tmp = next - 1
        else:
            tmp = next + 1
        f[i] = tmp
    return f[0]


    # @cache
    # def dfs(i: int):
    #     if i == N - 1:
    #         return nums[-1] + 1
    #     next = dfs(i + 1)
    #     x = nums[i]
    #     if next == x:
    #         return next
    #     elif next == x + 1:
    #         return next
    #     elif next > x + 1:
    #         return next - 1
    #     else:
    #         return next + 1
    # return dfs(0)


def solution3(nums: List[int]) -> int:
    N = len(nums)

    @cache
    def dfs(i: int, j: int) -> int:
        if
        return min(dfs(i - 1, j + 1) + 1, max(dfs(i - 1, j), nums[N - i]), max(dfs(i - 1, j - 1), nums[N - i] + 1))


def tst(nums: List[int], expect: int):
    output = solution(nums)
    # p = 'PASSED' if output == expect else 'FAILED'
    # print(f'[{p}] nums={nums} output={output} expect={expect}')
    utils.tst(f'test nums={nums}', output, expect)


if __name__ == '__main__':
    tst([1, 2, 3, 4, 5], 2)
    tst([3, 1, 4, 1, 5, 9, 2, 6], 3)
    tst([5, 4, 3, 2, 1], 5)
    tst([5, 0, 0, 0, 0], 1)
