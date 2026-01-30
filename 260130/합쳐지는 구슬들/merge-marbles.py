from collections import defaultdict

def is_range(x,y):
    return 0<=x<n and 0<=y<n


def move(B):
    visited = [[0 for _ in range(n)] for _ in range(n)]
    dir = {
        'U': (-1,0),
        'L': (0,-1),
        'R': (0,1),
        'D': (1,0)
    }
    c_dir = {
        'U': 'D',
        'L': 'R',
        'R': 'L',
        'D': 'U'
    }

    next_positions = defaultdict(list)


    for (idx, wi, ri, ci, di) in B:

        dr, dc = dir[di]
        nr = ri + dr
        nc = ci + dc

        if not is_range(nr, nc):
            nr = ri
            nc = ci
            di = c_dir[di]

        next_positions[(nr, nc)].append((idx, wi, di))
        new_B = []
        for (r, c), gathered in next_positions.items():
            if len(gathered) == 1:
                # 공이 하나면 그대로 유지
                idx, w, d = gathered[0]
                new_B.append([idx, w, r, c, d])
            else:
                # 여러 개면 무게 합산 및 가장 큰 번호(idx) 찾기
                total_weight = sum(b[1] for b in gathered)
                # 번호(idx)가 가장 큰 공의 정보를 기준으로 남깁니다.
                best_ball = max(gathered, key=lambda x: x[0])
                new_B.append([best_ball[0], total_weight, r, c, best_ball[2]])
            
    return new_B


def simulate():

    balls = []
    for i in range(1, m+1):
        ri, ci, di, wi = input().split()
        balls.append([i, int(wi), int(ri) - 1, int(ci) - 1, di])

    for _ in range(t):
        balls = move(balls)
        if not balls:break
    
    if not balls:
        print(0, 0)
    else:
        target = max(ball[1] for ball in balls)
        print(len(balls), target)

# Please write your code here.
if __name__ == "__main__":
    n, m, t = map(int, input().split())
    simulate()
    