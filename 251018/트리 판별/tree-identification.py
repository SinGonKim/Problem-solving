m = int(input())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
is_root = [True for _ in range(10001)]
used = [False for _ in range(10001)]
root = None
graph = [[] for _ in range(10001)]


for edge in edges:
    s, e = edge[0], edge[1]
    is_root[e] = False
    used[s] = True
    used[e] = True
    graph[s].append(e)

for i in range(1,m+1):
    if used[i] == True and is_root[i] == True:
        root = i
        break

from collections import deque
que = deque()
que.append(root)
visited = [0 for _ in range(10001)]
visited[root] = 1

is_tree = True
while que:
    idx = que.popleft()
    # print(idx)
    for nx in graph[idx]:
        if visited[nx]:
            is_tree = False
            continue
        visited[nx] = 1
        que.append(nx)

for node in range(1,10001):
    if used[node] == True and visited[node] == 0:
        is_tree= False
if is_tree:
    print(1)
else:
    print(0)