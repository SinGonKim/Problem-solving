n = int(input())
m = list(map(int, input().split()))

# Please write your code here.
dp = [0 for _ in range(n)]
dp[0] = 1
for i in range(1,n):
    for j in range(i):
        if m[i] > m[j]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))

