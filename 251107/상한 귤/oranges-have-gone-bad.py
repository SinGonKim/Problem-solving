n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
visited = [[-1]*n for _ in range(n)]
S = []
for i in range(n):
    for j in range(n):
        if grid[i][j] == 2:
            S.append((i,j))



from collections import deque

def bfs():
    que = deque()
    for s in S:
        que.append(s)
        visited[s[0]][s[1]] = 0
    
    dxs = [-1,1,0,0]
    dys = [0,0,-1,1]
    while que:
        x, y = que.popleft()
        for dx, dy in zip(dxs,dys):
            nx = x + dx ; ny = y + dy
            if 0<=nx<n and 0<=ny<n and visited[nx][ny] == -1 and grid[nx][ny]==1:
                visited[nx][ny] = visited[x][y] + 1
                que.append((nx,ny))


bfs()

for i in range(n):
    for j in range(n):
        if visited[i][j] == -1 and grid[i][j] == 1:
            visited[i][j] = -2

for i in range(n):
    print(*visited[i])