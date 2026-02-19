n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

def is_range(x, y):
    return 0 <= x < n and 0 <= y < m

def can_go(x, y):
    return is_range(x,y) and a[x][y] == 1 and not visited[x][y]

from collections import deque
que = deque()
visited = [[False for _ in range(m)] for _ in range(n)]

for i in range(n):
    for j in range(m):
        if a[i][j] == 0:
            cnt = 0
            for dx, dy in zip(dxs, dys):
                ni = i + dx; nj = j + dy
                if is_range(ni, nj) and a[ni][nj] == 1:
                    cnt += 1
            if 1 <= cnt < 4:
                que.append((i,j,0))
                visited[i][j] = True
cur_time = 0
res = 0

while que:
    x, y, t = que.popleft()
    if cur_time == t:
        res += 1
    else:
        cur_time += 1
        res = 1
    
    for dx, dy in zip(dxs, dys):
        nx = x + dx; ny = y + dy
        if can_go(nx, ny):
            que.append((nx, ny, t + 1))
            visited[nx][ny] = True
print(cur_time, res)

