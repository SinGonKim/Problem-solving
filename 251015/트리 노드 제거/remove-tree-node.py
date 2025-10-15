n = int(input())
parent = list(map(int, input().split()))
remove_node = int(input())

# Please write your code here.
graph = [[] for _ in range(n)]
root = -1
is_deleted = [False for _ in range(n)]
for i, p in enumerate(parent):
    if p == -1:
        root = i
        continue
    graph[p].append(i)
    

is_deleted[remove_node] = True
ans = 0

def dfs(x):
    global ans

    if is_deleted[x]:
        return
    
    is_leaf = True

    if len(graph[x]):
        for y in graph[x]:
            if is_deleted[y]:continue
            dfs(y)
            is_leaf = False
    if is_leaf:
        ans += 1
            
dfs(root)
print(ans)