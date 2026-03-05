from sortedcontainers import SortedSet

n, m = map(int, input().split())
sequence = SortedSet(list(map(int, input().split())))
query = list(map(int, input().split()))

# Please write your code here.
for q in query:
    idx = sequence.bisect_left(q)
    if idx == 0:
        if sequence[idx] > q:
            print(-1)
    elif sequence[idx] == q:
        print(sequence[idx])
        sequence.remove(sequence[idx])
    else:
        print(sequence[idx-1])
        sequence.remove(sequence[idx-1])