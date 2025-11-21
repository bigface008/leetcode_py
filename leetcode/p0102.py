# https://leetcode.cn/problems/binary-tree-level-order-traversal/
import collections
from typing import Optional, List
from utils import TreeNode


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if root is None:
            return ans
        dq = collections.deque()
        dq.append(root)
        while dq:
            level_size = len(dq)
            level = []
            for _ in range(level_size):
                node = dq.popleft()
                level.append(node.val)
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            ans.append(level)
        return ans