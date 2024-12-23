# https://ivanzz1001.github.io/records/post/data-structure/2018/06/24/ds-red-black-tree
from typing import List, Optional
from enum import Enum

import utils


class Color(Enum):
    BLACK = 0
    RED = 1


class TreeNode:
    def __init__(self, val: int, color: Color):
        self.val = val
        self.is_black = color
        self.right: Optional[TreeNode] = None
        self.left: Optional[TreeNode] = None


class RBTree:
    def __init__(self):
        self.root: Optional[TreeNode] = TreeNode(0, Color.BLACK)


def check1(b1: bool, b2: bool, b3: bool) -> bool:
    # print(f'(b1 and b2) or b3', (b1 and b2) or b3)
    # print(f'b1 and (b2 or b3)', b1 and (b2 or b3))
    v1 = (b1 and b2) or b3
    v2 = b1 and (b2 or b3)
    print(f'({b1} and {b2}) or {b3} == {b1} and ({b2} or {b3})? {v1 == v2}')


def check2(a: bool, b: bool) -> bool:
    c = a or b
    print(f'not {a} and ({a} or {b}) == {c} and not {a}: {(not a and (a or b)) == (c and not a)}')


def check3(nums: List[int], l: int, r: int, prefix: List[int]):
    res = 0
    for i in range(l, r + 1):
        res |= nums[i]
    res2 = prefix[r + 1] & (~prefix[l])
    utils.tst(f'OR({nums[l:r + 1]}) = {res}; prefix[{r}+1] & ~prefix[{l}] == {res2}', res2, res)


if __name__ == '__main__':
    nums = [2, 5, 7]
    N = len(nums)
    prefix = [0] * (N + 1)
    for i in range(N):
        prefix[i + 1] = prefix[i] | nums[i]
    check3(nums, 0, 2, prefix)
    check3(nums, 0, 1, prefix)
    check3(nums, 0, 0, prefix)
    check3(nums, 1, 2, prefix)
    check3(nums, 1, 1, prefix)
    check3(nums, 2, 2, prefix)
