import sys
sys.setrecursionlimit(10**5+1)

n = int(input())
edges = [tuple(map(int, input().split())) for _ in range(n - 1)]

# Please write your code here.
graph = [[] for _ in range(n+1)]
for edge in edges:
    graph[edge[0]].append(edge[1])
    graph[edge[1]].append(edge[0])

dp = [[0,0] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]

def dfs(x):
    visited[x] = 1
    dp[x][1] = 1

    dp[x][0] = 0

    for y in graph[x]:
        if not visited[y]:
            dfs(y)
            dp[x][1] += min(dp[y][0], dp[y][1])
            dp[x][0] += dp[y][1]
dfs(1)
print(min(dp[1][0], dp[1][1]))