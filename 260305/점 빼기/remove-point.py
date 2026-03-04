import sys
input = sys.stdin.readline
from sortedcontainers import SortedSet
n, m = map(int, input().split())

# Store points as list of tuples (x, y)
points = SortedSet([tuple(map(int, input().split())) for _ in range(n)])

# Store queries
queries = [int(input()) for _ in range(m)]

# Please write your code here.
for query in queries:
    idx = points.bisect_left((query,0))
    if idx == n:
        print(-1, -1)
    else:
        x = points[idx]
        print(*x)
        points.remove(x)
        n -= 1