# https://leetcode.cn/problems/check-if-two-chessboard-squares-have-the-same-color/?envType=daily-question&envId=2024-12-03
class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        N = 8
        row1, col1 = ord(coordinate1[0]) - ord('a'), int(coordinate1[1]) - 1
        row2, col2 = ord(coordinate2[0]) - ord('a'), int(coordinate2[1]) - 1
        return (row1 + col1) % 2 == (row2 + col2) % 2
