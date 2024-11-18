from typing import List
from functools import cache


# Knapsack on a tree. You are given a tree of n vertices. Every vertex
# has a positive weight wi (a real number). Your goal is to choose a subset of vertices
# such that no two vertices are connected by an edge, and maximize the weight of the
# vertices you choose. Give a linear time O(n) algorithm for that.
def solution(tree: List[List[int]]) -> int:

    @cache
    def dfs(node: int, select: bool) -> int:
        pass

    return max(dfs(0, True), dfs(0, False))