# https://leetcode.cn/problems/balanced-binary-tree/?envType=daily-question&envId=2026-02-08
from typing import Optional, Tuple
from utils import TreeNode


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(node: Optional[TreeNode]) -> Tuple[int, bool]:
            if node is None:
                return 0, True
            height_left, res_left = dfs(node.left)
            if not res_left:
                return 0, False
            height_right, res_right = dfs(node.right)
            if not res_right:
                return 0, False
            if abs(height_right - height_left) > 1:
                return 0, False
            return max(height_right, height_left) + 1, True

        return dfs(root)[1]


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(3)
    root.left.left.left = TreeNode(4)
    root.left.left.right = TreeNode(4)
    print(Solution().isBalanced(root))