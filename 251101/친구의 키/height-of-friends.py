n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
graph = [[] for _ in range(n+1)]
indegree = [0]*(n+1)

for edge in edges:
    a, b= edge
    graph[a].append(b)
    indegree[b] += 1 

from collections import deque

que = deque()
for i in range(1,n+1):
    if not indegree[i]:
        que.append(i)

answer = []

while que:
    x = que.popleft()
    answer.append(x)
    
    for y in graph[x]:
        indegree[y] -= 1

        if not indegree[y]:
            que.append(y)

print(*answer)