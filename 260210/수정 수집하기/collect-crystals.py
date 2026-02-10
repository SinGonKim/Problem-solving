

import sys

def solve():
    # 입력 처리
    n, k = map(int, input().split()) # k번 이동해서 최대 수집 수정 개수
    s = input()

    # dp[시간][이동횟수]
    # dp[i][j]: i번째 시간까지 j번 이동했을 때의 최대 수정 개수
    dp = [[0] * (k + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        # 현재 떨어지는 수정의 위치 (L=0, R=1)
        current_pos = 0 if s[i-1] == 'L' else 1
        
        for j in range(k + 1):
            # j번 이동했을 때 엘라의 현재 위치
            # 0번 이동: L(0), 1번 이동: R(1), 2번 이동: L(0) ...
            ella_pos = j % 2
            
            # 수정을 얻을 수 있는지 확인
            score = 1 if ella_pos == current_pos else 0
            
            # 1. 이동하지 않고 이전 시간에서 그대로 온 경우
            dp[i][j] = dp[i-1][j] + score
            
            # 2. 이전에 j-1번 이동했다가 지금 1번 더 이동해서 온 경우
            if j > 0:
                dp[i][j] = max(dp[i][j], dp[i-1][j-1] + score)

    # 모든 이동 횟수 중 최댓값 출력
    print(max(dp[n]))

solve()