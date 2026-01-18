import sys
from bisect import bisect_left, bisect_right
n, q = map(int, input().split())
points = sorted(list(map(int, input().split())))
ranges = [tuple(map(int, input().split())) for _ in range(q)]

# Please write your code here.
for s, e in ranges:
    left_idx = bisect_left(points, s)
    right_idx = bisect_right(points, e)
    print(right_idx-left_idx)