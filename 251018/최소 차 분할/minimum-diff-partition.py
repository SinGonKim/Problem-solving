n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
import sys
INT_MAX = sys.maxsize

s = sum(arr)
dp = [[0 for _ in range(s+1)] for _ in range(n+1)]

dp[0][0] = 1

for i in range(1,n+1):
    for j in range(s+1):
        if j >= arr[i-1] and dp[i-1][j-arr[i-1]]:
            dp[i][j] = 1
        if dp[i-1][j]:
            dp[i][j] = 1

ans = INT_MAX
for i in range(1,s):
    if dp[n][i]:
        ans = min(ans, abs(s-2*i))
print(ans)