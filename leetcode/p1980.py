# https://leetcode.cn/problems/find-unique-binary-string/?envType=daily-question&envId=2026-03-08
from typing import List, Dict, Tuple, Set, Optional


# class PrefixTreeNode:
#     def __init__(self):
#         self.is_leaf = False
#         self.left: Optional[PrefixTreeNode] = None
#         self.right: Optional[PrefixTreeNode] = None
#
#
# class PrefixTree:
#     def __init__(self, N: int):
#         self.N = N
#         self.root: Optional[PrefixTreeNode] = None
#
#     def insert(self, num_str: str) -> None:
#         node = self.root
#         for ch in num_str:
#             v = int(ch)
#             if v == 0:
#                 if not node.left:
#                     node.left = PrefixTreeNode()
#                 node = node.left
#             elif v == 1:
#                 if not node.right:
#                     node.right = PrefixTreeNode()
#                 node = node.right
#         node.is_leaf = True
#
#     def generate(self) -> List[int]:
#         res: List[int] = []
#         group: List[int] = []
#
#         def backtrack(node: Optional[PrefixTreeNode]) -> None:
#             if node.left and not node.right:
#                 group.append(0)
#                 backtrack(node.left)



class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        st = {int(s, 2) for s in nums}
        ans = 0
        while ans in st:
            ans += 1
        return f"{ans:0{len(nums)}b}"