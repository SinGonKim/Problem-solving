n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
visited = [[0 for _ in range(m)] for _ in range(n)]

dxs = [0,1] ; dys = [1,0]

def is_range(x,y):
    if 0<=x<n and 0<=y<m:
        return True
    return False

def dfs(x,y):
    visited[x][y] = 1
    if x == n-1 and y == m-1:
        return
    for dx, dy in zip(dxs,dys):
        nx = x +dx ; ny = y + dy
        if is_range(nx,ny) and grid[nx][ny] == 1:
            dfs(nx,ny)

dfs(0,0)
if visited[n-1][m-1]:
    print(1)
else:
    print(0)

