import sys
from collections import deque

sys.setrecursionlimit(10**6+1)
input = sys.stdin.readline

n = int(input())
edges = [[] for _ in range(n+1)]

for _ in range(n-1):
    x, y, w = map(int, input().split())
    edges[x].append((y, w))
    edges[y].append((x, w))

def bfs(start):
    visited = [False] * (n+1)
    visited[start] = True
    queue = deque([(start, 0)])
    max_len = 0
    max_node = start
    
    while queue:
        node, dist = queue.popleft()
        
        if dist > max_len:
            max_len = dist
            max_node = node
        
        for next_node, weight in edges[node]:
            if not visited[next_node]:
                visited[next_node] = True
                queue.append((next_node, dist + weight))
    
    return max_node, max_len

farthest_node, _ = bfs(1)
_, diameter = bfs(farthest_node)

print(diameter)