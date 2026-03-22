# https://leetcode.cn/problems/fancy-sequence/?envType=daily-question&envId=2026-03-15
from typing import List, Tuple


# a1, m1, a2, m2, ...
# (t + a1) * m1 = m1 * t1 + m1 * a1 + a2
# m1 * m2 * t1 + m1 * m2 * a1 + m2 * a2

class Fancy:

    def __init__(self):
        self.nums: List[Tuple[int, int]] = [] # num, completed_op_idx
        self.op_arr: List[Tuple[bool, int]] = [] # is_add, num, len
        self.MOD = pow(10, 9) + 7

    def append(self, val: int) -> None:
        self.nums.append((val, len(self.op_arr) - 1))

    def addAll(self, inc: int) -> None:
        self.op_arr.append((True, inc))


    def multAll(self, m: int) -> None:
        self.op_arr.append((False, m))

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.nums):
            return -1
        num, completed_op_idx = self.nums[idx]
        for op_idx in range(completed_op_idx + 1, len(self.op_arr)):
            is_add, op_num = self.op_arr[op_idx]
            if is_add:
                num += op_num
            else:
                num *= op_num
        self.nums[idx] = (num, len(self.op_arr) - 1)
        return num % self.MOD


if __name__ == "__main__":
    f = Fancy()
    f.append(2)
    f.addAll(3)
    f.append(7)
    f.multAll(2)
    print(f.getIndex(0))