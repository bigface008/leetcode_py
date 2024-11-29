from typing import List

import utils


# https://leetcode.com/problems/combination-sum/
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        N = len(candidates)
        candidates.sort()
        ans = []
        group = []

        def dfs(idx: int, target: int):
            if target == 0:
                ans.append(group.copy())
                return
            for i in range(idx, N):
                x = candidates[i]
                if target < x:
                    break
                group.append(x)
                dfs(i, target - x)
                group.pop()

        dfs(0, target)
        return ans


def tst(candidates: List[int], target: int, expect: List[List[int]]):
    output = Solution().combinationSum(candidates, target)
    utils.tst(f'combinationSum {candidates} {target}', output, expect)


if __name__ == '__main__':
    tst([2, 3, 6, 7], 7, [[2, 2, 3], [7]])
