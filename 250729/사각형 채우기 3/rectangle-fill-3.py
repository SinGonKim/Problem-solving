n = int(input())
mod = 1000000007
# Please write your code here.
dp = [0 for _ in range(1001)]
dp[0] = 1
dp[1] = 2
dp[2] = 7
for i in range(3,n+1):
    dp[i] = (2*dp[i-1] + 3*dp[i-2] + 2*dp[i-3])%mod
print(dp[n])