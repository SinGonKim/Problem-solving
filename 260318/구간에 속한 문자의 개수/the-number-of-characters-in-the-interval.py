import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
grid = [input().strip() for _ in range(n)]

# prefix[x][i][j]:
# 문자 x(0:a, 1:b, 2:c)가 (1,1) ~ (i,j) 범위에 몇 개 있는지
prefix = [[[0] * (m + 1) for _ in range(n + 1)] for _ in range(3)]

mapping = {'a': 0, 'b': 1, 'c': 2}

for i in range(1, n + 1):
    row = grid[i - 1]
    for j in range(1, m + 1):
        ch_idx = mapping[row[j - 1]]
        for x in range(3):
            prefix[x][i][j] = (
                prefix[x][i - 1][j]
                + prefix[x][i][j - 1]
                - prefix[x][i - 1][j - 1]
            )
        prefix[ch_idx][i][j] += 1

out = []
for _ in range(k):
    r1, c1, r2, c2 = map(int, input().split())
    res = []
    for x in range(3):
        cnt = (
            prefix[x][r2][c2]
            - prefix[x][r1 - 1][c2]
            - prefix[x][r2][c1 - 1]
            + prefix[x][r1 - 1][c1 - 1]
        )
        res.append(cnt)
    out.append(f"{res[0]} {res[1]} {res[2]}")

for o in out:
    print(o)