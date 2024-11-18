import heapq


# https://leetcode.com/problems/longest-happy-string
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        pq = [(-a, 'a'), (-b, 'b'), (-c, 'c')]
        res = ''
        heapq.heapify(pq)
        while True:
            cnt, ch = heapq.heappop(pq)
            cnt = -cnt
            if cnt == 0:
                break
            if len(res) >= 2 and res[-1] == res[-2] == ch:
                cnt2, ch2 = heapq.heappop(pq)
                if cnt2 == 0:
                    break
                cnt2 = -cnt2
                res += ch2
                cnt2 -= 1
                heapq.heappush(pq, (-cnt2, ch2))
            else:
                if cnt >= 2:
                    res += ch * 2
                    cnt -= 2
                else:
                    res += ch
                    cnt -= 1
            heapq.heappush(pq, (-cnt, ch))
        return res

        # arr = [(a, 'a'), (b, 'b'), (c, 'c')]
        # res = ''
        # while True:
        #     arr.sort(reverse=True)
        #     if arr[0][0] == 0:
        #         break
        #     add_new_ch = False
        #     for i in range(3):
        #         cnt, ch = arr[i]
        #         if cnt == 0:
        #             continue
        #         if len(res) > 0 and res[-1] == ch:
        #             continue
        #         add_new_ch = True
        #         if i == 0:
        #             if cnt >= 2:
        #                 res += ch * 2
        #                 cnt -= 2
        #             else:
        #                 res += ch
        #                 cnt -= 1
        #         else:
        #             res += ch
        #             cnt -= 1
        #         arr[i] = (cnt, ch)
        #         if i != 0:
        #             break
        #     if not add_new_ch:
        #         break
        # return res

        # while True:
        #     arr.sort()
        #     cnt2, ch2 = list(arr[2])
        #     cnt1, ch1 = list(arr[1])
        #     cnt0, ch0 = list(arr[0])
        #     needCheck = False
        #     if cnt2 != 0:
        #         if len(res) > 0 and res[-1] == ch2:
        #             pass
        #         else:
        #             if cnt2 >= 2:
        #                 cnt2 -= 2
        #                 res += ch2 * 2
        #             else:
        #                 cnt2 -= 1
        #                 res += ch2
        #     else:
        #         pass
        #
        #     if cnt1 >= 1 and res[-1] != ch1:
        #         cnt1 -= 1
        #         res += ch1
        #     elif cnt0 >= 1 and res[-1] != ch0:
        #         cnt0 -= 1
        #         res += ch0
        #     else:
        #         break
        #
        #     arr[2] = (cnt2, ch2)
        #     arr[1] = (cnt1, ch1)
        #     arr[0] = (cnt0, ch0)
        # return res


def tst(a: int, b: int, c: int):
    print(Solution().longestDiverseString(a, b, c))


if __name__ == '__main__':
    tst(1, 1, 7)
    # tst(1, 4, 5)
    # tst(0, 8, 11)
    # tst(3, 0, 4)


        # arr = [a, b, c]
        # arr.sort()
        # a, b, c = arr
        # cnt_a, cnt_b, cnt_c = a, b, c





        #
        # cnt_a, cnt_b, cnt_c = a, b, c
        # while cnt_a and cnt_b and cnt_c:



        # if 2 * (a + b + 1) <= c:
        #     # return ''.join(str(i) for i in (c, c, a, c, c, b, c, c))
        #     res = ''
        #     cnt_a, cnt_b = a, b
        #     for _ in range(a + b):
        #         res += f'{c}{c}'
        #         if cnt_a > 0:
        #             res += str(a)
        #             cnt_a -= 1
        #         elif cnt_b > 0:
        #             res += str(b)
        #             cnt_b -= 1
        #     res += f'{c}{c}'
        #     return res



