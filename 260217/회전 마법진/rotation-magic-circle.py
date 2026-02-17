import sys
input = sys.stdin.readline

N = int(input())
a = input().strip()
b = input().strip()

INF = sys.maxsize

dp = [INF] * 10 # dp[i] : *자리 숫자가 i가 되는데 돌리는 최소 회전 수
dp[0] = 0  # 누적 반시계 회전량 = 0 -> 반시계만 뒤에 영향을 주므로

for i in range(N):
    ai = ord(a[i]) - ord('0')
    bi = ord(b[i]) - ord('0')
    ndp = [INF] * 10 # 다음자리숫자로 가기 위한 dp

    for k in range(10):
        if dp[k] == INF: # 반시계 방향으로 돌아간 횟수 dp[k]는 시작을 k에서 할 수 없음
            continue

        cur = (ai + k) % 10 
        need_ccw = (bi - cur) % 10          # 반시계로 need_ccw만큼 돌리면 맞음
        need_cw = (10 - need_ccw) % 10      # 시계로 돌리는 경우(현재만 영향)

        # 1) 반시계 회전: 뒤에도 같이 돌아가므로 누적 k가 증가
        nk = (k + need_ccw) % 10
        ndp[nk] = min(ndp[nk], dp[k] + need_ccw)

        # 2) 시계 회전: 현재만 돌아가므로 누적 k 유지
        ndp[k] = min(ndp[k], dp[k] + need_cw)

    dp = ndp

print(min(dp))
