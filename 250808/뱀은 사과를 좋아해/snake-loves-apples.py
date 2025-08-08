import sys
from collections import deque

def read_input():
    input = sys.stdin.readline
    N, M, K = map(int, input().split())

    # 사과 좌표는 0-index로 저장
    apples = set()
    for _ in range(M):
        ax, ay = map(int, input().split())
        apples.add((ax - 1, ay - 1))

    moves = []
    for _ in range(K):
        d, t = input().split()
        moves.append((d, int(t)))
    return N, apples, moves

def simulate(N, apples, moves):
    # 뱀: head는 왼쪽(인덱스 0)
    snake = deque([(0, 0)])
    occupied = {(0, 0)}  # 몸이 차지한 칸 집합(O(1) 충돌 체크)
    time = 0

    dirvec = {
        "L": (0, -1),
        "R": (0,  1),
        "U": (-1, 0),
        "D": (1,  0),
    }

    for d, steps in moves:
        dx, dy = dirvec[d]
        for _ in range(steps):
            time += 1
            x, y = snake[0]
            nx, ny = x + dx, y + dy

            # 벽 충돌
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                print(time)
                return

            eat = (nx, ny) in apples

            # 사과를 못 먹으면 꼬리가 한 칸 빠지므로,
            # 충돌 체크 전에 꼬리 칸을 occupied에서 잠시 제거(자기자신 위로 이동 허용 케이스 방지)
            if not eat:
                tx, ty = snake[-1]
                occupied.remove((tx, ty))

            # 자기 몸 충돌
            if (nx, ny) in occupied:
                print(time)
                return

            # 이동 적용
            snake.appendleft((nx, ny))
            occupied.add((nx, ny))

            if eat:
                apples.remove((nx, ny))   # 길이 +1 (꼬리 유지)
            else:
                snake.pop()               # 꼬리 실제로 제거(위에서 occupied는 이미 제거됨)

    # 모든 이동을 끝냈다면 마지막 시간 출력
    print(time)

def main():
    N, apples, moves = read_input()
    simulate(N, apples, moves)

if __name__ == "__main__":
    main()
