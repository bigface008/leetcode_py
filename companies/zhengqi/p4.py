import utils
from utils import TreeNode
from typing import Optional


def solution(root: Optional[TreeNode], low: int, high: int):
    if root is None:
        return 0
    ans = 0

    def dfs(node: Optional[TreeNode]) -> int:
        nonlocal ans
        if node is None:
            return 0
        curr = node.val
        if low <= curr <= high:
            ans += curr
            dfs(node.left)
            dfs(node.right)
        elif curr < low:
            dfs(node.right)
        else:
            dfs(node.left)

    dfs(root)
    return ans


def tst(root: Optional[TreeNode], low: int, high: int, expect: int):
    output = solution(root, low, high)
    print(f'ouput={output} expect={expect}')


if __name__ == '__main__':
    t1 = TreeNode(10)
    t1.left = TreeNode(5)
    t1.left.left = TreeNode(3)
    t1.left.right = TreeNode(7)
    t1.right = TreeNode(15)
    t1.right.right = TreeNode(18)
    tst(t1, 7, 15, 32)

    t2 = TreeNode(10)
    t2.left = TreeNode(5)
    t2.left.left = TreeNode(3)
    t2.left.left.left = TreeNode(1)
    t2.left.right = TreeNode(7)
    t2.left.right.left = TreeNode(6)
    t2.right = TreeNode(15)
    t2.right.left = TreeNode(13)
    t2.right.right = TreeNode(18)
    tst(t2, 6, 10, 23)

