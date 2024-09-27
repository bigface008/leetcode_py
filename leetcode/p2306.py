from collections import defaultdict
from typing import List

import utils


# https://leetcode.cn/problems/naming-a-company/?envType=daily-question&envId=2024-09-25
class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        N = len(ideas)
        dic = defaultdict(set)
        ans = 0
        for s in ideas:
            dic[s[0]].add(s[1:])
        chs = list(dic.keys())
        # print(f'dic={dic}')
        NC = len(chs)
        for i in range(NC):
            for j in range(i + 1, NC):
                ki, kj = chs[i], chs[j]
                si, sj = dic[ki], dic[kj]
                valid_cnt = len(si.intersection(sj))
                si_cnt, sj_cnt = len(si) - valid_cnt, len(sj) - valid_cnt
                # print(f'ki={ki} kj={kj} si={si} sj={sj} valid_cnt={valid_cnt}')
                ans += si_cnt * sj_cnt * 2
        return ans


        # dic = set(ideas)
        # N = len(ideas)
        # ans = 0
        # for i in range(N):
        #     for j in range(i + 1, N):
        #         na, nb = ideas[i], ideas[j]
        #         na, nb = (nb[0] + na[1:]), (na[0] + nb[1:])
        #         # print(f'{ideas[i]} {ideas[j]} -> {na} {nb}')
        #         if (na not in dic) and (nb not in dic):
        #             # print(f'>>> {ideas[i]} {ideas[j]} -> {na} {nb}')
        #             ans += 2
        # return ans


# class TrieNode:


def tst(ideas: List[int], expect: int):
    output = Solution().distinctNames(ideas)
    utils.tst(f'distinct names ideas={ideas}', output, expect)


if __name__ == '__main__':
    tst(["coffee", "donuts", "time", "toffee"], 6)
    tst(["lack", "back"], 0)
