import sys

COIN_NUM = 9
INT_MAX = sys.maxsize

# 변수 선언 및 입력:
n = int(input())
m = 3

grid = [
    input()
    for _ in range(n)
]

coin_pos = list()
selected_pos = list()

start_pos = (-1, -1)
end_pos = (-1, -1)

ans = INT_MAX


def dist(a, b):
    (ax, ay), (bx, by) = a, b
    return abs(ax - bx) + abs(ay - by)


def calc():
    num_moves = dist(start_pos, selected_pos[0])
    for i in range(m - 1):
        num_moves += dist(selected_pos[i], selected_pos[i + 1])
    num_moves += dist(selected_pos[m - 1], end_pos)
    
    return num_moves


def find_min_moves(curr_idx, cnt):
    global ans
    
    if cnt == m:
        # 선택된 모든 조합에 대해 이동 횟수를 계산합니다.
        ans = min(ans, calc())
        return
    
    if curr_idx == len(coin_pos):
        return
    
    # curr_idx index 에 있는 동전을 선택하지 않은 경우
    find_min_moves(curr_idx + 1, cnt)
    
    # curr_idx index 에 있는 동전을 선택한 경우
    selected_pos.append(coin_pos[curr_idx])
    find_min_moves(curr_idx + 1, cnt + 1)
    selected_pos.pop()

    
for i in range(n):
    for j in range(n):
        if grid[i][j] == 'S':
            start_pos = (i, j)
        if grid[i][j] == 'E':
            end_pos = (i, j)

# 동전을 오름차순으로 각 위치를 집어넣습니다.
# 이후에 증가하는 순서대로 방문하기 위함입니다.
for num in range(1, COIN_NUM + 1):
    for i in range(n):
        for j in range(n):
            if grid[i][j] == str(num):
                coin_pos.append((i, j))
                
find_min_moves(0, 0)

if ans == INT_MAX:
    ans = -1

print(ans)
