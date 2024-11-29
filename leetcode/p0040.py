from typing import List
import utils
from collections import defaultdict


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        N = len(candidates)
        candidates.sort()
        ans = []
        path = []

        def dfs(idx: int, target: int):
            if target < 0:
                return
            if target == 0:
                ans.append(path.copy())
                return
            for i in range(idx, N):
                x = candidates[i]
                if i > idx and candidates[i - 1] == x:
                    continue
                if target < x:
                    break
                path.append(x)
                dfs(i + 1, target - x)
                path.pop()

        dfs(0, target)
        return ans


# class Solution:
#     def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
#         candidates.sort()
#         ans = []
#         path = []
#
#         def backtrack(start: int, sum: int):
#             if sum > target:
#                 return
#             if sum == target:
#                 ans.append(path.copy())
#             for i in range(start, len(candidates)):
#                 cand = candidates[i]
#                 if sum + cand > target:
#                     return
#                 if i > start and candidates[i - 1] == cand:
#                     continue
#                 sum += cand
#                 path.append(cand)
#                 backtrack(i + 1, sum)
#                 path.pop()
#                 sum -= cand
#
#         backtrack(0, 0)
#         return ans


class Solution2:
    def __init__(self):
        self.paths = []
        self.path = []

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        '''
        类似于求三数之和，求四数之和，为了避免重复组合，需要提前进行数组排序
        '''
        self.paths.clear()
        self.path.clear()
        # 必须提前进行数组排序，避免重复
        candidates.sort()
        self.backtracking(candidates, target, 0, 0)
        return self.paths

    def backtracking(self, candidates: List[int], target: int, sum_: int, start_index: int) -> None:
        # Base Case
        if sum_ == target:
            self.paths.append(self.path[:])
            return

        # 单层递归逻辑
        for i in range(start_index, len(candidates)):
            # 剪枝，同39.组合总和
            if sum_ + candidates[i] > target:
                return

            # 跳过同一树层使用过的元素
            if i > start_index and candidates[i] == candidates[i - 1]:
                continue

            sum_ += candidates[i]
            self.path.append(candidates[i])
            self.backtracking(candidates, target, sum_, i + 1)
            self.path.pop()  # 回溯，为了下一轮for loop
            sum_ -= candidates[i]  # 回溯，为了下一轮for loop


def tst(candidates: List[int], target: int, expect: List[List[int]]):
    output = Solution().combinationSum2(candidates, target)
    utils.tst(f'comb sum II candidates={candidates} target={target}', output, expect)


if __name__ == '__main__':
    tst([10, 1, 2, 7, 6, 1, 5], 8, [
        [1, 1, 6],
        [1, 2, 5],
        [1, 7],
        [2, 6]
    ])
    # tst([2, 5, 2, 1, 2], 5, [
    #     [1, 2, 2],
    #     [5]
    # ])
