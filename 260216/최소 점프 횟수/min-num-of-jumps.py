import sys
n = int(input())
num = [0] + list(map(int, input().split()))

# Please write your code here.
dp = [-1 for _ in range(n+1)]


def solve(idx):
    if idx == n:
        return
    if num[idx] == 0:
        return
    
    for l in range(num[idx], 0, -1):
        if idx + l > n:continue
        dp[idx+l] = min(dp[idx+l] if dp[idx+l] != -1 else sys.maxsize, dp[idx] + 1)
        solve(idx + l)

dp[1] = 0
solve(1)

print(dp[n])