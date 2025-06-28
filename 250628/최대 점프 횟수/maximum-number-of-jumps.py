n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
import sys
input = sys.stdin.readline
INF = sys.maxsize

dp = [-INF for _ in range(n)]

dp[0] = 0

for i in range(1,n):
    for j in range(i):
        if j + arr[j] >= i:
            dp[i] = max(dp[j]+1, dp[i])
print(max(dp))
