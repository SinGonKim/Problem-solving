n = int(input())
bomb = []
grid = []
for i in range(n):
    row = list(map(int, input().split()))
    for j, r in enumerate(row):
        if r == 1:
            bomb.append((i,j))
    grid.append(row)

# Please write your code here.
direction = [[(-2,0), (-1,0), (1,0), (2,0)], [(-1,0), (1,0), (0,-1), (0,1)], [(-1,-1), (1,-1), (-1,1), (1,1)]]

def in_range(row, col):
    return 0 <= row < n and 0 <= col < n

def max_destroyed():
    max_cnt = 0

    def _destroyed(bomb_idx_list = [], l = 0):
        nonlocal max_cnt

        if l == len(bomb):
            _grid = [[0 for _ in range(n)] for _ in range(n)]

            for idx, b_d in enumerate(bomb):
                row, col = b_d
                _grid[row][col] = 1
                b = direction[bomb_idx_list[idx]]

                for coord in b:
                    add_row, add_col = coord
                    _row, _col = row + add_row, col + add_col

                    if in_range(_row, _col):
                        _grid[_row][_col] = 1
            cnt = sum(map(sum, _grid))
            max_cnt = max(cnt, max_cnt)
            return
        for i in range(len(direction)):
            _destroyed(bomb_idx_list + [i], l+1)
    
    _destroyed()
    return max_cnt

print(max_destroyed())
