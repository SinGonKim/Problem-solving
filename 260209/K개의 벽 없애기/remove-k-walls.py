n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())

r1 -= 1
c1 -= 1
r2 -= 1
c2 -= 1

# Please write your code here.
from collections import deque

def is_range(x,y):
    return 0<=x<n and 0<=y<n


def bfs():
    dxs = [-1, 1, 0, 0]
    dys = [0, 0, -1, 1]
    que = deque()
    que.append((r1,c1,k,0))
    visited = [[[-1]*(k+1) for _ in range(n)] for _ in range(n)]
    visited[r1][c1][k] = 0

    while que:
        x, y, num, cnt = que.popleft()
        
 
        if x == r2 and y == c2:
            return cnt
        
        for dx, dy in zip(dxs, dys):
            nx = x + dx; ny = y + dy
            if is_range(nx,ny):
                if grid[nx][ny] == 0 and visited[nx][ny][num] == -1:
                    visited[nx][ny][num] = cnt + 1
                    que.append((nx, ny, num, cnt + 1))
                elif num > 0 and visited[nx][ny][num-1] == -1:
                    visited[nx][ny][num-1] = cnt + 1
                    que.append((nx,ny,num-1, cnt+1))

    return -1

ans = bfs()

print(ans)
