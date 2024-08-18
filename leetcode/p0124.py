from typing import Optional
from utils import TreeNode
from functools import cache
from math import inf


# https://leetcode.com/problems/binary-tree-maximum-path-sum/
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = -inf

        def dfs(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0
            leftMaxSum = dfs(node.left) if node.left is not None else 0
            rightMaxSum = dfs(node.right) if node.right is not None else 0
            nonlocal ans
            ans = max(ans, leftMaxSum + rightMaxSum + node.val, leftMaxSum + node.val, rightMaxSum + node.val, node.val)
            return max(leftMaxSum, rightMaxSum, 0) + node.val

        dfs(root)
        return ans
