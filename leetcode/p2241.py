# https://leetcode.cn/problems/design-an-atm-machine/?envType=daily-question&envId=2025-01-05
from typing import List
from collections import Counter


class ATM:

    def __init__(self):
        self.account = [0] * 5
        self.N = 5
        self.idx2Val = (20, 50, 100, 200, 500)

    def deposit(self, banknotesCount: List[int]) -> None:
        # self.account = banknotesCount
        for i, x in enumerate(banknotesCount):
            self.account[i] += x

    def withdraw(self, amount: int) -> List[int]:
        ans = [0] * 5
        for i in range(4, -1, -1):
            note_cnt = self.account[i]
            note = self.idx2Val[i]
            need_cnt = amount // note
            if need_cnt <= note_cnt:
                ans[i] += need_cnt
                amount -= need_cnt * note
            else:
                ans[i] += note_cnt
                amount -= note_cnt * note
        if amount == 0:
            for i in range(5):
                self.account[i] -= ans[i]
            return ans
        else:
            return [-1]


def check():
    atm = ATM()
    atm.deposit([0,0,1,2,1])
    print(atm.withdraw(600))
    atm.deposit([0,1,0,1,1])
    print(atm.withdraw(600))



if __name__ == '__main__':
    check()