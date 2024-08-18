from typing import List
import utils


# https://leetcode.com/problems/lemonade-change/?envType=daily-question&envId=2024-08-15
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        num5 = 0
        num10 = 0
        num20 = 0
        for bill in bills:
            if bill == 5:
                num5 += 1
            elif bill == 10:
                if num5 == 0:
                    return False
                num5 -= 1
                num10 += 1
            else:
                if num10 == 0:
                    if num5 >= 3:
                        num5 -= 3
                    else:
                        return False
                else:
                    if num5 == 0:
                        return False
                    num5 -= 1
                    num10 -= 1
                num20 += 1
        return True


def tst(bills: List[int], expect: int):
    output = Solution().lemonadeChange(bills)
    utils.tst(f'lemonade change bills={bills}', output, expect)


if __name__ == '__main__':
    tst([5, 5, 5, 10, 5, 5, 10, 20, 20, 20], False)
