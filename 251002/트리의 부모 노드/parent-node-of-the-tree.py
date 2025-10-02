n = int(input())
edges = [tuple(map(int, input().split())) for _ in range(n - 1)]

# Please write your code here.
from collections import defaultdict
parents = defaultdict(int)

for edge in edges:
    parents[edge[1]] = edge[0]

for i in range(2,n+1):
    print(parents[i])

