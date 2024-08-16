from functools import cache
from typing import List


# https://leetcode.com/problems/edit-distance/description/

# dfs(i, j) =
# if w1[i] == w2[j]:
#   dfs(i-1, j-1)
# else:
#   min(dfs(i-1, j-1), dfs(i, j-1), dfs(i-1,j)) + 1


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @cache
        def dfs(i: int, j: int) -> int:
            if i < 0:
                return j + 1
            if j < 0:
                return i + 1
            if word1[i] == word2[j]:
                return dfs(i - 1, j - 1)
            else:
                return min(dfs(i - 1, j - 1), dfs(i, j - 1), dfs(i - 1, j)) + 1

        return dfs(len(word1) - 1, len(word2) - 1)
