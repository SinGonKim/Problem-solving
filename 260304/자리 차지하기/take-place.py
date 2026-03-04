import sys
from sortedcontainers import SortedSet

n, m = map(int, input().split())
a = list(map(int, input().split()))

# 비어있는 의자들 1..m
s = SortedSet(range(1, m + 1))

ans = 0
for x in a:
    idx = s.bisect_right(x) - 1
    if idx < 0:
        break  # x 이하에 빈 의자 없음 -> 종료
    seat = s[idx]
    s.remove(seat)
    ans += 1

print(ans)