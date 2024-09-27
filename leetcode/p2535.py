from typing import List


# https://leetcode.cn/problems/difference-between-element-sum-and-digit-sum-of-an-array
class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        s1 = sum(nums)
        s2 = 0
        for x in nums:
            tmp = 0
            while x > 0:
                tmp += x % 10
                x //= 10
            s2 += tmp
        return abs(s1 - s2)