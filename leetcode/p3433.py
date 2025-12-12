# https://leetcode.com/problems/count-mentions-per-user/?envType=daily-question&envId=2025-12-12
from typing import List, Dict, Tuple, Optional
from functools import cmp_to_key


class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        def cmp(t1: Tuple[str, str, str], t2: Tuple[str, str, str]) -> int:
            msg1, time1, info1 = t1
            msg2, time2, info2 = t2
            time1 = int(time1)
            time2 = int(time2)
            if time1 < time2:
                return -1
            elif time1 > time2:
                return 1
            else:
                if msg1 == 'OFFLINE' and msg2 == 'MESSAGE':
                    return -1
                elif msg1 == 'MESSAGE' and msg2 == 'OFFLINE':
                    return 1
                else:
                    return 0

        events.sort(key=cmp_to_key(cmp))
        ans = [0] * numberOfUsers
        offline_time_remain = [0] * numberOfUsers
        all_mention_cnt = 0
        curr_time = 0
        for msg, timestamp, info in events:
            diff = int(timestamp) - curr_time
            if diff != 0:
                for usr_idx, time in enumerate(offline_time_remain):
                    if time != 0:
                        offline_time_remain[usr_idx] = max(0, offline_time_remain[usr_idx] - diff)
            curr_time = int(timestamp)
            if msg == 'MESSAGE':
                if info == 'ALL':
                    all_mention_cnt += 1
                elif info != 'HERE':
                    for uid in info.split():
                        ans[int(uid[2:])] += 1
                else:
                    for usr_idx in range(numberOfUsers):
                        if offline_time_remain[usr_idx] == 0:
                            ans[usr_idx] += 1
            else:
                usr_idx = int(info)
                offline_time_remain[usr_idx] += 60
        for usr_idx in range(numberOfUsers):
            ans[usr_idx] += all_mention_cnt
        return ans


if __name__ == '__main__':
    # print(Solution().countMentions(3, [["MESSAGE", "2", "HERE"], ["OFFLINE", "2", "1"], ["OFFLINE", "1", "0"],
    #                                    ["MESSAGE", "61", "HERE"]]))
    print(Solution().countMentions(5, [["OFFLINE", "28", "1"], ["OFFLINE", "14", "2"], ["MESSAGE", "2", "ALL"],
                                       ["MESSAGE", "28", "HERE"], ["OFFLINE", "66", "0"], ["MESSAGE", "34", "id2"],
                                       ["MESSAGE", "83", "HERE"], ["MESSAGE", "40", "id3 id3 id2 id4 id4"]]))
