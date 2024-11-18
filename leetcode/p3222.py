# https://leetcode.cn/problems/find-the-winning-player-in-coin-game/description/?envType=daily-question&envId=2024-11-05
class Solution:
    def losingPlayer(self, x: int, y: int) -> str:
        cur_player = 0
        while x > 0 and y >= 4:
            x -= 1
            y -= 4
            cur_player = 1 - cur_player
        if cur_player == 1:
            return 'Alice'
        else:
            return 'Bob'

