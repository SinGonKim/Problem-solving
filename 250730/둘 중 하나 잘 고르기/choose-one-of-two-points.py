n = int(input())
red = [0]
blue = [0]

for _ in range(2 * n):
    r, b = map(int, input().split())
    red.append(r)
    blue.append(b)

# Please write your code here.
dp = [[0 for _ in range(n+1)] for _ in range(n+1)]


for i in range(1,2*n+1):
    r = red[i]; b = blue[i]
    for j in range(min(i,n)):
        if i-j-1>n:continue
        dp[j+1][i-j-1] = max(dp[j][i-j-1]+r, dp[j+1][i-j-1])
        dp[i-j-1][j+1] = max(dp[i-j-1][j]+b, dp[i-j-1][j+1])
print(dp[n][n])
