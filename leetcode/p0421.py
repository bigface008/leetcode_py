from typing import List

import utils


# https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        ans, mask = 0, 0
        maxBit = max(nums).bit_length() - 1
        for i in range(maxBit, -1, -1):
            mask |= 1 << i
            newAns = ans | (1 << i)
            seen = set()
            for x in nums:
                x &= mask
                if newAns ^ x in seen:
                    ans = newAns
                    break
                seen.add(x)
        return ans


def tst(nums: List[int], expect: int):
    output = Solution().findMaximumXOR(nums)
    utils.tst(f'max xor nums={nums}', output, expect)


if __name__ == '__main__':
    tst([3, 10, 5, 25, 2, 8], 28)
    tst([14, 70, 53, 83, 49, 91, 36, 80, 92, 51, 66, 70], 127)
