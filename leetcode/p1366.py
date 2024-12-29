# https://leetcode.cn/problems/rank-teams-by-votes/?envType=daily-question&envId=2024-12-29
from collections import defaultdict
from functools import cmp_to_key
from typing import List

import utils


class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        N = len(votes[0])
        LN = 26
        cnt = [[0] * LN for _ in range(N)]
        for vote in votes:
            for i, ch in enumerate(vote):
                cnt[i][ord(ch) - ord('A')] += 1

        def cmp(a: str, b: str) -> int:
            ai, bi = ord(a) - ord('A'), ord(b) - ord('A')
            i = 0
            while i < N and cnt[i][ai] == cnt[i][bi]:
                i += 1
            if i == N:
                # print(f'cmp({a}, {b}) -> {ord(a) - ord(b)}, i == N')
                return ord(a) - ord(b)
            # print(f'cmp({a}, {b}) -> {cnt[i][bi] - cnt[i][ai]}, cnt[i][ai] = {cnt[i][ai]}, cnt[i][bi] = {cnt[i][bi]}, i = {i}')
            return cnt[i][bi] - cnt[i][ai]

        ans = ''.join(sorted(votes[0], key=cmp_to_key(cmp)))
        return ans




        # N = len(votes[0])
        # LN = 26
        # cnt = [[0] * LN for _ in range(N)]
        # for vote in votes:
        #     for i, ch in enumerate(vote):
        #         cnt[i][ord(ch) - ord('A')] += 1
        # sorted_set = set()
        # ans = ''
        # for i in range(N):
        # #     _, ich = max((ch_cnt, -ich) for ich, ch_cnt in enumerate(cnt[i]) if chr(ord('A') + ich) not in sorted_set)
        # #     ich = -ich
        # #     ch = chr(ord('A') + ich)
        # #     ans += ch
        # #     sorted_set.add(ch)
        # # return ans
        #     max_cnt = 0
        #     same_ich = []
        #     for ich, ch_cnt in enumerate(cnt[i]):
        #         ch = chr(ord('A') + ich)
        #         if ch in sorted_set:
        #             continue
        #         if ch_cnt > max_cnt:
        #             same_ich = [ich]
        #             max_cnt = ch_cnt
        #         elif ch_cnt == max_cnt:
        #             same_ich.append(ich)
        #     j = i + 1
        #     while len(same_ich) != 1 and j < N:
        #         new_same_ich = []
        #         new_max_cnt = 0
        #         for ich in same_ich:
        #             c = cnt[j][ich]
        #             if c > new_max_cnt:
        #                 new_max_cnt = c
        #                 new_same_ich = [ich]
        #             elif c == new_max_cnt:
        #                 new_same_ich.append(ich)
        #         same_ich = new_same_ich
        #         j += 1
        #
        #     ch = chr(ord('A') + same_ich[0])
        #     sorted_set.add(ch)
        #     ans += ch
        # return ans


def check(votes: List[int], expect: str):
    output = Solution().rankTeams(votes)
    utils.tst(f'votes={votes}', output, expect)


if __name__ == '__main__':
    check(["WXYZ", "XYZW"], "XWYZ")
