from typing import Optional

from holoviews import output

import utils
from utils import ListNode, TreeNode


# https://leetcode.com/problems/linked-list-in-binary-tree/?envType=daily-question&envId=2024-09-07
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:

        def dfs1(node: Optional[TreeNode]) -> bool:
            if not node:
                return False
            if node.val == head.val and dfs2(node, head):
                return True
            return dfs1(node.left) or dfs1(node.right)

        def dfs2(node: Optional[TreeNode], list_node: Optional[ListNode]) -> bool:
            if (not node and not list_node) or (node and not list_node):
                return True
            if not node and list_node:
                return False
            if node.val != list_node.val:
                return False
            return dfs2(node.left, list_node.next) or dfs2(node.right, list_node.next)

        return dfs1(root)


def tst():
    root = TreeNode(1)
    root.left = TreeNode(4)
    root.right = TreeNode(4)
    root.left.right = TreeNode(2)
    root.left.right.left = TreeNode(1)
    root.right.left = TreeNode(2)
    root.right.left.left = TreeNode(6)
    root.right.left.right = TreeNode(8)
    root.right.left.right.left = TreeNode(1)
    root.right.left.right.right = TreeNode(3)
    head = ListNode(4)
    head.next = ListNode(2)
    head.next.next = ListNode(8)
    utils.tst(f'test', Solution().isSubPath(head, root), True)


if __name__ == '__main__':
    tst()
