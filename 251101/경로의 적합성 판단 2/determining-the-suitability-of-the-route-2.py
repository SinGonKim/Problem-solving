n, m, k = map(int, input().split())

edges = [tuple(map(int, input().split())) for _ in range(m)]
path = list(map(int, input().split()))

# Please write your code here.


parent = [i for i in range(n+1)]
graph = [[] for _ in range(n+1)]

def find(x):
    if parent[x] == x:
        return x
    return find(parent[x])


def union(x,y):
    x = find(x)
    y = find(y)

    if x > y:
        x, y = y, x
    parent[y] = x

for edge in edges:
    union(edge[0], edge[1])

for i in range(k-1):
    if parent[path[i]] != parent[path[i+1]]:
        print(0)
        break
else:
    print(1)