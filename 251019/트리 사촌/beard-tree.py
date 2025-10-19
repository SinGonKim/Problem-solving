n, k = map(int, input().split())
sequence = [0] + list(map(int, input().split()))

# Please write your code here.

par = [0 for _ in range(n+1)]
ans = 0

target_node_index = 0

for i in range(1,n+1):
    if sequence[i] == k:
        target_node_index = i

parent_node = 0
for i in range(2,n+1):
    if sequence[i] > sequence[i-1] + 1:
        parent_node += 1
    par[i] = parent_node

for node in range(1,n+1):
    if par[par[node]] == 0 or par[par[target_node_index]] == k: continue

    if par[node] != par[target_node_index] and par[par[node]] == par[par[target_node_index]]:
        ans += 1
print(ans)