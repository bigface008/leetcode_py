import collections
from typing import Optional
from utils import TreeNode


# https://leetcode.com/problems/cousins-in-binary-tree-ii/?envType=daily-question&envId=2024-10-23
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root
        dq = collections.deque()
        dq.append((root, None))
        parent_mp = {}
        while dq:
            level_size = len(dq)
            level_sum = 0
            level = list(dq)
            for _ in range(level_size):
                node, parent = dq.popleft()
                level_sum += node.val
                if node.left is not None:
                    dq.append((node.left, node))
                if node.right is not None:
                    dq.append((node.right, node))
            for node, parent in level:
                if parent is None:
                    node.val = 0
                    continue
                if parent.left is node:
                    if parent.right is not None:
                        val = level_sum - node.val - parent.right.val
                        node.val = val
                        parent.right.val = val
                    else:
                        node.val = level_sum - node.val
                else:
                    if parent.left is None:
                        node.val = level_sum - node.val
        return root
