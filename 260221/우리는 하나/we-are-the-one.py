
# Please write your code here.
from collections import deque
import heapq

def initialize():
    for i in range(n):
        for j in range(n):
            visited[i][j] = 0

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def can_go(x, y, bx, by):
    if not in_range(x, y):
        return False
    if bx != -1 and by != -1:
        if d < abs(grid[x][y] - grid[bx][by]) or u > abs(grid[x][y] - grid[bx][by]):
            return False
    if visited[x][y] != 0:
        return False
    return True

def bfs():
    cnt = 1
    while que:
        x, y = que.popleft()
        for dx, dy in zip(dxs, dys):
            nx = x + dx; ny = y + dy
            if can_go(nx, ny, x, y):
                cnt += 1
                visited[nx][ny] = 1
                que.append((nx, ny))
    return cnt

def choose_nextcity():
    local_max = 0

    for i in range(n):
        for j in range(n):
            if can_go(i, j, -1, -1):
                visited[i][j] = 1
                que.append((i, j))
                cnt = bfs()
                cntlist.append(cnt)
            #방금 다녀온 start가 max가아니면
            #reset
 
            if local_max < cnt:
                local_max = cnt


def compare_k():
    choose_nextcity()
    cntlist.sort(reverse=True)
    total = 0
    for i in range(k):
        total += cntlist[i]
    print(total)


if __name__ == "__main__":
    n, k, u, d = map(int, input().split()) # 격자 크기, 고를 도시의 수, 높이의 차 U<=x<=D
    grid = [list(map(int, input().split())) for _ in range(n)]

    visited = [[0 for _ in range(n)] for _ in range(n)]

    dxs = [-1, 1, 0 , 0]
    dys = [0, 0, -1, 1]

    que = deque()
    cntlist = []
    compare_k()