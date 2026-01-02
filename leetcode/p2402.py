# https://leetcode.cn/problems/meeting-rooms-iii/description/?envType=daily-question&envId=2025-12-27
from collections import defaultdict
from typing import List, Dict, Tuple, Optional
import heapq


class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort(key=lambda t: t[0])
        rooms = [(-1, i) for i in range(n)]  # (end_time, room_idx)
        heapq.heapify(rooms)
        book_times_cnt = defaultdict(int)
        curr_time = -1
        for start, end in meetings:
            while start > rooms[0][0]:
                prev_end_time, room_idx = rooms[0]
                heapq.heappop(rooms)
                heapq.heappush(rooms, (start, room_idx))
            prev_end_time, room_idx = rooms[0]
            curr_time = max(curr_time, prev_end_time, start)
            heapq.heappop(rooms)
            book_times_cnt[room_idx] += 1
            next_end_time = (max(start, curr_time) + end - start) if curr_time != -1 else end
            heapq.heappush(rooms, (next_end_time, room_idx))
        ans = -1
        max_book_cnt = -1
        room_indices = list(book_times_cnt.keys())
        room_indices.sort()
        for room_idx in room_indices:
            cnt = book_times_cnt[room_idx]
            if cnt > max_book_cnt:
                max_book_cnt = cnt
                ans = room_idx
        return ans


if __name__ == '__main__':
    # print(Solution().mostBooked(3, [[1, 20], [2, 10], [3, 5], [4, 9], [6, 8]]))
    print(Solution().mostBooked(4, [[18, 19], [3, 12], [17, 19], [2, 13], [7, 10]]))
    # print(Solution().mostBooked(2, [[0, 10], [1, 2], [12, 14], [13, 15]]))
