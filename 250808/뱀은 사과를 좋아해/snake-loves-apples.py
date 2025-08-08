from collections import deque 

N, M, K = map(int, input().split())
apples = [tuple(map(lambda x: int(x)-1, input().split())) for _ in range(M)]
movement = [tuple(map(lambda x: int(x) if x.isdecimal() else x, input().split())) for _ in range(K)]

# 뱀의 모든 좌표를 기억해두는 배열
snake = deque([(0, 0)])
# 사과 위치를 표시하는 set (O(1) 조회)
apple_set = {(apple_x, apple_y) for apple_x, apple_y in apples}
# 뱀 위치를 표시하는 set (O(1) 조회 및 추가/삭제)
snake_set = {(0, 0)}

# 방향 매핑을 딕셔너리로 정의 (switch-case 대신)
directions = {
    'L': (0, -1),
    'R': (0, 1),
    'U': (-1, 0),
    'D': (1, 0)
}

def move(direction):
    head_x, head_y = snake[0]  # deque의 첫 번째 원소가 머리
    dx, dy = directions[direction]
    nx, ny = head_x + dx, head_y + dy
    
    # 경계 체크
    if nx < 0 or nx >= N or ny < 0 or ny >= N:
        return True
    
    # 자기 몸과 충돌 체크
    if (nx, ny) in snake_set:
        return True
    
    # 새로운 머리 위치 추가
    snake.appendleft((nx, ny))
    snake_set.add((nx, ny))
    
    # 사과를 먹었는지 확인
    if (nx, ny) in apple_set:
        apple_set.remove((nx, ny))
    else:
        # 사과를 못 먹었다면 꼬리 제거
        tail = snake.pop()
        snake_set.remove(tail)
    
    return False

def main():
    seconds = 0
    
    for direction, times in movement:
        for _ in range(times):
            seconds += 1
            if move(direction):
                print(seconds)
                return
    
    print(seconds)

main()