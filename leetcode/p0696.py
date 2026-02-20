# https://leetcode.com/problems/count-binary-substrings/?envType=daily-question&envId=2026-02-19
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        N = len(s)
        curr_len = 1
        prev_len = 0
        ans = 0
        for i in range(N - 1):
            if s[i + 1] == s[i]:
                curr_len += 1
            else:
                ans += min(curr_len, prev_len)
                prev_len = curr_len
                curr_len = 1
        ans += min(curr_len, prev_len)
        return ans



        # N = len(s)
        # i = 1
        # prev_len = 0
        # ans = 0
        # start = 0
        # while i < N:
        #     while i < N and s[i - 1] == s[i]:
        #         i += 1
        #     curr_len = i - start
        #     ans += min(curr_len, prev_len)
        #     prev_len = curr_len
        #     start = i
        #     i += 1
        # last_len = i - start
        # ans += min(last_len, prev_len)
        # return ans



        # i = 1
        # while i < N:
        #     left_start = i - 1
        #     while i < N and s[i - 1] == s[i]:
        #         i += 1
        #     if i < N:
        #         left_end = i - 1
        #         right_start = i
        #         while i < N and s[i - 1] == s[i]:

        # for i in range(1, N):
        #     prev_d, d = s[i - 1], s[i]
        #     if prev_d != d:
        #


if __name__ == "__main__":
    # print(Solution().countBinarySubstrings("10101"))
    print(Solution().countBinarySubstrings("00110011"))
