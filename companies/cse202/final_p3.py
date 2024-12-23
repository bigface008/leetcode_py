from typing import List, Tuple

import utils


def count_smaller_to_left(arr) -> Tuple[List[int], List[int]]:
    def dfs2(indices: List[int], start: int, end: int):
        if start >= end:
            return

        mid = (start + end) // 2
        dfs2(indices, start, mid)
        dfs2(indices, mid + 1, end)

        left = start
        right = mid + 1
        temp = []
        num_right_smaller = 0

        while left <= mid and right <= end:
            if arr[indices[left]] > arr[indices[right]]:
                num_right_smaller += 1
                temp.append(indices[right])
                right += 1
            else:
                post[indices[left]] += num_right_smaller
                temp.append(indices[left])
                left += 1

        while left <= mid:
            post[indices[left]] += num_right_smaller
            temp.append(indices[left])
            left += 1

        while right <= end:
            temp.append(indices[right])
            right += 1

        indices[start:end + 1] = temp

    def dfs(indices: List[int], start: int, end: int):
        if start >= end:
            return

        mid = (start + end) // 2
        dfs(indices, start, mid)
        dfs(indices, mid + 1, end)

        left = start
        right = mid + 1
        temp = []
        num_left_smaller = 0

        while left <= mid and right <= end:
            if arr[indices[left]] < arr[indices[right]]:
                num_left_smaller += 1
                temp.append(indices[left])
                left += 1
            else:
                prev[indices[right]] += num_left_smaller
                temp.append(indices[right])
                right += 1

        while left <= mid:
            temp.append(indices[left])
            left += 1

        while right <= end:
            prev[indices[right]] += num_left_smaller
            temp.append(indices[right])
            right += 1

        indices[start:end + 1] = temp

    n = len(arr)
    prev = [0] * n
    post = [0] * n
    dfs(list(range(n)), 0, n - 1)
    dfs2(list(range(n)), 0, n - 1)
    print(f'ans={arr} prev={prev} post={post}')
    return prev, post


def count_smaller_elements(arr):
    def dfs(indices: List[int], start: int, end: int):
        if start >= end:
            return

        mid = (start + end) // 2
        dfs(indices, start, mid)
        dfs(indices, mid + 1, end)

        left = start
        right = mid + 1
        temp = []
        num_left_smaller = 0
        num_right_smaller = 0

        while left <= mid and right <= end:
            if arr[indices[left]] <= arr[indices[right]]:
                left_counts[indices[left]] += num_right_smaller
                temp.append(indices[left])
                left += 1
            else:
                num_right_smaller += 1
                temp.append(indices[right])
                right += 1

        while left <= mid:
            left_counts[indices[left]] += num_right_smaller
            temp.append(indices[left])
            left += 1

        while right <= end:
            right_counts[indices[right]] += num_left_smaller
            temp.append(indices[right])
            right += 1

        indices[start:end + 1] = temp

    n = len(arr)
    left_counts = [0] * n
    right_counts = [0] * n
    indices = list(range(n))
    dfs(indices, 0, n - 1)
    print(f'arr={arr} left_counts={left_counts} right_counts={right_counts}')
    return left_counts, right_counts


def dfs(nums: List[int], left: int, right: int) -> int:
    if left >= right:
        return 0
    mid = (left + right) // 2
    ans = dfs(nums, left, mid) + dfs(nums, mid + 1, right)

    # Merge & Sort
    i, j = left, mid + 1
    temp = []
    left_smaller_cnt = 0
    # while i <= mid and j <= right:
    #     if nums[]
    # N2 = right - left + 1
    # temp = [0] * N2
    # j = mid + 1
    # for i in range(left, mid + 1):
    #     while j <= right and nums[i] >= nums[j]:
    #         temp.append(nums[j])
    #         j = j + 1
    #     ans = ans + (right - j + 1)
    #     temp.append(nums[i])
    #
    # while j <= right:
    #     temp.append(nums[j])
    #     j = j + 1

    # Write back the sorted array
    for i in range(left, right + 1):
        nums[i] = temp[i - left]
    print(f'left={left} right={right} ans={ans}')
    return ans


def check(nums: List[int]):
# def check(nums: List[int], expect1: List[int], expect2: List[int]):
    temp = nums.copy()
    output = count_smaller_to_left(temp)
    # output = dfs(temp, 0, len(temp) - 1)
    # utils.tst(f'nums={nums}', output, expect)


if __name__ == '__main__':
    check([1, 3, 2, 3, 1])
    # check([1, 3, 2, 3, 1], [0, 1, 1, 2, 0], [0, 2, 1, 1, 0])
    check([1, 0, 1])
    check([1, 2, 3, 4, 5, 6])
    check([6, 5, 4, 3, 2, 1])
    check([1, 2, 3, 2, 1])
    check([1, 2, 3, 2, 1, 0, -1, -2, -3])
