import sys

def solve():
    T_cases = int(input())
    
    # 평면 좌표계 기준 방향 매핑 (U: y증가, D: y감소, L: x감소, R: x증가)
    d_map = {
        'U': (0, 1),
        'D': (0, -1),
        'L': (-1, 0),
        'R': (1, 0)
    }

    for _ in range(T_cases):
        N = int(input())
  
        balls = []
        for i in range(N):
            cli = input().split()
            xi, yi, wi = map(int, cli[:-1])
            di = cli[-1]
            # 좌표 2배 확장 (0.5초 단위 충돌을 정수 단위로 계산 가능하게 함)
            balls.append([wi, i, xi * 2 + 2000, yi * 2 + 2000, di])
        balls.sort(key=lambda x: (-x[0], -x[1]))

        last_collision_time = -1
    
        # 최대 4000초 시뮬레이션 (좌표 범위 0~4000 내에서 모든 충돌 완료)
        for t in range(1, 4001):
            if len(balls) <= 1:
                break
            
            new_pos_dict = {}
            collision_occurred = False
            survivors = []
            
            # 각 구슬 이동 및 충돌 체크
            for b in balls:
                dx, dy = d_map[b[4]]
                b[2] += dx # nx
                b[3] += dy # ny
                
                # 범위를 완전히 벗어난 구슬은 다시 돌아올 수 없으므로 제거 대상 (벽이 없기 때문)
                if not (0 <= b[2] <= 4000 and 0 <= b[3] <= 4000):
                    continue
                
                pos = (b[2], b[3])
                if pos not in new_pos_dict:
                    new_pos_dict[pos] = b
                    survivors.append(b)
                else:
                    # 이미 누군가 좌표를 선점함 = 충돌 발생
                    collision_occurred = True
                    # 선점한 구슬이 더 강하므로 현재 구슬은 survivors에 추가하지 않음
            
            # 다음 턴의 구슬 목록 갱신
            balls = survivors
            
            if collision_occurred:
                last_collision_time = t

        # 결과 출력 (충돌이 한 번도 없었다면 초기값 -1 출력)
        print(last_collision_time)

if __name__ == "__main__":
    solve()