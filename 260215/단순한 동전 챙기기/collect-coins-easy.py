n = int(input())
grid = [list(input()) for _ in range(n)]

# Please write your code here.
steps = [] 
for i in range(n):
    for j in range(n):
        if grid[i][j] == 'S':
            start = (i,j)
        elif grid[i][j] == 'E':
            end = (i,j)
        elif grid[i][j] != '.':
            steps.append((int(grid[i][j]), i, j))

from itertools import combinations
import sys
answer = sys.maxsize
for comb in combinations(steps, 3):
    prev = start
    comb_sort = sorted(list(comb))
    res = 0
    for _, x, y in comb_sort:
        res += abs(prev[0]-x) + abs(prev[1]-y)
        prev = (x,y)
    res += abs(prev[0]-end[0]) + abs(prev[1]-end[1])
    answer = min(answer, res)
print(answer if answer != sys.maxsize else -1)
