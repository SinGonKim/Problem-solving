N, M, K = map(int, input().split()) # 격자의 크기, 사과의 개수, 밤의 방향 변환 횟수

apples = [tuple(map(lambda x: int(x)-1, input().split())) for _ in range(M)]
movement = [tuple(map(lambda x: int(x) if x.isdecimal() else x, input().split())) for _ in range(K)]

# Please write your code here.
from collections import deque
snake = deque()

# 사과 위치
apple = [[False for _ in range(N)] for _ in range(N)]
board = [[False for _ in range(N)] for _ in range(N)]


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


def set_up(x,y):
    snake.append((x,y))
    apply_snake_loc()

    for ax, ay in apples:
        apple[ax][ay] = True
set_up(0,0)

def move(direction):
    head = 0
    x, y = snake[head]

    if direction == "L":
        nx, ny = x, y-1
        if nx < 0 or nx >=N or ny<0 or ny>=N:return True
        if apple[nx][ny]:
            apple[nx][ny] = False
            snake.appendleft((nx,ny))
        else:
            snake.appendleft((nx,ny))
            snake.pop()
    
    elif direction == 'R':
        nx, ny = x, y+1
        if nx < 0 or nx>=N or ny<0 or ny>= N:
            return True
        
        if apple[nx][ny]:
            apple[nx][ny] = False
            snake.appendleft((nx,ny))
        else:
            snake.appendleft((nx,ny))
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
    if ended:return True
    return False


def main():
    seconds = 0
    for d, times in movement:
        for _ in range(int(times)):
            seconds += 1
            ended = move(d)
            if ended:
                print(seconds)
                return
    print(seconds)
    return

main()