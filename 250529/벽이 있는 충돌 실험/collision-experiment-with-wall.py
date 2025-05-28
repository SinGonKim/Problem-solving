Max_N = 50

T = int(input())

dir_map = {
    'U': 0,
    'D': 3,
    'L': 1,
    'R': 2
}

grid = [
    [0 for _ in range(Max_N)]
    for _ in range(Max_N)
]


def in_range(row, col):
    return 0<= row < N and 0 <= col < N

def move(x, y, d):
    dxs, dys = [-1, 0, 0, 1], [0, -1, 1, 0]
    nx, ny = x + dxs[d], y + dys[d]

    if in_range(nx, ny):
        return nx, ny, d
    else:
        return x, y, 3-d

def init_grid(next_marbles_list):
    for x, y, _ in next_marbles_list:
        grid[x][y] = 0

def move_all():
    next_marbles_list = list()

    for x, y, d in marbles:
        nx, ny, d = move(x, y, d)
        grid[nx][ny] += 1
        next_marbles_list.append((nx, ny, d))
    return next_marbles_list




def check_dupl(next_marbles_list):
    global marbles
    cnt = 0
    next_marbles = []

    for x, y, d in next_marbles_list:
        if grid[x][y] == 1:
            next_marbles.append((x,y,d))
            cnt += 1
    
    marbles = next_marbles
    return cnt


def simulate():
    for _ in range(2*N):
        next_marbles_list = move_all()
        ans = check_dupl(next_marbles_list)
        init_grid(next_marbles_list)
    
    print(ans)

for _ in range(T):
    N, M = map(int, input().split())
    marbles = []


    for _ in range(M):
        xi, yi, di = tuple(input().split())
        xi, yi, di = int(xi) -1, int(yi) - 1, dir_map[di]
        marbles.append((xi, yi, di))
    
    simulate()

    # Please write your code here.
