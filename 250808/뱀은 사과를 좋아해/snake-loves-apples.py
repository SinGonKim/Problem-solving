from collections import deque 

N, M, K = map(int, input().split())
apples = [tuple(map(lambda x: int(x)-1, input().split())) for _ in range(M)]
movement = [tuple(map(lambda x: int(x) if x.isdecimal() else x, input().split())) for _ in range(K)]

# 뱀의 모든 좌표를 기억해두는 배열
snake = deque()
# 사과 위치를 표시하는 배열
apple = [[False for _ in range(N)] for __ in range(N)]
# 뱀 위치를 표시하는 배열
board = [[False for _ in range(N)] for __ in range(N)]

# 변경된 뱀의 위치를 board에 반영하는 함수
def apply_snake_loc():
    global board
    for i in range(N):
        for j in range(N):
            board[i][j] = False

    for loc_x, loc_y in snake:
        if board[loc_x][loc_y]:
            return True
        board[loc_x][loc_y] = True
    return False

# 초기 게임 세팅 함수
def setUp():
    snake.append((0, 0))
    apply_snake_loc()

    for apple_x, apple_y in apples:
        apple[apple_x][apple_y] = True

# 정해진 방향으로 뱀을 움직이는 함수
def move(direction):
    X, Y, HEAD = 0, 1, 0
    x, y = snake[HEAD]

    if direction == "L":
        nx, ny = x, y-1
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            return True
        # 사과를 먹었다면...
        if apple[nx][ny]:
            apple[nx][ny] = False
            snake.appendleft((nx, ny))
        # 사과를 못먹었다면...
        else:
            snake.appendleft((nx, ny))
            snake.pop()
    elif direction == "R":
        nx, ny = x, y+1
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            return True
        # 사과를 먹었다면...
        if apple[nx][ny]:
            apple[nx][ny] = False
            snake.appendleft((nx, ny))
        # 사과를 못먹었다면...
        else:
            snake.appendleft((nx, ny))
            snake.pop()
    elif direction == "U":
        nx, ny = x-1, y
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            return True
        # 사과를 먹었다면...
        if apple[nx][ny]:
            apple[nx][ny] = False
            snake.appendleft((nx, ny))
        # 사과를 못먹었다면...
        else:
            snake.appendleft((nx, ny))
            snake.pop()
    else:
        nx, ny = x+1, y
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            return True
        # 사과를 먹었다면...
        if apple[nx][ny]:
            apple[nx][ny] = False
            snake.appendleft((nx, ny))
        # 사과를 못먹었다면...
        else:
            snake.appendleft((nx, ny))
            snake.pop()

    ended = apply_snake_loc()
    if ended:
        return True
    return False

# 메인 실행함수
def main():
    seconds = 0
    for d, times in movement:
        for _ in range(times):
            seconds += 1
            ended = move(d)
            # print_snake()
            # print()
            if ended:
                print(seconds)
                return
    
    print(seconds)
    return

setUp()
main()

