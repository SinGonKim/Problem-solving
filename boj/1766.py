import sys
import collections
input = sys.stdin.readline
N, M = map(int, input().split())
in_deque = [0]*(N+1)
graph = [[] for _ in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    in_deque[b] +=1
    graph[a].append(b)
result = []
q = []
for i in range(1, N+1):
    if in_deque[i] ==0:
        q.append(i)
while q:
    node = q[0]
    result.append(node)
    for i in graph[node]:
        in_deque[i] -=1
        if in_deque[i] ==0:
            q.append(i)
    del(q[0])
    q.sort()
for i in result:
    print(i, end = " ")
