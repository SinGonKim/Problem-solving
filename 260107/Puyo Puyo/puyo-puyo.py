n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
import sys
sys.setrecursionlimit(10000)
visited = [[0 for _ in range(n)] for _ in range(n)]
num_popping_blocks = 0  # 터지게 되는 블록의 수
max_block_size = 0      # 가장 큰 블록의 크기


def is_range(x,y):
    if 0<=x<n and 0<=y<n:
        return True
    return False


def dfs(row, col, h):
    dxs = [-1,1,0,0]
    dys = [0,0,-1,1]

    visited[row][col] = 1
    cnt = 1

    for dx, dy in zip(dxs, dys):
        if is_range(row+dx, col+dy) and visited[row+dx][col+dy] == 0 and grid[row+dx][col+dy] == h:
            cnt += dfs(row+dx, col+dy, h)

    return cnt

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            current_block_size = dfs(i,j,grid[i][j])

            if current_block_size >= 4:
                num_popping_blocks += 1
            if current_block_size > max_block_size:
                max_block_size = current_block_size

print(num_popping_blocks, max_block_size)