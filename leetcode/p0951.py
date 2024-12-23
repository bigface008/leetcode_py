# https://leetcode.cn/problems/flip-equivalent-binary-trees/
from typing import Optional
from utils import TreeNode


class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        def dfs(r1: Optional[TreeNode], r2: Optional[TreeNode]) -> bool:
            if not r1 and not r2:
                return True
            if not r1 or not r2:
                return False
            if r1.val != r2.val:
                return False
            if dfs(r1.left, r2.left) and dfs(r1.right, r2.right):
                return True
            if dfs(r1.left, r2.right) and dfs(r1.right, r2.left):
                return True
            return False

        return dfs(root1, root2)
