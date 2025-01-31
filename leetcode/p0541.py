# https://leetcode.cn/problems/reverse-string-ii/?envType=daily-question&envId=2025-01-31
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        N = len(s)
        window_len = 2 * k
        window_cnt = N // window_len
        remain = N % window_len
        res = list(s)
        for i in range(window_cnt):
            start = i * window_len
            end = i * window_len + k
            res[start:end] = reversed(res[start:end])
        i2 = window_cnt * window_len
        if remain < k:
            res[i2:] = reversed(res[i2:])
        else:
            res[i2:i2 + k] = reversed(res[i2:i2 + k])
        return ''.join(res)