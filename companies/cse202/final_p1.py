1.
prev = [0] * N
2.
for i < - 1 to N - 1:
# Binary search the result.
3.
start < - prev[i - 1]
4.
end < - i

5.
while start <= end:
    6.
    mid < - (start + end) / 2
7.
if nums[i] - nums[mid] >= L:
    8.
    start < - mid + 1
9. else:
10.
end < - mid - 1