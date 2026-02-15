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
            steps.append((i,j))

from itertools import permutations
import sys
answer = sys.maxsize
for per in permutations(steps, 3):
    prev = start
    res = 0
    for x, y in per:
        res += abs(prev[0]-x) + abs(prev[1]-y)
        prev = (x,y)
    res += abs(prev[0]-end[0]) + abs(prev[1]-end[1])
    answer = min(answer, res)
print(answer if answer != sys.maxsize else -1)
