from typing import List


# https://leetcode.cn/problems/make-a-square-with-the-same-color/description/?envType=daily-question&envId=2024-08-31
class Solution:
    def canMakeSquare(self, grid: List[List[str]]) -> bool:
        N = 3
        b_cnt = 0
        for i in range(2):
            for j in range(2):
                if grid[i][j] == 'B':
                    b_cnt += 1
        if b_cnt >= 3 or b_cnt <= 1:
            return True
        b_cnt = 0
        for i in range(1, 3):
            for j in range(2):
                if grid[i][j] == 'B':
                    b_cnt += 1
        if b_cnt >= 3 or b_cnt <= 1:
            return True
        b_cnt = 0
        for i in range(2):
            for j in range(1, 3):
                if grid[i][j] == 'B':
                    b_cnt += 1
        if b_cnt >= 3 or b_cnt <= 1:
            return True
        b_cnt = 0
        for i in range(1, 3):
            for j in range(1, 3):
                if grid[i][j] == 'B':
                    b_cnt += 1
        if b_cnt >= 3 or b_cnt <= 1:
            return True
        return False
