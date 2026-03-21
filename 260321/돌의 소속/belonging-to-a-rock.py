N, Q = map(int, input().split())
arr = [int(input()) for _ in range(N)]
queries = [tuple(map(int, input().split())) for _ in range(Q)]

# Please write your code here.
pre_sum = [[0 for _ in range(4)] for _ in range(N+1)]
for i in range(N):
    for j in range(1,4):
        pre_sum[i+1][j] = pre_sum[i][j]
    pre_sum[i+1][arr[i]] += 1

for query in queries:
    s, e = query
    for j in range(1, 4):
        res = pre_sum[e][j] - pre_sum[s-1][j]
        print(res, end = ' ')
    print()