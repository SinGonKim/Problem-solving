N, M = map(int, input().split())
numbers = [0] + list(map(int, input().split()))

# Please write your code here.
dp = [[-1]*(M+1) for _ in range(N+1)]
dp[0][0] = 0

for i in range(1, N+1):
    for j in range(max(1, i-1)):
        for k in range(i,N+1):
            for l in range(1,M+1):
                if dp[j][l-1] == -1: continue
                dp[k][l] = max(dp[k][l], dp[j][l-1] + sum(numbers[i:k+1]))

print(dp[N][M])
