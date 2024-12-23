# https://leetcode.cn/problems/minimum-moves-to-capture-the-queen/?envType=daily-question&envId=2024-12-05
class Solution:
    def minMovesToCaptureTheQueen(self, a: int, b: int, c: int, d: int, e: int, f: int) -> int:
        rook_dist = (1 if a != e else 0) + (1 if b != f else 0)
        bishop_dist = (1 if (c + d) != (e + f) else 0) + (1 if (c - d) != (e - f) else 0)
        s1, d1 = a + b, a - b
        s2, d2 = c + d, c - d
        s3, d3 = e + f, e - f
        if a == e == c and (b < d < f or f < d < b):
            return bishop_dist
        if b == d == f and (a < c < e or e < c < a):
            return bishop_dist
        if s1 == s2 == s3 and (d2 < d1 < d3 or d3 < d1 < d2):
            return rook_dist
        if d1 == d2 == d3 and (s2 < s1 < s3 or s3 < s1 < s2):
            return rook_dist
        return min(rook_dist, bishop_dist)
