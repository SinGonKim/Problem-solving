n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
from collections import deque
visited = [[0 for _ in range(m)] for _ in range(n)]

def is_range(x,y):
    if 0<=x<n and 0<=y<m:
        return True
    return False
def bfs():

    que = deque()
    dxs = [-1, 1, 0, 0]
    dys = [0, 0, -1, 1]
    visited[0][0] = 1
    que.append((0,0))

    while len(que):
        x, y = que.popleft()
        if x == n-1 and y == m-1:
            return 1

        for dx, dy in zip(dxs, dys):
            nx = x + dx; ny = y + dy
            if is_range(nx,ny) and visited[nx][ny] == 0 and a[nx][ny] == 1:
                visited[nx][ny] = 1
                que.append((nx,ny))
    return 0
ans = bfs()
print(ans)