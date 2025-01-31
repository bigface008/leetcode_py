# https://leetcode.com/problems/make-lexicographically-smallest-array-by-swapping-elements/?envType=daily-question&envId=2025-01-25
from collections import defaultdict
from typing import List

import utils


# 1 2 3
# 1 3 2
# 2 3 1
# 3 2 1


class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        N = len(nums)
        seq = [(x, i) for i, x in enumerate(nums)]
        seq.sort()
        i = 0
        ans = [0] * N
        while i < N:
            j = i + 1
            indices = [seq[i][1]]
            values = [seq[i][0]]
            while j < N and abs(seq[j][0] - seq[j - 1][0]) <= limit:
                indices.append(seq[j][1])
                values.append(seq[j][0])
                j += 1
            indices.sort()
            for idx, val in zip(indices, values):
                ans[idx] = val
            i = j
        return ans


class Solution2:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        N = len(nums)
        seq = [(x, i) for i, x in enumerate(nums)]
        seq.sort()
        parents = list(range(N))
        ranks = [0] * N

        def findParent(node: int) -> int:
            while parents[node] != node:
                parents[node] = parents[parents[node]]
                node = parents[node]
            return node

        for i in range(1, N):
            if abs(seq[i][0] - seq[i - 1][0]) <= limit:
                pv = findParent(i)
                pu = findParent(i - 1)
                if pv == pu:
                    continue
                if ranks[pu] > ranks[pv]:
                    parents[i] = pu
                elif ranks[pu] < ranks[pv]:
                    parents[i - 1] = pv
                else:
                    parents[i] = pu
                    ranks[pu] += 1
        ans = [0] * N
        sorted_comp = defaultdict(list)
        for i in range(N):
            pa = parents[i]
            sorted_comp[pa].append(i)
        for k, v in sorted_comp.items():
            indices = [seq[vi][1] for vi in v]
            indices.sort()
            values = [seq[vi][0] for vi in v]
            values.sort()
            for nums_i, val in zip(indices, values):
                ans[nums_i] = val
        return ans


def check(nums: List[int], limit: int, expect: List[int]):
    output = Solution().lexicographicallySmallestArray(nums, limit)
    utils.tst(f'nums={nums} limit={limit}', output, expect)


if __name__ == '__main__':
    check([1, 5, 3, 9, 8], 2, [1, 3, 5, 8, 9])
