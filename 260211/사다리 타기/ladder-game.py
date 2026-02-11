n, m = map(int, input().split())
edges = sorted([tuple(map(int, input().split())) for _ in range(m)], key = lambda x: (x[1],x[0]))


# Please write your code here.
result = [0 for _ in range(n)]

for num in range(1,n+1):
    row, col = 1, num
    for edge in edges:
        ai, bi = edge
        if bi < row: continue
        elif bi > row:
            row = bi
        
        if col == ai:
            col = ai + 1
        elif col == ai + 1:
            col = ai
    result[col-1] = num

answer = 0
for i in range(n,0,-1):
    for j in range(1, i):
        if result[j-1] > result[j]:
            result[j-1], result[j] = result[j], result[j-1]
            answer += 1
print(answer)