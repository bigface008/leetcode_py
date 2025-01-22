# https://leetcode.com/problems/bitwise-xor-of-all-pairings/?envType=daily-question&envId=2025-01-16
from typing import List


# a0 a1 a2 ... an-1

# b0 b1 b2 ... bn-1

# a0 xor b0, a0 xor b1, a0 ... bn-1
# ...


class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        N = len(nums1)
        M = len(nums2)
        ans = 0
        if M % 2 == 1:
            for x in nums1:
                ans ^= x
        if N % 2 == 1:
            for x in nums2:
                ans ^= x
        return ans


def check1(a: int, b: int, c: int):
    b = (a ^ b) ^ c == a ^ (b ^ c)
    if b:
        print(f'[PASS] a={a} b={b} c={c}')
    else:
        print(f'[FAIL] a={a} b={b} c={c}')


if __name__ == '__main__':
    # check1(3, 2, 1)
    # check1(3, 3, 1)
    # check1(3, 3, 3)
    # check1(2, 3, 1)
    # check1(2, 2, 1)
    # check1(2, 2, 2)
    # check1(1, 2, 3)
    # check1(1, 2, 2)
    # check1(1, 2, 1)
    # check1(1, 1, 1)
    # check1(991, 21, 12)
    # check1(991, 21, 12)
