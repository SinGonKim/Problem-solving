

def simulate():
    dp = [[0 for _ in range(n)] for _ in range(n)]
    dp[0][0] = grid[0][0]
    for col in range(1,n):
        dp[0][col] = max(dp[0][col-1], grid[0][col])
    for row in range(1,n):
        dp[row][0] = max(dp[row-1][0], grid[row][0])
    
    for row in range(1,n):
        for col in range(1,n):
            dp[row][col] = min(max(grid[row][col],dp[row-1][col]), max(grid[row][col], dp[row][col-1]))
    print(dp[n-1][n-1])
# Please write your code here.
if __name__ == "__main__":
    n = int(input())
    grid = [list(map(int, input().split())) for _ in range(n)]
    simulate()
