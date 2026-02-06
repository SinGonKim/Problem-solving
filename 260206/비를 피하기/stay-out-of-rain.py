from collections import deque
n, h, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

def is_range(x, y):
    return 0<=x<n and 0<=y<n


def bfs():
    stops = [(i,j,0) for i in range(n) for j in range(n) if grid[i][j] == 3]
    que = deque(stops)
    dxs = [-1, 1, 0, 0]
    dys = [0, 0, -1, 1]
    visited = [[-1 for _ in range(n)] for _ in range(n)]
    for stop in stops:
        x, y, cnt = stop
        visited[x][y] = 0
    
    while que:
        x, y, cnt = que.popleft()

        for dx, dy in zip(dxs, dys):
            nx = x + dx; ny = y + dy
            if is_range(nx, ny) and grid[nx][ny] != 1 and visited[nx][ny] == -1:
                visited[nx][ny] = cnt + 1
                que.append((nx,ny,cnt+1))

    for i in range(n):
        for j in range(n):
            if grid[i][j] == 2:
                print(visited[i][j], end = ' ')
            else:
                print(0, end = ' ')
        print()
bfs()