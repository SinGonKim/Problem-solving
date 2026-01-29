import sys

# 입력을 효율적으로 읽기 위해 sys.stdin.read 사용
def solve():
    T_cases = int(input())
    
    # 평면 좌표계 기준 방향 매핑 (U: y증가, D: y감소, L: x감소, R: x증가)
    dxs = {'U': 0, 'D': 0, 'L': -1, 'R': 1}
    dys = {'U': 1, 'D': -1, 'L': 0, 'R': 0}

    for _ in range(T_cases):
        N = int(input())
  
        balls = []
        for i in range(N):
            cli = input().split()
            xi, yi, wi = map(int, cli[:-1])
            di = cli[-1]
            # 1. 좌표 2배 확장 (0.5초 단위 충돌을 정수 단위로 계산 가능하게 함)
            balls.append({'w': wi, 'id': i, 'x': xi * 2, 'y': yi * 2, 'd': di})

        last_collision_time = -1
        
        # 시뮬레이션: 최대 거리가 4000이므로 4000초면 모든 충돌 가능성이 종료됨
        for t in range(0, 4001):
            if len(balls) <= 1:
                break
            
            # t=0일 때는 이동하지 않고 현재 위치에서 충돌 확인, 그 외엔 이동 후 확인
            if t > 0:
                for b in balls:
                    b['x'] += dxs[b['d']]
                    b['y'] += dys[b['d']]
            
            # 위치별 구슬 모으기 (딕셔너리 사용하여 시간 단축)
            pos_dict = {}
            for b in balls:
                p = (b['x'], b['y'])
                if p not in pos_dict:
                    pos_dict[p] = []
                pos_dict[p].append(b)
            
            collision_occurred = False
            next_generation = []
            
            for p in pos_dict:
                group = pos_dict[p]
                if len(group) > 1:
                    collision_occurred = True
                    # 영향력 규칙: 무게 내림차순 -> 번호(id) 내림차순 정렬
                    group.sort(key=lambda x: (-x['w'], -x['id']))
                    next_generation.append(group[0]) # 가장 영향력 큰 구슬만 생존
                else:
                    next_generation.append(group[0])
            
            balls = next_generation
            if collision_occurred:
                last_collision_time = t
        
        print(last_collision_time)

if __name__ == "__main__":
    solve()