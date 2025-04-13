n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
graph = [[] for _ in range(n+1)]
for i in range(m):
    s, e = edges[i]
    graph[s].append(e)
    graph[e].append(s)

visited = [0 for _ in range(n+1)]

def dfs(s):
    visited[s] = 1
    for e in graph[s]:
        if visited[e] == 0:
            dfs(e)

dfs(1)
cnt = sum(visited)-1

print(cnt)