n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]


def in_range(x,y):
    if 0 <= x < n and 0 <= y < n:
        return True
    else:
        return False


def game_play(x, y, d):
    tmp = 1

    while True:
        nx = x + dxs[d]
        ny = y + dys[d]
        tmp += 1
        if not in_range(nx,ny):break
        if grid[nx][ny] == 1:
            d = 3 - d
        elif grid[nx][ny] == 2:
            if d == 0:
                d = 1
            elif d == 1:
                d = 0
            elif d == 2:
                d = 3
            elif d == 3:
                d = 2
        x, y = nx, ny
    

    return tmp


ans = 0
for i in range(n):
    ans = max(ans, game_play(i,0,0))
    ans = max(ans, game_play(i,n-1,2))
    ans = max(ans, game_play(0,i,1))
    ans = max(ans, game_play(n-1,i,3))

print(ans)