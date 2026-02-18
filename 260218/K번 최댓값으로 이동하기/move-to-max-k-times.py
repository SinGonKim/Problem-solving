n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c = map(lambda a: int(a) - 1, input().split())

# Please write your code here.
from collections import deque

def is_range(x, y):
    return 0 <= x < n and 0 <= y < n

def can_go(x, y):
    return is_range(x, y) and visited[x][y] == False 

def bfs(row, col):

    dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]

    que = deque()
    adjacent = []

    que.append((row, col))
    visited[row][col] = True

    while que:
        x, y = que.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if can_go(nx, ny) and grid[nx][ny] < grid[row][col]:
                que.append((nx, ny))
                adjacent.append((nx, ny))
                visited[nx][ny] = True
    return adjacent

for _ in range(k):
    visited = [[False for _ in range(n)] for _ in range(n)]
    result = bfs(r, c)

    if not result:break

    mx = -1
    for x, y in result:
        mx = max(mx, grid[x][y])
    
    nx, ny = -1, -1
    for i in range(n):
        for j in range(n):
            if grid[i][j] == mx and (i,j) in result:
                nx, ny = i, j
                break
        if nx != -1:break
    r, c = nx, ny

print(r+1, c+1)