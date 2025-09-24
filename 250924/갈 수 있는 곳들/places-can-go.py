n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
points = [tuple(map(int, input().split())) for _ in range(k)]

# Please write your code here.
answer = 0
visited = [[0 for _ in range(n)] for _ in range(n)]

from collections import deque

def is_range(x, y):
    if 0<=x<n and 0<=y<n:
        return True
    return False


def bfs(x,y):
    cnt = 0
    que = deque()
    que.append((x,y))
    visited[x][y] = 1
    cnt += 1

    dxs = [0, 0, -1, 1]
    dys = [-1, 1, 0, 0]

    while que:
        cx, cy = que.popleft()
        for dx, dy in zip(dxs, dys):
            nx = cx + dx; ny = cy + dy

            if is_range(nx,ny) and grid[nx][ny] == 0 and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                cnt += 1
                que.append((nx,ny))
    return cnt

for point in points:
    x, y = point[0]-1, point[1]-1
    if visited[x][y] == 0 and grid[x][y] == 0:
        res = bfs(x,y)
        answer += res
print(answer)

