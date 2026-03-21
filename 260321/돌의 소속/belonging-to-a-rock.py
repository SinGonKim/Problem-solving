N, Q = map(int, input().split())
arr = [int(input()) for _ in range(N)]
queries = [tuple(map(int, input().split())) for _ in range(Q)]

# Please write your code here.
pre_sum = [[0 for _ in range(N+1)] for _ in range(4)]
for i in range(N):
    for j in range(1,4):
        pre_sum[j][i+1] = pre_sum[j][i]
    pre_sum[arr[i]][i+1] += 1

for query in queries:
    s, e = query
    for j in range(1, 4):
        res = pre_sum[j][e] - pre_sum[j][s-1]
        print(res, end = ' ')
    print()