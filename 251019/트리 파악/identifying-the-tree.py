n = int(input())
edges = [tuple(map(int, input().split())) for _ in range(n - 1)]

# Please write your code here.
graph = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]
depth = [0 for _ in range(n+1)]

for edge in edges:
    graph[edge[0]].append(edge[1])
    graph[edge[1]].append(edge[0])

S = 0
root = 1
visited[root] = 1

def DFS(x):
    global S
    is_leaf = True
    for y in graph[x]:
        if visited[y]:continue
        is_leaf = False
        visited[y] = True
        depth[y] = depth[x] + 1
        DFS(y)
    
    if is_leaf:
        S += depth[x]


DFS(root)

if S%2:
    print(1)
else:
    print(0)