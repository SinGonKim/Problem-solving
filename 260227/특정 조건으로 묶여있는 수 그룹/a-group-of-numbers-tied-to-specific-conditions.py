import sys
input = sys.stdin.readline

def solve():
    N, K = map(int, input().split())
    A = sorted([int(input()) for _ in range(N)])

    best_at_r = [0] * N 
    r = 0
    for l in range(N):
        if r < l:
            r = l
        while r < N and A[r] - A[l] <= K:
            r += 1
        rr = r - 1
        w = rr - l + 1
        if w > best_at_r[rr]:
            best_at_r[rr] = w

    # prefixBest[i] = i 이하에서 끝나는 구간들 중 최대 길이
    prefixBest = [0] * N
    cur = 0
    for i in range(N):
        if best_at_r[i] > cur:
            cur = best_at_r[i]
        prefixBest[i] = cur

    ans = prefixBest[N - 1]  # 그룹 1개만 쓰는 경우

    # 두 번째 구간의 시작을 l로 두고, 첫 번째는 l-1 이전에 끝나게
    r = 0
    for l in range(N):
        if r < l:
            r = l
        while r < N and A[r] - A[l] <= K:
            r += 1
        rr = r - 1
        w = rr - l + 1
        left_best = prefixBest[l - 1] if l > 0 else 0
        if w + left_best > ans:
            ans = w + left_best
    print(ans)

if __name__ == "__main__":
    solve()