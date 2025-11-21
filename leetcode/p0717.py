# https://leetcode.com/problems/1-bit-and-2-bit-characters/?envType=daily-question&envId=2025-11-18
from typing import List, Optional

from you_get.json_output import last_info


class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        if len(bits) == 0 or bits[-1] == 1:
            return False
        if len(bits) == 1 and bits[0] == 0:
            return True
        N = len(bits)
        cache: List[Optional[bool]] = [None] * N

        def is_feasible(last_idx: int) -> bool:
            if last_idx < 0:
                return False
            if cache[last_idx] is not None:
                return cache[last_idx]
            res = False
            if last_idx == 0:
                res = bits[0] == 0
            elif last_idx == 1:
                res = not (bits[0] == 0 and bits[1] == 1)
            elif bits[last_idx] == 1:
                if bits[last_idx - 1] == 0:
                    res = False
                else:
                    res = is_feasible(last_idx - 2)
            else:
                res = is_feasible(last_idx - 1) or (bits[last_idx - 1] == 1 and is_feasible(last_idx - 2))
            cache[last_idx] = res
            return res

        res = is_feasible(N - 2)
        return res

        # if len(bits) == 0 or bits[-1] == 1:
        #     return False
        # N = len(bits)
        # if N % 2 == 0:
        #     if bits[-2] == 1:
        #         return False
        #     for i in range(0, N - 2, 2):
        #         if bits[i] == 0 and bits[i + 1] == 1:
        #             return False
        #     return True
        # else:
        #     for i in range(0, N - 1, 2):
        #         if bits[i] == 0 and bits[i + 1] == 1:
        #             return False
        #     return True


if __name__ == '__main__':
    Solution().isOneBitCharacter([1,1,1,0])
