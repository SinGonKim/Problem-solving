n = int(input())
a = [0] + list(map(int, input().split()))

# Please write your code here.
dp = [0 for _ in range(n+1)]
for i in range(1,n+1):
    dp[i] = max(dp[i-1]+a[i], a[i])
print(max(dp[1:]))
