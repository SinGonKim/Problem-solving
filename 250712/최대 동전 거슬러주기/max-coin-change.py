N, M = map(int, input().split())
coin = list(map(int, input().split()))

import copy
dp = [-1 for _ in range(M+1)]
dp[0] = 0
# Please write your code here.
for i in range(M+1):
    for j in coin:
        if i - j <0: continue
        elif dp[i-j] == -1: continue
        dp[i] = max(dp[i], dp[i-j]+1)
ans = dp[M]


print(ans)