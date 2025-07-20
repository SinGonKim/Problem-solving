n, k = map(int, input().split())
numbers = [0] + list(map(int, input().split()))
import sys
INF = sys.maxsize
# Please write your code here.
dp = [[-INF for _ in range(k+1)] for _ in range(n+1)]

for i in range(n+1):
    if numbers[i] >= 0:
        dp[i][0] = numbers[i]
    else:
        dp[i][1] = numbers[i]
max_result = max(dp[0])

for i in range(1, n+1):
    for j in range(k+1):
        if numbers[i] >= 0:
            if dp[i-1][j] != -INF:
                dp[i][j] = dp[i-1][j] + numbers[i]
            # i번째 숫자에서 새로운 구간을 시작하는 경우
            dp[i][j] = max(dp[i][j], numbers[i])
        else:
            if j>=1:
                if dp[i-1][j-1] == -INF:
                    dp[i][j] = max(dp[i][j], numbers[i])
                else:
                    dp[i][j] = max(dp[i-1][j-1]+numbers[i], numbers[i])
    max_result = max(max_result, max(dp[i]))

print(max_result)