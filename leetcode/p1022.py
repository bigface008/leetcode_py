# https://leetcode.cn/problems/sum-of-root-to-leaf-binary-numbers/?envType=daily-question&envId=2026-02-24
from typing import Optional
from utils import TreeNode


class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def dfs(node: Optional[TreeNode], above_value: int):
            if node is None:
                return
            new_value = (above_value << 1) + node.val
            if node.left is None and node.right is None:
                nonlocal ans
                ans += new_value
                return
            dfs(node.left, new_value)
            dfs(node.right, new_value)

        dfs(root, 0)
        return ans


        # ans = 0
        #
        # def dfs(node: Optional[TreeNode], above_value: int):
        #     if node is None:
        #         nonlocal ans
        #         ans += above_value
        #         return
        #     new_value = (above_value << 1) + node.val
        #     dfs(node.left, new_value)
        #     dfs(node.right, new_value)
        #
        # dfs(root, 0)
        # return ans


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(1)
    root.right = TreeNode(1)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(1)
    print(Solution().sumRootToLeaf(root))
