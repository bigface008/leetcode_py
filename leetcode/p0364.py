# https://leetcode.cn/problems/nested-list-weight-sum-ii/
from typing import List


class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        res, level_sum = 0, 0
        while nestedList:
            next_level = []
            for n in nestedList:
                if n.isInteger():
                    level_sum += n.getInteger()
                else:
                    next_level.extend(n.getList())
            nestedList = next_level
            res += level_sum
        return res


# class Solution:
#     def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
#         max_depth = 1
#
#         def dfs1(ni: NestedInteger, level: int):
#             nonlocal max_depth
#             if ni.isInteger():
#                 max_depth = max(max_depth, level)
#                 return
#             for x in ni.getList():
#                 dfs1(x, level + 1)
#
#         for x in nestedList:
#             dfs1(x, 1)
#
#         def dfs(ni: NestedInteger, level: int) -> int:
#             if ni.isInteger():
#                 return ni.getInteger() * (max_depth - level + 1)
#             ans = 0
#             for x in ni.getList():
#                 ans += dfs(x, level + 1)
#             return ans
#
#         return sum(dfs(x, 1) for x in nestedList)


class NestedInteger:
   def __init__(self, value=None):
       """
       If value is not specified, initializes an empty list.
       Otherwise initializes a single integer equal to value.
       """

   def isInteger(self):
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       :rtype bool
       """

   def add(self, elem):
       """
       Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
       :rtype void
       """

   def setInteger(self, value):
       """
       Set this NestedInteger to hold a single integer equal to value.
       :rtype void
       """

   def getInteger(self):
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       :rtype int
       """

   def getList(self):
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       :rtype List[NestedInteger]
       """


