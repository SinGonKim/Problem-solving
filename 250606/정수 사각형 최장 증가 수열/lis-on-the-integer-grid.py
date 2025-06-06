def is_range(x,y):
    return 0<=x<n and 0<=y<n

def simulate(x,y,cnt):
    dxs = [-1,1,0,0]
    dys = [0,0,-1,1]
    dp[x][y] = max(dp[x][y], cnt)

    for dx, dy in zip(dxs, dys):
        nx = x + dx; ny = y + dy
        if is_range(nx,ny) and grid[nx][ny] > grid[x][y]:
            if dp[nx][ny] == 0:
                result =  simulate(nx,ny,1)
            else:
                result = dp[nx][ny]
            dp[x][y] = max(dp[x][y], cnt+result)
    return dp[x][y]


if __name__ == "__main__":
    n = int(input())
    grid = [list(map(int, input().split())) for _ in range(n)]

    # Please write your code here.
    dp = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if dp[i][j] == 0:
                simulate(i,j,1)
    
    target = -1
    for i in range(n):
        for j in range(n):
            target = max(target, dp[i][j])
    print(target) 