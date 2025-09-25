n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [int(input()) for _ in range(m)]

# Please write your code here.
from bisect import bisect_left, bisect_right
for querry in queries:
    min_idx = bisect_left(arr, querry)
    max_idx = bisect_right(arr, querry)
    print(max_idx-min_idx)
