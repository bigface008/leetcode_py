# https://leetcode.com/problems/walking-robot-simulation-ii/?envType=daily-question&envId=2026-04-07
from typing import List
class Robot:

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.direction = 'E'
        self.x = 0
        self.y = 0

    def step(self, num: int) -> None:
        while num != 0:
            if self.direction == 'E':
                x2 = self.x + num
                if x2 >= self.width:
                    self.direction = 'N'
                    num -= self.width - 1 - self.x
                    self.x = self.width - 1
                else:
                    self.x = x2
                    break
            elif self.direction == 'W':
                x2 = self.x - num
                if x2 < 0:
                    self.direction = 'S'
                    num -= self.x
                    self.x = 0
                else:
                    self.x = x2
                    break
            elif self.direction == 'S':
                y2 = self.y - num
                if y2 < 0:
                    self.direction = 'E'
                    num -= self.y
                    self.y = 0
                else:
                    self.y = y2
                    break
            else:
                y2 = self.y + num
                if y2 >= self.height:
                    self.direction = 'W'
                    num -= self.height - 1 - self.y
                    self.y = self.height - 1
                else:
                    self.y = y2
                    break

    def getPos(self) -> List[int]:
        return [self.x, self.y]

    def getDir(self) -> str:
        if self.direction == 'E':
            return 'East'
        elif self.direction == 'W':
            return 'West'
        elif self.direction == 'S':
            return 'South'
        else:
            return 'North'

    def getNextDirection(self, direction: str) -> str:
        if direction == 'E':
            return 'N'
        elif direction == 'W':
            return 'S'
        elif direction == 'S':
            return 'E'
        else:
            return 'W'

# class Robot:
#
#     def __init__(self, width: int, height: int):
#         self.width = width
#         self.height = height
#         self.direction = 'E'
#         self.x = 0
#         self.y = 0
#
#     def step(self, num: int) -> None:
#         while num != 0:
#             if self.direction == 'E':
#                 x2 = self.x + num
#                 if x2 >= self.width:
#                     self.direction = 'N'
#                     num -= self.width - 1 - self.x
#                     self.x = self.width - 1
#                 else:
#                     self.x = x2
#                     break
#             elif self.direction == 'W':
#                 x2 = self.x - num
#                 if x2 < 0:
#                     self.direction = 'S'
#                     num -= self.x
#                     self.x = 0
#                 else:
#                     self.x = x2
#                     break
#             elif self.direction == 'S':
#                 y2 = self.y - num
#                 if y2 < 0:
#                     self.direction = 'E'
#                     num -= self.y
#                     self.y = 0
#                 else:
#                     self.y = y2
#                     break
#             else:
#                 y2 = self.y + num
#                 if y2 >= self.height:
#                     self.direction = 'W'
#                     num -= self.height - 1 - self.y
#                     self.y = self.height - 1
#                 else:
#                     self.y = y2
#                     break
#
#     def getPos(self) -> List[int]:
#         return [self.x, self.y]
#
#     def getDir(self) -> str:
#         if self.direction == 'E':
#             return 'East'
#         elif self.direction == 'W':
#             return 'West'
#         elif self.direction == 'S':
#             return 'South'
#         else:
#             return 'North'
#
#     def getNextDirection(self, direction: str) -> str:
#         if direction == 'E':
#             return 'N'
#         elif direction == 'W':
#             return 'S'
#         elif direction == 'S':
#             return 'E'
#         else:
#             return 'W'


if __name__ == '__main__':
    robot = Robot(6, 3)
    print(robot.step(2))
    print(robot.step(2))
    print(robot.getPos())
