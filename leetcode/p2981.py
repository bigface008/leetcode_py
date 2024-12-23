# https://leetcode.com/problems/find-longest-special-substring-that-occurs-thrice-i/?envType=daily-question&envId=2024-12-10
from collections import Counter, defaultdict

import utils


class Solution:
    def maximumLength(self, s: str) -> int:
        N = len(s)
        counter = Counter()
        con_mp = defaultdict(list)
        con_len = 0
        ans = -1
        for i in range(N + 1):
            ch = s[i] if i < N else None
            if 0 < i < N and ch == s[i - 1]:
                con_len += 1
                # if con_len >= 3:
                #     ans = max(ans, con_len - 2)
            else:
                if con_len != 0:
                    con_mp[s[i - 1]].append(con_len)
                    if con_len >= 3:
                        ans = max(ans, con_len - 2)
                    # all_groups = con_mp[s[i - 1]]
                    # if len(all_groups) == 2:
                    #     if all_groups[0] != all_groups[1]:
                    #         ans = max(ans, min(all_groups[0], all_groups[1]))
                    #     elif all_groups[0] != 1:
                    #         ans = max(ans, all_groups[0] - 1)
                    # elif len(all_groups) >= 3:
                    #     ans = max(ans, min(l for l in all_groups))
                con_len = 1
            # counter[ch] += 1
            # if counter[ch] >= 3:
            #     ans = max(ans, 1)
        for k, v in con_mp.items():
            if len(v) == 2:
                if v[0] != v[1]:
                    ans = max(ans, min(v[0], v[1]))
                elif v[0] != 1:
                    ans = max(ans, v[0] - 1)
            elif len(v) >= 3:
                cnt = Counter(v)
                times = list(cnt.keys())
                times.sort(reverse=True)
                if cnt[times[0]] >= 3:
                    ans = max(ans, times[0])
                elif cnt[times[0]] == 2:
                    ans = max(ans, times[0] - 1)
                else:
                    ans = max(ans, times[1])
        # print(con_mp)
            #     ans = max(ans, min(l for l in v))
        return ans


def check(s: str, expect: int):
    output = Solution().maximumLength(s)
    utils.tst(f's={s}', output, expect)


if __name__ == '__main__':
    # check('cccerrrecdcdccedecdcccddeeeddcdcddedccdceeedccecde', 2)
    check('jinhhhtttttttefffffjjjjjjjjjfffffjjjjjjjjjqvvvvvvg', 8)
