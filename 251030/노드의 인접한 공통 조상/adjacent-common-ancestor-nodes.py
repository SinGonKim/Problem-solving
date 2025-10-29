n = int(input())

graph = [[] for _ in range(n+1)]
parents = [0 for _ in range(n+1)]
root = [1 for _ in range(n+1)]
for _ in range(n - 1):
    f, t = map(int, input().split())
    graph[f].append(t)
    parents[t] = f
    root[t] = 0
for i in range(1,n+1):
    if root[i] == 1:
        root = i
        break

depth = [0 for _ in range(n+1)]
def dfs(x):
    for y in graph[x]:
        depth[y] = depth[x] + 1

        dfs(y)

dfs(root)

a, b = map(int, input().split())

# Please write your code here.
while depth[a] != depth[b]:
    if depth[a] > depth[b]:
        a = parents[a]
    else:
        b = parents[b]
while a != b:
    a = parents[a]
    b = parents[b]
print(a)