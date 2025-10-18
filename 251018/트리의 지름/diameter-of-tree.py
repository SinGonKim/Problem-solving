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

visited = [0 for _ in range(n+1)]
dist = [0 for _ in range(n+1)]
def dfs(x, total_dist):
    for y, d in edges[x]:
        if not visited[y]:
            visited[y] = 1
            dist[y] = total_dist + d
            dfs(y, total_dist+d)

def find_largest(x):
    for i in range(1,n+1):
        visited[i] = 0
        dist[i] = 0
    
    visited[x] = 1
    dist[x] = 0
    dfs(x,0)

    farthest_dist = -1
    farthest_vertex = -1
    for i in range(1,n+1):
        if dist[i] > farthest_dist:
            farthest_dist = dist[i]
            farthest_vertex = i
    return farthest_vertex, farthest_dist

f_vertex, _ = find_largest(1)
_, diameter = find_largest(f_vertex)
print(diameter)