\
import sys
sys.setrecursionlimit(100000)

# 변수 선언 및 입력:
n = int(input())
edges = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
dist = [0] * (n + 1)
max_dist = 0
last_node = 0

# n - 1개의 간선 정보를 입력받습니다.
for _ in range(n - 1):
    x, y = tuple(map(int, input().split()))
    edges[x].append(y)
    edges[y].append(x)


# 모든 노드의 정점을 탐색하는 DFS를 진행합니다.
def dfs(x):
    global max_dist, last_node
    
    for y in edges[x]:
        # 이미 방문한 정점이면 스킵합니다.
        if visited[y]: 
            continue

        visited[y] = True
        dist[y] = dist[x] + 1

        # 현재 정점을 기준으로 가장 먼 노드를 찾습니다.
        if dist[y] > max_dist:
            max_dist = dist[y]
            last_node = y

        dfs(y)


# DFS를 통해 가장 먼 노드를 찾습니다.
visited[1] = True
dfs(1)

# 가장 먼 노드에서 시작해 다시 한번 DFS를 돌려 트리의 가장 긴 거리를 찾습니다.
for i in range(1, n + 1):
    visited[i] = False
    dist[i] = 0

visited[last_node] = True
dfs(last_node)
# 트리의 가장 긴 거리를 출력합니다.
print((max_dist+1)//2)