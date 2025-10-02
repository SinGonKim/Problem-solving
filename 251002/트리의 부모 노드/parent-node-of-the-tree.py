n = int(input())
edges = [tuple(map(int, input().split())) for _ in range(n - 1)]

# Please write your code here.
graph = [[] for _ in range(n+1)]
for edge in edges:
    graph[edge[0]].append(edge[1])
    graph[edge[1]].append(edge[0])

visited = [0 for _ in range(n+1)]

parents = [0 for _ in range(n+1)]

def dfs(s):
    for x in graph[s]:
        if visited[x] == 1: continue
        
        parents[x] = s
        visited[x] = 1
        dfs(x)

dfs(1)

for i in range(2,n+1):
    print(parents[i])

