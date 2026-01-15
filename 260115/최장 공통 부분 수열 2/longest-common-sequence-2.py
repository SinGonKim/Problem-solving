A = " " + input().strip()
B = " " + input().strip()

# Please write your code here.
a = len(A)
b = len(B)
dp = [["" for _ in range(b)] for _ in range(a)]


for i in range(1,a):
    for j in range(1,b):
        if A[i] == B[j]:
            if len(dp[i][j]) < len(dp[i-1][j-1]) + 1:
                dp[i][j] = dp[i-1][j-1] + A[i]
        else:
            if len(dp[i-1][j]) > len(dp[i][j]):
                dp[i][j] = dp[i-1][j]
            if len(dp[i][j-1]) > len(dp[i][j]):
                dp[i][j] = dp[i][j-1]
            if len(dp[i-1][j-1]) > len(dp[i][j]):
                dp[i][j] = dp[i-1][j-1]

print(dp[a-1][b-1])