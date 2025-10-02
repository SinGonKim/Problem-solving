n = int(input())
edges = [tuple(map(int, input().split())) for _ in range(n - 1)]

# Please write your code here.
parents = [0 for _ in range(n+1)]

for edge in edges:
    parents[edge[1]] = edge[0]

for i in range(2,n+1):
    print(parents[i])

