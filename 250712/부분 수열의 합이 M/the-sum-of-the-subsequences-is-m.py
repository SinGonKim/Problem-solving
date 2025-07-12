n, m = map(int, input().split())
coin = list(map(int, input().split()))

# Please write your code here.
import sys
import copy
INF = sys.maxsize
dp = [INF for _ in range(m+1)]
dp[0] = 0
stack = [0]
for j in range(n):
    tmp = set()
    tp = copy.deepcopy(dp)
    for i in stack:
        if i + coin[j] > m: continue
        dp[i+coin[j]] = min(dp[i+coin[j]], tp[i] + 1)
        tmp.add(i+coin[j])
    stack = stack + list(tmp)
ans = dp[m]
if ans == INF:
    ans = -1
print(ans)
