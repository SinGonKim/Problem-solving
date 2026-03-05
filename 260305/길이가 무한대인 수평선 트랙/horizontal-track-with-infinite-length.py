n, t = map(int, input().split())
from sortedcontainers import SortedSet

S = SortedSet()

for i in range(n):
    s, v = map(int, input().split())
    S.add((s,v))

# Please write your code here.
group = 0
leader = None

for i in range(len(S)-1, -1, -1):
    x, v = S[i]
    d = x + v * t
    idx = S.bisect_left((d,0))
    if leader is None or d < leader:
        group += 1
        leader = d
print(group)