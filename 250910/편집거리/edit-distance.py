A = input()
B = input()

# Please write your code here.
n, m = len(A), len(B)


dp = [[1001 for _ in range(m)] for _ in range(n)]

dp[0][0] = 0 if A[0] == B[0] else 1

for i in range(1,m):
    if A[i] == B[0]:
        dp[i][0] = dp[i-1][0]
    else:
        dp[i][0] = dp[i-1][0] + 1

for i in range(1,n):
    if A[0] == B[i]:
        dp[0][i] = dp[0][i-1]
    else:
        dp[0][i] = dp[0][i-1] + 1

for i in range(1,n):
    for j in range(1,m):
        if A[i] == B[j]:
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1]+2)
print(dp[n-1][m-1])