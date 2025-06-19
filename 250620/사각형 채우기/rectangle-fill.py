n = int(input())

# Please write your code here.
dp = [0 for _ in range(n+1)]
dp[1] = 1
if n >=2:
    dp[2] = 2
if n>=3:
    dp[3]= 3
if n>=4:
    for i in range(4,n+1):
        dp[i] = (dp[i-2] + dp[i-1])%10007
print(dp[n])
