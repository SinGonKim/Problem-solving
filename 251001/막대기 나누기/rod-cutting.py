n = int(input())
profit = list(map(int, input().split()))

# Please write your code here.
dp = [0 for _ in range(n+1)]

target = 0
idx = 0
for i, p in enumerate(profit, 1):
    if p/i > target:
        dp[i] = i
        target = p/i
        idx = i
    else:
        dp[i] = idx

L = n
answer = 0
idx = -1

while L:
    answer += (L//dp[idx])*profit[dp[idx]-1]
    L %= dp[idx]
    idx -= 1
print(answer)

