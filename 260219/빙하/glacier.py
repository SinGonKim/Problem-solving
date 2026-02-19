import sys
from collections import deque

# 입력 받기
n, m = map(int, sys.stdin.readline().split())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

def get_outside_air():
    """
    현재 grid 상태에서 외부 공기(0)인 부분들을 찾아 visited에 표시합니다.
    (0,0)은 항상 바깥쪽이므로 여기서 시작하는 BFS를 사용합니다.
    """
    is_outside = [[False for _ in range(m)] for _ in range(n)]
    q = deque([(0, 0)])
    is_outside[0][0] = True
    
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and not is_outside[nx][ny]:
                # 빙하가 아닌(0인) 곳만 타고 나갑니다.
                if grid[nx][ny] == 0:
                    is_outside[nx][ny] = True
                    q.append((nx, ny))
    return is_outside

time = 0
last_ice_count = 0

while True:
    # 1. 현재 남아있는 빙하의 개수를 세어둡니다.
    current_ice = []
    for r in range(n):
        for c in range(m):
            if grid[r][c] == 1:
                current_ice.append((r, c))
    
    # 빙하가 하나도 없으면 종료
    if not current_ice:
        break
    
    # 마지막 빙하 개수를 업데이트 (전부 녹기 전의 상태를 보존)
    last_ice_count = len(current_ice)
    
    # 2. 외부 공기 위치 파악
    is_outside = get_outside_air()
    
    # 3. 이번 초에 녹을 빙하 찾기
    melt_list = []
    for x, y in current_ice:
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if is_outside[nx][ny]: # 외부 공기와 접촉했다면
                    melt_list.append((x, y))
                    break
    
    # 4. 빙하를 녹임 (동시에 녹아야 하므로 한꺼번에 처리)
    for x, y in melt_list:
        grid[x][y] = 0
        
    time += 1

print(time, last_ice_count)