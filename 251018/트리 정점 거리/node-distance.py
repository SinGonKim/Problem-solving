import sys
sys.setrecursionlimit(10**5)
n, m = map(int, input().split())

edges = [tuple(map(int, input().split())) for _ in range(n - 1)]
queries = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
graph = [[] for _ in range(n+1)]

for edge in edges:
    x, y, dist = edge[0], edge[1], edge[2]
    graph[x].append((y,dist))
    graph[y].append((x,dist))


visited= [-1 for _ in range(n+1)]
dist = [[0 for _ in range(n+1)] for _ in range(n+1)]

def dfs(s,e):
    
    for nx, d in graph[e]:
        if visited[nx] == -1:
            visited[nx] = 1
            dist[s][nx] = dist[s][e] + d
            dfs(s,nx)
    return


for i in range(1,n+1):
    for j in range(1,n+1):
        visited[j] = -1
    visited[i] = 1
    dfs(i,i)


for query in queries:
    x, y = query[0], query[1]
    print(dist[x][y])
