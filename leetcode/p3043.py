from typing import List, Optional

import utils


# https://leetcode.com/problems/find-the-length-of-the-longest-common-prefix
class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        seen = set()
        for x in arr1:
            while x > 0:
                seen.add(x)
                x //= 10

        ans = 0
        for x in arr2:
            while x > 0:
                if x in seen:
                    ans = max(ans, len(str(x)))
                    break
                x //= 10
        return ans

        # t1 = PrefixTree()
        # for x in arr1:
        #     t1.addValue(x)
        # t2 = PrefixTree()
        # for x in arr2:
        #     t2.addValue(x)
        #
        # def dfs(node1: Optional[Node], node2: Optional[Node]) -> int:
        #     if node1 is None or node2 is None:
        #         return 0
        #     if node1.val != node2.val:
        #         return 0
        #     ans = 0
        #     for i in range(10):
        #         tmp = dfs(node1.children[i], node2.children[i])
        #         ans = max(tmp + 1, ans)
        #     return ans
        #
        # return dfs(t1.root, t2.root) - 1


class Node:
    def __init__(self, val: int):
        self.val = val
        self.children: List[Optional[Node]] = [None] * 10
        self.isNum = False


class PrefixTree:
    def __init__(self):
        self.root = Node(0)

    def addValue(self, val: int):
        s = str(val)
        p = self.root
        for i, ch in enumerate(s):
            x = int(ch)
            if p.children[x] is None:
                p.children[x] = Node(x)
            p = p.children[x]
        p.isNum = True

    def findValue(self, val: int) -> bool:
        s = str(val)
        p = self.root
        for i, ch in enumerate(s):
            x = int(ch)
            if p.children[x] is None:
                return False
            p = p.children[x]
        return p.isNum


def tst(arr1: List[int], arr2: List[int], expect: int):
    output = Solution().longestCommonPrefix(arr1, arr2)
    utils.tst(f'longest common prefix arr1={arr1} arr2={arr2}', output, expect)


if __name__ == '__main__':
    tst([1, 10, 100], [1000], 3)
