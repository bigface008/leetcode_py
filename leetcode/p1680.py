# https://leetcode.cn/problems/concatenation-of-consecutive-binary-numbers/?envType=daily-question&envId=2026-02-28
class Solution:
    def concatenatedBinary(self, n: int) -> int:
        MOD = pow(10, 9) + 7
        ans = 0
        prev_len = 0
        for d in range(1, n + 1):
            if d & (d - 1) == 0:
                prev_len += 1
            ans = ((ans << prev_len) + d) % MOD
        return ans

        # ans = 0
        # prev_len = 0
        # for d in range(n, 0, -1):
        #     ans += (d << prev_len) % MOD
        #     prev_len += d.bit_length()
        # return ans % MOD



#
#         def dfs(digit: int, prev_len: int) -> int:
#             dv = digit << prev_len
#             remainder = dv % MOD
#             if digit != 1:
#                 remainder = (remainder + dfs(digit - 1, prev_len + digit.bit_length())) % MOD
#             return remainder
#
#         return dfs(n, 0)


        # value = n
        # for d in range(n - 1, 0, -1):
        #     value += d << value.bit_length()
        #     if value > MOD:
        #         value %= MOD
        # return value


if __name__ == "__main__":
    # print(Solution().concatenatedBinary(1))
    print(Solution().concatenatedBinary(3))
