from sortedcontainers import SortedSet

n, m = map(int, input().split())
arr = SortedSet(map(int, input().split()))
queries = [int(input()) for _ in range(m)]

# Please write your code here.
n = len(arr)
for query in queries:
    if arr.bisect_left(query) < n:
        print(arr[arr.bisect_left(query)])
    else:
        print(-1)