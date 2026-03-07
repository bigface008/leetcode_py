# https://leetcode.com/problems/minimum-number-of-flips-to-make-the-binary-string-alternating/?envType=daily-question&envId=2026-03-07
class Solution:
    def minFlips(self, s: str) -> int:
        N = len(s)
        pre_sum_0 = [0] * (N + 1)
        pre_sum_1 = [0] * (N + 1)
        for i in range(N):
            if s[i] == '0':
                if i % 2 == 0:
                    pre_sum_0[i + 1] = pre_sum_0[i]
                    pre_sum_1[i + 1] = pre_sum_1[i] + 1
                else:
                    pre_sum_0[i + 1] = pre_sum_0[i] + 1
                    pre_sum_1[i + 1] = pre_sum_1[i]
            else:
                if i % 2 == 0:
                    pre_sum_0[i + 1] = pre_sum_0[i] + 1
                    pre_sum_1[i + 1] = pre_sum_1[i]
                else:
                    pre_sum_0[i + 1] = pre_sum_0[i]
                    pre_sum_1[i + 1] = pre_sum_1[i] + 1
        ans = min(pre_sum_0[-1], pre_sum_1[-1])
        for move_len in range(1, N):
            new_start_idx = move_len
            unmove_cnt_0, unmove_cnt_1 = 0, 0
            if new_start_idx % 2 == 0:
                unmove_cnt_0 = pre_sum_0[N] - pre_sum_0[new_start_idx]
                unmove_cnt_1 = pre_sum_1[N] - pre_sum_1[new_start_idx]
            else:
                unmove_cnt_0 = pre_sum_1[N] - pre_sum_1[new_start_idx]
                unmove_cnt_1 = pre_sum_0[N] - pre_sum_0[new_start_idx]
            move_new_start_idx = N - move_len
            move_cnt_0, move_cnt_1 = pre_sum_0[move_len] - pre_sum_0[0], pre_sum_1[move_len] - pre_sum_1[0]
            all_0, all_1 = 0, 0
            if (N - move_len) % 2 == 0:
                all_0 = unmove_cnt_0 + move_cnt_0
                all_1 = unmove_cnt_1 + move_cnt_1
            else:
                all_0 = unmove_cnt_0 + move_cnt_1
                all_1 = unmove_cnt_1 + move_cnt_0
            ans = min(ans, all_0, all_1)
        return ans


if __name__ == '__main__':
    print(Solution().minFlips("111000"))

