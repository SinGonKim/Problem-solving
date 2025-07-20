n, k = map(int, input().split())
numbers = [0] + list(map(int, input().split()))
import sys
INF = sys.maxsize
# Please write your code here.
dp = [[-INF for _ in range(k+1)] for _ in range(n+1)]

# 초기화: 첫 번째 숫자(numbers[1])
if numbers[1] >= 0:
    dp[1][0] = numbers[1]
else:
    dp[1][1] = numbers[1]  # K ≥ 1이므로 안전
max_result = max(dp[1])

for i in range(2, n+1):
    for j in range(k+1):
        if numbers[i] >= 0:
            if dp[i-1][j] != -INF:
                dp[i][j] = dp[i-1][j] + numbers[i]
            # i번째 숫자에서 새로운 구간을 시작하는 경우
            if j == 0:
                dp[i][j] = max(dp[i][j], numbers[i])
        else:
            if j>=1:
                if dp[i-1][j-1] != -INF:
                    dp[i][j] = dp[i-1][j-1]+numbers[i]

                dp[i][j] = max(dp[i][j], numbers[i])

    max_result = max(max_result, max(dp[i]))

print(max_result)