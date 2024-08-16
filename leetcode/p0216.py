from typing import List

# https://leetcode.com/problems/combination-sum-iii/
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        path = []

        def dfs(i: int, sum: int):
            if sum > n:
                return
            if sum == n and len(path) == k:
                ans.append(path.copy())
                return
            remainCnt = k - len(path)
            needSum = n - sum
            remainSum = (9 + (9 - (remainCnt - 1))) * remainCnt // 2
            if needSum > remainSum:
                return
            for j in range(i, 10):
                if 10 - j < remainCnt:
                    return
                path.append(j)
                dfs(j + 1, sum + j)
                path.pop()

        dfs(1, 0)
        return ans


def tst(k: int, n: int, expect: List[List[int]]):
    pass


if __name__ == '__main__':
    tst(3, 7, [[1,2,4]])
    tst(3, 9, [[1,2,6],[1,3,5],[2,3,4]])
    tst(4, 1, [])