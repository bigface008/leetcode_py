# https://leetcode.com/problems/find-the-number-of-distinct-colors-among-the-balls/?envType=daily-question&envId=2025-02-07
from collections import defaultdict
from typing import List


class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        Q = len(queries)
        counter = defaultdict(int)
        labels = defaultdict(int)
        ans = [0] * Q
        for i, (x, y) in enumerate(queries):
            if x in labels:
                color_x = labels[x]
                counter[color_x] -= 1
                if color_x != y and counter[color_x] == 0:
                    del counter[color_x]
            labels[x] = y
            counter[y] += 1
            ans[i] = len(counter)
        return ans