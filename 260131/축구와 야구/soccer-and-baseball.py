n = int(input())
P = [(0.0)]
for _ in range(n):
    si, bi = map(int, input().split())
    P.append((si,bi))

# Please write your code here.
dp = [[[0]*(n-18) for _ in range(10)] for _ in range(12)]

for idx in range(1,n+1):
    si, bi = P[idx]
    for s in range(min(idx,11)):
        for b in range(min(idx-s,9)):
            for o in range(idx-s-b):
                dp[s+1][b][o] = max(dp[s][b][o]+si, dp[s+1][b][o])
                dp[s][b+1][o] = max(dp[s][b][o]+bi, dp[s][b+1][o])
                dp[s][b][o+1] = max(dp[s][b][o+1], dp[s][b][o])
print(dp[11][9][-1])