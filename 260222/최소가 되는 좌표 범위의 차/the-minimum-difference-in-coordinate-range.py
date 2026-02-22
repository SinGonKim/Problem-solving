import sys
from collections import deque

def solve():
    input = sys.stdin.readline
    N, D = map(int, input().split())
    pts = [tuple(map(int, input().split())) for _ in range(N)]
    pts.sort()  # x 기준 정렬

    xs = [p[0] for p in pts]
    ys = [p[1] for p in pts]

    minDQ = deque()  # ys 인덱스, y 증가 유지 -> front가 최소
    maxDQ = deque()  # ys 인덱스, y 감소 유지 -> front가 최대

    ans = 10**18
    l = 0

    for r in range(N):
        # maxDQ 갱신: 뒤에서부터 y가 작거나 같으면 제거 (감소 유지)
        while maxDQ and ys[maxDQ[-1]] <= ys[r]:
            maxDQ.pop()
        maxDQ.append(r)

        # minDQ 갱신: 뒤에서부터 y가 크거나 같으면 제거 (증가 유지)
        while minDQ and ys[minDQ[-1]] >= ys[r]:
            minDQ.pop()
        minDQ.append(r)

        # 조건 만족하면 l을 줄여가며 최소 폭 갱신
        while maxDQ and minDQ and ys[maxDQ[0]] - ys[minDQ[0]] >= D:
            ans = min(ans, xs[r] - xs[l])

            # l이 빠질 때 덱 front에 있으면 제거
            if maxDQ[0] == l:
                maxDQ.popleft()
            if minDQ[0] == l:
                minDQ.popleft()
            l += 1

    print(-1 if ans == 10**18 else ans)

if __name__ == "__main__":
    solve()