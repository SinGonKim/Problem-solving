n = int(input())
coin = [1,2,5]
mod = 10007
# Please write your code here.
dp = [0 for _ in range(n+1)]
dp[0] = 1
for i in range(n+1):
    for j in coin:
        if i + j > n: continue
        dp[i+j] += dp[i]
        dp[i+j]%mod
print(dp[n]) 