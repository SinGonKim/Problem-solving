import copy
from collections import deque

n, k, m = map(int, input().split()) # N: 격자 크키, K: 시작점 수, M 치워야 할 돌의 개수
grid = [list(map(int, input().split())) for _ in range(n)]
S = []
for _ in range(k):
    ri, ci = map(int, input().split())
    S.append((ri-1, ci-1))

# Please write your code here.
from itertools import combinations
stones = []
for row in range(n):
    for col in range(n):
        if grid[row][col] == 1:
            stones.append((row,col))

def can_go(x, y):
    return 0 <= x < n and 0 <= y < n and tmp[x][y] == 0

def bfs():

    dxs = [-1, 0, 1, 0]
    dys = [0, -1, 0, 1]
    que = deque()
    visited = [[False for _ in range(n)] for _ in range(n)]
    result = 0

    for s in S:
        que.append(s)
        visited[s[0]][s[1]] = True
        result += 1
    
    while que:
        x, y = que.popleft()
        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy
            if can_go(nx,ny) and visited[nx][ny] == False:
                que.append((nx,ny))
                visited[nx][ny] = True
                result += 1
    return result

    result = 0

answer = 0 
for comb in combinations(stones, m):
    tmp = copy.deepcopy(grid)
    for r, c in comb:
        tmp[r][c] = 0
    res = bfs()
    answer = max(answer, res)    
print(answer)
