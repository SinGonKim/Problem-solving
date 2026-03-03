n = int(input())
queries = list(map(int, input().split()))

# Please write your code here.
from sortedcontainers import SortedSet
import sys
INF = sys.maxsize

s = SortedSet()
s.add(0)
min_dist = INF

for query in queries:
    r_idx = s.bisect_right(query)

    l_idx = s.bisect_right(query)

    if r_idx == len(s):
        value = query - s[-1]
    elif l_idx == 0:
        value = s[0] - query
    else:
        value = min(abs(query-s[l_idx-1]), abs(s[r_idx] - query))
    if min_dist > value:
        min_dist = value
    s.add(query)
    print(min_dist)
