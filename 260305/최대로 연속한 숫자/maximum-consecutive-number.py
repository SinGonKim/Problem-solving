import sys
from sortedcontainers import SortedSet, SortedList

input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

s = SortedList()

# 경계 추가
s.add(-1)
s.add(n+1)

# 구간 길이 관리
lengths = SortedList([n+1])

for x in arr:
    pos = s.bisect_left(x)

    left = s[pos-1]
    right = s[pos]

    # 기존 구간 제거
    lengths.remove(right - left - 1)

    # 새 구간 추가
    lengths.add(x - left - 1)
    lengths.add(right - x - 1)
    s.add(x)
    print(lengths[-1])