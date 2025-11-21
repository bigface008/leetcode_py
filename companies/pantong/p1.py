from typing import List
from math import inf


# 1.1	You are climbing a stair case. It takes n steps to reach to the top.
# Each time you can either climb 1 or 2 steps. Write a function with lowest time
# complexity to return how many distinct ways can you climb to the top?

# def climb_stair(n: int) -> int:
#     # dp[i] = dp[i - 1] + dp[i - 2]
#     dp = [0] * (n + 1)
#     for i in range(n + 1):
#         if i == 0:
#             dp[0] = 1
#         elif i == 1:
#             dp[1] = 1
#         else:
#             dp[i] = dp[i - 1] + dp[i - 2]
#     return dp[-1]
def climb_stair(n: int) -> int:
    dp0, dp1 = 1, 1
    for i in range(1, n):
        dp0, dp1 = dp1, dp0 + dp1
    return dp1


# 1.2	Now, each time you can either climb 1 or 2,3…n steps. Write a function
# with lowest time complexity to return how many distinct ways can you climb to
# the top?

# dp[i] = sum(dp[k] for k in 0..<i)
# dp[i] = dp[i-1] + dp[i-2] + ... + dp[0]
#       = 2 * dp[i - 1]
# Examples:
# dp[2] = dp[1] + dp[0] = 2
# dp[3] = dp[2] + dp[1] + dp[0] = 4
# dp[n] = pow(2, n - 1)
def climb_stair_crazy(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    return 1 << (n - 1)


# 2.	Code exercise – Best Time to buy and sell stock
# Say you have an array for which the ith element is the price of a given stock on day i. If you were only permitted to
# complete at most one transaction (one transaction including first buy one share of the stock in one day and then sell
# the one share of the stock in another day), design an algorithm to find the maximum profit with O(n) time complexity

# For each day, we want to find the minimum price among all the previous days.
# So we just need to maintain the previous minimum price and update the maximum
# profit accordingly.
def max_profit(price_list: List[int]):
    prev_min = inf
    ans = 0
    for x in price_list:
        if x > prev_min:
            ans = max(ans, x - prev_min)
        prev_min = min(prev_min, x)
    return ans


# 3.	Code exercise – searching 2D matrix
# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
# Integers in each row are sorted from left to right in ascending order;
# The first integer of each row is greater than the last integer of the previous row.
def search_matrix(matrix: List[List[int]], target: int) -> bool:
    M, N = len(matrix), len(matrix[0])
    start_row, end_row = 0, M
    while start_row < end_row:
        mid = (start_row + end_row) // 2
        row = matrix[mid]
        if row[0] <= target:
            start_row = mid + 1
        else:
            end_row = mid
    if start_row < M and matrix[start_row][0] > target:
        start_row -= 1
    row = matrix[start_row]
    start, end = 0, N
    while start < end:
        mid = (start + end) // 2
        if row[mid] == target:
            return True
        if row[mid] < target:
            start = mid + 1
        else:
            end = mid
    if start < N and row[start] == target:
        return True
    if start - 1 >= 0 and row[start - 1] == target:
        return True
    return False




if __name__ == '__main__':
    # print(max_profit([7, 1, 5, 3, 6, 4]))
    # print(max_profit([7, 6, 4, 3, 1]))
    pass
