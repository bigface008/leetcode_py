# https://leetcode.cn/problems/delete-columns-to-make-sorted-ii/description/?envType=daily-question&envId=2025-12-21
from typing import List, Dict, Optional, Tuple, Set


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        N, M = len(strs), len(strs[0])
        check_list = list(range(N - 1))
        ans = 0
        for j in range(M):
            for i in check_list:
                if strs[i][j] > strs[i + 1][j]:
                    ans += 1
                    break
            else:
                new_size = 0
                for i in check_list:
                    if strs[i][j] == strs[i + 1][j]:
                        check_list[new_size] = i
                        new_size += 1
                del check_list[new_size:]
        return ans


        # N, M = len(strs), len(strs[0])
        # arr = [''] * N
        # ans = 0
        # for col_i in range(M):
        #     for w_i in range(N - 1):
        #         if arr[w_i] + strs[w_i][col_i] > arr[w_i + 1] + strs[w_i + 1][col_i]:
        #             ans += 1
        #             break
        #     else:
        #         for w_i, w in enumerate(strs):
        #             arr[w_i] += w[col_i]
        # return ans



if __name__ == '__main__':
    print(Solution().minDeletionSize(["xc", "yb", "za"]))
    # print(Solution().minDeletionSize(["ca", "bb", "ac"]))
