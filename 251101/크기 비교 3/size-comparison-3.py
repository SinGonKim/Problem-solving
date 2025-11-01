n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
indegree = [0 for _ in range(n+1)]
graph = [[] for _ in range(n+1)]
for edge in edges:
    a, b = edge
    graph[a].append(b)
    indegree[b] += 1

import heapq
heap = []

for i in range(1,n+1):
    if indegree[i] == 0:
        heapq.heappush(heap,i)

while heap:
    x = heapq.heappop(heap)
    print(x, end = ' ')

    for nx in graph[x]:
        # print(nx)
        indegree[nx] -= 1
        if not indegree[nx]:
            heapq.heappush(heap,nx)

