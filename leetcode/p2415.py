# https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/description/?envType=daily-question&envId=2024-12-20
from collections import deque
from typing import Optional
from utils import TreeNode


class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        dq = deque()
        dq.append(root)
        level = 0
        while dq:
            odd = level % 2 != 0
            level_size = len(dq)
            if odd:
                values = [0] * level_size
                nodes = [None] * level_size
            for i in range(level_size):
                node = dq.popleft()
                if odd:
                    values[i] = node.val
                    nodes[i] = node
                if node.left is not None:
                    dq.append(node.left)
                if node.right is not None:
                    dq.append(node.right)

            if odd:
                for i in range(level_size):
                    nodes[i].val = values[level_size - 1 - i]
            level += 1
        return root


        # def dfs(node: Optional[TreeNode], level: int) -> Optional[TreeNode]:
        #     if node is None:
        #         return node
        #     if level % 2 == 0:
        #         left = dfs(node.left, level + 1)
        #         right = dfs(node.right, level + 1)
        #         if left is not None:
        #             vl, vr = left.val, right.val
        #             node.right.val = vl
        #             node.left.val = vr
        #         node.right = left
        #         node.left = right
        #
        #     else:
        #         dfs(node.left, level + 1)
        #         dfs(node.right, level + 1)
        #     return node
        #
        # return dfs(root, 0)


def check(root: TreeNode):
    output = Solution().reverseOddLevels(root)
    pass


if __name__ == '__main__':
    t = TreeNode()
    t.val = 2
    t.right = TreeNode()
    t.right.val = 5
    t.left = TreeNode()
    t.left.val = 3
    t.right.right = TreeNode()
    t.right.right.val = 34
    t.right.left = TreeNode()
    t.right.left.val = 21
    t.left.right = TreeNode()
    t.left.right.val = 13
    t.left.left = TreeNode()
    t.left.left.val = 8
    check(t)