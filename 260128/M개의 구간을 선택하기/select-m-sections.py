import sys
INF = sys.maxsize

N, M = map(int, input().split())
numbers = list(map(int, input().split()))

# Please write your code here.
# dp[i][j][state]
# i: 현재 인덱스, j: 구간 개수, state: 0(미포함), 1(포함)
dp = [[[-INF]*2 for _ in range(M+1)] for _ in range(N+1)]
dp[0][0][0] = 0
for i in range(1,N+1):
    num = numbers[i-1]
    for j in range(M+1):
        dp[i][j][0] = max(dp[i][j][0], dp[i-1][j][1])
        if j == 0: continue #숫자선택안했으므
        res_extend = dp[i-1][j][1] + num
        res_new = dp[i-1][j-1][0] + num
        dp[i][j][1] = max(res_extend, res_new)
print(max(dp[N][M]))