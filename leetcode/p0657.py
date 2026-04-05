# https://leetcode.com/problems/robot-return-to-origin/?envType=daily-question&envId=2026-04-05
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        up_cnt, down_cnt, left_cnt, right_cnt = 0, 0, 0, 0
        for move in moves:
            if move == 'U':
                up_cnt += 1
            elif move == 'D':
                down_cnt += 1
            elif move == 'L':
                left_cnt += 1
            else:
                right_cnt += 1
        return up_cnt == down_cnt and left_cnt == right_cnt