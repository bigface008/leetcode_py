from typing import List
from functools import cache
from math import inf


# https://leetcode.com/problems/longest-path-with-different-adjacent-characters/description/
class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        ans = 0
        N = len(parent)
        tree = [[] for _ in range(N)]
        for i in range(1, N):
            tree[parent[i]].append(i)

        @cache
        def dfs(nodeIdx: int):
            nonlocal ans
            nodeLen = 0
            for childIdx in tree[nodeIdx]:
                childLen = dfs(childIdx) + 1
                if s[nodeIdx] != s[childIdx]:
                    ans = max(ans, nodeLen + childLen)
                    nodeLen = max(nodeLen, childLen)
            return nodeLen
        dfs(0)
        return ans + 1


if __name__ == '__main__':
    print(2 ^ 1)