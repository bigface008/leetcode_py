# https://leetcode.cn/problems/split-the-array/?envType=daily-question&envId=2024-12-28
from collections import Counter
from typing import List

import utils


class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        cnt = Counter()
        for x in nums:
            cnt[x] += 1
            if cnt[x] >= 3:
                return False
        return True


def solution(nums: List[int]) -> List[int]:
    pass


def check(nums: List[int]):
    print(f'Checking {nums}')
    N = len(nums)
    B = max(nums).bit_length()
    f = [[0] * B for _ in range(N + 1)]
    for i, x in enumerate(nums):
        for b in range(B):
            f[i + 1][b] = f[i][b] + (0 if (x & (1 << b) == 0) else 1)
    for i in range(N):
        for j in range(i + 1, N + 1):
            arr = nums[i:j]
            res = 0
            for x in arr:
                res |= x
            exp = 0
            for b in range(B):
                exp += 0 if f[j][b] - f[i][b] == 0 else (1 << b)
            msg = '[PASSED]' if exp == res else '[FAILED]'
            print(f'{msg} nums[{i}:{j}] = {arr}, res = {res}, expect = {exp}')

# nums[i] ... nums[0] | 0 = f[i + 1]
# nums[j] ... nums[0] | 0 = f[j + 1]
# nums[j] ... nums[i + 1] | f[i + 1] = f[j + 1]
# nums[j] ... nums[i + 1] = f[j + 1] | ~f[i + 1]
# nums[j - 1] ... nums[i] = f[j] | ~f[i]

# f[i + 1][k] = nums[i][k] == 1 + nums[i - 1][k] == 1 + ... + nums[0][k] + 0
# f[j + 1][k] = nums[j][k] == 1 ...
# f[j + 1][k] = nums[j][k] == 1 + ... + nums[i + 1][k] == 1 + f[i + 1][k]
# f[j + 1][k] - f[i + 1][k] = nums[j] ... nums[i + 1]
# f[j][k] - f[i][k] = nums[j - 1] ... nums[i]


if __name__ == '__main__':
    check([1, 2, 3, 4, 5])
    check([5, 4, 3, 2, 1])
    check([4, 2, 9, 22, 13])
    check([81, 22, 0, 13, 91, 18])
    check([0])
