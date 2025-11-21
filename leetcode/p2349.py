# https://leetcode.com/problems/design-a-number-container-system/?envType=daily-question&envId=2025-02-08
from collections import defaultdict
from sortedcontainers import SortedList


class NumberContainers:

    def __init__(self):
        self.num_2_indices = defaultdict(SortedList)
        self.index_2_num = defaultdict(int)

    def change(self, index: int, number: int) -> None:
        if index in self.index_2_num:
            prev_num = self.index_2_num[index]
            if prev_num != number:
                self.num_2_indices[prev_num].remove(index)
                if not self.num_2_indices[prev_num]:
                    del self.num_2_indices[prev_num]
        if index not in self.num_2_indices[number]:
            self.num_2_indices[number].add(index)
        # self.num_2_indices[number].add(index)
        self.index_2_num[index] = number

    def find(self, number: int) -> int:
        if number not in self.num_2_indices:
            return -1
        return self.num_2_indices[number][0]


if __name__ == '__main__':
    container = NumberContainers()
    container.change(1, 10)
    container.change(1, 10)
    container.change(1, 20)
    container.find(10)


    # container = NumberContainers()
    # container.find(10)
    # container.change(2, 10)
    # container.change(1, 10)
    # container.change(3, 10)
    # container.change(5, 10)
    # container.find(10)
    # container.change(1, 20)
    # container.find(10)