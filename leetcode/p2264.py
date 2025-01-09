# https://leetcode.cn/problems/largest-3-same-digit-number-in-string/description/?envType=daily-question&envId=2025-01-08
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        N = len(num)
        ans = ''
        for i in range(2, N):
            if num[i - 2] == num[i - 1] == num[i]:
                # ans = max(ans, int(num[i]) * 111)
                val = int(num[i]) * 111
                if ans == '':
                    ans = '000'
                if val > int(ans):
                    ans = num[i] * 3
        return ans