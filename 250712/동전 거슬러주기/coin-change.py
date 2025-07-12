n, m = map(int, input().split())
coin = list(map(int, input().split()))
import sys
INF = sys.maxsize
# Please write your code here.
dp = [INF for _ in range(m+1)]
dp[0] = 0
for i in range(1,m+1):
    for j in range(n):
        if i - coin[j] >= 0:
            dp[i] = min(dp[i], dp[i-coin[j]] + 1)
ans = dp[m]

if ans == INF:
    ans = -1
print(ans)
