n, m = map(int, input().split())

# Store points as list of tuples
points = [tuple(map(int, input().split())) for _ in range(n)]

# Store queries as list of tuples
queries = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
from sortedcontainers import SortedSet

s = SortedSet(points)

for query in queries:
    idx = s.bisect_left(query)
    if idx == 0:
        print(-1, -1)
    elif idx == n:
        print(-1, -1)
    else:
        x, y = s[idx]
        print(x, y)