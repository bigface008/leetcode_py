# https://leetcode.cn/problems/cat-and-mouse/?envType=daily-question&envId=2025-02-10
from typing import List


class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:
        N = len(graph)
        CASES = 2 * N * (N - 1)
        dp = [[[-1] * CASES for _ in range(N)] for _ in range(N)]

        def getResult(mouse: int, cat: int, turns: int) -> int:
            if turns == CASES:
                return 0
            res = dp[mouse][cat][turns]
            if res != -1:
                return res
            if mouse == 0:
                res = 1
            elif cat == mouse:
                res = 2
            else:
                res = getNextResult(mouse, cat, turns)
            dp[mouse][cat][turns] = res
            return res

        def getNextResult(mouse: int, cat: int, turns: int) -> int:
            curMove = mouse if turns % 2 == 0 else cat
            defaultRes = 1 if curMove != mouse else 2
            res = defaultRes
            for next in graph[curMove]:
                if curMove == cat and next == 0:
                    continue
                nextMouse = next if curMove == mouse else mouse
                nextCat = next if curMove == cat else cat
                nextRes = getResult(nextMouse, nextCat, turns + 1)
                if nextRes != defaultRes:
                    res = nextRes
                    if res != 0:
                        break
            return res

        return getResult(1, 2, 0)