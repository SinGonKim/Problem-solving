import sys
input = sys.stdin.readline
from collections import deque
def bfs():
    que = deque([1])
    visited[1] = True #시작점 처음 방문 했으므로
    while que:
        x = que.popleft()
        if x==100:
            print(board[100])
            break
        for i in range(6):
            Nx = x + dx[i]
            if Nx >100 or visited[Nx]==True:
                continue
            if Nx in U.keys():
                Nx = U[Nx]
            elif Nx in D.keys():
                Nx = D[Nx]
            if visited[Nx] == False:
                que.append(Nx)
                visited[Nx] = True
                board[Nx] = board[x] + 1
    return
if __name__ =="__main__":
    n, m = map(int, input().split()) #사다리수, 뱀의수
    U = dict() #사다리 좌표
    D = dict() #뱀 좌표
    board = [0 for _ in range(101)]
    dx = [1, 2, 3, 4, 5, 6]
    visited = [False for _ in range(101)]
    for _ in range(n):
        start, end = map(int,input().split())
        U[start] = end
    for _ in range(m):
        start, end = map(int,input().split())
        D[start] = end
    bfs()
