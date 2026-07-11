# https://leetcode.com/problems/count-complete-substrings/
from typing import Dict, List, Set
from collections import defaultdict


class Solution:
    def countCompleteSubstrings(self, word: str, k: int) -> int:
        N = len(word)

        def count_in_window(start: int, end: int) -> int:
            LEN = end - start + 1
            res = 0
            for diff_ch_cnt in range(1, 27):
                window_len = diff_ch_cnt * k
                if window_len > LEN:
                    break
                counter = defaultdict(int)
                for i in range(window_len):
                    counter[word[i + start]] += 1
                if all(cnt == 0 or cnt == k for cnt in counter.values()):
                    res += 1
                for i in range(window_len, LEN):
                    new_ch = word[i + start]
                    drop_ch = word[i + start - window_len]
                    counter[new_ch] += 1
                    counter[drop_ch] -= 1
                    if counter[drop_ch] == 0:
                        del counter[drop_ch]
                    if all(cnt == 0 or cnt == k for cnt in counter.values()):
                        res += 1
            return res

        i = 0
        ans = 0
        while i < N:
            start = i
            while i + 1 < N and abs(ord(word[i]) - ord(word[i + 1])) <= 2:
                i += 1
            ans += count_in_window(start, i)
            i += 1
        return ans


if __name__ == "__main__":
    print(Solution().countCompleteSubstrings("aaabbbccc", 3))


        # N = len(word)
        # mx_k_cnt = N // k
        # pre_sum_arr_mp: List[List[int]] = [[0] * (N + 1) for _ in range(26)]
        # diff_pre_sum_arr_mp: List[List[int]] = [[0] * N for _ in range(26)]
        # for i, ch in enumerate(word):
        #     ch_i = ord(ch) - ord('a')
        #     pre_sum_arr_mp[ch_i][i + 1] = pre_sum_arr_mp[ch_i][i] + 1
        #     if i + 1 < N:
        #         ch_i_next = ord(word[i + 1]) - ord('a')
        #         diff = abs(ch_i_next - ch_i)
        #         diff_pre_sum_arr_mp[diff][i + 1] = diff_pre_sum_arr_mp[diff][i] + 1
        #
        # def get_ch_cnt_in_window(ch: str, start: int, end: int) -> int:
        #     if start > end:
        #         return 0
        #     pre_sum_arr = pre_sum_arr_mp[ord(ch) - ord('a')]
        #     return pre_sum_arr[end + 1] - pre_sum_arr[start]
        #
        # def check_window(window_len: int) -> int:
        #     res = 0
        #     chs: Dict[str, int] = defaultdict(int)
        #     for i in range(window_len):
        #         chs[word[i]] += 1
        #     window_each_ch_cnt = get_ch_cnt_in_window(word[0], 0, window_len - 1)
        #     is_complete = True
        #     for ch in chs.keys():
        #         cnt = get_ch_cnt_in_window(ch, 0, window_len - 1)
        #         if cnt != window_each_ch_cnt:
        #             is_complete = False
        #             break
        #     if is_complete:
        #         res += 1
        #     for i in range(window_len, N):
        #         new_ch = word[i]
        #         drop_ch = word[i - window_len]
        #         chs[new_ch] += 1
        #         chs[drop_ch] -= 1
        #         if chs[drop_ch] == 0:
        #             del chs[drop_ch]
        #         window_each_ch_cnt = get_ch_cnt_in_window(word[i - window_len + 1], 0, window_len - 1)
        #
        #
        # ans = 0
        # for cnt in range(1, mx_k_cnt + 1):
        #     ans += check_window(cnt * k)
        # return ans