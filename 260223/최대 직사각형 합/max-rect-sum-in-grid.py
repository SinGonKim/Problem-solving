import sys

def kadane(arr):
    best = cur = arr[0]
    for x in arr[1:]:
        cur = x if cur + x < x else cur + x
        if best < cur:
            best = cur
    return best

def main():
    input = sys.stdin.readline
    N = int(input().strip())
    A = [list(map(int, input().split())) for _ in range(N)]

    ans = -10**18  # 충분히 작은 값 (N<=300, 값 범위 고려해도 안전)
    for top in range(N):
        colsum = [0] * N
        for bottom in range(top, N):
            row = A[bottom]
            # 열별 누적합 갱신
            for c in range(N):
                colsum[c] += row[c]
            # 현재 top..bottom 구간에서 최대 부분배열 합
            cur_best = kadane(colsum)
            if ans < cur_best:
                ans = cur_best

    print(ans)

if __name__ == "__main__":
    main()