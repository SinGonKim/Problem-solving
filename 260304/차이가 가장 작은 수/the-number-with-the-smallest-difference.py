n, m = map(int, input().split())
from sortedcontainers import SortedSet
s = SortedSet([int(input()) for _ in range(n)])

# Please write your code here.
n = len(s)
import sys
answer = sys.maxsize
for i in range(n-1):
    min_idx = s.bisect_left(s[i]+m)
    if min_idx == n:break
    answer =  min(s[min_idx] - s[i], answer)

print(-1 if answer == sys.maxsize else answer)