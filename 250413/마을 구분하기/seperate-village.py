n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
dxs = [-1,1,0,0]
dys = [0,0,-1,1]

visited = [[0 for _ in range(n)] for _ in range(n)]

def is_range(x,y):
    if 0<=x<n and 0<=y<n:
        return True
    return False
def dfs(x,y):
    global num
    visited[x][y] = 1
    num += 1
    for dx, dy in zip(dxs,dys):
        nx = x + dx ; ny = y + dy
        if is_range(nx,ny) and grid[nx][ny] == 1 and visited[nx][ny] == 0:
            dfs(nx,ny)

cnt = 0
Target = []
for i in range(n):
    for j in range(n):
        if grid[i][j] == 1 and visited[i][j] == 0:
            num = 0
            dfs(i,j)
            cnt += 1
            Target.append(num)
print(cnt)
for t in sorted(Target):
    print(t)