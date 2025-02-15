# https://leetcode.cn/problems/nested-list-weight-sum/
from typing import List


class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:

        def dfs(ni: NestedInteger, level: int) -> int:
            if ni.isInteger():
                return ni.getInteger() * level
            ans = 0
            for x in ni.getList():
                ans += dfs(x, level + 1)
            return ans

        return sum(dfs(x, 1) for x in nestedList)


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