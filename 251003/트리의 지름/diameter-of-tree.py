
import sys

sys.setrecursionlimit(10**6+1)

input = sys.stdin.readline

n = int(input())

edges = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]

parents = [0 for _ in range(n+1)]

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

    if not visited[x]:
        visited[x] = True

        if (max_len < length):
            max_len = length
            max_len_point = x

        for y, w in edges[x]:
            dfs(y, length+w)

max_len = 0
max_len_point = 0
dfs(1,0)

clear()

dfs(max_len_point, 0)

print(max_len)