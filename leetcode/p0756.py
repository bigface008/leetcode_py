# https://leetcode.cn/problems/pyramid-transition-matrix/?envType=daily-question&envId=2025-12-29
from typing import List, Dict, Optional, Tuple
from collections import defaultdict
from functools import cache


class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        bottom_to_top: Dict[str, List[str]] = defaultdict(list)
        for s in allowed:
            bottom_to_top[s[:2]].append(s[2])

        @cache
        def dfs(bt: str) -> bool:
            if len(bt) == 2:
                prefix = bt[0] + bt[1]
                return prefix in bottom_to_top
            N = len(bt)
            options: List[str] = []
            option: List[str] = []

            def backtrack(idx: int):
                nonlocal options
                if idx == N - 1:
                    options.append(''.join(option))
                    return
                prefix = bt[idx] + bt[idx + 1]
                if prefix not in bottom_to_top:
                    return
                for top in bottom_to_top[prefix]:
                    option.append(top)
                    backtrack(idx + 1)
                    option.pop()

            backtrack(0)
            for s in options:
                if dfs(s):
                    return True
            return False

        return dfs(bottom)


# class Solution:
#     def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
#         bottom_to_top: Dict[str, List[str]] = defaultdict(list)
#         for s in allowed:
#             bottom_to_top[s[:2]].append(s[2])
#
#         def dfs(bt: List[str]) -> bool:
#             if len(bt) == 2:
#                 prefix = bt[0] + bt[1]
#                 return prefix in bottom_to_top
#             N = len(bt)
#             options: List[List[str]] = []
#             option: List[str] = []
#
#             def backtrack(idx: int):
#                 nonlocal options
#                 if idx == N - 1:
#                     options.append(option.copy())
#                     return
#                 prefix = bt[idx] + bt[idx + 1]
#                 if prefix not in bottom_to_top:
#                     return
#                 for top in bottom_to_top[prefix]:
#                     option.append(top)
#                     backtrack(idx + 1)
#                     option.pop()
#
#             backtrack(0)
#             for option in options:
#                 if dfs(option):
#                     return True
#             return False
#
#         return dfs(list(bottom))


if __name__ == '__main__':
    print(Solution().pyramidTransition("DAAAAD",
                                       ["DAD", "DAE", "DAB", "DAF", "DAC", "EAD", "EAE", "EAB", "EAF", "EAC", "BAD",
                                        "BAE", "BAB", "BAF", "BAC", "FAD", "FAE", "FAB", "FAF", "FAC", "CAD", "CAE",
                                        "CAB", "CAF", "CAC", "ADD", "ADE", "ADB", "ADF", "ADC", "AED", "AEE", "AEB",
                                        "AEF", "AEC", "ABD", "ABE", "ABB", "ABF", "ABC", "AFD", "AFE", "AFB", "AFF",
                                        "AFC", "ACD", "ACE", "ACB", "ACF", "ACC", "AAD", "AAE", "AAB", "AAF", "AAC",
                                        "AAA"]))
    # print(Solution().pyramidTransition("AAAA", ["AAB", "AAC", "BCD", "BBE", "DEF"]))
    # print(Solution().pyramidTransition('BCD', ["BCC", "CDE", "CEA", "FFF"]))
