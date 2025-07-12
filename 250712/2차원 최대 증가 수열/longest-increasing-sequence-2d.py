n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
dp = [[0]*m for _ in range(n)]
dp[0][0] = 1

for i in range(1,n):
    for j in range(1,m):

        if grid[i][j] <= grid[0][0]:continue
        else:
            dp[i][j] = 2
        
        for q in range(1,i):
            for w in range(1,j):
                if grid[i][j] > grid[q][w]:
                    dp[i][j] = max(dp[i][j], dp[q][w] + 1)
max_value = 0
for i in range(n):
    for j in range(m):
        max_value = max(max_value, dp[i][j])
print(max_value)