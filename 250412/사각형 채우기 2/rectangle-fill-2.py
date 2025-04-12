n = int(input())

# Please write your code here.
dp = [0 for _ in range(n+1)]
dp[1] = 1
if n>1:
    dp[2] = 3
if n>2:
    for i in range(3,n+1):
        dp[i] = (dp[i-2]*2 + dp[i-1])%10007
print(dp[n])