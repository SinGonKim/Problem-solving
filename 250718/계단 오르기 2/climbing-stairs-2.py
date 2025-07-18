n = int(input())
coin = [0] + list(map(int, input().split()))

# Please write your code here.
dp = [[-1 for _ in range(4)] for _ in range(n+1)]

dp[0][0] = 0; dp[1][1] = coin[1]

for i in range(2,n+1):
    if dp[i-2][0] != -1:
        dp[i][0] = dp[i-2][0] + coin[i]
    
    for j in range(1,4):
        dp[i][j] = max(dp[i-1][j-1], dp[i-2][j])
        if dp[i][j] != -1:
            dp[i][j] += coin[i]
print(max(dp[-1]))
        