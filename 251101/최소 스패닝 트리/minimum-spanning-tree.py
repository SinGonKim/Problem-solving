n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)] # point a, point b, length
edges.sort(key = lambda x: x[-1])
parents = [i for i in range(n+1)]
mst = 0
# Please write your code here.
def find(x):
    if x != parents[x]:
        return find(parents[x])
    return x

def union(x,y):
    x = find(x)
    y = find(y)

    if x > y:
        x, y = y, x
    parents[y] = x


for edge in edges:
    u, v, l = edge
    if find(u) != find(v):
        mst += l
        union(u,v)
print(mst)