n = int(input())
mod = 1000000007
# Please write your code here.
dp = [0 for _ in range(1001)]
dphalf = [0 for _ in range(1001)]
dp[0] = 1
dp[1] = 2
dp[2] = 7

dphalf[1] = 1
dphalf[2] = 3

for i in range(3,n+1):
    dp[i] = (2*dp[i-1] + dp[i-2] +dphalf[i-1]*2)%mod
    dphalf[i] = (dp[i-1] + dphalf[i-1])%mod
print(dp[n])