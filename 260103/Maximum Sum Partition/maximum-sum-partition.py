n = int(input())
arr = [0] + list(map(int, input().split()))

# Please write your code here.
import sys
INT_MIN = -sys.maxsize
m = sum(arr)
offset = m
dp = [[0 for _ in range(2*m+1)] for _ in range(n+1)]

for i in range(n+1):
    for j in range(-m,m+1):
        dp[i][j+offset] = INT_MIN
dp[0][0+offset] = 0

for i in range(1,n+1):
    for j in range(-m,m+1):
        if -m<=j-arr[i]<=m and dp[i-1][j-arr[i]+offset] != INT_MIN:
            dp[i][j+offset] = max(dp[i][j+offset], dp[i-1][j-arr[i]+offset] + arr[i])

        if -m<=j+arr[i]<=m and dp[i-1][j+arr[i]+offset] != INT_MIN:
            dp[i][j+offset] = max(dp[i][j+offset], dp[i-1][j+arr[i]+offset])

        if dp[i-1][j+offset] != INT_MIN:
            dp[i][j+offset] = max(dp[i][j+offset], dp[i-1][j+offset])


print(dp[n][0+offset])