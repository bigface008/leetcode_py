from typing import List


# https://leetcode.cn/problems/shopping-offers/?envType=daily-question&envId=2024-11-03
class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        N = len(price)

        def dfs(itemCnts: List[int]):
            if all(x == 0 for x in itemCnts):
                return 0
            