from itertools import groupby


# https://leetcode.cn/problems/maximize-the-confusion-of-an-exam/
class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        ans = 0
        left = 0
        t_cnt = f_cnt = 0
        for right, x in enumerate(answerKey):
            if x == 'T':
                t_cnt += 1
            else:
                f_cnt += 1
            if t_cnt <= k or f_cnt <= k:
                ans = max(right - left + 1, ans)
            else:
                if answerKey[left] == 'T':
                    t_cnt -= 1
                else:
                    f_cnt -= 1
                left += 1
        return ans


        # def count_max_ans_len() -> int:
        #     return max((len(list(group)) for key, group in groupby(keys)), default=0)

        # def dfs(i: int, op_cnt: int):
        #     # def dfs(i: int, op_cnt: int, max_same_ans_cnt: int):
        #     if op_cnt < 0:
        #         return
        #     if i == N:
        #         cnt = count_max_ans_len()
        #         nonlocal ans
        #         ans = max(ans, cnt)
        #         return
        #     dfs(i + 1, op_cnt) # not change
        #     if op_cnt != 0:
        #         if keys[i] == 1:
        #             keys[i] = 0
        #             dfs(i + 1, op_cnt - 1)
        #             keys[i] = 1
        #         else:
        #             keys[i] = 1
        #             dfs(i + 1, op_cnt - 1)
        #             keys[i] = 0
        # prev_1_start = -1
        # for i, k in enumerate(keys):
        #     if k == 1:
        #         prev_1_start = i
        #     else:
        #         break
        # prev_0_start = -1
        # for i, k in enumerate(keys):
        #     if k == 1:
        #         prev_1_start = i
        #     else:
        #         break
        # dfs(0, k)
        # return ans


