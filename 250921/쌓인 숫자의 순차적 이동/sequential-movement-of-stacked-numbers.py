from collections import defaultdict
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
move_nums = list(map(int, input().split()))

graph = [[[] for _ in range(n)] for _ in range(n)]
pos = defaultdict(list)

for i in range(n):
    for j in range(n):
        graph[i][j].append(grid[i][j])
        pos[grid[i][j]] = [i,j]

def is_range(x, y):
    if 0<=x<n and 0<=y<n:
        return True
    return False

def move(row, col, idx):
    dxs = [-1, 0, 1, -1, 1, -1, 0, 1]
    dys = [-1, -1, -1, 0, 0, 1, 1, 1]

    target = 0
    tx, ty = -1, -1
    for dx, dy in zip(dxs, dys):
        if is_range(row+dx, col+dy) and len(graph[row+dx][col+dy]):
            result = max(graph[row+dx][col+dy])
            if result > target:
                target = result
                tx, ty = row+dx, col+ dy
    if tx != -1 and ty != -1:
        # print(f"move to {row}, {col} -> {tx}, {ty}")
        for c in graph[row][col][idx:]:
            pos[c][0], pos[c][1] = tx, ty
        graph[tx][ty] = graph[tx][ty] + graph[row][col][idx:]
        graph[row][col] = graph[row][col][:idx]



# Please write your code here.
for num in move_nums:
    flag = False
    x, y = pos[num][0], pos[num][1]
    idx = graph[x][y].index(num)
    move(x,y,idx)

for i in range(n):
    for j in range(n):
        if len(graph[i][j]) == 0:
            print("None")
        else:
            print(*graph[i][j][::-1])