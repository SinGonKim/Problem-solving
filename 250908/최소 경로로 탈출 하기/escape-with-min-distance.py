n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
from collections import deque
import sys
INF = sys.maxsize

def in_range(x,y):
    if 0<=x<n and 0<=y<m:
        return True
    return False
def bfs(x,y):
    que = deque()
    que.append((0,0,0))
    visited = [[INF for _ in range(m)] for _ in range(n)]
    visited[0][0] = 0

    dxs = [-1, 1, 0 ,0]
    dys = [0, 0, -1, 1]
    while que:
        x, y, c = que.popleft()

        for dx, dy in zip(dxs, dys):
            nx = x +dx; ny = y + dy
            if not in_range(nx,ny):continue
            if nx == n-1 and ny == m-1:
                return c+1
            if a[nx][ny] == 1 and visited[nx][ny] >c+1:
                visited[nx][ny] = c + 1
                que.append((nx,ny,c+1))
    return -1

ans = bfs(0,0)
print(ans)

