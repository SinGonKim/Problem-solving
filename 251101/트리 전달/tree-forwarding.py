import sys
sys.setrecursionlimit(10**6+1)

n, m = map(int, input().split())

# 1-based indexing for parent array
parent = [-1] + list(map(int, input().split()))

children = [[] for _ in range(n+1)]

for i in range(1,n+1):
    p, c = parent[i], i
    if p == -1: continue
    children[p].append(c)

weights = [0]*(n+1)

def dfs(n):
    for nn in children[n]:
        weights[nn] += weights[n]
        dfs(nn)


for _ in range(m):
    node, weight = map(int, input().split())
    weights[node] += weight

dfs(1)

# Please write your code here.
print(*weights[1:])