import collections
from typing import List

# 16, 4, 7, 17
# 16, 7, 17, 4
# 16, 17, 4, 7
# 17, 4, 7, 16
# 17, 7, 16, 4
# 17, 16,


# https://leetcode.cn/problems/find-the-first-player-to-win-k-games-in-a-row/?envType=daily-question&envId=2024-10-24
class Solution:
    def findWinningPlayer(self, skills: List[int], k: int) -> int:
        N = len(skills)
        dq = collections.deque()
        win_times = [0] * N
        if k > N:
            k = N
        for i, skill in enumerate(skills):
            dq.append([skill, i])
        while True:
            skill1, i1 = dq.popleft()
            skill2, i2 = dq.popleft()
            if win_times[i1] == k:
                return i1
            if win_times[i2] == k:
                return i2
            if skill1 > skill2:
                win_times[i1] += 1
                win_times[i2] = 0
                dq.appendleft([skill1, i1])
                dq.append([skill2, i2])
            else:
                win_times[i2] += 1
                win_times[i1] = 0
                dq.appendleft([skill2, i2])
                dq.append([skill1, i1])
        return -1

