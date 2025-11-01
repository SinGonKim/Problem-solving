n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
indegree = [0 for _ in range(n+1)]

graph = [[] for _ in range(n+1)]

from collections import deque

for edge in edges:
    a, b = edge
    graph[a].append(b)
    indegree[b] += 1

que = deque()
for i in range(1,n+1):
    if not indegree[i]:
        que.append(i)

if not len(que):
    print("Inconsistent")
else:
    stack = []
    while que:
        x = que.popleft()
        stack.append(x)
        for nx in graph[x]:
            indegree[nx] -= 1
            if not indegree[nx]:
                que.append(nx)
            elif indegree[nx] < 0:
                break
    if len(stack) != n:
        print('Inconsistent')
    else:
        print("Consistent")