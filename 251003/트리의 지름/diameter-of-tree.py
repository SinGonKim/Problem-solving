
import sys

sys.setrecursionlimit(10**6+1)

input = sys.stdin.readline

n = int(input())

edges = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]


for _ in range(n-1):
    x, y, w = map(int, input().split())
    edges[x].append((y,w))
    edges[y].append((x,w))

def clear():
    max_len = 0
    for i in range(1, n+1):
        visited[i] = False

def dfs(x, length):
    global max_len, max_len_point

    if (max_len < length):
        max_len = length
        max_len_point = x

    for y, w in edges[x]:
        if not visited[y]:
            visited[y] = True
            dfs(y, length+w)

max_len = 0
max_len_point = 0
visited[1] = True
dfs(1,0)

clear()
visited[max_len_point] = True
dfs(max_len_point, 0)

print(max_len)