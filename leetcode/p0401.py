# https://leetcode.cn/problems/binary-watch/?envType=daily-question&envId=2026-02-17
from typing import List, Tuple


class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        seq_to_time = [1, 2, 4, 8, 1, 2, 4, 8, 16, 32]
        ans: List[int] = []

        def get_time_str(time: Tuple[int, int]) -> str:
            if time[1] < 10:
                minute_str = '0' + str(time[1])
            else:
                minute_str = str(time[1])
            return str(time[0]) + ':' + minute_str

        def backtrack(start: int, remain: int, time: Tuple[int, int]):
            if remain == 0:
                if time[0] > 11 or time[1] > 59:
                    return
                ans.append(get_time_str(time))
                return

            for i in range(start, len(seq_to_time)):
                new_hour, new_min = time
                if i < 4:
                    new_hour += seq_to_time[i]
                else:
                    new_min += seq_to_time[i]
                backtrack(i + 1, remain - 1, (new_hour, new_min))

        backtrack(0, turnedOn, (0, 0))
        return ans



    # def readBinaryWatch(self, turnedOn: int) -> List[str]:
    #
    #     def count1(time: int) -> int:
    #         return time.bit_count()
    #
    #     ans: List[str] = []
    #     for hour in range(12):
    #         for minute in range(60):
    #             if count1(hour) + count1(minute) == turnedOn:
    #                 hour_str = str(hour)
    #                 if minute < 10:
    #                     minute_str = '0' + str(minute)
    #                 else:
    #                     minute_str = str(minute)
    #                 ans.append(hour_str + ':' + minute_str)
    #     return ans





