# https://leetcode.cn/problems/balance-a-binary-search-tree/?envType=daily-question&envId=2026-02-09
from typing import Optional, List, Dict

from utils import TreeNode


class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        nodes: List[int] = []

        def dfs1(node: Optional[TreeNode]):
            if node is None:
                return
            dfs1(node.left)
            nodes.append(node.val)
            dfs1(node.right)

        def dfs2(start: int, end: int) -> Optional[TreeNode]:
            if start >= end:
                return None
            mid = (start + end) // 2
            node = TreeNode(nodes[mid])
            node.left = dfs2(start, mid)
            node.right = dfs2(mid + 1, end)
            return node

        dfs1(root)
        return dfs2(0, len(nodes))


if __name__ == "__main__":
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.right = TreeNode(3)
    root.right.right.right = TreeNode(4)
    print(Solution().balanceBST(root))