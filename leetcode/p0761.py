# https://leetcode.cn/problems/special-binary-string/?envType=daily-question&envId=2026-02-20
from typing import List, Tuple


class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        if len(s) <= 2:
            return s

        substrs = []
        diff = 0
        start = 0
        for i, ch in enumerate(s):
            if ch == '1':
                diff += 1
            else:
                diff -= 1
                if diff == 0:
                    substrs.append('1' + self.makeLargestSpecial(s[start + 1: i]) + '0')
                    start = i + 1

        substrs.sort(reverse=True)
        return ''.join(substrs)



        # N = len(s)
        # chs = list(s)
        #
        # def swap():
        #     nonlocal chs
        #     str_pos: List[Tuple[int, int]] = []
        #     swap_cnt = 0
        #     curr_len = 1
        #     prev_len = 0
        #
        #     def check_swap(i: int):
        #         if chs[i] == '0' and prev_len != 0:
        #             nonlocal swap_cnt
        #             str_len = min(prev_len, curr_len) * 2
        #             if prev_len < curr_len:
        #                 start = i - curr_len - prev_len + 1
        #             else:
        #                 start = i - str_len + 1
        #             if str_pos:
        #                 prev_start, prev_end = str_pos[-1]
        #                 prev_str_len = prev_end - prev_start + 1
        #                 if prev_end + 1 == start and prev_str_len < str_len:
        #                     swap_cnt += 1
        #                     for j in range(str_len // 2):
        #                         chs[prev_start + j] = '1'
        #                         chs[prev_start + str_len // 2 + j] = '0'
        #                     for j in range(prev_str_len // 2):
        #                         chs[prev_start + str_len + j] = '1'
        #                         chs[prev_start + str_len + prev_str_len // 2 + j] = '0'
        #             str_pos.append((start, i))
        #
        #     for i in range(N - 1):
        #         if chs[i + 1] == chs[i]:
        #             curr_len += 1
        #         else:
        #             check_swap(i)
        #             prev_len = curr_len
        #             curr_len = 1
        #     check_swap(N - 1)
        #     if swap_cnt != 0:
        #         swap()
        #
        # swap()
        # return ''.join(chs)


if __name__ == "__main__":
    print(Solution().makeLargestSpecial("110110100100"))
    # print(Solution().makeLargestSpecial("11011000"))
    # 110110100100
    #
    # 111010010100
