n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
rows = [i for i in range(n)]
cols = [i for i in range(n)]

from itertools import permutations
answer = 0
for rs in permutations(rows,n):
    for cs in permutations(cols,n):
        cnt = 0
        for r, c in zip(rs, cs):
            cnt += grid[r][c]
        answer = max(answer, cnt)
print(answer)