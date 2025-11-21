from typing import List, Dict, Tuple

# https://leetcode.com/problems/maximum-number-of-operations-to-move-ones-to-the-end/?envType=daily-question&envId=2025-11-13
# 1001101
# 0,3,4,6
# 2,3,4,6
# 2,3,5,6
# 2,4,5,6
# 3,4,5,6

# 111000
# 0,1,2
# [k] [t] k + t
# if t != 0:


# K[j]
# K[j + 1]


# 1    2     3    4
#      1,2   3    4
#      1    2,3   4
#      1    2,   3,4
#           1,2  3,4
#           1    2,3,4
#               1,2,3,4



# 100100
# 001100
# 001001
# 000011

# 100100100
# 001100100
# 001001100
# 001001001
# 000011001
# 000010011

# 1:3
# 2:2
# 3:1


# cnt[i]  cnt[i next]
# cnt[i] =
#   if i no gap with i next:
#      cnt[i next]
#   else:
#      cnt[i next] + 1

class Solution:
    def maxOperations(self, s: str) -> int:
        res = 0
        curr_cnt = 0
        N = len(s)
        last_one_pos = N
        for pos in range(N - 1, -1, -1):
            if s[pos] == '0':
                continue
            if last_one_pos == N:
                if pos < N - 1:
                    curr_cnt = 1
                    res = 1
            else:
                if last_one_pos - pos > 1:
                    curr_cnt += 1
                res += curr_cnt
            last_one_pos = pos
        return res

    def maxOperationsV0(self, s: str) -> int:
        res = 0
        curr_cnt = 0
        N = len(s)
        one_pos: list[int] = []
        for i, ch in enumerate(s):
            if ch == '1':
                one_pos.append(i)
        M = len(one_pos)
        for i in range(M - 1, -1, -1):
            pos = one_pos[i]
            if i == M - 1:
                if pos < N - 1:
                    curr_cnt = 1
                    res = 1
            else:
                if one_pos[i + 1] - pos > 1:
                    curr_cnt += 1
                res += curr_cnt
        return res



    # def maxOperations(self, s: str) -> int:
    #     one_pos: list[int] = []
    #     for i, ch in enumerate(s):
    #         if ch == '1':
    #             one_pos.append(i)
    #     N = len(one_pos)
    #     M = len(s)
    #     cnt = 0
    #
    #     def modify_pos_arr():
    #         nonlocal cnt
    #         updated = False
    #         for i, pos in enumerate(one_pos):
    #             if i + 1 < N:
    #                 if one_pos[i + 1] > pos + 1:
    #                     cnt += 1
    #                     one_pos[i] = one_pos[i + 1] - 1
    #                     updated = True
    #             elif pos < M - 1:
    #                 cnt += 1
    #                 one_pos[i] = M - 1
    #                 updated = True
    #
    #         if updated:
    #             modify_pos_arr()
    #
    #     modify_pos_arr()
    #     return cnt