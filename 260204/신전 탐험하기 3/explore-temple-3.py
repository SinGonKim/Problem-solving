n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
dp = [[0 for _ in range(m)] for _ in range(n)] # i층에서 j번째 선택했을 때 maximum

for i in range(m):
    dp[0][i] = a[0][i]

for i in range(1,n):
    for j in range(m):
        for k in range(m):
            if j == k: continue
            dp[i][j] = max(dp[i][j], dp[i-1][k] + a[i][j])
print(max(dp[n-1]))

