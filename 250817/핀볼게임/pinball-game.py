n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def game_play(x, y, d):
    steps = 1
    visited = set()
    
    while True:
        # 무한루프 체크: (위치, 방향) 조합이 반복되면 종료
        state = (x, y, d)
        if state in visited:
            steps += 1
            break
        visited.add(state)
        
        # 다음 위치 계산
        nx = x + dxs[d]
        ny = y + dys[d]
        steps += 1
        
        # 격자를 벗어나면 종료
        if not in_range(nx, ny):
            break
            
        # 방향 변경 로직
        if grid[nx][ny] == 1:
            d = 3 - d  # 반대 방향
        elif grid[nx][ny] == 2:
            # 원래 코드의 방향 변경 로직 복원
            if d == 0:
                d = 1
            elif d == 1:
                d = 0
            elif d == 2:
                d = 3
            elif d == 3:
                d = 2
        
        x, y = nx, ny
    
    return steps

# 메모이제이션 제거 - 시작점이 모두 다르므로 효과 제한적
ans = 0

# 원래 코드와 동일한 순서로 시작점 설정
for i in range(n):
    ans = max(ans, game_play(i, 0, 0))      # 왼쪽 가장자리에서 오른쪽으로
    ans = max(ans, game_play(i, n-1, 2))    # 오른쪽 가장자리에서 왼쪽으로
    ans = max(ans, game_play(0, i, 1))      # 위쪽 가장자리에서 아래로
    ans = max(ans, game_play(n-1, i, 3))    # 아래쪽 가장자리에서 위로

print(ans)