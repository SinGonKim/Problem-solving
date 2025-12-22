from copy import deepcopy
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
answer = (-1,-1)
# Please write your code here.
S = set()
for g in grid:
    for x in g:
        S.add(x-1)
S.discard(0)
S = sorted(list(S))


def change_to_zero_less_k(k):
    vilage_copy = deepcopy(grid)
    for row in range(n):
        for col in range(m):
            vilage_copy[row][col] -= k
    return vilage_copy

def is_range(row,col):
    if 0<=row<n and 0<=col<m:
        return True
    return False

def dfs(row,col):
    visited[row][col] = True
    dxs = [-1, 1, 0, 0]
    dys = [0, 0, -1, 1]

    for dx, dy in zip(dxs, dys):
        nx = row + dx; ny = col + dy
        if is_range(nx,ny) and not visited[nx][ny] and vilage_copy[nx][ny] >0:
            dfs(nx,ny)
    return

for k in S:
    cnt = 0
    vilage_copy = change_to_zero_less_k(k)
    visited = [[False for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and vilage_copy[i][j] > 0:
                dfs(i,j)
                cnt += 1

    if answer[1] <= cnt:
        answer = (k, cnt)
print(*answer)

