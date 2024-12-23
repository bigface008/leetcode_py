# https://leetcode.cn/problems/determine-color-of-a-chessboard-square/?envType=daily-question&envId=2024-12-09
class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        i1 = ord(coordinates[0]) - ord('a')
        i2 = int(coordinates[1]) - 1
        return (i1 + i2) % 2 == 1
