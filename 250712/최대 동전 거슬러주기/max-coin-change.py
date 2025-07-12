N, M = map(int, input().split())
coin = list(map(int, input().split()))

import copy
dp = [0 for _ in range(M+1)]

# Please write your code here.
for i in range(M+1):
    for j in coin:
        if i - j <0: continue
        dp[i] = max(dp[i], dp[i-j]+1)
ans = dp[M]
if ans == 0:
    ans = -1
print(ans)