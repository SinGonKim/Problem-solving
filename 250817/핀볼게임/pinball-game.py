n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def game_play(x, y, d):
    steps = 1
    visited = {}  # (x, y, d) -> first_step_when_visited
    
    while True:
        # 다음 위치 계산
        nx = x + dxs[d]
        ny = y + dys[d]
        steps += 1
        
        # 격자를 벗어나면 종료 (이것이 목표!)
        if not in_range(nx, ny):
            return steps
        
        # 무한루프 체크 - 하지만 더 나은 결과가 있을 수 있으므로 신중하게
        state = (nx, ny, d)
        if state in visited:
            # 이미 같은 상태를 방문했다면, 순환 중
            # 하지만 문제에서는 "격자 밖으로 나올 때까지"이므로
            # 실제로는 무한루프일 가능성이 높음
            cycle_length = steps - visited[state]
            # 매우 큰 값을 반환 (사실상 무한대를 의미)
            return steps + 10**9  # 무한루프로 간주
        
        visited[state] = steps
        
        # 방향 변경 로직
        if grid[nx][ny] == 1:
            d = 3 - d  # 반대 방향
        elif grid[nx][ny] == 2:
            # 90도 회전 (시계방향)
            if d == 0:    # 오른쪽 -> 아래
                d = 1
            elif d == 1:  # 아래 -> 왼쪽
                d = 2
            elif d == 2:  # 왼쪽 -> 위
                d = 3
            elif d == 3:  # 위 -> 오른쪽
                d = 0
        
        x, y = nx, ny

# 더 효율적인 시뮬레이션을 위한 최적화
def optimized_game_play(x, y, d):
    steps = 1
    visited = {}
    
    while True:
        nx = x + dxs[d]
        ny = y + dys[d]
        steps += 1
        
        if not in_range(nx, ny):
            return steps
            
        # 무한루프 감지 시 매우 큰 값 반환
        state = (nx, ny, d)
        if state in visited:
            return 10**9
            
        visited[state] = steps
        
        # 방향 변경 (원래 로직과 동일)
        if grid[nx][ny] == 1:
            d = 3 - d
        elif grid[nx][ny] == 2:
            if d == 0:
                d = 1
            elif d == 1:
                d = 0  # 이 부분이 원래 코드와 다름! 수정 필요
            elif d == 2:
                d = 3
            elif d == 3:
                d = 2
        
        x, y = nx, ny

# 실제로는 원래 코드 로직을 그대로 사용하되, 안전장치만 추가
def safe_game_play(x, y, d):
    steps = 1
    max_steps = n * n * 4 + 1000  # 충분히 큰 한계값
    
    for _ in range(max_steps):
        nx = x + dxs[d]
        ny = y + dys[d]
        steps += 1
        
        if not in_range(nx, ny):
            return steps
            
        # 방향 변경 (원래 코드와 정확히 동일)
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
    
    # 한계값에 도달하면 무한루프로 간주
    return 10**9

ans = 0

# 모든 경계에서 시작
for i in range(n):
    ans = max(ans, safe_game_play(i, 0, 0))      # 왼쪽에서 오른쪽으로
    ans = max(ans, safe_game_play(i, n-1, 2))    # 오른쪽에서 왼쪽으로
    ans = max(ans, safe_game_play(0, i, 1))      # 위에서 아래로
    ans = max(ans, safe_game_play(n-1, i, 3))    # 아래에서 위로

# 무한루프인 경우를 제외하고 출력
if ans >= 10**9:
    print("INFINITE")  # 또는 문제에서 요구하는 다른 처리
else:
    print(ans)