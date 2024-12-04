from utils import TreeNode
from typing import Optional, Tuple
from math import inf


def solution(root: Optional[TreeNode]) -> int:
    ans = -inf

    def dfs(node: Optional[TreeNode]) -> Tuple[int, int]:
        if node is None:
            return (0, 0)
        curr = node.val
        left1, left2 = dfs(node.left)
        right1, right2 = dfs(node.right)
        res = (curr + max(left1, left2), curr + max(right1, right2))
        nonlocal ans
        ans = max(ans, res[0] + res[1] - curr)
        return res

    dfs(root)
    return ans


def tst(root: Optional[TreeNode], expect: int):
    print(solution(root) == expect)


if __name__ == '__main__':
    t1 = TreeNode(1)
    t1.left = TreeNode(2)
    t1.right = TreeNode(3)
    tst(t1, 6)

    t2 = TreeNode(10)
    t2.left = TreeNode(2)
    t2.left.left = TreeNode(20)
    t2.left.right = TreeNode(1)
    t2.right = TreeNode(10)
    t2.right.right = TreeNode(-25)
    t2.right.right.left = TreeNode(3)
    t2.right.right.right = TreeNode(4)
    tst(t2, 42)
