# https://leetcode.com/problems/neighboring-bitwise-xor/?envType=daily-question&envId=2025-01-17
from functools import reduce
from typing import List


class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        return reduce(lambda a, b: a ^ b, derived) == 0



class Solution2:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        N = len(derived)
        origin = [0] * N
        for i in range(1, N):
            if derived[i - 1] == 0:
                origin[i] = origin[i - 1]
            else:
                origin[i] = 1 - origin[i - 1]
        if derived[-1] == 1:
            return origin[0] != origin[-1]
        else:
            return origin[0] == origin[-1]