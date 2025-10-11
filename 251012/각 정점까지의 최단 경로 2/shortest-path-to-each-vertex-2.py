n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
import sys
INF = sys.maxsize
graph = [[INF for _ in range(n+1)] for _ in range(n+1)]

for i in range(n+1):
    graph[i][i] = 0

for edge in edges:
    x, y, w = edge
    graph[x][y] = min(graph[x][y], w)

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(1,n+1):
    for j in range(1,n+1):
        if graph[i][j] == INF:
            print(-1, end = ' ')
        else:
            print(graph[i][j], end= ' ')
    print()