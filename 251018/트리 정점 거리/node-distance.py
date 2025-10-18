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


def dfs(s,e):
    
    if s == e:
        return
    
    for nx, d in graph[s]:
        if visited[nx] == -1:
            visited[nx] = visited[s] + d
            dfs(nx,e)
    return

for query in queries:
    x, y = query[0], query[1]
    visited[x] = 0
    dfs(x,y)
    print(visited[y])
    visited= [-1 for _ in range(n+1)]