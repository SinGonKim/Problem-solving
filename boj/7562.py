import sys
input = sys.stdin.readline
from collections import deque
def bfs(x0, y0, x1, y1):
    q = deque()
    q.append([x0, y0])
    T[x0][y0] = 1 #지나간 곳은 체크 다시 지나갈 필요가 없다. 반복되기 때문!
    while q:
        a, b = q.popleft()
        if a == x1 and b == y1:
            print(T[x1][y1]-1)    #종착점까지 걸린 단계 출력!
            return
        for i in range(8):
            x = a + idx[i]
            y = b + idy[i]
            if 0 <= x < l and 0 <= y < l and T[x][y] == 0:
                q.append([x, y])
                T[x][y] = T[a][b] + 1
for _ in range(int(input())):
    l = int(input())
    x0, y0 = map(int, input().split()) # 초기 위치 설정
    x1, y1 = map(int, input().split()) # 종착점
    idx = [-2, -2, -1, -1, 1, 1, 2, 2]
    idy = [-1, 1, -2, 2, -2, 2, -1, 1]
    T = [[0 for _ in range(l)] for _ in range(l)]
    bfs(x0, y0, x1, y1)
