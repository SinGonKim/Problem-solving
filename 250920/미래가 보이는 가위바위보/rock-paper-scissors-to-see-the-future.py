N = int(input())
B = [""] + [input() for _ in range(N)]

# Please write your code here.
dp = [[0, 0, 0] for _ in range(N+1)]

for i in range(1,N+1):
    if B[i] == 'H':
        dp[i][0] = dp[i-1][0] + 1
        dp[i][1] = dp[i-1][1]
        dp[i][2] = dp[i-1][2]
    elif B[i] == 'S':
        dp[i][0] = dp[i-1][0]
        dp[i][1] = dp[i-1][1] + 1
        dp[i][2] = dp[i-1][2]
    else:
        dp[i][0] = dp[i-1][0]
        dp[i][1] = dp[i-1][1]
        dp[i][2] = dp[i-1][2] + 1
ans = 0
for i in range(1,N+1):
    ans = max(ans, dp[i][0]+ dp[N][1]-dp[i][1], dp[i][0]+  dp[N][2] - dp[i][2])
    ans = max(ans, dp[i][1]+ dp[N][0]-dp[i][0], dp[i][1]+ dp[N][2] - dp[i][2])
    ans = max(ans, dp[i][2]+ dp[N][1]-dp[i][1], dp[i][2]+ dp[N][0] - dp[i][0])
print(ans)