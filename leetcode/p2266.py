from functools import cache
from itertools import groupby


# https://leetcode.cn/problems/count-number-of-texts/
class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        MOD = pow(10, 9) + 7
        N = len(pressedKeys)
        book = [
            'abc',
            'def',
            'ghi',
            'jkl',
            'mno',
            'pqrs',
            'tuv',
            'wxyz',
        ]

        @cache
        def dfs(press_num: int, press_time: int) -> int:
            if press_time < 0:
                return 0
            if press_time == 0:
                return 1
            ss = book[press_num - 2]
            res = 0
            for i, ch in enumerate(ss):
                res += dfs(press_num, press_time - i - 1)
                res %= MOD
            return res

        ans = 1
        for key, group in groupby(pressedKeys):
            press_num = int(key)
            press_time = len(list(group))
            ans *= dfs(press_num, press_time)
            ans %= MOD
        return ans


class Solution2:
    def countTexts(self, pressedKeys: str) -> int:
        book = [  # num -> cnt -> char
            'abc',
            'def',
            'ghi',
            'jkl',
            'mno',
            'pqrs',
            'tuv',
            'wxyz',
        ]
        MOD = pow(10, 9) + 7
        N = len(pressedKeys)

        @cache
        def dfs(pressed_num: int, press_time: int) -> int:
            if press_time < 0:
                return 0
            if press_time == 0:
                return 1
            # print(f'pressed_num {pressed_num}')
            ss = book[pressed_num - 2]
            res = 0
            for i, ch in enumerate(ss):
                res += dfs(pressed_num, press_time - i - 1)
                res %= MOD
            return res

        ans = 1
        same_ch_cnt = 1
        for i in range(1, N):
            if pressedKeys[i - 1] == pressedKeys[i]:
                same_ch_cnt += 1
            else:
                ans *= dfs(int(pressedKeys[i - 1]), same_ch_cnt)
                ans %= MOD
                same_ch_cnt = 1
        ans *= dfs(int(pressedKeys[-1]), same_ch_cnt)
        ans %= MOD
        return ans


if __name__ == '__main__':
    print(Solution().countTexts("444479999555588866"))
