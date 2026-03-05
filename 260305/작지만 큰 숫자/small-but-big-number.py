from sortedcontainers import SortedSet

n, m = map(int, input().split())
sequence = SortedSet(list(map(int, input().split())))
query = list(map(int, input().split()))

# Please write your code here.
for q in query:
    idx = sequence.bisect_right(q) - 1   # q 이하의 마지막 위치
    if idx < 0:
        print(-1)
    else:
        print(sequence[idx])
        sequence.pop(idx)                # 인덱스로 제거