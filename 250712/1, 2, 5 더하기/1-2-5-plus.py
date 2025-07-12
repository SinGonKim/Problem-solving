n = int(input())
coin = [1,2,5]
mod = 10007
# Please write your code here.
dp = [0 for _ in range(n+1)]
dp[0] = 1
for i in range(n+1):
    for j in range(len(coin)):
        if i - coin[j] <0: continue
        dp[i] = (dp[i] + dp[i-coin[j]])%mod
print(dp[n]) 