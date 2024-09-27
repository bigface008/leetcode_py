# https://leetcode.com/problems/k-th-smallest-in-lexicographical-order
class Solution:
    def findKthNumber(self, n: int, k: int) -> int:

        def count_subtree_size(num: int) -> int:
            cnt = 0
            width = 1
            while True:
                if num + width - 1 <= n:
                    cnt += width
                    num *= 10
                    width *= 10
                else:
                    if n - num >= 0:
                        cnt += n - num + 1
                    break
            return cnt

        num = 1
        cnt = 0
        while True:
            if cnt == k - 1:
                break
            tmp = count_subtree_size(num)
            if tmp + cnt >= k:
                num *= 10
                cnt += 1
            else:
                num += 1
                cnt += tmp
        return num

        # # get the node number of the tree whose root is x, all nodes in the tree should be <= n
        # def count(num: int) -> int:
        #     cnt = 0
        #     width = 1
        #     while True:
        #         if num + width - 1 <= n:
        #             cnt += width
        #             num *= 10
        #             width *= 10
        #         else:
        #             if n - num >= 0:
        #                 cnt += n - num + 1
        #             break
        #     return cnt
        #
        # num = 1
        # cnt = 0
        # while True:
        #     if cnt == k - 1:
        #         break
        #     tmp = count(num)
        #     if tmp + cnt >= k:
        #         num *= 10
        #         cnt += 1
        #     else:
        #         num += 1
        #         cnt += tmp
        # return num




        # num = 1
        # for i in range(k - 1):
        #     if num * 10 <= n:
        #         num *= 10
        #     else:
        #         while num % 10 == 9 or num + 1 > n:
        #             num //= 10
        #         num += 1
        #     print(num)
        # return num
