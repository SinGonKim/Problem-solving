n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

def is_range(x, y):
    return 0 <= x < n and 0 <= y < m

def can_go(x, y):
    return is_range(x,y) and visited[x][y] == -1

from collections import deque
que = deque()
visited = [[-1 for _ in range(m)] for _ in range(n)]

for i in range(n):
    if a[i][0] == 0:
        visited[i][0] = 0
        que.append((i,0))
    if a[i][-1] == 0:
        visited[i][-1] = 0
        que.append((i,m-1))

for j in range(m):
    if a[0][j] == 0:
        visited[0][j] = 0
        que.append((0,j))
    if a[-1][j] == 0:
        visited[-1][j] = 0
        que.append((n-1,j))


while que:
    x, y = que.popleft()
    
    for dx, dy in zip(dxs, dys):
        nx = x + dx; ny = y + dy
        if can_go(nx, ny):
            if a[nx][ny] == 0:
                que.append((nx, ny))
                visited[nx][ny] = visited[x][y]
            else:
                que.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1
            
last_time = max(visited[i][j] for i in range(n) for j in range(m))

cnt = 0
for i in range(n):
    for j in range(m):
        if visited[i][j] == last_time:
            cnt += 1
print(last_time, cnt)
