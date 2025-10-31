n, m = map(int, input().split())
query = [list(map(int, input().split())) for _ in range(m)]

# Please write your code here.
parents = [i for i in range(n+1)]


def find(x):

    if parents[x] == x:
        return x
    return find(parents[x])

def union(x, y):
    x = find(x)
    y = find(y)

    if x > y:
        x, y = y, x
    
    parents[y] = x


for cmd, a, b in query:
    if cmd == 0:
        union(a,b)
        
    else:
        if find(a) == find(b):
            print(1)
        else:
            print(0)