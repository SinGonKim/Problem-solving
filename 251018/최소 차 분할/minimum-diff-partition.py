n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
import sys
INT_MAX = sys.maxsize

s = sum(arr)
dp = [0 for _ in range(s+1)]
dp[0] = 1

for i in range(n):
    for j in range(s,0,-1):
        if j >= arr[i] and dp[j-arr[i]]:
            dp[j] = 1
ans = INT_MAX
for i in range(1,s+1):
    if dp[i]:
        ans = min(ans, abs(s-2*i))
print(ans)