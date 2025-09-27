N, M = map(int, input().split())
nums = list(map(int, input().split()))

# Please write your code here.
dp = [[0 for _ in range(41)] for _ in range(N+1)]
dp[0][20] = 1
for idx, num in enumerate(nums,1):

    for i in range(41):
        prev = dp[idx-1][i]
        if i-20+num <=20:
            dp[idx][i+num] += prev
        if -20 <= i-20-num:
            dp[idx][i-num] += prev

print(dp[N][M+20])