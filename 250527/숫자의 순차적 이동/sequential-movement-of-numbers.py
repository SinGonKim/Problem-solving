from collections import defaultdict
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
dxs = [-1,-1,-1,0,0,1,1,1]
dys = [-1,0,1,-1,1,-1,0,1]

pos = defaultdict(list)

for i in range(n):
    for j in range(n):
        pos[grid[i][j]].append([i,j])

def is_range(x,y):
    if 0<=x<n and 0<=y<n:
        return True
    return False

for _ in range(m):

    for k in range(1,n*n+1):
        x, y = pos[k].pop()
        target = -1
        tx, ty = -1, -1
        for dx, dy in zip(dxs, dys):
            nx = x+dx; ny = y + dy
            if is_range(nx,ny) and grid[nx][ny] > target:
                tx = nx; ty = ny
                target = grid[tx][ty]
        pos[target].pop()
        grid[x][y], grid[tx][ty] = grid[tx][ty], grid[x][y]
        pos[k].append([tx,ty])
        pos[target].append([x,y])    
  

        
for i in range(n):    
    print(*grid[i])
