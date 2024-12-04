# https://leetcode.com/problems/check-if-n-and-its-double-exist/?envType=daily-question&envId=2024-12-01
from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        st = set()
        for x in arr:
            if 2 * x in st:
                return True
            if x % 2 == 0 and x // 2 in st:
                return True
            st.add(x)
        return False
