from typing import Optional
from utils import TreeNode
from functools import cache


# https://leetcode.com/problems/diameter-of-binary-tree/
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(root: Optional[TreeNode]) -> int:
            if root is None:
                return -1
            l_left = dfs(root.left)
            l_right = dfs(root.right)
            nonlocal ans
            ans = max(ans, l_left + l_right + 2)
            return max(l_left, l_right) + 1
        dfs(root)
        return ans