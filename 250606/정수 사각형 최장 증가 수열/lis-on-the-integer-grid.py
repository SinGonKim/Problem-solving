def is_range(x,y):
    return 0<=x<n and 0<=y<n

def simulate(x,y,cnt):
    dxs = [-1,1,0,0]
    dys = [0,0,-1,1]

    for dx, dy in zip(dxs, dys):
        nx = x + dx; ny = y + dy
        if is_range(nx,ny) and grid[nx][ny] > grid[x][y]:
            simulate(nx,ny,cnt+1)
    dp[x][y] = max(dp[x][y], cnt)
    return


if __name__ == "__main__":
    n = int(input())
    grid = [list(map(int, input().split())) for _ in range(n)]

    # Please write your code here.
    dp = [[1 for _ in range(n)] for _ in range(n)]
    visited = [[-1 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if visited[i][j] == -1:
                simulate(i,j,1)
            else:
                row = visited[i][j]//n
                col = visited[i][j]%n
                dp[i][j] = dp[i][j] + dp[row][col]
    target = -1
    for i in range(n):
        for j in range(n):
            target = max(target, dp[i][j])
    print(target) 