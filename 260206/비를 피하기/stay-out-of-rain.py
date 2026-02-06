from collections import deque

n, h, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
people = []
for row in range(len(grid)):
    for col in range(len(grid[0])):
        if grid[row][col] == 2:
            people.append((row,col))
answers = [[0 for _ in range(n)] for _ in range(n)]

def is_range(x,y):
    return 0<=x<n and 0<=y<n

def bfs(p:tuple):
    dxs = [-1, 1, 0, 0]
    dys = [0, 0, -1, 1]

    que = deque()
    p_row, p_col = p
    que.append((p_row, p_col, 0))
    visited = [[False for _ in range(n)] for _ in range(n)]
    visited[p_row][p_col] = 1

    while que:
        x, y, cnt = que.popleft()
        for dx, dy in zip(dxs, dys):
            nx = x + dx; ny = y + dy
            if is_range(nx,ny) and grid[nx][ny] != 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                if grid[nx][ny] == 3:
                    return cnt + 1
                else:
                    que.append((nx, ny, cnt + 1))
    return -1



for person in people:
    answer = bfs(person)
    answers[person[0]][person[1]] = answer

for ans in answers:
    print(*ans)
