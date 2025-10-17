m = int(input())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
is_root = [0 for _ in range(10001)]
used = [False for _ in range(10001)]
root = 0
graph = [[] for _ in range(10001)]
is_tree = True

for edge in edges:
    s, e = edge[0], edge[1]
    used[s] = True
    used[e] = True
    graph[s].append(e)
    is_root[e] += 1

for i in range(1,m+1):
    if used[i] == True and is_root[i] == 0:
        if root != 0:
            is_tree = False
        root = i
if is_tree == False:
    print(0)
else:
    from collections import deque
    que = deque()
    que.append(root)
    visited = [0 for _ in range(10001)]
    visited[root] = 1

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