from sortedcontainers import SortedSet

n, m = map(int, input().split())
sequence = SortedSet(list(map(int, input().split())))
query = list(map(int, input().split()))

# Please write your code here.
for q in query:
    idx = sequence.bisect_left(q)
    if idx >= n:
        print(-1)
    elif sequence[idx] == q:
        print(sequence[idx])
        sequence.remove(sequence[idx])
    elif idx <= 0:
        print(-1)
    else:
        print(sequence[idx-1])
        sequence.remove(sequence[idx-1])