# https://leetcode.com/problems/stone-game-ix/description/?envType=daily-question&envId=2026-08-16
from functools import cache
from typing import List, Dict, Tuple


# A 1 -> B 1 -> A 2 -> B 1 -> A 2 ->
# A 2 -> B 2 -> A 1 -> B 2 ->

# [1, 0, 2]


class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        cnt = [0] * 3
        for x in stones:
            cnt[x % 3] += 1

        N = len(stones)
        def check(N: int, cnt: List[int]) -> bool:
            if cnt[1] == 0:
                return False
            cnt[1] -= 1
            rounds = 1 + min(cnt[1], cnt[2]) * 2 + cnt[0]
            if cnt[1] > cnt[2]:
                rounds += 1
            return rounds < N and rounds % 2 > 0

        return check(N, cnt[:]) or check(N, [cnt[0], cnt[2], cnt[1]])

