N, M = map(int, input().split())
clothes = [tuple(map(int, input().split())) for _ in range(N)]
s = [0] + [x[0] for x in clothes]
e = [0] + [x[1] for x in clothes]
v = [0] + [x[2] for x in clothes]

# Please write your code here.
G = [[0 for _ in range(N+1)] for _ in range(M+1)]

for i in range(1,M+1):
    for j in range(1,N+1):
        if s[j] <= i <= e[j]:
            for k in range(1,N+1):
                if s[k] <= i-1 <= e[k]:
                    G[i][j] = max(G[i][j], G[i-1][k] + abs(v[j] - v[k]))
                else:
                    G[i][j] = max(G[i][j], G[i-1][k])
print(max(G[M]))