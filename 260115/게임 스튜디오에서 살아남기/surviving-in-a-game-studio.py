n = int(input())

# Please write your code here.
dp = [[[0 for _ in range(3)] for _ in range(3)] for _ in range(n+1)]
dp[0][0][0] = 1
for day in range(1,n+1):
    for t in range(3): # 누적 T
        dp[day][0][t] += (dp[day-1][0][t] + dp[day-1][1][t] + dp[day-1][2][t]) # day = G
        dp[day][1][t] += (dp[day-1][0][t]) # day = B and 연속 1개
        dp[day][2][t] += (dp[day-1][1][t]) # day = B and 연속 2개
        if t < 2:
            dp[day][0][t+1] += (dp[day-1][0][t] + dp[day-1][1][t] + dp[day-1][2][t]) # day = T
        dp[day][0][t] %= 10**9 + 7
        dp[day][1][t] %= 10**9 + 7
        dp[day][2][t] %= 10**9 + 7
            
answer = 0
for b in range(3):
    for t in range(3):
        answer += dp[n][b][t]
answer %= 10**9 + 7
print(answer)
